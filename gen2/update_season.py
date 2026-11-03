"""Append the week (WEEK env) to both season ledgers: rows, totals, awards, graded calls,
and the new calls with machine-checkable check blocks. Safe to run twice."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "Kent Frenger",
        "worstOwner": "Beth Couture",
        "startOfWeek": "Spencer Lentz",
        "sitOfWeek": "Scott Reisert",
        "wasteOfWeek": "Doug Fields",
    },
    "foh": {
        "ownerOfWeek": "Eric Olson",
        "worstOwner": "Michael Turner",
        "startOfWeek": "Ryan Kelly",
        "sitOfWeek": "Spencer Lentz",
        "wasteOfWeek": "Aron Rogers",
    },
}

NEW = {
    "dlffl": [
        ("Spencer Lentz", "Spencer Lentz beats Geoff Cavender.",
         9, {"type": "h2h", "winner": "Spencer Lentz", "loser": "Geoff Cavender", "week": 9}),
        ("Geoff Cavender", "Geoff Cavender scores 110 or more in Week 9.",
         9, {"type": "scoreAtLeast", "owner": "Geoff Cavender", "week": 9, "value": 110}),
        ("Kent Frenger", "Kent Frenger beats Doug Fields.",
         9, {"type": "h2h", "winner": "Kent Frenger", "loser": "Doug Fields", "week": 9}),
        ("Doug Fields", "Doug Fields scores between 92 and 106 again.",
         9, {"type": "scoreBetween", "owner": "Doug Fields", "week": 9, "low": 92, "high": 106}),
        ("dennis couture", "DA beats Adam Calvelage for the fifth straight time.",
         9, {"type": "h2h", "winner": "dennis couture", "loser": "Adam Calvelage", "week": 9}),
        ("Adam Calvelage", "Jayden Daniels clears 20 for Adam Calvelage.",
         9, {"type": "playerAtLeast", "owner": "Adam Calvelage", "week": 9, "player": "Jayden Daniels", "value": 20}),
        ("Scott Howard", "Scott Howard beats Mama Beth for the seventh straight time.",
         9, {"type": "h2h", "winner": "Scott Howard", "loser": "Beth Couture", "week": 9}),
        ("Beth Couture", "Mama Beth starts Tyler Allgeier in Week 9.",
         9, {"type": "startsPlayer", "owner": "Beth Couture", "week": 9, "player": "Tyler Allgeier"}),
        ("Ryan Reed", "Ryan Reed beats Adam Hershberger.",
         9, {"type": "h2h", "winner": "Ryan Reed", "loser": "Adam Hershberger", "week": 9}),
        ("Adam Hershberger", "Jameson Williams clears 15 for Adam Hershberger.",
         9, {"type": "playerAtLeast", "owner": "Adam Hershberger", "week": 9, "player": "Jameson Williams", "value": 15}),
        ("Casey Couture", "Casey Couture beats Scott Reisert.",
         9, {"type": "h2h", "winner": "Casey Couture", "loser": "Scott Reisert", "week": 9}),
        ("Scott Reisert", "Jahmyr Gibbs clears 20 again for Scott Reisert.",
         9, {"type": "playerAtLeast", "owner": "Scott Reisert", "week": 9, "player": "Jahmyr Gibbs", "value": 20}),
    ],
    "foh": [
        ("Matt Davis", "Matt Davis beats Spencer Lentz.",
         9, {"type": "h2h", "winner": "Matt Davis", "loser": "Spencer Lentz", "week": 9}),
        ("Spencer Lentz", "Tee Higgins clears 20 again for Spencer Lentz.",
         9, {"type": "playerAtLeast", "owner": "Spencer Lentz", "week": 9, "player": "Tee Higgins", "value": 20}),
        ("Bob Dorsch", "Bob Dorsch beats Aron Rogers.",
         9, {"type": "h2h", "winner": "Bob Dorsch", "loser": "Aron Rogers", "week": 9}),
        ("Aron Rogers", "Aron Rogers leaves under five on his bench in Week 9.",
         9, {"type": "benchUnder", "owner": "Aron Rogers", "week": 9, "value": 5}),
        ("Ryan Kelly", "Ryan Kelly beats Rahul Pahuja.",
         9, {"type": "h2h", "winner": "Ryan Kelly", "loser": "Rahul Pahuja", "week": 9}),
        ("Rahul Pahuja", "Rahul Pahuja leaves under five on his bench in Week 9.",
         9, {"type": "benchUnder", "owner": "Rahul Pahuja", "week": 9, "value": 5}),
        ("Michael Smith", "Michael Smith beats Michael Turner.",
         9, {"type": "h2h", "winner": "Michael Smith", "loser": "Michael Turner", "week": 9}),
        ("Michael Turner", "Michael Turner clears 100 in Week 9.",
         9, {"type": "scoreAtLeast", "owner": "Michael Turner", "week": 9, "value": 100}),
        ("Aaron Jezioro", "Aaron Jezioro beats Billy Norton.",
         9, {"type": "h2h", "winner": "Aaron Jezioro", "loser": "Billy Norton", "week": 9}),
        ("Billy Norton", "Kirk Cousins clears 20 again for Billy Norton.",
         9, {"type": "playerAtLeast", "owner": "Billy Norton", "week": 9, "player": "Kirk Cousins", "value": 20}),
        ("Eric Olson", "Eric Olson clears 120 on his bye.",
         9, {"type": "scoreAtLeast", "owner": "Eric Olson", "week": 9, "value": 120}),
    ],
}

UPDATED = "2026-11-03"

NOTE = {
    "dlffl": (
        "Week 8 published 2026-11-03. Boomer went 7 and 5 and is 38 and 46 on the season. Boomer runs at full heat. "
        "HALFTIME retired after Week 7 (one-off). New from Week 8: THE OWNER SPOTLIGHT (gen2/spotlight.py, one owner "
        "a week from the all-time log; Week 8 Casey Couture) and a lifetime series line on every matchup card "
        "(gen2/series.py). Grade every call that resolves at the TOP of the next issue, right or wrong, before "
        "anything else, then make a new call on every team at the bottom."
    ),
    "foh": (
        "Week 8 published 2026-11-03. Boomer went 8 and 3 and is 34 and 42 on the season. HALFTIME retired after "
        "Week 7 (one-off). New from Week 8: THE OWNER SPOTLIGHT (gen2/spotlight.py, one owner a week from the "
        "all-time log; Week 8 Bob Dorsch) and a lifetime series line on every matchup card (gen2/series.py, FoH "
        "numbers say since 2011). Grade every call that resolves at the TOP of the next issue, right or wrong, "
        "before anything else, then make a new call on every team at the bottom."
    ),
}


def run(league):
    facts = load(f"{league}_wk{os.environ.get('WEEK', '8')}_facts.json")
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
