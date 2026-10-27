"""Append the week (WEEK env) to both season ledgers: rows, totals, awards, graded calls,
and the new calls with machine-checkable check blocks. Safe to run twice."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "Scott Howard",
        "worstOwner": "dennis couture",
        "startOfWeek": "Kent Frenger",
        "sitOfWeek": "Ryan Reed",
        "wasteOfWeek": "Spencer Lentz",
    },
    "foh": {
        "ownerOfWeek": "Matt Davis",
        "worstOwner": "Aaron Jezioro",
        "startOfWeek": "Aron Rogers",
        "sitOfWeek": "Michael Turner",
        "wasteOfWeek": "Ryan Kelly",
    },
}

NEW = {
    "dlffl": [
        ("Scott Howard", "Scott Howard beats Spencer Lentz.",
         8, {"type": "h2h", "winner": "Scott Howard", "loser": "Spencer Lentz", "week": 8}),
        ("Spencer Lentz", "Drake Maye clears 25 again for Spencer Lentz.",
         8, {"type": "playerAtLeast", "owner": "Spencer Lentz", "week": 8, "player": "Drake Maye", "value": 25}),
        ("Adam Hershberger", "Adam Hershberger beats DA for the fourth straight time.",
         8, {"type": "h2h", "winner": "Adam Hershberger", "loser": "dennis couture", "week": 8}),
        ("dennis couture", "Josh Allen clears 25 for DA.",
         8, {"type": "playerAtLeast", "owner": "dennis couture", "week": 8, "player": "Josh Allen", "value": 25}),
        ("Beth Couture", "Mama Beth starts Omar Cooper Jr. in Week 8.",
         8, {"type": "startsPlayer", "owner": "Beth Couture", "week": 8, "player": "Omar Cooper Jr."}),
        ("Ryan Reed", "Ryan Reed starts Bo Nix in Week 8.",
         8, {"type": "startsPlayer", "owner": "Ryan Reed", "week": 8, "player": "Bo Nix"}),
        ("Adam Calvelage", "Adam Calvelage beats Doug Fields.",
         8, {"type": "h2h", "winner": "Adam Calvelage", "loser": "Doug Fields", "week": 8}),
        ("Doug Fields", "Doug Fields scores between 92 and 106 again.",
         8, {"type": "scoreBetween", "owner": "Doug Fields", "week": 8, "low": 92, "high": 106}),
        ("Kent Frenger", "Kent Frenger beats Casey Couture.",
         8, {"type": "h2h", "winner": "Kent Frenger", "loser": "Casey Couture", "week": 8}),
        ("Casey Couture", "Casey Couture leaves under five on his bench again.",
         8, {"type": "benchUnder", "owner": "Casey Couture", "week": 8, "value": 5}),
        ("Geoff Cavender", "Geoff Cavender beats Scott Reisert.",
         8, {"type": "h2h", "winner": "Geoff Cavender", "loser": "Scott Reisert", "week": 8}),
        ("Scott Reisert", "Scott Reisert leaves under five on his bench in Week 8.",
         8, {"type": "benchUnder", "owner": "Scott Reisert", "week": 8, "value": 5}),
    ],
    "foh": [
        ("Matt Davis", "Matt Davis clears 130 on his bye.",
         8, {"type": "scoreAtLeast", "owner": "Matt Davis", "week": 8, "value": 130}),
        ("Eric Olson", "Eric Olson beats Bob Dorsch.",
         8, {"type": "h2h", "winner": "Eric Olson", "loser": "Bob Dorsch", "week": 8}),
        ("Bob Dorsch", "Bob Dorsch starts Rhamondre Stevenson in Week 8.",
         8, {"type": "startsPlayer", "owner": "Bob Dorsch", "week": 8, "player": "Rhamondre Stevenson"}),
        ("Spencer Lentz", "Spencer Lentz beats Rahul Pahuja.",
         8, {"type": "h2h", "winner": "Spencer Lentz", "loser": "Rahul Pahuja", "week": 8}),
        ("Rahul Pahuja", "Rahul Pahuja leaves under ten on his bench in Week 8.",
         8, {"type": "benchUnder", "owner": "Rahul Pahuja", "week": 8, "value": 10}),
        ("Aron Rogers", "Tony Pollard clears 20 again for Aron Rogers.",
         8, {"type": "playerAtLeast", "owner": "Aron Rogers", "week": 8, "player": "Tony Pollard", "value": 20}),
        ("Michael Smith", "Michael Smith beats Aron Rogers.",
         8, {"type": "h2h", "winner": "Michael Smith", "loser": "Aron Rogers", "week": 8}),
        ("Ryan Kelly", "Ryan Kelly beats Billy Norton.",
         8, {"type": "h2h", "winner": "Ryan Kelly", "loser": "Billy Norton", "week": 8}),
        ("Billy Norton", "Billy Norton clears 90 in Week 8.",
         8, {"type": "scoreAtLeast", "owner": "Billy Norton", "week": 8, "value": 90}),
        ("Michael Turner", "Michael Turner beats Aaron Jezioro and takes the lead in the series.",
         8, {"type": "h2h", "winner": "Michael Turner", "loser": "Aaron Jezioro", "week": 8}),
        ("Aaron Jezioro", "Aaron Jezioro starts Ja'Marr Chase in Week 8.",
         8, {"type": "startsPlayer", "owner": "Aaron Jezioro", "week": 8, "player": "Ja'Marr Chase"}),
    ],
}

UPDATED = "2026-10-27"

NOTE = {
    "dlffl": (
        "Week 7 published 2026-10-27, on time, the halfway mark. Boomer went 4 and 8 and is 31 and 41 on the season. "
        "Boomer runs at full heat. New HALFTIME segment this week (gen2/halftime.py). Grade every call that resolves "
        "at the TOP of the next issue, right or wrong, before anything else, then make a new call on every team at "
        "the bottom."
    ),
    "foh": (
        "Week 7 published 2026-10-27, on time, the halfway mark. Boomer went 5 and 7 and is 26 and 39 on the season; "
        "the Turner Halloween call from Week 1 closed WRONG this week (no Week 8 game ends before Halloween). New "
        "HALFTIME segment this week (gen2/halftime.py). Grade every call that resolves at the TOP of the next issue, "
        "right or wrong, before anything else, then make a new call on every team at the bottom."
    ),
}


def run(league):
    facts = load(f"{league}_wk{os.environ.get('WEEK', '7')}_facts.json")
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
