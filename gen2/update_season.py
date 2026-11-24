"""Append the week (WEEK env) to both season ledgers: rows, totals, awards, graded calls,
and the new calls with machine-checkable check blocks. Safe to run twice."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "Scott Reisert",
        "worstOwner": "Doug Fields",
        "startOfWeek": "Scott Howard",
        "sitOfWeek": "Geoff Cavender",
        "wasteOfWeek": "Adam Calvelage",
    },
    "foh": {
        "ownerOfWeek": "Matt Davis",
        "worstOwner": "Michael Turner",
        "startOfWeek": "Michael Smith",
        "sitOfWeek": "Billy Norton",
        "wasteOfWeek": "Spencer Lentz",
    },
}

NEW = {
    "dlffl": [
        ("Spencer Lentz", "C.J. Stroud starts for Spencer Lentz in Week 12.",
         12, {"type": "startsPlayer", "owner": "Spencer Lentz", "week": 12, "player": "C.J. Stroud"}),
        ("dennis couture", "DA beats Spencer Lentz.",
         12, {"type": "h2h", "winner": "dennis couture", "loser": "Spencer Lentz", "week": 12}),
        ("Kent Frenger", "Kent Frenger beats Adam Hershberger.",
         12, {"type": "h2h", "winner": "Kent Frenger", "loser": "Adam Hershberger", "week": 12}),
        ("Adam Hershberger", "Trevor Lawrence clears 20 for Adam Hershberger.",
         12, {"type": "playerAtLeast", "owner": "Adam Hershberger", "week": 12, "player": "Trevor Lawrence", "value": 20}),
        ("Scott Howard", "Scott Howard beats Geoff Cavender.",
         12, {"type": "h2h", "winner": "Scott Howard", "loser": "Geoff Cavender", "week": 12}),
        ("Geoff Cavender", "George Pickens clears 15 for Geoff Cavender.",
         12, {"type": "playerAtLeast", "owner": "Geoff Cavender", "week": 12, "player": "George Pickens", "value": 15}),
        ("Scott Reisert", "Scott Reisert beats Adam Calvelage.",
         12, {"type": "h2h", "winner": "Scott Reisert", "loser": "Adam Calvelage", "week": 12}),
        ("Adam Calvelage", "Jonah Coleman clears 15 for Adam Calvelage.",
         12, {"type": "playerAtLeast", "owner": "Adam Calvelage", "week": 12, "player": "Jonah Coleman", "value": 15}),
        ("Casey Couture", "Casey Couture beats Ryan Reed.",
         12, {"type": "h2h", "winner": "Casey Couture", "loser": "Ryan Reed", "week": 12}),
        ("Ryan Reed", "Ryan Reed scores 95 or more in Week 12.",
         12, {"type": "scoreAtLeast", "owner": "Ryan Reed", "week": 12, "value": 95}),
        ("Beth Couture", "Mama Beth beats Doug Fields.",
         12, {"type": "h2h", "winner": "Beth Couture", "loser": "Doug Fields", "week": 12}),
        ("Doug Fields", "Doug Fields scores 90 or more in Week 12.",
         12, {"type": "scoreAtLeast", "owner": "Doug Fields", "week": 12, "value": 90}),
    ],
    "foh": [
        ("Michael Turner", "Michael Turner clears 80 in Week 12.",
         12, {"type": "scoreAtLeast", "owner": "Michael Turner", "week": 12, "value": 80}),
        ("Aron Rogers", "Aron Rogers beats Michael Turner.",
         12, {"type": "h2h", "winner": "Aron Rogers", "loser": "Michael Turner", "week": 12}),
        ("Matt Davis", "Matt Davis beats Michael Smith.",
         12, {"type": "h2h", "winner": "Matt Davis", "loser": "Michael Smith", "week": 12}),
        ("Michael Smith", "Dak Prescott clears 25 again for Michael Smith.",
         12, {"type": "playerAtLeast", "owner": "Michael Smith", "week": 12, "player": "Dak Prescott", "value": 25}),
        ("Rahul Pahuja", "Rahul Pahuja beats Bob Dorsch.",
         12, {"type": "h2h", "winner": "Rahul Pahuja", "loser": "Bob Dorsch", "week": 12}),
        ("Bob Dorsch", "Bob Dorsch scores 100 or more in Week 12.",
         12, {"type": "scoreAtLeast", "owner": "Bob Dorsch", "week": 12, "value": 100}),
        ("Eric Olson", "Josh Allen clears 20 for Eric Olson.",
         12, {"type": "playerAtLeast", "owner": "Eric Olson", "week": 12, "player": "Josh Allen", "value": 20}),
        ("Billy Norton", "Ladd McConkey starts for Billy Norton in Week 12.",
         12, {"type": "startsPlayer", "owner": "Billy Norton", "week": 12, "player": "Ladd McConkey"}),
        ("Aaron Jezioro", "Brock Purdy clears 20 again for Aaron Jezioro.",
         12, {"type": "playerAtLeast", "owner": "Aaron Jezioro", "week": 12, "player": "Brock Purdy", "value": 20}),
        ("Spencer Lentz", "Spencer Lentz leaves under ten on his bench in Week 12.",
         12, {"type": "benchUnder", "owner": "Spencer Lentz", "week": 12, "value": 10}),
        ("Ryan Kelly", "Ryan Kelly clears 100 on his bye.",
         12, {"type": "scoreAtLeast", "owner": "Ryan Kelly", "week": 12, "value": 100}),
    ],
}

UPDATED = "2026-11-24"

NOTE = {
    "dlffl": (
        "Week 11 published 2026-11-24. Boomer went 4 and 8 and is 50 and 70 on the season. Boomer runs at full heat. "
        "THE RACE (gen2/race.py, FantasyPros playoff and title odds) runs after the Scoreboard through the playoff cut. "
        "No series line on the cards and no Owner Spotlight (both pulled after Week 8). Mama Beth is never the headline, "
        "Worst Owner or a jab target. Grade every call that resolves at the TOP of the next issue, right or wrong, "
        "before anything else, then make a new call on every team at the bottom."
    ),
    "foh": (
        "Week 11 published 2026-11-24. Boomer went 8 and 3 and is 53 and 56 on the season. THE RACE (gen2/race.py, "
        "FantasyPros playoff and title odds) runs after the Scoreboard through the playoff cut. No series line on the "
        "cards and no Owner Spotlight (both pulled after Week 8). Grade every call that resolves at the TOP of the next "
        "issue, right or wrong, before anything else, then make a new call on every team at the bottom."
    ),
}


def run(league):
    facts = load(f"{league}_wk{os.environ.get('WEEK', '11')}_facts.json")
    season = load(f"{league}_season.json")
    wk = facts["week"]

    # 1. grade
    graded = {"RIGHT": 0, "WRONG": 0, "OPEN": 0}
    for p in season["predictions"]:
        if p.get("graded"):
            continue
        verdict, why = grade(p, facts)
        if verdict is None:
            graded["OPEN"] += 1
            continue
        p["graded"] = wk
        p["correct"] = verdict == "RIGHT"
        p["evidence"] = why
        graded[verdict] += 1

    # 2. weekly rows and totals
    for t in facts["perTeam"]:
        o = season["owners"].setdefault(t["owner"], {
            "team": t["name"], "display": t["owner"], "weeks": [], "totals": {
                "pointsFor": 0, "benchPoints": 0, "allPlayW": 0, "allPlayL": 0, "weeksPlayed": 0},
            "awards": {k: [] for k in AWARDS[league]},
        })
        if any(w["week"] == wk for w in o["weeks"]):
            continue
        apw, apl = (int(x) for x in t["allPlay"].split("-"))
        # all-play counts only teams that played this week (a bye score never counts, either way)
        played = {}
        for m in facts["matchups"]:
            played[m["homeOwner"]] = m["homeScore"]; played[m["awayOwner"]] = m["awayScore"]
        if facts.get("byes") and t["owner"] in played:
            me = played[t["owner"]]
            apw = sum(1 for o2, s2 in played.items() if o2 != t["owner"] and me > s2)
            apl = sum(1 for o2, s2 in played.items() if o2 != t["owner"] and me < s2)
        won, margin, opp = result_for(facts, t["owner"])
        row = {
            "week": wk, "score": t["score"], "benchPoints": t["left"], "optimal": t["optimal"],
            "allPlayW": apw, "allPlayL": apl,
            "result": "bye" if won is None else ("won" if won else "lost"),
            "margin": margin, "opponent": opp,
        }
        if t.get("worst"):
            row["worstSit"] = {
                "benched": t["worst"]["benched"], "pts": t["worst"]["benchedPts"],
                "started": t["worst"]["started"], "startedPts": t["worst"]["startedPts"],
                "cost": t["worst"]["delta"],
            }
        o["weeks"].append(row)
        tot = o["totals"]
        tot["pointsFor"] = round(tot["pointsFor"] + t["score"], 2)
        tot["benchPoints"] = round(tot["benchPoints"] + t["left"], 2)
        tot["allPlayW"] += apw
        tot["allPlayL"] += apl
        tot["weeksPlayed"] += 1

    # 3. awards (PHASE=rows stops after grading and rows, so the scan can see the week before the
    #    booth has picked awards or made calls; the full run afterwards is safe to repeat)
    rows_only = os.environ.get("PHASE") == "rows"
    for kind, owner in ({} if rows_only else AWARDS[league]).items():
        aw = season["owners"][owner].setdefault("awards", {})
        aw.setdefault(kind, [])
        if wk not in aw[kind]:
            aw[kind].append(wk)

    # 4. new calls
    n = max((p["n"] for p in season["predictions"]), default=0)
    have = {(p["week"], p["owner"], p["call"]) for p in season["predictions"]}
    for owner, call, resolves, check in ([] if rows_only else NEW[league]):
        if (wk, owner, call) in have:
            continue                      # idempotent: a second run never appends the calls twice
        n += 1
        season["predictions"].append({
            "n": n, "week": wk, "by": "Boomer", "owner": owner, "call": call,
            "resolvesWeek": resolves, "graded": None, "correct": None, "check": check,
        })

    season["throughWeek"] = wk
    season["updated"] = UPDATED
    if not rows_only:
        season["note"] = NOTE[league]
    season["record"] = {
        "graded": sum(1 for p in season["predictions"] if p.get("graded")),
        "right": sum(1 for p in season["predictions"] if p.get("correct") is True),
        "wrong": sum(1 for p in season["predictions"] if p.get("correct") is False),
        "open": sum(1 for p in season["predictions"] if p.get("graded") is None),
    }
    with open(os.path.join(DATA, f"{league}_season.json"), "w", encoding="utf-8") as fh:
        json.dump(season, fh, indent=1)
    print(league, "graded", graded, "record", season["record"], "owners", len(season["owners"]))


if __name__ == "__main__":
    for lg in ("dlffl", "foh"):
        run(lg)
