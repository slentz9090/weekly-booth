// THE WEEKLY BOOTH: ESPN pull -> docs/data/<league>_wk<N>_facts.json
//
// Runs INSIDE Chrome on a fantasy.espn.com tab (the container cannot reach ESPN).
// Paste this file into javascript_tool, then call:
//     await boothFacts('foh', 3)      // or 'dlffl'
// It returns the facts object. To get it into the container, either
//   * have Chrome download it:  boothDownload(obj)   (lands in ~/Downloads, stage it), or
//   * boothShow(obj) writes it into the page as <pre>, then read it with get_page_text.
// To check the builder against a week that already shipped:
//     await boothSelfTest('foh', 2)   // diffs against the committed wk2 facts on GitHub
//
// Schema matches the Week 2 facts files. Validated against Week 2 on 2026-09-28: Dewart Lake
// identical; Friends of Herb identical once Ryan Kelly's best lineup was corrected to 64.72 (the
// Week 2 in-browser build had skipped his -1 defense). Refuses to run while any matchup is UNDECIDED.
(() => {
const LEAGUES = { dlffl: [404188, 'Dewart Lake FFL'], foh: [757898, 'Friends of Herb'] };
const POS = { 1: 'QB', 2: 'RB', 3: 'WR', 4: 'TE', 5: 'K', 16: 'D/ST' };
const SLOT = { 0: 'QB', 2: 'RB', 4: 'WR', 6: 'TE', 16: 'D/ST', 17: 'K', 23: 'FLEX', 3: 'RB/WR', 5: 'WR/TE', 7: 'OP' };
const BENCH = 20, IR = 21;
const r2 = x => Math.round((x + Number.EPSILON) * 100) / 100;
const r1 = x => Math.round((x + Number.EPSILON) * 10) / 10;
const r3 = x => Math.round((x + Number.EPSILON) * 1000) / 1000;
const base = (id, season) =>
  `https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/${season}/segments/0/leagues/${id}`;

async function get(url, filter) {
  const h = filter ? { 'x-fantasy-filter': JSON.stringify(filter) } : {};
  const r = await fetch(url, { credentials: 'include', headers: h });
  if (!r.ok) throw new Error(`${r.status} ${url}`);
  return r.json();
}

function ptsOf(player, sp, src) {
  const s = (player.stats || []).find(x => x.scoringPeriodId === sp && x.statSourceId === src);
  return s ? s.appliedTotal : 0;
}

// Best lineup. Single-position slots fill first, then wider slots, each with the best
// eligible player left. Exact for ESPN's standard QB/RB/WR/TE/FLEX/K/DST layouts.
function optimal(players, slotCounts) {
  const slots = [];
  for (const [sid, n] of Object.entries(slotCounts)) {
    const s = +sid;
    if (s === BENCH || s === IR || !n) continue;
    for (let i = 0; i < n; i++) slots.push(s);
  }
  const breadth = s => new Set(players.filter(p => p.elig.includes(s)).map(p => p.pos)).size || 99;
  slots.sort((a, b) => breadth(a) - breadth(b));
  const used = new Set();
  let total = 0;
  for (const s of slots) {
    const best = players.filter(p => !used.has(p.id) && p.elig.includes(s)).sort((a, b) => b.pts - a.pts)[0];
    if (best) { used.add(best.id); total += best.pts; }
  }
  return total;
}

async function boothFacts(league, week) {
  const [id, leagueName] = LEAGUES[league];
  const season = 2026;
  const d = await get(`${base(id, season)}?view=mTeam&view=mSettings&view=mStatus&view=mMatchupScore&view=mBoxscore&view=mRoster&scoringPeriodId=${week}`);
  const members = {};
  (d.members || []).forEach(m => { members[m.id] = `${(m.firstName || '').trim()} ${(m.lastName || '').trim()}`.trim(); });
  const T = {};
  d.teams.forEach(t => { T[t.id] = { name: t.name || `${t.location} ${t.nickname}`, owner: members[(t.owners || [])[0]], t }; });
  const slotCounts = d.settings.rosterSettings.lineupSlotCounts;

  const games = d.schedule.filter(m => m.matchupPeriodId === week);
  const undecided = games.filter(m => m.away && m.winner === 'UNDECIDED');
  if (undecided.length) throw new Error(`Week ${week} not final: ${undecided.length} matchup(s) UNDECIDED`);

  // per team, from the week's roster
  const per = {};
  const sideScore = s => (s.totalPoints || s.totalPointsLive || 0);
  for (const m of games) {
    for (const side of [m.home, m.away]) {
      if (!side) continue;
      const entries = (side.rosterForCurrentScoringPeriod || {}).entries || [];
      const ps = entries.map(e => {
        const p = e.playerPoolEntry.player;
        return {
          id: p.id, n: p.fullName, pos: POS[p.defaultPositionId] || String(p.defaultPositionId),
          slotId: e.lineupSlotId, slot: SLOT[e.lineupSlotId] || String(e.lineupSlotId),
          elig: p.eligibleSlots || [], pts: r2(ptsOf(p, week, 0)), proj: r2(ptsOf(p, week, 1)),
        };
      });
      const starters = ps.filter(p => p.slotId !== BENCH && p.slotId !== IR);
      const bench = ps.filter(p => p.slotId === BENCH);
      const actual = r2(starters.reduce((a, p) => a + p.pts, 0));
      const opt = r2(optimal(ps.filter(p => p.slotId !== IR), slotCounts));
      // best single swap: a benched player who is eligible for a starter's slot
      let worst = null;
      for (const s of starters) for (const b of bench) {
        if (!b.elig.includes(s.slotId)) continue;
        const delta = r2(b.pts - s.pts);
        if (delta > 0 && (!worst || delta > worst.delta))
          worst = { delta, slot: s.slot, started: s.n, startedPts: s.pts, benched: b.n, benchedPts: b.pts };
      }
      const byPts = (a, b) => b.pts - a.pts;
      const top = [...starters].sort(byPts).slice(0, 3).map(p => ({ n: p.n, pos: p.pos, pts: p.pts, proj: p.proj }));
      const bustP = [...starters].sort((a, b) => (a.pts - a.proj) - (b.pts - b.proj))[0];
      const benchSorted = [...bench].sort(byPts);
      const score = r2(side === m.home && !m.away ? (sideScore(side) || actual) : sideScore(side));
      per[side.teamId] = {
        teamId: side.teamId, name: T[side.teamId].name, owner: T[side.teamId].owner,
        score, actual, optimal: opt, left: r2(opt - actual), eff: opt ? r1(actual / opt * 100) : 100,
        worst,
        top,
        bust: bustP ? { n: bustP.n, pos: bustP.pos, pts: bustP.pts, proj: bustP.proj, miss: r2(bustP.pts - bustP.proj) } : null,
        bestBench: benchSorted[0] ? { n: benchSorted[0].n, pos: benchSorted[0].pos, pts: benchSorted[0].pts } : null,
        benchTop: benchSorted.slice(0, 2).map(p => ({ n: p.n, pos: p.pos, pts: p.pts, proj: p.proj })),
        starterLow: [...starters].sort((a, b) => a.pts - b.pts).slice(0, 2).map(p => ({ n: p.n, pos: p.pos, slot: p.slot, pts: p.pts, proj: p.proj })),
      };
    }
  }
  // all-play on the week's score, bye team included
  const all = Object.values(per);
  for (const t of all) {
    let w = 0, l = 0;
    for (const o of all) if (o !== t) { if (t.score > o.score) w++; else if (t.score < o.score) l++; }
    t.allPlay = `${w}-${l}`;
    t.expWins = r3(w / (all.length - 1));
  }

  const matchups = games.filter(m => m.away).map(m => {
    const h = per[m.home.teamId], a = per[m.away.teamId];
    const hs = sideScore(m.home), as = sideScore(m.away);
    const win = m.winner === 'HOME' ? h : m.winner === 'AWAY' ? a : null;
    const lose = win === h ? a : win === a ? h : null;
    return {
      homeId: h.teamId, home: h.name, homeOwner: h.owner, homeScore: r2(hs),
      awayId: a.teamId, away: a.name, awayOwner: a.owner, awayScore: r2(as),
      winnerId: win ? win.teamId : null, winner: win ? win.name : null, loserId: lose ? lose.teamId : null,
      margin: r2(Math.abs(hs - as)),
    };
  });
  const byes = games.filter(m => !m.away).map(m => {
    const t = per[m.home.teamId];
    return { teamId: t.teamId, name: t.name, owner: t.owner, score: t.score };
  });

  const standings = d.teams.map(t => {
    const o = t.record.overall, p = per[t.id];
    return {
      teamId: t.id, name: T[t.id].name, owner: T[t.id].owner, w: o.wins, l: o.losses, tie: o.ties,
      pf: r2(o.pointsFor), pa: r2(o.pointsAgainst), seed: t.playoffSeed, eff: p.eff, allPlay: p.allPlay,
    };
  }).sort((a, b) => a.seed - b.seed);

  // moves executed for this scoring period, with each player's points that week
  const tx = await get(`${base(id, season)}?view=mTransactions2&scoringPeriodId=${week}`);
  const txs = (tx.transactions || []).filter(x => x.status === 'EXECUTED' && ['FREEAGENT', 'WAIVER'].includes(x.type) && x.scoringPeriodId === week);
  const ids = [...new Set(txs.flatMap(x => (x.items || []).map(i => i.playerId)))];
  const info = {};
  if (ids.length) {
    const k = await get(`${base(id, season)}?view=kona_player_info&scoringPeriodId=${week}`,
      { players: { filterIds: { value: ids } } });
    (k.players || []).forEach(pe => {
      const p = pe.player;
      info[p.id] = { n: p.fullName, pos: POS[p.defaultPositionId] || String(p.defaultPositionId), pts: r2(ptsOf(p, week, 0)) };
    });
  }
  const moves = txs.map(x => ({
    type: x.type, sp: x.scoringPeriodId, team: T[x.teamId].name, owner: T[x.teamId].owner,
    added: (x.items || []).filter(i => i.type === 'ADD').map(i => info[i.playerId] || { n: String(i.playerId), pos: '?', pts: 0 }),
    dropped: (x.items || []).filter(i => i.type === 'DROP').map(i => info[i.playerId] || { n: String(i.playerId), pos: '?', pts: 0 }),
  }));

  const nextWeek = d.schedule.filter(m => m.matchupPeriodId === week + 1).map(m => ({
    home: T[m.home.teamId].name, homeOwner: T[m.home.teamId].owner,
    away: m.away ? T[m.away.teamId].name : null, awayOwner: m.away ? T[m.away.teamId].owner : null,
  }));

  const played = matchups.flatMap(m => [
    { name: m.home, owner: m.homeOwner, score: m.homeScore }, { name: m.away, owner: m.awayOwner, score: m.awayScore }]);
  const high = played.reduce((a, b) => (b.score > a.score ? b : a));
  const low = played.reduce((a, b) => (b.score < a.score ? b : a));
  const biggestMargin = matchups.reduce((a, b) => (b.margin > a.margin ? b : a));
  const closest = matchups.reduce((a, b) => (b.margin < a.margin ? b : a));

  return {
    league, leagueId: id, leagueName, week, generatedAt: new Date().toISOString(),
    matchups, byes, perTeam: Object.values(per), standings, moves, nextWeek, high, low, biggestMargin, closest,
  };
}

// Compare against a committed facts file. Returns a list of differences (empty = identical
// apart from generatedAt and list order of moves).
async function boothSelfTest(league, week) {
  const mine = await boothFacts(league, week);
  const ref = await fetch(`https://raw.githubusercontent.com/slentz9090/weekly-booth/main/docs/data/${league}_wk${week}_facts.json?x=${Date.now()}`).then(r => r.json());
  const diffs = [];
  const norm = v => JSON.stringify(v);
  const cmp = (path, a, b) => {
    if (a && b && typeof a === 'object' && typeof b === 'object' && !Array.isArray(a)) {
      for (const k of new Set([...Object.keys(a), ...Object.keys(b)])) cmp(`${path}.${k}`, a[k], b[k]);
    } else if (Array.isArray(a) && Array.isArray(b) && a.length === b.length) {
      a.forEach((x, i) => cmp(`${path}[${i}]`, x, b[i]));
    } else if (norm(a) !== norm(b)) diffs.push(`${path}: mine=${norm(a)} ref=${norm(b)}`.slice(0, 220));
  };
  for (const k of Object.keys(ref)) {
    if (k === 'generatedAt') continue;
    if (k === 'perTeam' || k === 'standings') {
      const by = xs => Object.fromEntries(xs.map(x => [x.owner, x]));
      cmp(k, by(mine[k] || []), by(ref[k]));
      if (k === 'standings') cmp('standingsOrder', mine[k].map(x => x.owner), ref[k].map(x => x.owner));
    } else if (k === 'moves') {
      const key = m => norm([m.owner, m.type, m.added.map(p => p.n).sort(), m.dropped.map(p => p.n).sort()]);
      const A = new Map(mine.moves.map(m => [key(m), m])), B = new Map(ref.moves.map(m => [key(m), m]));
      for (const [kk, m] of B) if (!A.has(kk)) diffs.push(`moves: missing ${kk}`); else cmp(`moves${kk}`, A.get(kk), m);
      for (const kk of A.keys()) if (!B.has(kk)) diffs.push(`moves: extra ${kk}`);
    } else cmp(k, mine[k], ref[k]);
  }
  return diffs;
}

function boothShow(obj) {
  document.open(); document.write('<pre id="facts"></pre>'); document.close();
  document.getElementById('facts').textContent = JSON.stringify(obj);
}

function boothDownload(obj) {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([JSON.stringify(obj, null, 1)], { type: 'application/json' }));
  a.download = `${obj.league}_wk${obj.week}_facts.json`;
  document.body.appendChild(a); a.click(); a.remove();
}

Object.assign(window, { boothFacts, boothSelfTest, boothShow, boothDownload });
})();
