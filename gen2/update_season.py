"""Append Week 2 to both season ledgers: rows, totals, awards, graded calls,
and the new Week 3 calls with machine-checkable check blocks."""
import json
import os

from compute import DATA, grade, load, result_for

AWARDS = {
    "dlffl": {
        "ownerOfWeek": "Scott Reisert",
        "worstOwner": "Adam Hershberger",
        "startOfWeek": "Ryan Reed",
        "sitOfWeek": "Beth Couture",
        "wasteOfWeek": "Ryan Reed",
    },
    "foh": {
        "ownerOfWeek": "Aron Rogers",
        "worstOwner": "Ryan Kelly",
        "startOfWeek": "Eric Olson",
        "sitOfWeek": "Michael Turner",
        "wasteOfWeek": "Aaron Jezioro",
    },
}

NEW = {
    "dlffl": [
        ("dennis couture", "DA clears 120 for the third straight week.",
         3, {"type": "scoreAtLeast", "owner": "dennis couture", "week": 3, "value": 120}),
        ("Scott Reisert", "Scott Reisert leaves under ten on his bench again in Week 3.",
         3, {"type": "benchUnder", "owner": "Scott Reisert", "week": 3, "value": 10}),
        ("Spencer Lentz", "Spencer Lentz wins his first game of the season.",
         3, {"type": "winsWeek", "owner": "Spencer Lentz", "week": 3}),
        ("Beth Couture", "Mama Beth leaves under ten on her bench in Week 3.",
         3, {"type": "benchUnder", "owner": "Beth Couture", "week": 3, "value": 10}),
        ("Kent Frenger", "Kenneth Walker III goes for 15 or more again for Kent Frenger.",
         3, {"type": "playerAtLeast", "owner": "Kent Frenger", "week": 3, "player": "Kenneth Walker III", "value": 15}),
        ("Casey Couture", "Casey Couture starts Stefon Diggs in Week 3.",
         3, {"type": "startsPlayer", "owner": "Casey Couture", "week": 3, "player": "Stefon Diggs"}),
        ("Adam Calvelage", "CeeDee Lamb clears 20 again for Adam Calvelage.",
         3, {"type": "playerAtLeast", "owner": "Adam Calvelage", "week": 3, "player": "CeeDee Lamb", "value": 20}),
        ("Geoff Cavender", "Geoff Cavender goes 3 and 0.",
         3, {"type": "winsWeek", "owner": "Geoff Cavender", "week": 3}),
        ("Ryan Reed", "Jaxon Smith-Njigba clears 20 again for Ryan Reed.",
         3, {"type": "playerAtLeast", "owner": "Ryan Reed", "week": 3, "player": "Jaxon Smith-Njigba", "value": 20}),
        ("Doug Fields", "Doug Fields beats Scott Howard on Sunday.",
         3, {"type": "h2h", "winner": "Doug Fields", "loser": "Scott Howard", "week": 3}),
        ("Scott Howard", "Scott Howard starts Dak Prescott in Week 3.",
         3, {"type": "startsPlayer", "owner": "Scott Howard", "week": 3, "player": "Dak Prescott"}),
        ("Adam Hershberger", "Adam Hershberger clears 100 for the first time this season.",
         3, {"type": "scoreAtLeast", "owner": "Adam Hershberger", "week": 3, "value": 100}),
    ],
    "foh": [
        ("Rahul Pahuja", "Rahul Pahuja makes it three straight wins.",
         3, {"type": "winsWeek", "owner": "Rahul Pahuja", "week": 3}),
        ("Aron Rogers", "Aron Rogers leaves under ten behind again in Week 3.",
         3, {"type": "benchUnder", "owner": "Aron Rogers", "week": 3, "value": 10}),
        ("Matt Davis", "Matt Davis gets a receiver into his top three scorers in Week 3.",
         3, {"type": "posInTop3", "owner": "Matt Davis", "week": 3, "pos": "WR"}),
        ("Spencer Lentz", "Spencer Lentz beats Bob Dorsch on Sunday.",
         3, {"type": "h2h", "winner": "Spencer Lentz", "loser": "Bob Dorsch", "week": 3}),
        ("Eric Olson", "Josh Allen clears 25 again for Eric Olson.",
         3, {"type": "playerAtLeast", "owner": "Eric Olson", "week": 3, "player": "Josh Allen", "value": 25}),
        ("Michael Smith", "Michael Smith clears 120 again.",
         3, {"type": "scoreAtLeast", "owner": "Michael Smith", "week": 3, "value": 120}),
        ("Bob Dorsch", "Bob Dorsch clears 110 in Week 3.",
         3, {"type": "scoreAtLeast", "owner": "Bob Dorsch", "week": 3, "value": 110}),
        ("Billy Norton", "Billy Norton starts Stefon Diggs in Week 3.",
         3, {"type": "startsPlayer", "owner": "Billy Norton", "week": 3, "player": "Stefon Diggs"}),
        ("Michael Turner", "Michael Turner wins his first, over Billy Norton.",
         3, {"type": "h2h", "winner": "Michael Turner", "loser": "Billy Norton", "week": 3}),
        ("Ryan Kelly", "Ryan Kelly clears 90 in Week 3.",
         3, {"type": "scoreAtLeast", "owner": "Ryan Kelly", "week": 3, "value": 90}),
        ("Aaron Jezioro", "Aaron Jezioro starts Brock Purdy in Week 4.",
         4, {"type": "startsPlayer", "owner": "Aaron Jezioro", "week": 4, "player": "Brock Purdy"}),
    ],
}

NOTE = (
    "Week 2 published 2026-09-24, three days late: the scheduled Tuesday run had no browser tools and stopped at "
    "its preflight check. Boomer went 4 and 8 in Dewart Lake and 4 and 6 with one open in Friends of Herb. Awards "
    "match the published pages. Grade every call that resolves at the TOP of the next issue, right or wrong, "
    "before anything else, then make a new call on every team at the bottom."
)


def run(league):
    facts = load(f"{league}_wk2_facts.json")
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
    season["updated"] = "2026-09-24"
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
