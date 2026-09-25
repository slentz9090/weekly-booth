"""Grade last week's calls, build the ledger, shortlist the Hardware.

Every number the pages speak comes from here or from the facts JSON. Nothing is
typed by hand into the editorial without appearing in this output first.
"""
from __future__ import annotations

import json
import os
import sys

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wb", "docs", "data")


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return json.load(fh)


def by_owner(facts):
    return {t["owner"]: t for t in facts["perTeam"]}


def result_for(facts, owner):
    """(won, margin, opponent) for a head to head week. Bye returns (None, 0, None)."""
    for m in facts["matchups"]:
        if m["homeOwner"] == owner:
            return (m["winnerId"] == m["homeId"], m["margin"], m["awayOwner"])
        if m["awayOwner"] == owner:
            return (m["winnerId"] == m["awayId"], m["margin"], m["homeOwner"])
    return (None, 0.0, None)


def score_rank(facts, owner):
    order = sorted(facts["perTeam"], key=lambda t: -t["score"])
    for i, t in enumerate(order, 1):
        if t["owner"] == owner:
            return i
    return None


def player_pts(team, name):
    """Points for a named player on that team, from whichever list carries him."""
    for key in ("top", "benchTop", "starterLow"):
        for p in team.get(key) or []:
            if p["n"] == name:
                return p["pts"]
    for key in ("bust", "bestBench"):
        p = team.get(key)
        if p and p["n"] == name:
            return p["pts"]
    w = team.get("worst")
    if w:
        if w["started"] == name:
            return w["startedPts"]
        if w["benched"] == name:
            return w["benchedPts"]
    return None


def started(team, name):
    """True if the player appears among that team's starters in the facts."""
    for p in (team.get("top") or []) + (team.get("starterLow") or []):
        if p["n"] == name:
            return True
    b = team.get("bust")
    if b and b["n"] == name:
        return True
    w = team.get("worst")
    if w and w["started"] == name:
        return True
    return False


def benched(team, name):
    for p in team.get("benchTop") or []:
        if p["n"] == name:
            return True
    bb = team.get("bestBench")
    if bb and bb["n"] == name:
        return True
    w = team.get("worst")
    if w and w["benched"] == name:
        return True
    return False


