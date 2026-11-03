"""Lifetime series helper (added Week 8, 2026-11-03) for the series line on every matchup card.

    python3 gen2/series.py <league> <week>          -> this week's pairs, after this week's result
    python3 gen2/series.py <league> <week> --next   -> next week's pairs, before they play

Uses gen2/data/<league>_games.json (all decided games incl. playoffs, this season appended through the
previous week by append_current.py) plus the week's facts. Dewart Lake data starts in 2009, Friends of
Herb in 2011 (the CBS era has no game log), so the FoH line must say "since 2011".
"""
import json, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "docs", "data")
PW = os.path.join(HERE, "data")
SEASON = 2026


def norm(n):
    return n.title() if (n.isupper() or n.islower()) and " " in n else n


def log_with_week(league, week):
    G = json.load(open(os.path.join(PW, f"{league}_games.json")))["games"]
    F = json.load(open(os.path.join(DATA, f"{league}_wk{week}_facts.json")))
    games = list(G)
    for m in F["matchups"]:
        w = "tie" if m["winnerId"] is None else ("home" if m["winnerId"] == m["homeId"] else "away")
        games.append({"year": SEASON, "period": week, "playoff": False, "tier": "NONE", "weeks": 1,
                      "home": norm(m["homeOwner"]), "homeTeam": m["home"], "homeScore": m["homeScore"],
                      "away": norm(m["awayOwner"]), "awayTeam": m["away"], "awayScore": m["awayScore"],
                      "winner": w})
    return games, F


def pair(games, a, b):
    """(a_wins, b_wins, ties, streak_holder, streak_len, playoff_games, first_year, last5)"""
    ps = sorted((g for g in games if {g["home"], g["away"]} == {a, b}), key=lambda g: (g["year"], g["period"]))
    seq = []
    for g in ps:
        seq.append(None if g["winner"] == "tie" else (g["home"] if g["winner"] == "home" else g["away"]))
    aw, bw, t = seq.count(a), seq.count(b), seq.count(None)
    holder, k = None, 0
    if seq:
        holder = seq[-1]
        for x in reversed(seq):
            if x == holder: k += 1
            else: break
    po = sum(1 for g in ps if g["playoff"] and g["tier"] == "WINNERS_BRACKET")  # real bracket only; consolation games are not "the playoffs"
    first = ps[0]["year"] if ps else None
    last = [(g["year"], g["period"], g["home"], g["homeScore"], g["away"], g["awayScore"], g["tier"] if g["playoff"] else "") for g in ps[-5:]]
    return aw, bw, t, holder, k, po, first, last


def line(league, a, b, aw, bw, t, holder, k, po, first):
    since = "since 2011" if league == "foh" else f"since {first}"
    if aw == bw:
        s = f"Tied {aw}-{bw} in {aw + bw + t} meetings"
    else:
        lead, lw, ll = (a, aw, bw) if aw > bw else (b, bw, aw)
        s = f"{lead.split()[-1] if False else lead} leads {lw}-{ll}"
    if t:
        s += f"-{t}"
    s += f" {since}"
    if po:
        s += f", {po} in the playoffs"
    if k >= 2 and holder:
        s += f" · {holder} has won {k} straight"
    return s


if __name__ == "__main__":
    lg, wk = sys.argv[1], int(sys.argv[2])
    games, F = log_with_week(lg, wk)
    if "--next" in sys.argv:
        gl = [g for g in games]  # includes this week
        for n in F["nextWeek"]:
            if not n["away"]:
                print(f"{n['homeOwner']}: bye"); continue
            a, b = norm(n["homeOwner"]), norm(n["awayOwner"])
            r = pair(gl, a, b)
            print(f"{b} at {a}: " + line(lg, a, b, *r[:7]) + "  last5=" + str(r[7]))
    else:
        for m in F["matchups"]:
            a, b = norm(m["homeOwner"]), norm(m["awayOwner"])
            r = pair(games, a, b)
            print(f"{a} v {b}: " + line(lg, a, b, *r[:7]) + "  last5=" + str(r[7]))
