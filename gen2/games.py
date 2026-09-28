"""Build the all-time game log for each league from the raw ESPN history pulls.

Inputs (staged from Spencer's Downloads):
  ffl_<year>_core.json.gz         Dewart Lake, 2009-2025
  friends_of_herb_<year>_raw.json Friends of Herb, ESPN era 2011-2025
Output: gen2/data/<league>_games.json (not committed; rebuilt each run), one row per decided head-to-head game.

Owner identity is the member's "First Last" name, which is what the history files use.
Dewart Lake's two-week playoff rounds are ONE game whose score spans two weeks, so those rows
carry weeks=2 and are excluded from any single-week score distribution.
"""
import gzip, json, os, sys

UP = "/mnt/user-data/uploads/Downloads"
DOCS = os.path.join(os.path.dirname(__file__), "data")   # not served on the site


def load(league, year):
    if league == "dlffl":
        p = f"{UP}/ffl_{year}_core.json.gz"
        if not os.path.exists(p):
            return None
        raw = json.load(gzip.open(p))
        b = json.loads(raw["rawBody"])
        return b[0] if isinstance(b, list) else b
    p = f"{UP}/friends_of_herb_{year}_raw.json"
    if not os.path.exists(p):
        return None
    c = json.load(open(p))["core"]
    return c[0] if isinstance(c, list) else c


def owner_names(core):
    def norm(n):
        # ESPN stores a few owners in all caps or all lower ("RYAN COUTURE", "dennis couture").
        return n.title() if (n.isupper() or n.islower()) and " " in n else n
    mem = {m["id"]: norm(f'{m.get("firstName","").strip()} {m.get("lastName","").strip()}'.strip())
           for m in core.get("members", [])}
    out = {}
    for t in core["teams"]:
        ids = t.get("owners") or [t.get("primaryOwner")]
        names = [mem.get(i) for i in ids if mem.get(i)]
        out[t["id"]] = {"owner": names[0] if names else f"team{t['id']}",
                        "team": (t.get("name") or f'{t.get("location","")} {t.get("nickname","")}').strip()}
    return out


def games(league, years):
    rows = []
    for y in years:
        core = load(league, y)
        if core is None:
            continue
        own = owner_names(core)
        s = core["settings"]["scheduleSettings"]
        mlen = s.get("matchupPeriodLength", 1)
        plen = s.get("playoffMatchupPeriodLength", mlen)
        for m in core["schedule"]:
            if not m.get("away") or m.get("winner") in (None, "UNDECIDED"):
                continue
            h, a = m["home"], m["away"]
            po = m.get("playoffTierType", "NONE") != "NONE"
            winner = {"HOME": "home", "AWAY": "away", "TIE": "tie"}[m["winner"]]
            rows.append({
                "year": y, "period": m["matchupPeriodId"], "playoff": po,
                "tier": m.get("playoffTierType", "NONE"),
                "weeks": plen if po else mlen,
                "home": own[h["teamId"]]["owner"], "homeTeam": own[h["teamId"]]["team"],
                "homeScore": round(h["totalPoints"], 2),
                "away": own[a["teamId"]]["owner"], "awayTeam": own[a["teamId"]]["team"],
                "awayScore": round(a["totalPoints"], 2),
                "winner": winner,
            })
    return rows


if __name__ == "__main__":
    for lg, yrs in (("dlffl", range(2009, 2026)), ("foh", range(2011, 2026))):
        g = games(lg, yrs)
        p = os.path.join(DOCS, f"{lg}_games.json")
        json.dump({"league": lg, "note": __doc__.strip().splitlines()[0], "games": g},
                  open(p, "w"), separators=(",", ":"))
        print(lg, len(g), "games", os.path.getsize(p), "bytes")
