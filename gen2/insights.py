"""THE OUTLIER ENGINE. Pass 1 computes every metric against its own baseline, pass 2 scores each
one as a distance from normal (z), pass 3 tiers them for the editorial.

    python3 gen2/insights.py <league> <week>      -> docs/data/<league>_wk<N>_insights.json

Inputs: docs/data/<league>_wk<N>_facts.json (this week), docs/data/<league>_season.json,
docs/data/<league>_history.json, and two files rebuilt each run from the raw pulls in Spencer's
Downloads (not committed, not served): gen2/data/<league>_games.json (games.py, every decided game)
and gen2/data/<league>_playerweeks.json (playerweeks.py, every player-week since 2018).

Tiers (runbook, THE OUTLIER ENGINE), each insight carries two readings:
    zUnit  rarity for that owner, game or player-week
    z      league-week rarity: how often anyone in the league does this in a week
    HEADLINE  zUnit >= 2.5 and z >= 1.0
    PROMOTE   zUnit >= 2.0 and z >= 0.5
    SUPPORT   zUnit >= 1.0  (rides along with a promoted story only)
    SUPPRESS  otherwise, never printed
Insights are ordered by league-week z, so the rarest thing in the league this week comes first.
The page never says sigma. Every insight carries a plain-English `rarity` and a `plain` sentence.
"""
import json, math, os, sys
from collections import defaultdict
from statistics import NormalDist, mean, pstdev

DATA = os.path.join(os.path.dirname(__file__), "..", "docs", "data")
N = NormalDist()
SEASON = 2026
MIN_OWN_GAMES = 30      # below this, judge a score against the league, not the owner
MIN_H2H = 8
MIN_LUCK_WEEKS = 4      # one lucky week is not a trend
NICK = {"dlffl": {"Beth Couture": "Mama Beth", "Dennis Couture": "DA"}, "foh": {}}
SLOTS = {"QB": 1, "RB": 2, "WR": 2, "TE": 1, "K": 1, "DST": 1}   # plus one RB/WR/TE flex
PW = os.path.join(os.path.dirname(__file__), "data")


def z_from_upper_tail(p):
    """p = probability of something at least this extreme in the stated direction."""
    p = min(max(p, 1e-9), 0.5)
    return -N.inv_cdf(p)


def tier(z_unit, z_week=None):
    """Gate on BOTH readings. z_unit: how unusual for that owner, game or player-week (Spencer's
    thresholds). z_week: how often ANYONE in the league does this in a week. A 40-point start is
    2.5 per player-week but happens most Sundays somewhere in a 12-team league, so it cannot lead."""
    a = abs(z_unit)
    w = abs(z_week) if z_week is not None else a
    if a >= 2.5 and w >= 1.0:
        return "HEADLINE"
    if a >= 2.0 and w >= 0.5:
        return "PROMOTE"
    return "SUPPORT" if a >= 1.0 else "SUPPRESS"


def rarity(z):
    a = abs(z)
    if a < 1.0:
        return "ordinary"
    p = 1 - N.cdf(a)
    weeks = 1 / p
    if weeks >= 700:
        return "the league sees this about once in 50 seasons"
    if weeks >= 28:
        return f"the league sees this about once every {round(weeks / 14)} seasons"
    return f"the league sees this about 1 week in {round(weeks):,}"


def ordinal(n):
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"


def load(league, week):
    j = lambda n: json.load(open(os.path.join(DATA, n)))
    games = json.load(open(os.path.join(PW, f"{league}_games.json")))["games"]
    return (j(f"{league}_wk{week}_facts.json"), j(f"{league}_season.json"), games,
            j(f"{league}_history.json"))


def canon(name, known):
    for k in known:
        if k.lower() == name.lower():
            return k
    return name


