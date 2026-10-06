// Build facts files in the container from a raw bundle pulled in Chrome (Week 4 route).
// In Chrome, on a fantasy.espn.com tab, fetch per league: main (the six views), tx (mTransactions2),
// kona (kona_player_info for the moved player ids); download {dlffl:{main,tx,kona},foh:{...}} as
// booth_wk<N>_raw.json, stage it, then:  node gen2/facts_offline.js <bundle.json> <week>
const fs = require('fs'), path = require('path');
const [bundlePath, weekArg] = process.argv.slice(2);
const bundle = JSON.parse(fs.readFileSync(bundlePath, 'utf8'));
const IDS = { 404188: 'dlffl', 757898: 'foh' };
global.window = global;
global.fetch = async (url) => {
  const id = +url.match(/leagues\/(\d+)/)[1];
  const b = bundle[IDS[id]];
  const body = url.includes('mTransactions2') ? b.tx : url.includes('kona_player_info') ? b.kona : b.main;
  return { ok: true, status: 200, json: async () => body };
};
eval(fs.readFileSync(path.join(__dirname, 'espn_facts.js'), 'utf8'));
(async () => {
  for (const l of ['dlffl', 'foh']) {
    const f = await boothFacts(l, +weekArg);
    const out = path.join(__dirname, '..', 'docs', 'data', `${l}_wk${weekArg}_facts.json`);
    fs.writeFileSync(out, JSON.stringify(f, null, 1));
    console.log(l, f.matchups.map(m => `${m.homeOwner} ${m.homeScore} v ${m.awayOwner} ${m.awayScore}`).join(' | '), 'byes', JSON.stringify(f.byes), 'moves', f.moves.length);
  }
})();
