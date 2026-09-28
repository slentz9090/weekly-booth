"""Every player-week on every roster since 2018, for player-level outliers.

    python3 gen2/playerweeks.py   -> gen2/data/<league>_playerweeks.json

Row: [year, week, owner, player, pos, started(1/0), points, projection]
Only regular-season single weeks are kept (a two-week playoff round is not a week).
Kept out of docs/ so it is not served on the site.
"""
import gzip, json, os
from games import load as load_core, owner_names

UP = "/mnt/user-data/uploads/Downloads"
OUT = os.path.join(os.path.dirname(__file__), "data")
POS = {1: "QB", 2: "RB", 3: "WR", 4: "TE", 5: "K", 16: "DST"}
BENCH = {20, 21}


def weeks(league, year):
    if league == "dlffl":
        p = f"{UP}/ffl_{year}_weeks.json.gz"
        if not os.path.exists(p):
            return {}
        return {int(w["week"]): json.loads(w["rawBody"]) for w in json.load(gzip.open(p))["weeks"]
                if w.get("httpStatus") == 200}
    p = f"{UP}/friends_of_herb_{year}_raw.json"
    if not os.path.exists(p):
        return {}
    return {int(k): v for k, v in json.load(open(p))["weeks"].items()}


def build(league):
    rows = []
    for y in range(2018, 2026):
        core = load_core(league, y)
        if core is None:
            continue
        own = owner_names(core)
        reg = core["settings"]["scheduleSettings"]["matchupPeriodCount"]
        for wk, b in sorted(weeks(league, y).items()):
            if wk > reg:
                continue
            for t in b.get("teams", []):
                o = own.get(t["id"], {}).get("owner")
                for e in t.get("roster", {}).get("entries", []):
                    pl = e["playerPoolEntry"]["player"]
                    act = proj = None
                    for s in pl.get("stats", []):
                        if s.get("scoringPeriodId") == wk and s.get("statSplitTypeId") == 1:
                            if s.get("statSourceId") == 0:
                                act = s.get("appliedTotal")
                            elif s.get("statSourceId") == 1:
                                proj = s.get("appliedTotal")
                    if act is None:
                        continue
                    rows.append([y, wk, o, pl.get("fullName"), POS.get(pl.get("defaultPositionId"), "?"),
                                 0 if e["lineupSlotId"] in BENCH else 1, round(act, 2),
                                 round(proj, 2) if proj is not None else None])
    return rows


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for lg in ("dlffl", "foh"):
        r = build(lg)
        p = os.path.join(OUT, f"{lg}_playerweeks.json")
        json.dump({"league": lg, "cols": ["year", "week", "owner", "player", "pos", "started", "pts", "proj"],
                   "rows": r}, open(p, "w"), separators=(",", ":"))
        print(lg, len(r), "player-weeks", os.path.getsize(p), "bytes")
