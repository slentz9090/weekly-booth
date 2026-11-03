"""THE OWNER SPOTLIGHT (added Week 8, 2026-11-03). One owner per league per week, profiled from the
all-time game log that nobody else has.

    python3 gen2/spotlight.py <league> "<Owner Name>" <week>  -> prints the profile and writes
    docs/data/<league>_spotlight_wk<N>.json

Reads gen2/data/<league>_games.json (rebuilt each run by games.py + append_current.py, so it already
holds this season through the previous week), docs/data/<league>_history.json (titles, career
ranges) and docs/data/<league>_wk<N>_facts.json (this week). Dewart Lake two-week playoff rounds are
one game whose score spans two weeks (weeks=2); they count in records and series, never in
single-week score rankings.
"""
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "docs", "data")
PW = os.path.join(HERE, "data")
SEASON = 2026


def norm(n):
    return n.title() if (n.isupper() or n.islower()) and " " in n else n


def profile(league, owner, week):
    G = json.load(open(os.path.join(PW, f"{league}_games.json")))["games"]
    H = json.load(open(os.path.join(DATA, f"{league}_history.json")))
    F = json.load(open(os.path.join(DATA, f"{league}_wk{week}_facts.json")))
    active = {norm(t["owner"]) for t in F["perTeam"]}

    # add this week's games to the log view so "through this week" is true everywhere below
    games = list(G)
    for m in F["matchups"]:
        w = "tie" if m["winnerId"] is None else ("home" if m["winnerId"] == m["homeId"] else "away")
        games.append({"year": SEASON, "period": week, "playoff": False, "tier": "NONE", "weeks": 1,
                      "home": norm(m["homeOwner"]), "homeTeam": m["home"], "homeScore": m["homeScore"],
                      "away": norm(m["awayOwner"]), "awayTeam": m["away"], "awayScore": m["awayScore"],
                      "winner": w})

    mine = [g for g in games if owner in (g["home"], g["away"])]
    def side(g):
        me = "home" if g["home"] == owner else "away"
        op = "away" if me == "home" else "home"
        return g[me + "Score"], g[op + "Score"], g[op], (g["winner"] == me), (g["winner"] == "tie")

    out = {"owner": owner, "league": league, "week": week}
    reg = [g for g in mine if not g["playoff"]]
    po = [g for g in mine if g["playoff"] and g["tier"] == "WINNERS_BRACKET"]   # the real bracket only
    cons = [g for g in mine if g["playoff"] and g["tier"] != "WINNERS_BRACKET"]
    def rec(gs):
        w = sum(1 for g in gs if side(g)[3]); t = sum(1 for g in gs if side(g)[4]); return w, len(gs) - w - t, t
    out["careerRegular"] = rec(reg)
    out["careerPlayoff"] = rec(po)
    out["careerConsolation"] = rec(cons)
    out["seasons"] = sorted({g["year"] for g in mine})
    out["firstYear"] = min(out["seasons"])

    # single-week scores only
    single = [g for g in mine if g["weeks"] == 1]
    scores = sorted(((side(g)[0], g["year"], g["period"]) for g in single), reverse=True)
    out["games"] = len(single)
    out["best5"] = scores[:5]
    out["worst3"] = scores[-3:][::-1]
    out["careerPpg"] = round(sum(s[0] for s in scores) / len(scores), 2)
    # league-wide rank of career ppg among active owners (min 30 games)
    ppg = {}
    for o in active:
        ss = [side_(g, o) for g in games if g["weeks"] == 1 and o in (g["home"], g["away"])]
        if len(ss) >= 30:
            ppg[o] = round(sum(ss) / len(ss), 2)
    out["ppgRankAmongActive"] = (sorted(ppg.values(), reverse=True).index(out["careerPpg"]) + 1, len(ppg))
    out["ppgTable"] = sorted(ppg.items(), key=lambda kv: -kv[1])

    # margins
    wins = sorted(((round(side(g)[0] - side(g)[1], 2), side(g)[2], g["year"], g["period"]) for g in mine if side(g)[3]), reverse=True)
    losses = sorted(((round(side(g)[1] - side(g)[0], 2), side(g)[2], g["year"], g["period"]) for g in mine if not side(g)[3] and not side(g)[4]), reverse=True)
    out["biggestWins"] = wins[:3]
    out["biggestLosses"] = losses[:3]
    out["closestWins"] = sorted(wins, key=lambda x: x[0])[:3]
    out["closestLosses"] = sorted(losses, key=lambda x: x[0])[:3]

    # season records (regular season), best and worst
    by_year = defaultdict(lambda: [0, 0, 0, 0.0])
    for g in reg:
        s, o_, opp, won, tie = side(g)
        r = by_year[g["year"]]
        r[0] += won; r[1] += (not won and not tie); r[2] += tie; r[3] += s
    out["seasonRecords"] = {y: (r[0], r[1], r[2], round(r[3], 2)) for y, r in sorted(by_year.items())}

    # titles and finals from the log (tier WINNERS_BRACKET final = the last playoff period of a year)
    champs = [c for c in H["champions"] if c[1] == owner]
    out["titles"] = [c[0] for c in champs]
    out["titlesAllEras"] = (H.get("titlesAllEras", {}).get(owner, {}) or {}).get("total")
    finals = []
    for y in sorted({g["year"] for g in po}):
        yp = [g for g in games if g["year"] == y and g["playoff"] and g["tier"] == "WINNERS_BRACKET"]
        if not yp:
            continue
        last = max(g["period"] for g in yp)
        for g in yp:
            if g["period"] == last and owner in (g["home"], g["away"]):
                s, o_, opp, won, tie = side(g)
                finals.append((y, "won" if won else "lost", opp, s, o_))
    out["finals"] = finals
    out["playoffYears"] = sorted({g["year"] for g in po if g["tier"] == "WINNERS_BRACKET"})

    # streaks (all games, chronological)
    seq = [side(g)[3] for g in sorted(mine, key=lambda g: (g["year"], g["period"]))]
    best = cur = 0; worst = curl = 0
    for w in seq:
        cur = cur + 1 if w else 0; best = max(best, cur)
        curl = curl + 1 if not w else 0; worst = max(worst, curl)
    out["longestWinStreak"] = best
    out["longestLosingStreak"] = worst
    k = 0
    for w in reversed(seq):
        if w == seq[-1]: k += 1
        else: break
    out["currentStreak"] = (("W" if seq[-1] else "L"), k)

    # lifetime vs every active owner
    vs = defaultdict(lambda: [0, 0, 0])
    for g in mine:
        s, o_, opp, won, tie = side(g)
        r = vs[opp]; r[0] += won; r[1] += (not won and not tie); r[2] += tie
    out["vsActive"] = sorted(((o, tuple(r)) for o, r in vs.items() if o in active), key=lambda kv: -(kv[1][0] - kv[1][1]))
    out["vsAll"] = sorted(((o, tuple(r)) for o, r in vs.items()), key=lambda kv: -(kv[1][0] + kv[1][1]))

    # luck: all-play per season (single-week regular season games with every team's score that week)
    wk_scores = defaultdict(dict)
    for g in games:
        if g["playoff"] or g["weeks"] != 1:
            continue
        wk_scores[(g["year"], g["period"])][g["home"]] = g["homeScore"]
        wk_scores[(g["year"], g["period"])][g["away"]] = g["awayScore"]
    luck = {}
    for y, r in by_year.items():
        apw = apl = 0
        for (yy, p), sc in wk_scores.items():
            if yy != y or owner not in sc:
                continue
            for o, s in sc.items():
                if o == owner:
                    continue
                apw += sc[owner] > s; apl += sc[owner] < s
        gp = apw + apl
        if gp:
            exp = apw / gp * (r[0] + r[1] + r[2])
            luck[y] = (r[0], r[1], apw, apl, round(r[0] - exp, 2))
    out["luckBySeason"] = luck
    out["luckiest"] = max(luck.items(), key=lambda kv: kv[1][4]) if luck else None
    out["unluckiest"] = min(luck.items(), key=lambda kv: kv[1][4]) if luck else None

    # this season
    out["thisSeason"] = out["seasonRecords"].get(SEASON)
    out["thisSeasonLuck"] = luck.get(SEASON)
    pts_rank = sorted(((sum(side_(g, o) for g in games if g["year"] == SEASON and not g["playoff"] and o in (g["home"], g["away"])), o) for o in active), reverse=True)
    out["pointsRank2026"] = [o for _, o in pts_rank].index(owner) + 1

    p = os.path.join(DATA, f"{league}_spotlight_wk{week}.json")
    json.dump(out, open(p, "w"), indent=1, default=str)
    return out


def side_(g, o):
    return g["homeScore"] if g["home"] == o else g["awayScore"]


if __name__ == "__main__":
    lg, owner, wk = sys.argv[1], sys.argv[2], int(sys.argv[3])
    o = profile(lg, owner, wk)
    for k, v in o.items():
        if k in ("vsAll", "ppgTable", "seasonRecords", "luckBySeason"):
            print(k)
            items = v.items() if isinstance(v, dict) else v
            for a, b in items:
                print("   ", a, b)
        else:
            print(f"{k}: {v}")
