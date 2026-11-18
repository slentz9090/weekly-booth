"""Append the week (WEEK env) to both season ledgers: rows, totals, awards, graded calls,
and the new calls with machine-checkable check blocks. Safe to run twice."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "dennis couture",
        "worstOwner": "Casey Couture",
        "startOfWeek": "Geoff Cavender",
        "sitOfWeek": "Adam Hershberger",
        "wasteOfWeek": "Spencer Lentz",
    },
    "foh": {
        "ownerOfWeek": "Rahul Pahuja",
        "worstOwner": "Michael Turner",
        "startOfWeek": "Aron Rogers",
        "sitOfWeek": "Billy Norton",
        "wasteOfWeek": "Michael Smith",
    },
}

NEW = {
    "dlffl": [
        ("Spencer Lentz", "C.J. Stroud clears 20 for Spencer Lentz.",
         11, {"type": "playerAtLeast", "owner": "Spencer Lentz", "week": 11, "player": "C.J. Stroud", "value": 20}),
        ("Doug Fields", "Doug Fields beats Spencer Lentz.",
         11, {"type": "h2h", "winner": "Doug Fields", "loser": "Spencer Lentz", "week": 11}),
        ("Kent Frenger", "Kent Frenger beats Adam Calvelage.",
         11, {"type": "h2h", "winner": "Kent Frenger", "loser": "Adam Calvelage", "week": 11}),
        ("Adam Calvelage", "Brock Purdy clears 20 again for Adam Calvelage.",
         11, {"type": "playerAtLeast", "owner": "Adam Calvelage", "week": 11, "player": "Brock Purdy", "value": 20}),
        ("Ryan Reed", "Ryan Reed beats Geoff Cavender.",
         11, {"type": "h2h", "winner": "Ryan Reed", "loser": "Geoff Cavender", "week": 11}),
        ("Geoff Cavender", "Amon-Ra St. Brown clears 15 for Geoff Cavender.",
         11, {"type": "playerAtLeast", "owner": "Geoff Cavender", "week": 11, "player": "Amon-Ra St. Brown", "value": 15}),
        ("dennis couture", "DA beats Scott Reisert.",
         11, {"type": "h2h", "winner": "dennis couture", "loser": "Scott Reisert", "week": 11}),
        ("Scott Reisert", "Jahmyr Gibbs clears 20 again for Scott Reisert.",
         11, {"type": "playerAtLeast", "owner": "Scott Reisert", "week": 11, "player": "Jahmyr Gibbs", "value": 20}),
        ("Beth Couture", "Mama Beth beats Casey Couture.",
         11, {"type": "h2h", "winner": "Beth Couture", "loser": "Casey Couture", "week": 11}),
        ("Casey Couture", "Casey Couture scores 90 or more in Week 11.",
         11, {"type": "scoreAtLeast", "owner": "Casey Couture", "week": 11, "value": 90}),
        ("Scott Howard", "Scott Howard beats Adam Hershberger.",
         11, {"type": "h2h", "winner": "Scott Howard", "loser": "Adam Hershberger", "week": 11}),
        ("Adam Hershberger", "Chase Brown starts for Adam Hershberger in Week 11.",
         11, {"type": "startsPlayer", "owner": "Adam Hershberger", "week": 11, "player": "Chase Brown"}),
    ],
    "foh": [
        ("Spencer Lentz", "Patrick Mahomes clears 25 for Spencer Lentz.",
         11, {"type": "playerAtLeast", "owner": "Spencer Lentz", "week": 11, "player": "Patrick Mahomes", "value": 25}),
        ("Ryan Kelly", "Caleb Williams starts for Ryan Kelly in Week 11.",
         11, {"type": "startsPlayer", "owner": "Ryan Kelly", "week": 11, "player": "Caleb Williams"}),
        ("Eric Olson", "Eric Olson beats Michael Turner.",
         11, {"type": "h2h", "winner": "Eric Olson", "loser": "Michael Turner", "week": 11}),
        ("Michael Turner", "Michael Turner clears 90 in Week 11.",
         11, {"type": "scoreAtLeast", "owner": "Michael Turner", "week": 11, "value": 90}),
        ("Matt Davis", "Matt Davis beats Aaron Jezioro.",
         11, {"type": "h2h", "winner": "Matt Davis", "loser": "Aaron Jezioro", "week": 11}),
        ("Aaron Jezioro", "Ja'Marr Chase clears 20 again for Aaron Jezioro.",
         11, {"type": "playerAtLeast", "owner": "Aaron Jezioro", "week": 11, "player": "Ja'Marr Chase", "value": 20}),
        ("Billy Norton", "Billy Norton beats Bob Dorsch.",
         11, {"type": "h2h", "winner": "Billy Norton", "loser": "Bob Dorsch", "week": 11}),
        ("Bob Dorsch", "Saquon Barkley clears 12 for Bob Dorsch.",
         11, {"type": "playerAtLeast", "owner": "Bob Dorsch", "week": 11, "player": "Saquon Barkley", "value": 12}),
        ("Rahul Pahuja", "Rahul Pahuja beats Michael Smith.",
         11, {"type": "h2h", "winner": "Rahul Pahuja", "loser": "Michael Smith", "week": 11}),
        ("Michael Smith", "Dak Prescott clears 25 for Michael Smith.",
         11, {"type": "playerAtLeast", "owner": "Michael Smith", "week": 11, "player": "Dak Prescott", "value": 25}),
        ("Aron Rogers", "Aron Rogers clears 130 on his bye.",
         11, {"type": "scoreAtLeast", "owner": "Aron Rogers", "week": 11, "value": 130}),
    ],
}

UPDATED = "2026-11-17"

NOTE = {
    "dlffl": (
        "Week 10 published 2026-11-17. Boomer went 4 and 8 and is 46 and 62 on the season. Boomer runs at full heat. "
        "THE RACE (gen2/race.py, FantasyPros playoff and title odds) runs after the Scoreboard through the playoff cut. "
        "No series line on the cards and no Owner Spotlight (both pulled after Week 8). Mama Beth is never the headline, "
        "Worst Owner or a jab target. Grade every call that resolves at the TOP of the next issue, right or wrong, "
        "before anything else, then make a new call on every team at the bottom."
    ),
    "foh": (
        "Week 10 published 2026-11-17. Boomer went 7 and 4 and is 45 and 53 on the season. THE RACE (gen2/race.py, "
        "FantasyPros playoff and title odds) runs after the Scoreboard through the playoff cut. No series line on the "
        "cards and no Owner Spotlight (both pulled after Week 8). Grade every call that resolves at the TOP of the next "
        "issue, right or wrong, before anything else, then make a new call on every team at the bottom."
    ),
}


def run(league):
    facts = load(f"{league}_wk{os.environ.get('WEEK', '10')}_facts.json")
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
