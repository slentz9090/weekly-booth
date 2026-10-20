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

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")
SITE = "https://slentz9090.github.io/weekly-booth"

WK = int(os.environ.get("WEEK", "6"))

HEAD = {
    "dlffl": {
        "league": "Dewart Lake FFL",
        "headline": "DA Has Lost To Casey Couture Ten Straight Times. Two Bench Swaps Would Have Won This One By 0.38.",
        "accent": "var(--gold)",
        "meta": "12 teams · snake · 0.5 PPR",
        "note": ("Owner of the Week: Kent Frenger, 136.90, the high score of the week by 32.76. "
                 "Worst Owner: Scott Reisert, 68.68, who lost by 0.44 with the winning swap on his bench."),
        "date": "October 20, 2026",
        "sub": "Six games, Family Sunday goes to the sons, a 69-point winner, five pieces of hardware, the Bench Ledger, and twelve calls graded in public.",
    },
    "foh": {
        "league": "Friends of Herb",
        "headline": "Bob Dorsch Cut Tyler Shough For Scoring Less Than Zero. Aron Rogers Signed Him And He Scored 32.96.",
        "accent": "var(--blue)",
        "indexAccent": "var(--gold)",
        "meta": "11 teams · auction · 0.5 PPR",
        "note": ("Owner of the Week: Aron Rogers, 119.46, with a perfect lineup. Worst Owner: Matt Davis, 71.48, "
                 "a week after scoring 170.70."),
        "date": "October 20, 2026",
        "sub": "Five games, a bye, the Freiermuth Rule broken by its namesake, Billy Norton's first win, and eleven calls graded in public.",
    },
}

EXTRA_CARDS = {
    # published between issues; inserted above the previous week, below the new one
    "foh": [(
        "mnf-week-3.html", "Week 3 · Monday Night Special",
        "Aron Rogers Needs A Bear To Outrun His Own Teammate", "September 28, 2026",
        "Two unbeaten teams, fifteen meetings deep, down to two Chicago Bears running backs on Monday night.",
    )],
}

TEASERS = {
    "dlffl": """Gil and Boomer have Week 6 of the Dewart Lake FFL.

Family Sunday went to the sons. Casey beat DA for the tenth straight time, and two bench swaps would have won DA the damn game by 0.38. Spencer beat Mama Beth even though the running back he cut this week scored 13.70 for her after she claimed him. Ryan Reed won with 69.12, the fifth-lowest winning score in this league since 2009, because Scott Reisert left a half-point swap on his bench and lost by 0.44. Kent Frenger scored 136.90 and benched a quarterback who scored 26.96. Boomer took both parents and went 4 and 8.

{site}/dlffl/week-6.html
""",
    "foh": """Gil and Boomer have Week 6 of Friends of Herb.

Bob Dorsch cut Tyler Shough for scoring less than zero. Aron Rogers signed him and he scored 32.96, the most by any quarterback in a lineup this week. The receiver Dorsch signed instead scored 20.20 on Dorsch's bench in a 1.88-point loss, so the man the Freiermuth Rule is named for broke the Freiermuth Rule, with Pat Freiermuth in his lineup. Billy Norton won his first game, over a Matt Davis who scored 71.48 a week after scoring 170.70. Rahul Pahuja scored 136.24, the most in the league, on his bye. Boomer called two of those and still went 5 and 6.

{site}/foh/week-6.html
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
    cap = f"Season through Week {WK}: points left on the bench, points scored, and record against the whole league"
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
    def mk(href, label, headline, date, sub):
        return (
            f'<section class="mcard"><div class="mc-top"><h3 class="mc-rib" style="color:{spec.get("indexAccent", spec["accent"])}">{label}</h3></div>'
            f'<div class="mc-row win"><span class="mc-name"><a href="{href}">{headline}</a></span>'
            f'<span class="mc-sub">{date}</span></div>'
            f'<p class="mc-note">{sub}</p></section>'
        )
    cards = [mk(f"week-{WK}.html", f"Week {WK}", spec["headline"], spec["date"], spec["sub"])]
    cards += [mk(*c) for c in EXTRA_CARDS.get(league, []) if f'href="{c[0]}"' not in h]
    if f'href="week-{WK}.html"' not in h:
        h = h.replace('<h2 id="issues">Installments</h2>', '<h2 id="issues">Installments</h2>\n' + "\n".join(cards), 1)
    # swap the Week 1 ledger table for the season table
    note = ("Bench points are your best possible lineup minus the one you turned in. All-play is your record "
            "against every other team every week.")
    h = re.sub(r'<table class="led">.*?</table>', lambda _m: season_table(league, note), h, count=1, flags=re.S)
    dup = f'<p class="note">{note}</p>'
    while dup + dup in h:
        h = h.replace(dup + dup, dup)
    # social tags follow the newest week
    desc = {"dlffl": "Gil and Boomer call the Dewart Lake FFL every week of the 2026 season. Latest: " + spec["headline"].rstrip(".!?") + ".",
            "foh": "Gil and Boomer call Friends of Herb every week of the 2026 season. Latest: " + spec["headline"].rstrip(".!?") + "."}[league]
    h = re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',
               lambda m_: m_.group(1) + desc + m_.group(2), h)
    h = re.sub(r'og/' + league + r'-week-\d+\.png', f'og/{league}-week-{WK}.png', h)
    h = h.replace('<h2 id="season">The Bench Ledger</h2>',
                  '<h2 id="season">The Bench Ledger, Season To Date</h2>', 1)
    # the index pages embed the stylesheet they shipped with, so the Week 2
    # additions have to be injected here too
    if ".led th:nth-child(4){text-align:right" not in h:
      h = h.replace("</style>",
                  ".led th:nth-child(4){text-align:right;padding-right:0}\n"
                  "@media print{.led tbody tr:first-child th,"
                  ".led tbody tr:first-child td{color:#000 !important}}\n</style>", 1)
    open(path, "w", encoding="utf-8").write(h)
    print("patched", path, len(h), "bytes")


def homepage():
    """Disabled 2026-09-28. The root page stays neutral and never lists either league:
    the two leagues are separate audiences and must never link to each other."""
    return
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
