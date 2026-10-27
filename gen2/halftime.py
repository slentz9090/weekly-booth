"""HALFTIME: what the standings at the halfway mark (after Week 7) have meant in every season on record.

    python3 gen2/halftime.py <league> <week>   -> docs/data/<league>_halftime.json

Reads gen2/data/<league>_games.json (the rebuilt all-time log, regular season and playoffs),
docs/data/<league>_history.json (champions) and docs/data/<league>_wk<week>_facts.json and
<league>_season.json (this season's standings and all-play rows).

"Made the playoffs" = played a WINNERS_BRACKET game that season, which survives the field size
changing over the years. "Halfway" = standings after period 7, every season, ordered by wins then
points for. Only completed seasons count as history; the current season is never in the baseline.
"""
import json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "docs", "data")
HALF = 7


def nick(o):
    return {"Beth Couture": "Mama Beth", "dennis couture": "DA", "Dennis Couture": "DA"}.get(o, o)


def history(lg, week):
    G = json.load(open(os.path.join(HERE, "data", f"{lg}_games.json")))["games"]
    H = json.load(open(os.path.join(DATA, f"{lg}_history.json")))
    champ = {int(r[0]): r[1] for r in H["champions"] if r[1] and r[1] != "Unknown"}
    seasons = {}
    for g in G:
        y = g["year"]
        s = seasons.setdefault(y, {"rec": collections.defaultdict(lambda: [0, 0, 0.0]), "po": set(), "final": collections.defaultdict(lambda: [0, 0, 0.0])})
        if g["playoff"]:
            if g["tier"] == "WINNERS_BRACKET":
                s["po"].update([g["home"], g["away"]])
            continue
        for side, other in (("home", "away"), ("away", "home")):
            o = g[side]
            won = g["winner"] == side
            if g["period"] <= HALF:
                r = s["rec"][o]; r[0] += won; r[1] += (not won); r[2] += g[f"{side}Score"]
            r = s["final"][o]; r[0] += won; r[1] += (not won); r[2] += g[f"{side}Score"]
    out = []
    for y, s in sorted(seasons.items()):
        if y not in champ or not s["po"]:
            continue  # incomplete season (the current one) or no bracket on record
        rows = sorted(s["rec"].items(), key=lambda kv: (-kv[1][0], -kv[1][2]))
        if not rows or rows[0][1][0] + rows[0][1][1] < HALF:
            continue
        out.append({
            "year": y, "champion": champ[y], "playoffs": sorted(s["po"]),
            "half": [{"owner": o, "w": r[0], "l": r[1], "pf": round(r[2], 2), "rank": i + 1,
                      "madePlayoffs": o in s["po"], "wonTitle": o == champ[y]} for i, (o, r) in enumerate(rows)],
            "pfLeader": max(s["rec"].items(), key=lambda kv: kv[1][2])[0],
        })
    return out


