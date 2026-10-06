"""Append the current season's finished weeks (before WEEK) to the rebuilt baselines, so every rank
the engine prints already counts this season's earlier games. Run after games.py and playerweeks.py:

    python3 gen2/append_current.py <week>

Games come from docs/data/<league>_wk<k>_facts.json. Player-weeks come from the facts file when it
carries full lineups (Week 4 on), otherwise from gen2/lineups_2026_wk1to3.json (pulled 2026-10-06).
Idempotent: any existing rows for the season are dropped first.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "docs", "data")
PW = os.path.join(HERE, "data")
SEASON = 2026
POS = {1: "QB", 2: "RB", 3: "WR", 4: "TE", 5: "K", 16: "DST"}


def norm(n):
    return n.title() if (n.isupper() or n.islower()) and " " in n else n


def main(week):
    early = json.load(open(os.path.join(HERE, "lineups_2026_wk1to3.json")))
    for lg in ("dlffl", "foh"):
        gp = os.path.join(PW, f"{lg}_games.json")
        G = json.load(open(gp))
        G["games"] = [g for g in G["games"] if g["year"] != SEASON]
        pp = os.path.join(PW, f"{lg}_playerweeks.json")
        P = json.load(open(pp))
        P["rows"] = [r for r in P["rows"] if r[0] != SEASON]
        ng = npw = 0
        for k in range(1, week):
            f = json.load(open(os.path.join(DATA, f"{lg}_wk{k}_facts.json")))
            for m in f["matchups"]:
                w = "tie" if m["winnerId"] is None else ("home" if m["winnerId"] == m["homeId"] else "away")
                G["games"].append({"year": SEASON, "period": k, "playoff": False, "tier": "NONE", "weeks": 1,
                                   "home": norm(m["homeOwner"]), "homeTeam": m["home"], "homeScore": m["homeScore"],
                                   "away": norm(m["awayOwner"]), "awayTeam": m["away"], "awayScore": m["awayScore"],
                                   "winner": w})
                ng += 1
            byes = {b["owner"] for b in f.get("byes", [])}
            if f["perTeam"] and "starters" in f["perTeam"][0]:
                for t in f["perTeam"]:
                    if t["owner"] in byes:
                        continue
                    for st, key in ((1, "starters"), (0, "bench")):
                        for p in t[key]:
                            P["rows"].append([SEASON, k, norm(t["owner"]), p["n"],
                                              "DST" if p["pos"] == "D/ST" else p["pos"], st, p["pts"], p.get("proj")])
                            npw += 1
            else:
                scores = {t["owner"]: t["score"] for t in f["perTeam"]}
                for m in early[lg][str(k)]:
                    if len(m["sides"]) < 2:
                        continue
                    for s in m["sides"]:
                        tot = 0
                        for n, pos, slot, pts, proj in s["roster"]:
                            if pts is None:
                                continue
                            st = 0 if slot in (20, 21) else 1
                            tot += pts if st else 0
                            P["rows"].append([SEASON, k, norm(s["owner"]), n, POS.get(pos, "?"), st, round(pts, 2),
                                              round(proj, 2) if proj is not None else None])
                            npw += 1
                        assert abs(tot - scores[s["owner"]]) < 0.011, (lg, k, s["owner"], tot, scores[s["owner"]])
        json.dump(G, open(gp, "w"), separators=(",", ":"))
        json.dump(P, open(pp, "w"), separators=(",", ":"))
        print(lg, "appended", ng, "games,", npw, "player-weeks for", SEASON, "weeks 1 to", week - 1)


if __name__ == "__main__":
    main(int(sys.argv[1]))
