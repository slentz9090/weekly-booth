"""Append the week (WEEK env) to both season ledgers: rows, totals, awards, graded calls,
and the new calls with machine-checkable check blocks. Safe to run twice."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "Spencer Lentz",
        "worstOwner": "Casey Couture",
        "startOfWeek": "Adam Calvelage",
        "sitOfWeek": "Scott Howard",
        "wasteOfWeek": "Spencer Lentz",
    },
    "foh": {
        "ownerOfWeek": "Michael Smith",
        "worstOwner": "Aaron Jezioro",
        "startOfWeek": "Matt Davis",
        "sitOfWeek": "Rahul Pahuja",
        "wasteOfWeek": "Spencer Lentz",
    },
}

NEW = {
    "dlffl": [
        ("dennis couture", "DA hands Geoff Cavender his first loss.",
         5, {"type": "h2h", "winner": "dennis couture", "loser": "Geoff Cavender", "week": 5}),
        ("Geoff Cavender", "Geoff Cavender starts Matthew Stafford in Week 5.",
         5, {"type": "startsPlayer", "owner": "Geoff Cavender", "week": 5, "player": "Matthew Stafford"}),
        ("Spencer Lentz", "Spencer Lentz leaves under twenty on his bench in Week 5.",
         5, {"type": "benchUnder", "owner": "Spencer Lentz", "week": 5, "value": 20}),
        ("Adam Hershberger", "Malik Nabers clears 15 again for Adam Hershberger.",
         5, {"type": "playerAtLeast", "owner": "Adam Hershberger", "week": 5, "player": "Malik Nabers", "value": 15}),
        ("Casey Couture", "Casey Couture beats Doug Fields.",
         5, {"type": "h2h", "winner": "Casey Couture", "loser": "Doug Fields", "week": 5}),
        ("Doug Fields", "Doug Fields clears 100 in Week 5.",
         5, {"type": "scoreAtLeast", "owner": "Doug Fields", "week": 5, "value": 100}),
        ("Scott Reisert", "Scott Reisert beats Mama Beth by twenty or more.",
         5, {"type": "winsByAtLeast", "owner": "Scott Reisert", "week": 5, "value": 20}),
        ("Beth Couture", "Mama Beth clears 90 in Week 5.",
         5, {"type": "scoreAtLeast", "owner": "Beth Couture", "week": 5, "value": 90}),
        ("Ryan Reed", "Ryan Reed beats Kent Frenger.",
         5, {"type": "h2h", "winner": "Ryan Reed", "loser": "Kent Frenger", "week": 5}),
        ("Kent Frenger", "Kent Frenger clears 110 in Week 5.",
         5, {"type": "scoreAtLeast", "owner": "Kent Frenger", "week": 5, "value": 110}),
        ("Scott Howard", "Scott Howard wins his first game of the season.",
         5, {"type": "h2h", "winner": "Scott Howard", "loser": "Adam Calvelage", "week": 5}),
        ("Adam Calvelage", "CeeDee Lamb clears 20 again for Adam Calvelage.",
         5, {"type": "playerAtLeast", "owner": "Adam Calvelage", "week": 5, "player": "CeeDee Lamb", "value": 20}),
    ],
    "foh": [
        ("Eric Olson", "Eric Olson beats Ryan Kelly.",
         5, {"type": "h2h", "winner": "Eric Olson", "loser": "Ryan Kelly", "week": 5}),
        ("Ryan Kelly", "Ryan Kelly clears 80 in Week 5.",
         5, {"type": "scoreAtLeast", "owner": "Ryan Kelly", "week": 5, "value": 80}),
        ("Spencer Lentz", "Spencer Lentz starts Drake Maye in Week 5.",
         5, {"type": "startsPlayer", "owner": "Spencer Lentz", "week": 5, "player": "Drake Maye"}),
        ("Aron Rogers", "Aron Rogers leaves under ten on his bench for the fifth straight week.",
         5, {"type": "benchUnder", "owner": "Aron Rogers", "week": 5, "value": 10}),
        ("Matt Davis", "Matt Davis clears 120 for the fourth straight week.",
         5, {"type": "scoreAtLeast", "owner": "Matt Davis", "week": 5, "value": 120}),
        ("Michael Turner", "Michael Turner clears 110 in Week 5.",
         5, {"type": "scoreAtLeast", "owner": "Michael Turner", "week": 5, "value": 110}),
        ("Billy Norton", "Billy Norton clears 90 in Week 5.",
         5, {"type": "scoreAtLeast", "owner": "Billy Norton", "week": 5, "value": 90}),
        ("Rahul Pahuja", "Rahul Pahuja starts Kyle Monangai in Week 5.",
         5, {"type": "startsPlayer", "owner": "Rahul Pahuja", "week": 5, "player": "Kyle Monangai"}),
        ("Aaron Jezioro", "Aaron Jezioro leaves under fifteen on his bench in Week 5.",
         5, {"type": "benchUnder", "owner": "Aaron Jezioro", "week": 5, "value": 15}),
        ("Bob Dorsch", "Bob Dorsch beats Aaron Jezioro.",
         5, {"type": "h2h", "winner": "Bob Dorsch", "loser": "Aaron Jezioro", "week": 5}),
        ("Michael Smith", "Michael Smith clears 110 on his bye.",
         5, {"type": "scoreAtLeast", "owner": "Michael Smith", "week": 5, "value": 110}),
    ],
}

UPDATED = "2026-10-06"

NOTE = {
    "dlffl": (
        "Week 4 published 2026-10-06, on time. Boomer went 7 and 5, his first winning week, and is 17 and 19 on "
        "the season. Grade every call that resolves at the TOP of the next issue, right or wrong, before anything "
        "else, then make a new call on every team at the bottom."
    ),
    "foh": (
        "Week 4 published 2026-10-06, on time. Boomer went 4 and 7 and is 11 and 20 on the season, with one call "
        "still open: Michael Turner loses by under five before Halloween. He lost by 5.08 in Week 4, eight "
        "hundredths over. Eric Olson's OpenAI agent picked Spencer Lentz to beat Olson and was right by 57.48; "
        "Boomer had Olson. Grade every call that resolves at the TOP of the next issue, right or wrong, before "
        "anything else, then make a new call on every team at the bottom."
    ),
}


def run(league):
    facts = load(f"{league}_wk{os.environ.get('WEEK', '4')}_facts.json")
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
