"""Append the week (WEEK env) to both season ledgers: rows, totals, awards, graded calls,
and the new calls with machine-checkable check blocks. Safe to run twice."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "Spencer Lentz",
        "worstOwner": "Beth Couture",
        "startOfWeek": "dennis couture",
        "sitOfWeek": "Ryan Reed",
        "wasteOfWeek": "Scott Howard",
    },
    "foh": {
        "ownerOfWeek": "Matt Davis",
        "worstOwner": "Billy Norton",
        "startOfWeek": "Spencer Lentz",
        "sitOfWeek": "Ryan Kelly",
        "wasteOfWeek": "Eric Olson",
    },
}

NEW = {
    "dlffl": [
        ("dennis couture", "DA beats Casey Couture.",
         6, {"type": "h2h", "winner": "dennis couture", "loser": "Casey Couture", "week": 6}),
        ("Casey Couture", "Casey Couture leaves under ten on his bench in Week 6.",
         6, {"type": "benchUnder", "owner": "Casey Couture", "week": 6, "value": 10}),
        ("Spencer Lentz", "Spencer Lentz clears 150 for the third straight week.",
         6, {"type": "scoreAtLeast", "owner": "Spencer Lentz", "week": 6, "value": 150}),
        ("Beth Couture", "Mama Beth beats Spencer Lentz.",
         6, {"type": "h2h", "winner": "Beth Couture", "loser": "Spencer Lentz", "week": 6}),
        ("Adam Hershberger", "Adam Hershberger beats Doug Fields.",
         6, {"type": "h2h", "winner": "Adam Hershberger", "loser": "Doug Fields", "week": 6}),
        ("Doug Fields", "Doug Fields clears 100 in Week 6.",
         6, {"type": "scoreAtLeast", "owner": "Doug Fields", "week": 6, "value": 100}),
        ("Scott Reisert", "Scott Reisert leaves under ten on his bench in Week 6.",
         6, {"type": "benchUnder", "owner": "Scott Reisert", "week": 6, "value": 10}),
        ("Ryan Reed", "Ryan Reed beats Scott Reisert.",
         6, {"type": "h2h", "winner": "Ryan Reed", "loser": "Scott Reisert", "week": 6}),
        ("Geoff Cavender", "Geoff Cavender sets a perfect lineup again.",
         6, {"type": "benchUnder", "owner": "Geoff Cavender", "week": 6, "value": 0.01}),
        ("Adam Calvelage", "Adam Calvelage beats Geoff Cavender for the first time.",
         6, {"type": "h2h", "winner": "Adam Calvelage", "loser": "Geoff Cavender", "week": 6}),
        ("Scott Howard", "Scott Howard clears 150 again.",
         6, {"type": "scoreAtLeast", "owner": "Scott Howard", "week": 6, "value": 150}),
        ("Kent Frenger", "Tyler Shough gets back into double figures for Kent Frenger.",
         6, {"type": "playerAtLeast", "owner": "Kent Frenger", "week": 6, "player": "Tyler Shough", "value": 10}),
    ],
    "foh": [
        ("Michael Smith", "Michael Smith beats Bob Dorsch.",
         6, {"type": "h2h", "winner": "Michael Smith", "loser": "Bob Dorsch", "week": 6}),
        ("Bob Dorsch", "Bob Dorsch clears 110 in Week 6.",
         6, {"type": "scoreAtLeast", "owner": "Bob Dorsch", "week": 6, "value": 110}),
        ("Billy Norton", "Billy Norton wins his first game, over Matt Davis.",
         6, {"type": "h2h", "winner": "Billy Norton", "loser": "Matt Davis", "week": 6}),
        ("Matt Davis", "Matt Davis clears 120 for the fifth straight week.",
         6, {"type": "scoreAtLeast", "owner": "Matt Davis", "week": 6, "value": 120}),
        ("Aaron Jezioro", "Aaron Jezioro beats Eric Olson.",
         6, {"type": "h2h", "winner": "Aaron Jezioro", "loser": "Eric Olson", "week": 6}),
        ("Eric Olson", "Eric Olson leaves under fifteen on his bench in Week 6.",
         6, {"type": "benchUnder", "owner": "Eric Olson", "week": 6, "value": 15}),
        ("Michael Turner", "Michael Turner beats Spencer Lentz.",
         6, {"type": "h2h", "winner": "Michael Turner", "loser": "Spencer Lentz", "week": 6}),
        ("Spencer Lentz", "Spencer Lentz leaves under five on his bench again.",
         6, {"type": "benchUnder", "owner": "Spencer Lentz", "week": 6, "value": 5}),
        ("Ryan Kelly", "Ryan Kelly wins his first game, over Aron Rogers.",
         6, {"type": "h2h", "winner": "Ryan Kelly", "loser": "Aron Rogers", "week": 6}),
        ("Aron Rogers", "Aron Rogers leaves under ten on his bench in Week 6.",
         6, {"type": "benchUnder", "owner": "Aron Rogers", "week": 6, "value": 10}),
        ("Rahul Pahuja", "Rahul Pahuja clears 110 on his bye.",
         6, {"type": "scoreAtLeast", "owner": "Rahul Pahuja", "week": 6, "value": 110}),
    ],
}

UPDATED = "2026-10-13"

NOTE = {
    "dlffl": (
        "Week 5 published 2026-10-13, on time. Boomer went 6 and 6 and is 23 and 25 on the season. From Week 5 "
        "Boomer runs at full heat. Grade every call that resolves at the TOP of the next issue, right or wrong, "
        "before anything else, then make a new call on every team at the bottom."
    ),
    "foh": (
        "Week 5 published 2026-10-13, on time. Boomer went 5 and 6 and is 16 and 26 on the season, with one call "
        "still open: Michael Turner loses by under five before Halloween. Grade every call that resolves at the "
        "TOP of the next issue, right or wrong, before anything else, then make a new call on every team at the "
        "bottom."
    ),
}


def run(league):
    facts = load(f"{league}_wk{os.environ.get('WEEK', '5')}_facts.json")
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
