"""Append the week (WEEK env) to both season ledgers: rows, totals, awards, graded calls,
and the new calls with machine-checkable check blocks. Safe to run twice."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "Kent Frenger",
        "worstOwner": "Scott Reisert",
        "startOfWeek": "Adam Hershberger",
        "sitOfWeek": "Doug Fields",
        "wasteOfWeek": "Spencer Lentz",
    },
    "foh": {
        "ownerOfWeek": "Aron Rogers",
        "worstOwner": "Matt Davis",
        "startOfWeek": "Ryan Kelly",
        "sitOfWeek": "Bob Dorsch",
        "wasteOfWeek": "Spencer Lentz",
    },
}

NEW = {
    "dlffl": [
        ("Beth Couture", "Mama Beth beats Adam Hershberger.",
         7, {"type": "h2h", "winner": "Beth Couture", "loser": "Adam Hershberger", "week": 7}),
        ("Adam Hershberger", "Malik Nabers clears 20 again for Adam Hershberger.",
         7, {"type": "playerAtLeast", "owner": "Adam Hershberger", "week": 7, "player": "Malik Nabers", "value": 20}),
        ("Doug Fields", "Doug Fields starts Tre Tucker in Week 7.",
         7, {"type": "startsPlayer", "owner": "Doug Fields", "week": 7, "player": "Tre Tucker"}),
        ("dennis couture", "DA beats Doug Fields with Aaron Rodgers at quarterback.",
         7, {"type": "winWithStarter", "owner": "dennis couture", "week": 7, "player": "Aaron Rodgers"}),
        ("Spencer Lentz", "Spencer Lentz beats Ryan Reed by twenty or more.",
         7, {"type": "winsByAtLeast", "owner": "Spencer Lentz", "week": 7, "value": 20}),
        ("Ryan Reed", "Jaxon Smith-Njigba clears 20 again for Ryan Reed.",
         7, {"type": "playerAtLeast", "owner": "Ryan Reed", "week": 7, "player": "Jaxon Smith-Njigba", "value": 20}),
        ("Casey Couture", "Casey Couture beats Adam Calvelage for the sixth straight time.",
         7, {"type": "h2h", "winner": "Casey Couture", "loser": "Adam Calvelage", "week": 7}),
        ("Adam Calvelage", "Brock Purdy clears 20 for Adam Calvelage.",
         7, {"type": "playerAtLeast", "owner": "Adam Calvelage", "week": 7, "player": "Brock Purdy", "value": 20}),
        ("Scott Reisert", "Scott Reisert clears 120 in Week 7.",
         7, {"type": "scoreAtLeast", "owner": "Scott Reisert", "week": 7, "value": 120}),
        ("Scott Howard", "Scott Howard beats Scott Reisert.",
         7, {"type": "h2h", "winner": "Scott Howard", "loser": "Scott Reisert", "week": 7}),
        ("Geoff Cavender", "Geoff Cavender beats Kent Frenger for the first time.",
         7, {"type": "h2h", "winner": "Geoff Cavender", "loser": "Kent Frenger", "week": 7}),
        ("Kent Frenger", "Kent Frenger starts Tyler Shough in Week 7.",
         7, {"type": "startsPlayer", "owner": "Kent Frenger", "week": 7, "player": "Tyler Shough"}),
    ],
    "foh": [
        ("Bob Dorsch", "Bob Dorsch starts Germie Bernard in Week 7, bye or no bye.",
         7, {"type": "startsPlayer", "owner": "Bob Dorsch", "week": 7, "player": "Germie Bernard"}),
        ("Rahul Pahuja", "Rahul Pahuja starts C.J. Stroud in Week 7.",
         7, {"type": "startsPlayer", "owner": "Rahul Pahuja", "week": 7, "player": "C.J. Stroud"}),
        ("Matt Davis", "Matt Davis beats Rahul Pahuja.",
         7, {"type": "h2h", "winner": "Matt Davis", "loser": "Rahul Pahuja", "week": 7}),
        ("Michael Smith", "Michael Smith beats Eric Olson.",
         7, {"type": "h2h", "winner": "Michael Smith", "loser": "Eric Olson", "week": 7}),
        ("Eric Olson", "Eric Olson clears 100 in Week 7.",
         7, {"type": "scoreAtLeast", "owner": "Eric Olson", "week": 7, "value": 100}),
        ("Billy Norton", "Billy Norton beats Spencer Lentz for the fourth straight time.",
         7, {"type": "h2h", "winner": "Billy Norton", "loser": "Spencer Lentz", "week": 7}),
        ("Spencer Lentz", "Spencer Lentz leaves under ten on his bench in Week 7.",
         7, {"type": "benchUnder", "owner": "Spencer Lentz", "week": 7, "value": 10}),
        ("Aaron Jezioro", "Aaron Jezioro clears 100 in Week 7.",
         7, {"type": "scoreAtLeast", "owner": "Aaron Jezioro", "week": 7, "value": 100}),
        ("Aron Rogers", "Aron Rogers beats Aaron Jezioro for the ninth straight time.",
         7, {"type": "h2h", "winner": "Aron Rogers", "loser": "Aaron Jezioro", "week": 7}),
        ("Michael Turner", "Michael Turner beats Ryan Kelly.",
         7, {"type": "h2h", "winner": "Michael Turner", "loser": "Ryan Kelly", "week": 7}),
        ("Ryan Kelly", "Ryan Kelly clears 90 in Week 7.",
         7, {"type": "scoreAtLeast", "owner": "Ryan Kelly", "week": 7, "value": 90}),
    ],
}

UPDATED = "2026-10-20"

NOTE = {
    "dlffl": (
        "Week 6 published 2026-10-20, on time. Boomer went 4 and 8 and is 27 and 33 on the season. Boomer runs "
        "at full heat. Grade every call that resolves at the TOP of the next issue, right or wrong, before "
        "anything else, then make a new call on every team at the bottom."
    ),
    "foh": (
        "Week 6 published 2026-10-20, on time. Boomer went 5 and 6 and is 21 and 32 on the season, with one call "
        "still open: Michael Turner loses by under five before Halloween (resolves by Week 8). Grade every call "
        "that resolves at the TOP of the next issue, right or wrong, before anything else, then make a new call "
        "on every team at the bottom."
    ),
}


def run(league):
    facts = load(f"{league}_wk{os.environ.get('WEEK', '6')}_facts.json")
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