def run(league, week):
    facts, season, games, hist = load(league, week)
    owners_hist = hist["owners"]
    out = []
    nick = NICK.get(league, {})
    D = lambda o: nick.get(o, o)          # display name for the plain sentences

    def add(kind, who, value, z, plain, baseline, scope, extra=None):
        row = {"kind": kind, "owners": who, "value": value, "z": round(z, 2), "tier": tier(z),
               "direction": "high" if z > 0 else "low", "rarity": rarity(z), "plain": plain,
               "baseline": baseline, "scope": scope}
        if extra:
            row.update(extra)
        out.append(row)

    # ---------- baselines from the game log (single-week games only) ----------
    single = [g for g in games if g["weeks"] == 1]
    own_scores = defaultdict(list)
    all_scores, margins, loser_scores, winner_scores = [], [], [], []
    for g in single:
        for side in ("home", "away"):
            own_scores[g[side]].append(g[side + "Score"])
            all_scores.append(g[side + "Score"])
        m = abs(g["homeScore"] - g["awayScore"])
        margins.append(m)
        if g["winner"] != "tie":
            w, l = ("home", "away") if g["winner"] == "home" else ("away", "home")
            loser_scores.append(g[l + "Score"])
            winner_scores.append(g[w + "Score"])
    # this season's earlier weeks are already in the game log: append_current.py adds them before
    # the scan, so owner, league, margin, series and player-week ranks all count them.
    assert any(g["year"] == SEASON for g in games) or week == 1, "run gen2/append_current.py first"
    assert not any(g["year"] == SEASON and g["period"] >= week for g in games), "game log includes the week being judged"
    first_year = min(g["year"] for g in games)
    span = f"since {first_year}"

    bye_owners = {b["owner"] for b in facts.get("byes", [])}

    # ---------- 1. score vs the owner's own career, and vs the league's all time ----------
    for t in facts["perTeam"]:
        o = canon(t["owner"], owners_hist)
        if t["owner"] in bye_owners:
            continue        # a bye has no stakes: nothing about it is judged
        s = t["score"]
        mine = own_scores.get(o, [])
        if len(mine) >= MIN_OWN_GAMES:
            mu, sd = mean(mine), pstdev(mine)
            z = (s - mu) / sd
            rank_hi = 1 + sum(1 for x in mine if x > s)
            rank_lo = 1 + sum(1 for x in mine if x < s)
            n = len(mine) + 1
            if z >= 0:
                plain = f"{D(o)} scored {s:.2f}, the {ordinal(rank_hi)}-best game of {n} in a career {span}."
            else:
                plain = f"{D(o)} scored {s:.2f}, the {ordinal(rank_lo)}-worst game of {n} in a career {span}."
            add("score_vs_own_career", [o], s, z, plain, f"own career mean {mu:.1f}, n={len(mine)}", span,
                {"rankHigh": rank_hi, "rankLow": rank_lo, "games": n})
        # all-time league rank (percentile, robust to the long right tail)
        n = len(all_scores) + 1
        hi = 1 + sum(1 for x in all_scores if x > s)
        lo = 1 + sum(1 for x in all_scores if x < s)
        if hi <= lo:
            z = z_from_upper_tail((hi - 0.5) / n)
            plain = f"{D(o)}'s {s:.2f} is the {ordinal(hi)}-highest score in {n:,} team-weeks {span}."
        else:
            z = -z_from_upper_tail((lo - 0.5) / n)
            plain = f"{D(o)}'s {s:.2f} is the {ordinal(lo)}-lowest score in {n:,} team-weeks {span}."
        add("score_vs_league_all_time", [o], s, z, plain, f"{n:,} single-week scores", span,
            {"rankHigh": hi, "rankLow": lo})

    # ---------- 2. per matchup: margin, high score in a loss, low score in a win ----------
    for m in facts["matchups"]:
        if not m.get("awayOwner"):
            continue
        ho, ao = canon(m["homeOwner"], owners_hist), canon(m["awayOwner"], owners_hist)
        win_home = m["winnerId"] == m["homeId"]
        W, L = (ho, ao) if win_home else (ao, ho)
        ws, ls = (m["homeScore"], m["awayScore"]) if win_home else (m["awayScore"], m["homeScore"])
        mg = abs(m["homeScore"] - m["awayScore"])
        n = len(margins) + 1
        bigger = 1 + sum(1 for x in margins if x > mg)
        smaller = 1 + sum(1 for x in margins if x < mg)
        if bigger <= smaller:
            z = z_from_upper_tail((bigger - 0.5) / n)
            add("blowout", [W, L], mg, z,
                f"{D(W)} beat {D(L)} by {mg:.2f}, the {ordinal(bigger)}-biggest margin in {n:,} games {span}.",
                f"{n:,} margins", span)
        else:
            z = z_from_upper_tail((smaller - 0.5) / n)   # a nail-biter is rare on the small side
            add("nail_biter", [W, L], mg, z,
                f"{D(W)} beat {D(L)} by {mg:.2f}, the {ordinal(smaller)}-closest game in {n:,} {span}.",
                f"{n:,} margins", span)
        n2 = len(loser_scores) + 1
        r = 1 + sum(1 for x in loser_scores if x > ls)
        z = z_from_upper_tail((r - 0.5) / n2)
        add("high_score_in_a_loss", [L, W], ls, z,
            f"{D(L)} lost with {ls:.2f}, the {ordinal(r)}-most points in a loss in {n2:,} games {span}.",
            f"{n2:,} losing scores", span)
        r = 1 + sum(1 for x in winner_scores if x < ws)
        z = z_from_upper_tail((r - 0.5) / n2)
        add("low_score_in_a_win", [W, L], ws, z,
            f"{D(W)} won with {ws:.2f}, the {ordinal(r)}-fewest points in a win in {n2:,} games {span}.",
            f"{n2:,} winning scores", span)

        # ---------- 3. lifetime head to head for this pair, after this game ----------
        pair = [g for g in games if {g["home"], g["away"]} == {ho, ao}]
        seq = []
        for g in sorted(pair, key=lambda g: (g["year"], g["period"])):
            if g["winner"] == "tie":
                seq.append(None)
            else:
                seq.append(g["home"] if g["winner"] == "home" else g["away"])
        seq.append(W)
        w = sum(1 for x in seq if x == W)
        l = sum(1 for x in seq if x == L)
        t_ = sum(1 for x in seq if x is None)
        n3 = w + l + t_
        if n3 >= MIN_H2H:
            z = (w + 0.5 * t_ - n3 / 2) / math.sqrt(n3 / 4)
            lead, trail = (W, L) if w >= l else (L, W)
            lw, ll = max(w, l), min(w, l)
            # exact two-sided binomial (ties count as half a game each way, rounded down):
            # the normal approximation overstated rarity badly for short series (8-1 read 1 in 51, exact is 1 in 26)
            _k, _n = max(w, l) + t_ // 2, w + l + 2 * (t_ // 2)
            p_coin = min(1.0, 2 * sum(math.comb(_n, i) for i in range(_k, _n + 1)) / 2 ** _n) or 1e-9
            add("lifetime_series", [lead, trail], f"{lw}-{ll}" + (f"-{t_}" if t_ else ""), abs(z),
                f"{D(lead)} leads {D(trail)} {lw}-{ll}" + (f"-{t_}" if t_ else "") +
                f" all time ({span}). By coin flip that lopsided a series is about 1 in {round(1 / p_coin):,}.",
                "50/50 coin flip", span, {"games": n3})
        # streak held by this week's winner
        k = 0
        for x in reversed(seq):
            if x == W:
                k += 1
            else:
                break
        prev_streak_L = 0
        for x in reversed(seq[:-1]):
            if x == L:
                prev_streak_L += 1
            else:
                break
        if k >= 3:
            z = z_from_upper_tail(0.5 ** k)
            add("active_streak", [W, L], k, z,
                f"{D(W)} has now beaten {D(L)} {k} straight times.", "coin flip per game", span)
        if prev_streak_L >= 3:
            z = z_from_upper_tail(0.5 ** prev_streak_L)
            add("streak_snapped", [W, L], prev_streak_L, z,
                # "first time in N meetings" read as first-ever win on the Week 3 draft; say it plainly
                f"{D(W)} beat {D(L)}, snapping {D(L)}'s {prev_streak_L}-game winning streak in the series "
                f"(series now {w}-{l}" + (f"-{t_}" if t_ else "") + ").", "coin flip per game", span)
        if w == 1 and n3 >= 5:
            add("first_ever_win", [W, L], n3, z_from_upper_tail(0.5 ** (n3 - 1)),
                f"{D(W)}'s first win over {D(L)} in {n3} meetings.", "coin flip per game", span)

    # ---------- 4. luck: actual record vs all-play expectation, season to date ----------
    results = {}
    for k in range(1, week + 1):
        try:
            fk = json.load(open(os.path.join(DATA, f"{league}_wk{k}_facts.json")))
        except FileNotFoundError:
            continue
        for m in fk["matchups"]:
            if not m.get("awayOwner"):
                continue
            for side, oid in (("home", m["homeId"]), ("away", m["awayId"])):
                own_ = canon(m[side + "Owner"], owners_hist)
                results[(k, own_)] = "tie" if m["winnerId"] is None else ("won" if m["winnerId"] == oid else "lost")
    for o, v in season["owners"].items():
        o2 = canon(o, owners_hist)
        rows = []
        for w in v["weeks"]:
            if w["week"] > week:
                continue
            res_ = results.get((w["week"], o2))
            if res_ in ("won", "lost", "tie"):
                rows.append(dict(w, result=res_))
        if len(rows) < MIN_LUCK_WEEKS:
            continue
        act = sum(1 for w in rows if w["result"] == "won") + 0.5 * sum(1 for w in rows if w["result"] == "tie")
        ps = [w["allPlayW"] / max(1, w["allPlayW"] + w["allPlayL"]) for w in rows]
        exp = sum(ps)
        var = sum(p * (1 - p) for p in ps) or 0.25
        z = (act - exp) / math.sqrt(var)
        apw = sum(w["allPlayW"] for w in rows); apl = sum(w["allPlayL"] for w in rows)
        word = "lucky" if z > 0 else "unlucky"
        add("season_luck", [o2], round(act - exp, 2), z,
            f"{D(o2)} is {int(act)}-{len(rows) - int(act)} with an all-play record of {apw}-{apl}: "
            f"{abs(act - exp):.1f} wins {word} so far.", "all-play expected wins", f"{SEASON} season")

    # ---------- 5. player level and bench, against every player-week since 2018 ----------
    try:
        pw = json.load(open(os.path.join(PW, f"{league}_playerweeks.json")))["rows"]
    except FileNotFoundError:
        pw = []
    if pw:
        tw = defaultdict(list)
        for r in pw:
            tw[(r[0], r[1], r[2])].append(r)
        lost = {}
        for g in single:
            if g["year"] >= 2018 and g["winner"] != "tie":
                w_, l_ = (g["home"], g["away"]) if g["winner"] == "home" else (g["away"], g["home"])
                lost[(g["year"], g["period"], l_)] = abs(g["homeScore"] - g["awayScore"])
                lost[(g["year"], g["period"], w_)] = None
        starts = [r[6] for r in pw if r[5]]
        benched = [r[6] for r in pw if not r[5]]
        starts_in_loss = [r[6] for r in pw if r[5] and lost.get((r[0], r[1], r[2])) is not None]
        misses = [r[6] - r[7] for r in pw if r[5] and r[7] is not None and r[7] >= 10]
        lefts, effs, fork_gaps = [], [], []
        for k_, rs in tw.items():
            act = sum(r[6] for r in rs if r[5])
            by = defaultdict(list)
            for r in rs:
                by[r[4]].append(r[6])
            opt, flex = 0, []
            for pos_, n_ in SLOTS.items():
                v_ = sorted(by[pos_], reverse=True)
                opt += sum(v_[:n_])
                if pos_ in ("RB", "WR", "TE"):
                    flex += v_[n_:]
            opt += max(flex) if flex else 0
            left = max(0.0, opt - act)
            lefts.append(left)
            if opt > 0:
                effs.append(100 * act / opt)
            mg_ = lost.get(k_)
            if mg_ is not None and left > mg_:
                fork_gaps.append(left - mg_)
        span_p = "since 2018"

        def rank_hi(pool, x):
            return 1 + sum(1 for y in pool if y > x), len(pool) + 1

        def rank_lo(pool, x):
            return 1 + sum(1 for y in pool if y < x), len(pool) + 1

        lost_now = {}
        for m in facts["matchups"]:
            if not m.get("awayOwner"):
                continue
            for side, oid in (("home", m["homeId"]), ("away", m["awayId"])):
                lost_now[canon(m[side + "Owner"], owners_hist)] = (
                    None if m["winnerId"] == oid else m["margin"])
        for t in facts["perTeam"]:
            if t["owner"] in bye_owners:
                continue
            o = canon(t["owner"], owners_hist)
            top = (t.get("top") or [None])[0]
            if top:
                r_, n_ = rank_hi(starts, top["pts"])
                add("top_start", [o], top["pts"], z_from_upper_tail((r_ - 0.5) / n_),
                    f"{top['n']} gave {D(o)} {top['pts']:.2f}, the {ordinal(r_)}-best start in "
                    f"{n_:,} player-weeks {span_p}.", f"{n_:,} starts", span_p, {"player": top["n"]})
                if lost_now.get(o) is not None:
                    r_, n_ = rank_hi(starts_in_loss, top["pts"])
                    add("top_start_in_a_loss", [o], top["pts"], z_from_upper_tail((r_ - 0.5) / n_),
                        f"{D(o)} lost anyway with {top['n']} putting up {top['pts']:.2f}, the {ordinal(r_)}-most "
                        f"by one starter in a loss in {n_:,} {span_p}.", f"{n_:,} starts in losses", span_p,
                        {"player": top["n"]})
            bb = (t.get("benchTop") or [None])[0]
            if bb:
                r_, n_ = rank_hi(benched, bb["pts"])
                add("bench_bomb", [o], bb["pts"], z_from_upper_tail((r_ - 0.5) / n_),
                    f"{D(o)} left {bb['n']} on the bench for {bb['pts']:.2f}, the {ordinal(r_)}-most points "
                    f"by one benched player in {n_:,} {span_p}.", f"{n_:,} bench player-weeks", span_p,
                    {"player": bb["n"]})
            for sl in (t.get("starterLow") or []):
                if sl.get("proj") is not None and sl["proj"] >= 10:
                    miss = sl["pts"] - sl["proj"]
                    r_, n_ = rank_lo(misses, miss)
                    add("bust", [o], round(miss, 2), -z_from_upper_tail((r_ - 0.5) / n_),
                        f"{sl['n']} was projected {sl['proj']:.1f} and gave {D(o)} {sl['pts']:.2f}, the "
                        f"{ordinal(r_)}-worst miss by a projected 10-point starter in {n_:,} {span_p}.",
                        f"{n_:,} starts projected 10+", span_p, {"player": sl["n"]})
            r_, n_ = rank_hi(lefts, t["left"])
            if t["left"] > 0.005:
                add("points_left", [o], t["left"], z_from_upper_tail((r_ - 0.5) / n_),
                    f"{D(o)} left {t['left']:.2f} on the bench, the {ordinal(r_)}-most in {n_:,} team-weeks "
                    f"{span_p}.", f"{n_:,} team-weeks", span_p)
            else:
                p_perfect = sum(1 for x in lefts if x < 0.005) / len(lefts)
                add("perfect_lineup", [o], 0, z_from_upper_tail(p_perfect),
                    f"{D(o)} set a perfect lineup, which happens in {100 * p_perfect:.0f}% of team-weeks "
                    f"{span_p}.", f"{n_:,} team-weeks", span_p)
            mg_ = lost_now.get(o)
            if mg_ is not None and t["left"] > mg_:
                gap = t["left"] - mg_
                r_, n_ = rank_hi(fork_gaps, gap)
                w_ = t.get("worst") or {}
                add("benched_the_win", [o], round(gap, 2), z_from_upper_tail((r_ - 0.5) / n_ * len(fork_gaps) / max(1, len(lefts))),
                    f"{D(o)} lost by {mg_:.2f} with {t['left']:.2f} on the bench"
                    + (f" (started {w_.get('started')} for {w_.get('startedPts')}, benched {w_.get('benched')} "
                       f"for {w_.get('benchedPts')})" if w_ else "") + ".",
                    "losses where the bench held the margin", span_p,
                    {"decisive": w_.get("delta", 0) > mg_ if w_ else None})

    # ---------- league-week rarity ----------
    # z above is per unit (per owner, per game, per player-week). Newsworthiness is about the league:
    # how often does ANYONE in this league produce something this extreme in a week? With k units
    # tested per league-week, p_week = 1 - (1 - p_unit)^k. Tiers and rarity use the league-week z.
    T = sum(1 for t in facts["perTeam"] if t["owner"] not in bye_owners)
    M = sum(1 for m in facts["matchups"] if m.get("awayOwner"))
    kweek = {k_: T for k_ in ("score_vs_own_career", "score_vs_league_all_time", "season_luck",
                              "points_left", "perfect_lineup", "benched_the_win")}
    kweek.update({k_: M for k_ in ("blowout", "nail_biter", "high_score_in_a_loss", "low_score_in_a_win",
                                   "lifetime_series", "active_streak", "streak_snapped", "first_ever_win")})
    if pw:
        lw = len({(r[0], r[1]) for r in pw}) or 1
        kweek.update({"top_start": len(starts) / lw, "top_start_in_a_loss": len(starts_in_loss) / lw,
                      "bench_bomb": len(benched) / lw, "bust": len(misses) / lw})
    for r in out:
        k_ = kweek.get(r["kind"], 1)
        p_unit = 1 - N.cdf(abs(r["z"]))
        p_week = 1 - (1 - p_unit) ** k_
        zw = z_from_upper_tail(max(p_week, 1e-9)) if p_week < 0.5 else 0.0
        r["unitsPerWeek"] = round(k_, 1)
        r["zUnit"] = r["z"]
        r["z"] = round(zw if r["z"] >= 0 else -zw, 2)
        r["tier"] = tier(r["zUnit"], r["z"])
        r["rarity"] = rarity(r["z"])       # the wording: honest league-wide frequency
        r["direction"] = "high" if r["z"] >= 0 else "low"

    # ---------- rank and tier ----------
    out.sort(key=lambda r: -abs(r["z"]))
    # One story, one entry. The same player, the same game, or the same owner's score seen through
    # two metrics keeps only its strongest reading; the rest are marked duplicate (still in the file).
    def story(r):
        if r.get("player"):
            return ("player", r["player"], r["owners"][0])
        if r["kind"] in ("blowout", "nail_biter", "high_score_in_a_loss", "low_score_in_a_win"):
            return ("game", tuple(sorted(r["owners"])))
        if r["kind"].startswith("score_vs"):
            return ("score", r["owners"][0])
        if r["kind"] in ("points_left", "benched_the_win", "perfect_lineup"):
            return ("bench", r["owners"][0])
        return (r["kind"], tuple(sorted(r["owners"])))
    # a low score in a game is the same story as that game's low-scoring win
    seen = set()
    for r in out:
        k_ = story(r)
        r["duplicate"] = k_ in seen
        seen.add(k_)
    tiers = {t: sum(1 for r in out if r["tier"] == t and not r["duplicate"])
             for t in ("HEADLINE", "PROMOTE", "SUPPORT", "SUPPRESS")}
    res = {"league": league, "week": week, "tiers": tiers, "insights": out,
           "note": "Generated by gen2/insights.py. The page never prints z or sigma; use `plain` and `rarity`."}
    p = os.path.join(DATA, f"{league}_wk{week}_insights.json")
    json.dump(res, open(p, "w"), indent=1)
    return res


if __name__ == "__main__":
    lg, wk = sys.argv[1], int(sys.argv[2])
    r = run(lg, wk)
    print(lg, "week", wk, r["tiers"])
    for x in r["insights"]:
        if x["tier"] in ("HEADLINE", "PROMOTE") and not x["duplicate"]:
            print(f'  {x["tier"]:8} unit={x["zUnit"]:+.2f} week={x["z"]:+.2f}  {x["plain"]}')