def week_records(lg, week):
    """Every single-week period-<week> game on record, for 'this week in history'."""
    G = json.load(open(os.path.join(HERE, "data", f"{lg}_games.json")))["games"]
    rows = []
    for g in G:
        if g["playoff"] or g["weeks"] != 1 or g["period"] != week or g["year"] >= 2026:
            continue
        rows.append({"year": g["year"], "owner": g["home"], "score": g["homeScore"], "opp": g["away"], "oppScore": g["awayScore"]})
        rows.append({"year": g["year"], "owner": g["away"], "score": g["awayScore"], "opp": g["home"], "oppScore": g["homeScore"]})
    hi = sorted(rows, key=lambda r: -r["score"])[:3]
    lo = sorted(rows, key=lambda r: r["score"])[:3]
    wins = [r | {"margin": round(r["score"] - r["oppScore"], 2)} for r in rows if r["score"] > r["oppScore"]]
    blow = sorted(wins, key=lambda r: -r["margin"])[:3]
    close = sorted(wins, key=lambda r: r["margin"])[:3]
    return {"games": len(rows) // 2, "highest": hi, "lowest": lo, "biggestMargin": blow, "closest": close}


def main(lg, week):
    hist = history(lg, week)
    facts = json.load(open(os.path.join(DATA, f"{lg}_wk{week}_facts.json")))
    season = json.load(open(os.path.join(DATA, f"{lg}_season.json")))
    n = len(hist)
    leader_titles = sum(1 for s in hist if s["half"][0]["wonTitle"])
    leader_po = sum(1 for s in hist if s["half"][0]["madePlayoffs"])
    pf_titles = sum(1 for s in hist if s["pfLeader"] == s["champion"])
    pf_po = sum(1 for s in hist if s["pfLeader"] in s["playoffs"])
    by_rec = collections.defaultdict(lambda: {"n": 0, "po": 0, "titles": 0})
    champs_half = []
    for s in hist:
        for h in s["half"]:
            if h["w"] + h["l"] not in (6, 7):
                continue  # a bye-less double entry (one owner with two teams) is not a halfway line
            k = str(h["w"])
            by_rec[k]["n"] += 1; by_rec[k]["po"] += h["madePlayoffs"]; by_rec[k]["titles"] += h["wonTitle"]
            if h["wonTitle"]:
                champs_half.append({"year": s["year"], "owner": h["owner"], "w": h["w"], "l": h["l"], "rank": h["rank"], "pf": h["pf"]})
    worst_po = sorted([h | {"year": s["year"]} for s in hist for h in s["half"] if h["madePlayoffs"]], key=lambda h: (h["w"], h["pf"]))[:3]
    best_missed = sorted([h | {"year": s["year"]} for s in hist for h in s["half"] if not h["madePlayoffs"]], key=lambda h: (-h["w"], -h["pf"]))[:3]
    worst_champ = sorted(champs_half, key=lambda h: (h["w"], h["pf"]))[:3]
    lowest_rank_champ = max(champs_half, key=lambda h: h["rank"])
    # this season
    teams = {s["owner"]: s for s in facts["standings"]}
    # bye weeks never count in all-play (runbook convention). Week 1 rows predate the result field, so
    # the Week 1 bye comes from that week's facts file.
    wk1 = json.load(open(os.path.join(DATA, f"{lg}_wk1_facts.json")))
    b1 = wk1.get("byes") or ([wk1["bye"]] if wk1.get("bye") else [])
    wk1_byes = {b["owner"] for b in b1 if isinstance(b, dict) and b.get("owner")}
    cur = []
    for o, so in season["owners"].items():
        wk = [w for w in so["weeks"] if w.get("allPlayW") is not None and w.get("result") != "bye"
              and not (w["week"] == 1 and o in wk1_byes)]
        apw = sum(w["allPlayW"] for w in wk); apl = sum(w["allPlayL"] for w in wk)
        g = len(wk)
        st = teams.get(o)
        if not st:
            continue
        exp = apw / (apw + apl) * (st["w"] + st["l"]) if apw + apl else None
        cur.append({"owner": o, "display": nick(o), "team": st["name"], "w": st["w"], "l": st["l"], "pf": st["pf"], "seed": st["seed"],
                    "allPlayW": apw, "allPlayL": apl, "games": g, "expWins": round(exp, 2) if exp is not None else None,
                    "luck": round(st["w"] - exp, 2) if exp is not None else None,
                    "pfRank": sorted(teams.values(), key=lambda t: -t["pf"]).index(st) + 1,
                    "recKey": str(st["w"])})
    cur.sort(key=lambda c: c["seed"])
    for c in cur:
        r = by_rec.get(c["recKey"], {"n": 0, "po": 0, "titles": 0})
        c["histN"], c["histPO"], c["histTitles"] = r["n"], r["po"], r["titles"]
    out = {
        "league": lg, "week": week, "seasonsOnRecord": n, "firstYear": hist[0]["year"], "lastYear": hist[-1]["year"],
        "halfwayLeader": {"titles": leader_titles, "playoffs": leader_po, "n": n},
        "pointsLeader": {"titles": pf_titles, "playoffs": pf_po, "n": n},
        "byWins": dict(sorted(by_rec.items(), key=lambda kv: -int(kv[0]))),
        "leaderMissed": [{"year": s["year"], "owner": s["half"][0]["owner"], "w": s["half"][0]["w"], "l": s["half"][0]["l"]} for s in hist if not s["half"][0]["madePlayoffs"]],
        "lowestPfRankToMakePlayoffs": sorted([{"year": s["year"], "owner": h["owner"], "w": h["w"], "l": h["l"], "pfRank": sorted(s["half"], key=lambda x: -x["pf"]).index(h) + 1, "teams": len(s["half"])} for s in hist for h in s["half"] if h["madePlayoffs"]], key=lambda h: -h["pfRank"])[:3],
        "week7Records": week_records(lg, week),
        "championsAtHalfway": sorted(champs_half, key=lambda h: h["year"]),
        "worstHalfwayToMakePlayoffs": worst_po, "bestHalfwayToMiss": best_missed,
        "worstHalfwayChampion": worst_champ, "lowestRankedChampion": lowest_rank_champ,
        "current": cur,
    }
    json.dump(out, open(os.path.join(DATA, f"{lg}_halftime.json"), "w"), indent=1)
    print(f"{lg}: {n} seasons {hist[0]['year']}-{hist[-1]['year']}. Halfway leader won {leader_titles}, made playoffs {leader_po}. PF leader won {pf_titles}, playoffs {pf_po}.")
    for k, v in out["byWins"].items():
        print(f"  {k} wins: {v['n']} teams, playoffs {v['po']}, titles {v['titles']}")
    print("  leader missed:", out["leaderMissed"])
    print("  lowest PF rank to make playoffs:", out["lowestPfRankToMakePlayoffs"])
    print("  week 7 records:", json.dumps(out["week7Records"])[:900])
    print("  champions at halfway:", [(c['year'], c['owner'], f"{c['w']}-{c['l']}", c['rank']) for c in out['championsAtHalfway']])
    print("  worst halfway to make playoffs:", [(h['year'], h['owner'], f"{h['w']}-{h['l']}") for h in worst_po])
    print("  best halfway to miss:", [(h['year'], h['owner'], f"{h['w']}-{h['l']}", h['pf']) for h in best_missed])
    print("  2026:")
    for c in cur:
        print(f"   {c['seed']:2} {c['display']:18} {c['w']}-{c['l']} pf {c['pf']:7.2f} (#{c['pfRank']}) allplay {c['allPlayW']}-{c['allPlayL']} exp {c['expWins']} luck {c['luck']:+.2f} | hist {c['recKey']}: {c['histPO']}/{c['histN']} playoffs, {c['histTitles']} titles")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
