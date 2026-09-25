"""Index pages and the two teaser files.

The league index pages get a Week 2 card above Week 1 and their bench ledger
swapped for the season-to-date table. The homepage's "This Week" cards get
repointed at Week 2. Everything is a targeted patch of the published HTML so
the Week 1 pages keep their exact markup.
"""
import json
import os
import re

from compute import DATA, load

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wb", "docs")
SITE = "https://slentz9090.github.io/weekly-booth"

HEAD = {
    "dlffl": {
        "league": "Dewart Lake FFL",
        "headline": "DA Put 140 On His Wife And Boomer Had Her Winning",
        "accent": "var(--gold)",
        "meta": "12 teams · snake · 0.5 PPR",
        "note": ("Owner of the Week: Scott Reisert, 142.08 with a perfect lineup. Worst Owner: Adam Hershberger, "
                 "58.86, the lowest score in that league."),
        "date": "September 24, 2026",
        "sub": "Six games, five pieces of hardware, the Bench Ledger, and twelve calls graded in public.",
    },
    "foh": {
        "league": "Friends of Herb",
        "headline": "Michael Turner Benched 37 Points In A Game He Was Not Playing",
        "accent": "var(--blue)",
        "indexAccent": "var(--gold)",
        "meta": "11 teams · auction · 0.5 PPR",
        "note": ("Owner of the Week: Aron Rogers, 125.20 with 3.70 wasted. Worst Owner: Ryan Kelly, 52.52, the "
                 "lowest score of the season."),
        "date": "September 24, 2026",
        "sub": "Five games, a bye, the Freiermuth Rule, and eleven calls graded in public.",
    },
}

TEASERS = {
    "dlffl": """Gil and Boomer have Week 2 of the Dewart Lake FFL.

DA put 140.02 on Mama Beth, who left Patrick Mahomes and 31.98 on her bench, and Boomer had her winning that game. He went 4 and 8 on last week's calls and reads every one of them back at the top. Scott Reisert turned in a perfect lineup, one of you scored 58.86 and would have lost to the entire league, and the bench ledger now carries a running season total for all twelve of you.

{site}/dlffl/week-2.html
""",
    "foh": """Gil and Boomer have Week 2 of Friends of Herb.

Michael Turner benched Davante Adams and 37.50 on the one Sunday he had no opponent. Bob Dorsch released Pat Freiermuth, which has its own section for reasons everybody here understands. Rahul Pahuja took the week at 130.20, Josh Allen went for 46.82 in a loss, and Boomer went 4 and 6 and reads all of it back at the top.

{site}/foh/week-2.html
""",
}


def season_table(league, teams_note):
    s = load(f"{league}_season.json")
    rows = sorted(s["owners"].items(), key=lambda kv: -kv[1]["totals"]["benchPoints"])
    trs = []
    for i, (owner, o) in enumerate(rows, 1):
        t = o["totals"]
        trs.append(
            f"<tr><td>{i}</td><th scope=\"row\">{o['display']}</th>"
            f"<td>{t['benchPoints']:.2f}</td>"
            f"<td style=\"text-align:right\">{t['pointsFor']:.2f}</td>"
            f"<td style=\"text-align:right;padding-right:0\">{t['allPlayW']}-{t['allPlayL']}</td></tr>"
        )
    cap = f"Season through Week 2: points left on the bench, points scored, and record against the whole league"
    return (
        f'<table class="led"><caption>{cap}</caption><thead><tr>'
        f'<th scope="col"><span class="sr">Rank</span></th><th scope="col">Owner</th>'
        f'<th scope="col">Benched</th><th scope="col">Points</th><th scope="col">All-play</th>'
        f"</tr></thead><tbody>{''.join(trs)}</tbody></table>"
        f'<p class="note">{teams_note}</p>'
    )


def league_index(league):
    path = os.path.join(DOCS, league, "index.html")
    h = open(path, encoding="utf-8").read()
    spec = HEAD[league]
    card = (
        f'<section class="mcard"><div class="mc-top"><h3 class="mc-rib" style="color:{spec.get("indexAccent", spec["accent"])}">Week 2</h3></div>'
        f'<div class="mc-row win"><span class="mc-name"><a href="week-2.html">{spec["headline"]}</a></span>'
        f'<span class="mc-sub">{spec["date"]}</span></div>'
        f'<p class="mc-note">{spec["sub"]}</p></section>'
    )
    if 'href="week-2.html"' not in h:
        h = h.replace('<h2 id="issues">Installments</h2>', '<h2 id="issues">Installments</h2>\n' + card, 1)
    # swap the Week 1 ledger table for the season table
    note = ("Bench points are your best possible lineup minus the one you turned in. All-play is your record "
            "against every other team every week.")
    h = re.sub(r'<table class="led">.*?</table>', lambda _m: season_table(league, note), h, count=1, flags=re.S)
    h = h.replace('<h2 id="season">The Bench Ledger</h2>',
                  '<h2 id="season">The Bench Ledger, Season To Date</h2>', 1)
    # the index pages embed the stylesheet they shipped with, so the Week 2
    # additions have to be injected here too
    h = h.replace("</style>",
                  ".led th:nth-child(4){text-align:right;padding-right:0}\n"
                  "@media print{.led tbody tr:first-child th,"
                  ".led tbody tr:first-child td{color:#000 !important}}\n</style>", 1)
    open(path, "w", encoding="utf-8").write(h)
    print("patched", path, len(h), "bytes")


def homepage():
    path = os.path.join(DOCS, "index.html")
    h = open(path, encoding="utf-8").read()
    for league in ("dlffl", "foh"):
        spec = HEAD[league]
        new = (
            f'<section class="mcard"><div class="mc-top"><h3 class="mc-rib" style="color:{spec["accent"]}">'
            f'{spec["league"]} · Week 2</h3></div>'
            f'<div class="mc-row win"><span class="mc-name"><a href="{league}/week-2.html">{spec["headline"]}</a></span>'
            f'<span class="mc-sub">{spec["meta"]}</span></div>'
            f'<p class="mc-note">{spec["note"]}</p>'
            f'<p class="note"><a href="{league}/">All {spec["league"]} installments</a></p></section>'
        )
        pat = re.compile(
            r'<section class="mcard">(?:(?!</section>).)*?' + league + r'/week-[12]\.html.*?</section>', re.S)
        if pat.search(h):
            h = pat.sub(lambda _m: new, h, count=1)
        else:
            print("  homepage: no Week 1 card found for", league)
    open(path, "w", encoding="utf-8").write(h)
    print("patched", path, len(h), "bytes")


def teasers():
    for league, text in TEASERS.items():
        p = os.path.join(DOCS, f"{league}-latest.txt")
        body = text.format(site=SITE)
        assert "—" not in body and " ," not in body
        open(p, "w", encoding="utf-8").write(body)
        print("wrote", p, len(body), "bytes")


if __name__ == "__main__":
    for lg in ("dlffl", "foh"):
        league_index(lg)
    homepage()
    teasers()