def grade(pred, facts):
    """Returns (verdict, evidence) or (None, reason) when it does not resolve yet."""
    c = pred["check"]
    t = c["type"]
    owners = by_owner(facts)
    wk = facts["week"]
    # Multi-week calls carry their own week logic and can fail early: a call
    # that says "does not reach 120 in Week 2 or Week 3" is dead the moment he
    # reaches 120 in Week 2, and the booth grades it that week, not later.
    if pred.get("resolvesWeek") and pred["resolvesWeek"] != wk and t not in ("maxScoreUnder", "losesByUnder"):
        return (None, f"resolves in week {pred['resolvesWeek']}")
    o = c.get("owner") or c.get("winner")
    team = owners.get(o)
    if team is None:
        return (None, f"{o} not in week {wk}")

    if t == "scoringRankAtMost":
        r = score_rank(facts, o)
        return ("RIGHT" if r <= c["value"] else "WRONG", f"finished {r} in scoring at {team['score']:.2f}")
    if t == "h2h":
        won, margin, opp = result_for(facts, c["winner"])
        ok = won and opp == c["loser"]
        return ("RIGHT" if ok else "WRONG", f"{c['winner']} {'beat' if won else 'lost to'} {opp} by {margin:.2f}")
    if t == "outscores":
        a, b = owners[c["owner"]]["score"], owners[c["other"]]["score"]
        return ("RIGHT" if a > b else "WRONG", f"{a:.2f} to {b:.2f}")
    if t == "playerAtLeast":
        p = player_pts(team, c["player"])
        if p is None:
            return (None, f"{c['player']} not in the week's top or bench lines for {o}")
        return ("RIGHT" if p >= c["value"] else "WRONG", f"{c['player']} scored {p:.2f}")
    if t == "winsWeek":
        won, margin, opp = result_for(facts, o)
        return ("RIGHT" if won else "WRONG", f"{'beat' if won else 'lost to'} {opp} by {margin:.2f}")
    if t == "winsByMoreThan":
        won, margin, opp = result_for(facts, o)
        return ("RIGHT" if won and margin > c["value"] else "WRONG",
                f"{'won' if won else 'lost'} against {opp} by {margin:.2f}")
    if t == "winsByAtLeast":
        won, margin, opp = result_for(facts, o)
        return ("RIGHT" if won and margin >= c["value"] else "WRONG",
                f"{'won' if won else 'lost'} against {opp} by {margin:.2f}")
    if t == "startsPlayer":
        return ("RIGHT" if started(team, c["player"]) else "WRONG",
                f"{c['player']} {'started' if started(team, c['player']) else 'did not start'} for {o}")
    if t == "scoreUnder":
        return ("RIGHT" if team["score"] < c["value"] else "WRONG", f"scored {team['score']:.2f}")
    if t == "scoreAtLeast":
        return ("RIGHT" if team["score"] >= c["value"] else "WRONG", f"scored {team['score']:.2f}")
    if t == "benchUnder":
        return ("RIGHT" if team["left"] < c["value"] else "WRONG", f"left {team['left']:.2f} behind")
    if t == "benchAtLeastAndLoses":
        won, margin, opp = result_for(facts, o)
        ok = team["left"] >= c["value"] and won is False
        return ("RIGHT" if ok else "WRONG",
                f"left {team['left']:.2f} behind and {'lost' if won is False else 'won'}")
    if t == "winWithStarter":
        won, margin, opp = result_for(facts, o)
        ok = bool(won) and started(team, c["player"])
        return ("RIGHT" if ok else "WRONG",
                f"{'won' if won else 'lost'}, and {c['player']} "
                f"{'started' if started(team, c['player']) else 'was not in the lineup'}")
    if t == "posInTop3":
        got = [p["pos"] for p in team["top"]]
        return ("RIGHT" if c["pos"] in got else "WRONG", "top three were " + ", ".join(got))
    if t == "maxScoreUnder":
        weeks = c["weeks"]
        if wk < max(weeks):
            if team["score"] >= c["value"]:
                return ("WRONG", f"scored {team['score']:.2f} in week {wk}")
            return (None, f"still alive, {team['score']:.2f} in week {wk}, resolves week {max(weeks)}")
        return ("RIGHT" if team["score"] < c["value"] else "WRONG", f"scored {team['score']:.2f}")
    if t == "losesByUnder":
        won, margin, opp = result_for(facts, o)
        if won is False and margin < c["value"]:
            return ("RIGHT", f"lost to {opp} by {margin:.2f}")
        return (None, f"still open, resolves by week {max(c['weeks'])}")
    return (None, f"unknown check type {t}")


def ledger_rows(facts, season):
    rows = []
    for t in sorted(facts["perTeam"], key=lambda x: -x["left"]):
        owner = t["owner"]
        won, margin, opp = result_for(facts, owner)
        # The season ledger is written BEFORE the pages are generated, so its
        # totals already include this week. Do not add the week in again.
        tot = season["owners"].get(owner, {}).get("totals", {})
        weeks = season["owners"].get(owner, {}).get("weeks", [])
        if any(w.get("week") == facts["week"] for w in weeks):
            total = round(tot.get("benchPoints", 0.0), 2)
        else:
            total = round(tot.get("benchPoints", 0.0) + t["left"], 2)
        if won is None:
            verdict, cls = "Bye week", ""
        elif won:
            verdict, cls = "No, won", ""
        elif t["left"] > margin:
            verdict, cls = f"Yes, by {margin:.2f}", "yes"
        else:
            verdict, cls = f"No, lost by {margin:.2f}", ""
        rows.append((season["owners"].get(owner, {}).get("display", owner), t["left"], verdict, cls, total))
    return rows


