"""Append the week (WEEK env) to both season ledgers: rows, totals, awards, graded calls,
and the new calls with machine-checkable check blocks. Safe to run twice."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "Scott Howard",
        "worstOwner": "Ryan Reed",
        "startOfWeek": "Geoff Cavender",
        "sitOfWeek": "Spencer Lentz",
        "wasteOfWeek": "Scott Reisert",
    },
    "foh": {
        "ownerOfWeek": "Rahul Pahuja",
        "worstOwner": "Ryan Kelly",
        "startOfWeek": "Bob Dorsch",
        "sitOfWeek": "Aron Rogers",
        "wasteOfWeek": "Michael Smith",
    },
}

NEW = {
    "dlffl": [
        ("Spencer Lentz", "Spencer Lentz leaves under ten on his bench in Week 10.",
         10, {"type": "benchUnder", "owner": "Spencer Lentz", "week": 10, "value": 10}),
        ("Casey Couture", "Jonathan Taylor clears 15 for Casey Couture.",
         10, {"type": "playerAtLeast", "owner": "Casey Couture", "week": 10, "player": "Jonathan Taylor", "value": 15}),
        ("Kent Frenger", "Kenneth Walker III clears 20 again for Kent Frenger.",
         10, {"type": "playerAtLeast", "owner": "Kent Frenger", "week": 10, "player": "Kenneth Walker III", "value": 20}),
        ("dennis couture", "DA beats Kent Frenger.",
         10, {"type": "h2h", "winner": "dennis couture", "loser": "Kent Frenger", "week": 10}),
        ("Geoff Cavender", "Geoff Cavender beats Mama Beth.",
         10, {"type": "h2h", "winner": "Geoff Cavender", "loser": "Beth Couture", "week": 10}),
        ("Beth Couture", "Justin Jefferson clears 15 for Mama Beth.",
         10, {"type": "playerAtLeast", "owner": "Beth Couture", "week": 10, "player": "Justin Jefferson", "value": 15}),
        ("Scott Howard", "Scott Howard beats Ryan Reed.",
         10, {"type": "h2h", "winner": "Scott Howard", "loser": "Ryan Reed", "week": 10}),
        ("Ryan Reed", "Ryan Reed scores 90 or more in Week 10.",
         10, {"type": "scoreAtLeast", "owner": "Ryan Reed", "week": 10, "value": 90}),
        ("Adam Calvelage", "CeeDee Lamb clears 20 again for Adam Calvelage.",
         10, {"type": "playerAtLeast", "owner": "Adam Calvelage", "week": 10, "player": "CeeDee Lamb", "value": 20}),
        ("Adam Hershberger", "Adam Hershberger beats Adam Calvelage.",
         10, {"type": "h2h", "winner": "Adam Hershberger", "loser": "Adam Calvelage", "week": 10}),
        ("Doug Fields", "Doug Fields scores between 92 and 106 in Week 10.",
         10, {"type": "scoreBetween", "owner": "Doug Fields", "week": 10, "low": 92, "high": 106}),
        ("Scott Reisert", "Scott Reisert beats Doug Fields for the first time.",
         10, {"type": "h2h", "winner": "Scott Reisert", "loser": "Doug Fields", "week": 10}),
    ],
    "foh": [
        ("Spencer Lentz", "Spencer Lentz clears 120 on his bye.",
         10, {"type": "scoreAtLeast", "owner": "Spencer Lentz", "week": 10, "value": 120}),
        ("Aron Rogers", "Aron Rogers starts Tyler Shough in Week 10.",
         10, {"type": "startsPlayer", "owner": "Aron Rogers", "week": 10, "player": "Tyler Shough"}),
        ("Eric Olson", "Eric Olson beats Aron Rogers.",
         10, {"type": "h2h", "winner": "Eric Olson", "loser": "Aron Rogers", "week": 10}),
        ("Ryan Kelly", "Ryan Kelly clears 80 in Week 10.",
         10, {"type": "scoreAtLeast", "owner": "Ryan Kelly", "week": 10, "value": 80}),
        ("Matt Davis", "Matt Davis beats Ryan Kelly.",
         10, {"type": "h2h", "winner": "Matt Davis", "loser": "Ryan Kelly", "week": 10}),
        ("Michael Turner", "Breece Hall starts for Michael Turner in Week 10.",
         10, {"type": "startsPlayer", "owner": "Michael Turner", "week": 10, "player": "Breece Hall"}),
        ("Bob Dorsch", "Bob Dorsch beats Michael Turner.",
         10, {"type": "h2h", "winner": "Bob Dorsch", "loser": "Michael Turner", "week": 10}),
        ("Aaron Jezioro", "Aaron Jezioro clears 120 for the third straight week.",
         10, {"type": "scoreAtLeast", "owner": "Aaron Jezioro", "week": 10, "value": 120}),
        ("Rahul Pahuja", "Rahul Pahuja beats Aaron Jezioro.",
         10, {"type": "h2h", "winner": "Rahul Pahuja", "loser": "Aaron Jezioro", "week": 10}),
        ("Billy Norton", "Billy Norton beats Michael Smith.",
         10, {"type": "h2h", "winner": "Billy Norton", "loser": "Michael Smith", "week": 10}),
        ("Michael Smith", "Dak Prescott clears 20 again for Michael Smith.",
         10, {"type": "playerAtLeast", "owner": "Michael Smith", "week": 10, "player": "Dak Prescott", "value": 20}),
    ],
}

UPDATED = "2026-11-10"

NOTE = {
    "dlffl": (
        "Week 9 published 2026-11-10. Boomer went 4 and 8 and is 42 and 54 on the season. Boomer runs at full heat. "
        "THE RACE (gen2/race.py, FantasyPros playoff and title odds) runs after the Scoreboard through the playoff cut. "
        "No series line on the cards and no Owner Spotlight (both pulled after Week 8). Mama Beth is never the headline, "
        "Worst Owner or a jab target. Grade every call that resolves at the TOP of the next issue, right or wrong, "
        "before anything else, then make a new call on every team at the bottom."
    ),
    "foh": (
        "Week 9 published 2026-11-10. Boomer went 4 and 7 and is 38 and 49 on the season. THE RACE (gen2/race.py, "
        "FantasyPros playoff and title odds) runs after the Scoreboard through the playoff cut. No series line on the "
        "cards and no Owner Spotlight (both pulled after Week 8). Grade every call that resolves at the TOP of the next "
        "issue, right or wrong, before anything else, then make a new call on every team at the bottom."
    ),
}


def run(league):
    facts = load(f"{league}_wk{os.environ.get('WEEK', '9')}_facts.json")
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
