"""Append the week (WEEK env) to both season ledgers: rows, totals, awards, graded calls,
and the new Week 3 calls with machine-checkable check blocks."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "Scott Reisert",
        "worstOwner": "Casey Couture",
        "startOfWeek": "Spencer Lentz",
        "sitOfWeek": "Scott Howard",
        "wasteOfWeek": "Doug Fields",
    },
    "foh": {
        "ownerOfWeek": "Michael Turner",
        "worstOwner": "Ryan Kelly",
        "startOfWeek": "Bob Dorsch",
        "sitOfWeek": "Aaron Jezioro",
        "wasteOfWeek": "Eric Olson",
    },
}

NEW = {
    "dlffl": [
        ("Adam Hershberger", "Adam Hershberger beats Casey Couture for his first win.",
         4, {"type": "h2h", "winner": "Adam Hershberger", "loser": "Casey Couture", "week": 4}),
        ("Casey Couture", "Casey Couture starts Sam Darnold in Week 4.",
         4, {"type": "startsPlayer", "owner": "Casey Couture", "week": 4, "player": "Sam Darnold"}),
        ("Scott Reisert", "Scott Reisert goes 4 and 0.",
         4, {"type": "winsWeek", "owner": "Scott Reisert", "week": 4}),
        ("Spencer Lentz", "Bijan Robinson clears 20 again for Spencer Lentz.",
         4, {"type": "playerAtLeast", "owner": "Spencer Lentz", "week": 4, "player": "Bijan Robinson", "value": 20}),
        ("Doug Fields", "Doug Fields beats Geoff Cavender.",
         4, {"type": "h2h", "winner": "Doug Fields", "loser": "Geoff Cavender", "week": 4}),
        ("Geoff Cavender", "Geoff Cavender clears 100 in Week 4.",
         4, {"type": "scoreAtLeast", "owner": "Geoff Cavender", "week": 4, "value": 100}),
        ("Beth Couture", "Mama Beth beats Kent Frenger.",
         4, {"type": "h2h", "winner": "Beth Couture", "loser": "Kent Frenger", "week": 4}),
        ("Kent Frenger", "Tyler Shough clears 15 again for Kent Frenger.",
         4, {"type": "playerAtLeast", "owner": "Kent Frenger", "week": 4, "player": "Tyler Shough", "value": 15}),
        ("dennis couture", "DA beats Scott Howard.",
         4, {"type": "h2h", "winner": "dennis couture", "loser": "Scott Howard", "week": 4}),
        ("Scott Howard", "Scott Howard leaves under twenty on his bench in Week 4.",
         4, {"type": "benchUnder", "owner": "Scott Howard", "week": 4, "value": 20}),
        ("Ryan Reed", "Ryan Reed wins his first ever meeting with Adam Calvelage.",
         4, {"type": "h2h", "winner": "Ryan Reed", "loser": "Adam Calvelage", "week": 4}),
        ("Adam Calvelage", "Brock Purdy clears 20 again for Adam Calvelage.",
         4, {"type": "playerAtLeast", "owner": "Adam Calvelage", "week": 4, "player": "Brock Purdy", "value": 20}),
    ],
    "foh": [
        ("Eric Olson", "Eric Olson beats Spencer Lentz. The robot says Spencer.",
         4, {"type": "h2h", "winner": "Eric Olson", "loser": "Spencer Lentz", "week": 4}),
        ("Spencer Lentz", "Spencer Lentz scores 120 or more in Week 4.",
         4, {"type": "scoreAtLeast", "owner": "Spencer Lentz", "week": 4, "value": 120}),
        ("Matt Davis", "Matt Davis starts Joe Burrow in Week 4.",
         4, {"type": "startsPlayer", "owner": "Matt Davis", "week": 4, "player": "Joe Burrow"}),
        ("Aron Rogers", "Aron Rogers goes 4 and 0.",
         4, {"type": "winsWeek", "owner": "Aron Rogers", "week": 4}),
        ("Ryan Kelly", "Ryan Kelly clears 100 in Week 4.",
         4, {"type": "scoreAtLeast", "owner": "Ryan Kelly", "week": 4, "value": 100}),
        ("Bob Dorsch", "Bob Dorsch leaves under five on his bench again.",
         4, {"type": "benchUnder", "owner": "Bob Dorsch", "week": 4, "value": 5}),
        ("Rahul Pahuja", "Rahul Pahuja starts Harold Fannin Jr. in Week 4.",
         4, {"type": "startsPlayer", "owner": "Rahul Pahuja", "week": 4, "player": "Harold Fannin Jr."}),
        ("Michael Turner", "Michael Turner clears 120 again.",
         4, {"type": "scoreAtLeast", "owner": "Michael Turner", "week": 4, "value": 120}),
        ("Michael Smith", "Michael Smith beats Aaron Jezioro.",
         4, {"type": "h2h", "winner": "Michael Smith", "loser": "Aaron Jezioro", "week": 4}),
        ("Billy Norton", "Billy Norton clears 100 on his bye.",
         4, {"type": "scoreAtLeast", "owner": "Billy Norton", "week": 4, "value": 100}),
    ],
}

NOTE = (
    "Week 3 published 2026-09-29, on time. Boomer went 6 and 6 in Dewart Lake and 3 and 7 in Friends of Herb, "
    "with two Friends of Herb calls still open (Turner under five before Halloween, Jezioro starts Purdy in Week 4). "
    "Eric Olson's OpenAI agent picked Spencer Lentz to beat Olson in Week 4; Boomer's Week 4 call on Olson takes "
    "the other side, so grading Boomer's call grades the robot. Grade every call that resolves at the TOP of the next "
    "issue, right or wrong, before anything else, then make a new call on every team at the bottom."
)


def run(league):
    facts = load(f"{league}_wk{os.environ.get('WEEK', '2')}_facts.json")
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

    # 3. awards
    for kind, owner in AWARDS[league].items():
        aw = season["owners"][owner].setdefault("awards", {})
        aw.setdefault(kind, [])
        if wk not in aw[kind]:
            aw[kind].append(wk)

    # 4. new calls
    n = max((p["n"] for p in season["predictions"]), default=0)
    for owner, call, resolves, check in NEW[league]:
        n += 1
        season["predictions"].append({
            "n": n, "week": wk, "by": "Boomer", "owner": owner, "call": call,
            "resolvesWeek": resolves, "graded": None, "correct": None, "check": check,
        })

    season["throughWeek"] = wk
    season["updated"] = "2026-09-29"
    season["note"] = NOTE
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