def hardware(facts, season):
    """Shortlists, not verdicts. The booth picks from these."""
    per = facts["perTeam"]
    out = {}
    out["highest"] = sorted(per, key=lambda t: -t["score"])[:3]
    out["lowest"] = sorted(per, key=lambda t: t["score"])[:3]
    out["cleanest"] = sorted(per, key=lambda t: (t["left"], -t["eff"]))[:3]
    out["messiest"] = sorted(per, key=lambda t: -t["left"])[:3]
    best_starts = []
    for t in per:
        for p in t["top"]:
            best_starts.append((p["pts"] - (p.get("proj") or 0), t["owner"], p))
    out["startOfWeek"] = sorted(best_starts, key=lambda x: -x[0])[:4]
    sits = [(t["worst"]["delta"], t["owner"], t["worst"]) for t in per if t.get("worst")]
    out["sitOfWeek"] = sorted(sits, key=lambda x: -x[0])[:4]
    winners_waste = [t for t in per if result_for(facts, t["owner"])[0] is True]
    out["wasteOfWeek"] = sorted(winners_waste, key=lambda t: -t["left"])[:3]
    losers_cost = []
    for t in per:
        won, margin, opp = result_for(facts, t["owner"])
        if won is False and t["left"] > margin:
            losers_cost.append((t["left"] - margin, t["owner"], margin, t["left"]))
    out["costTheGame"] = sorted(losers_cost, key=lambda x: -x[0])
    return out


def waiver_swings(facts):
    """Point swing per move: what came in minus what went out, that week."""
    swings = []
    for m in facts["moves"]:
        added = sum(p["pts"] for p in m["added"])
        dropped = sum(p["pts"] for p in m["dropped"])
        swings.append((round(added - dropped, 2), m))
    return sorted(swings, key=lambda x: -x[0])


def main(league):
    facts = load(f"{league}_wk2_facts.json")
    season = load(f"{league}_season.json")
    print("=" * 70)
    print(league.upper(), "week", facts["week"])
    print("--- GRADES ---")
    for p in season["predictions"]:
        v, why = grade(p, facts)
        print(f"  #{p['n']:<2} {p['owner']:<18} {v or 'OPEN':<6} {p['call'][:62]:<64} | {why}")
    print("--- LEDGER ---")
    for i, r in enumerate(ledger_rows(facts, season), 1):
        print(f"  {i:>2} {r[0]:<18} {r[1]:>6.2f}  {r[2]:<20} season {r[4]:.2f}")
    print("--- HARDWARE SHORTLISTS ---")
    hw = hardware(facts, season)
    for k in ("highest", "lowest", "cleanest", "messiest"):
        print(f"  {k}: " + ", ".join(f"{t['owner']} {t['score']:.2f} (left {t['left']:.2f}, eff {t['eff']})" for t in hw[k]))
    print("  startOfWeek: " + " | ".join(f"{o} {p['n']} {p['pts']:.2f} vs proj {p.get('proj',0):.2f} (+{d:.2f})" for d, o, p in hw["startOfWeek"]))
    print("  sitOfWeek: " + " | ".join(f"{o} benched {w['benched']} {w['benchedPts']:.2f} for {w['started']} {w['startedPts']:.2f} (-{d:.2f})" for d, o, w in hw["sitOfWeek"]))
    print("  wasteOfWeek (winners): " + ", ".join(f"{t['owner']} left {t['left']:.2f}" for t in hw["wasteOfWeek"]))
    print("  cost the game: " + (", ".join(f"{o} left {left:.2f}, lost by {margin:.2f}" for _, o, margin, left in hw["costTheGame"]) or "nobody"))
    print("--- WAIVER SWINGS ---")
    for s, m in waiver_swings(facts):
        a = ", ".join(f"{p['n']} {p['pts']:.1f}" for p in m["added"]) or "nobody"
        d = ", ".join(f"{p['n']} {p['pts']:.1f}" for p in m["dropped"]) or "nobody"
        print(f"  {s:>+7.2f}  {m['owner']:<18} in: {a:<34} out: {d}")


if __name__ == "__main__":
    for lg in (sys.argv[1:] or ["dlffl", "foh"]):
        main(lg)
