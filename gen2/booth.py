"""THE WEEKLY BOOTH, page generator.

Rebuilt 2026-09-24 from the published Week 1 pages after the original gen2 was
lost with an old session scratchpad. The design system (style.css), the page
script (script.js) and the two league marks in assets/ were extracted verbatim
from docs/dlffl/week-1.html and docs/foh/week-1.html, so Week 2 renders in the
same skin as Week 1.

COMMIT THIS DIRECTORY TO THE REPO. The reason Week 2 cost an extra hour is that
nobody did that in Week 1.

AUDIO_ON stays False. See the runbook's audio section.
"""
from __future__ import annotations

import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

AUDIO_ON = False
SITE = "https://slentz9090.github.io/weekly-booth"

LEAGUES = {
    "dlffl": {
        "name": "Dewart Lake FFL",
        "dir": "dlffl",
        "mark": "mark_dlffl.svg",
        "markLabel": "Dewart Lake Fantasy Football League",
        "teams": 12,
    },
    "foh": {
        "name": "Friends of Herb",
        "dir": "foh",
        "mark": "mark_foh.svg",
        "markLabel": "Friends of Herb",
        "teams": 11,
    },
}


# Added in Week 2 for the graded calls and the ledger's season column. Kept
# apart from assets/style.css so that file stays a verbatim copy of Week 1.
EXTRA_CSS = """
.grade{display:inline-block;font-size:11.5px;font-weight:700;letter-spacing:.12em;
  text-transform:uppercase;padding:2px 7px;border-radius:999px;border:1px solid currentColor;
  vertical-align:2px;white-space:nowrap;margin-left:4px}
.gr-yes{color:var(--green)}
.gr-no{color:var(--red)}
.calls.graded .call-t{color:var(--tx)}
.led td:nth-child(5),.led th:nth-child(5){text-align:right;white-space:nowrap;width:1%}
.led td:nth-child(5){color:var(--mut)}
.gr-open{color:var(--mut)}
.led th:nth-child(4){text-align:right;padding-right:0}
.led td:nth-child(5){padding-right:0}
@media (max-width:380px){.led{font-size:14px}.led td,.led th{padding-right:7px}
  .led .led-v{white-space:normal}}
@media print{.led tbody tr:first-child th,.led tbody tr:first-child td{color:#000 !important}}
@media print{.grade{border-color:#000;color:#000}}
@media (forced-colors:active){.mc-row.lose .mc-fill{background:CanvasText}}
"""


def _asset(name: str) -> str:
    with open(os.path.join(ASSETS, name), encoding="utf-8") as fh:
        return fh.read()


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def slug(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
    return s


def num(v) -> str:
    """Scores always read with two decimals, the way the booth says them."""
    return f"{float(v):.2f}"


# ---------------------------------------------------------------- components

def gil(text: str) -> str:
    return f'<p><span class="who">GIL:</span> {text}</p>'


def boomer(text: str, tone: str = "") -> str:
    """tone: "" (plain panel), "good" or "bad". Gil never gets a panel."""
    cls = "bcom" + (f" bcom-{tone}" if tone else "")
    return f'<div class="{cls}"><p><span class="who">BOOMER:</span> {text}</p></div>'


def audio(*_args, **_kwargs) -> str:
    if not AUDIO_ON:
        return ""
    raise NotImplementedError("Audio is off. See the runbook before turning it back on.")


def mcard(anchor, ribbon, win, lose, note, scale, key=False, ribbon_color="var(--gold)"):
    """One matchup. win/lose are dicts: team, owner, score, left.

    The bar scale is shared by every card on the page: solid is points started,
    the hatched tail is points left on the bench. Bars default visible; the
    animation is the enhancement.
    """
    rows = []
    for side, t in (("win", win), ("lose", lose)):
        fill = t["score"] / scale * 100
        tail = t["left"] / scale * 100
        tail_div = (f'<div class="mc-tail" style="left:{fill:.2f}%;width:{tail:.2f}%"></div>'
                    if t["left"] > 0 else "")
        rows.append(
            f'<div class="mc-row {side}" id="t-{slug(t["team"])}">'
            f'<span class="mc-name">{esc(t["team"])}</span>'
            f'<span class="mc-score">{num(t["score"])}</span>'
            f'<span class="mc-sub">{esc(t["owner"])}</span>'
            f'<span class="mc-left">{"nothing left behind" if t["left"] == 0 else num(t["left"]) + " left behind"}</span>'
            f'<div class="mc-track" aria-hidden="true">'
            f'<div class="mc-fill" style="width:{fill:.2f}%"></div>'
            + tail_div
            + f"</div></div>"
        )
    keyline = (
        '<p class="mc-key">Solid = the points you started. Hatched = the points you left '
        "behind, meaning your best possible lineup minus the one you turned in. Every bar "
        "on this page is on the same scale.</p>"
        if key
        else ""
    )
    label = f'{win["team"]} versus {lose["team"]}'
    return (
        f'<section class="mcard" id="{anchor}" aria-labelledby="{anchor}-h">'
        f'<div class="mc-top"><h3 class="mc-rib" id="{anchor}-h" style="color:{ribbon_color}">{esc(ribbon)}</h3>'
        f'<button class="mc-lnk" type="button" data-a="{anchor}" aria-label="Share or copy a link to {esc(label)}">Link</button></div>'
        + "".join(rows)
        + f'<p class="mc-note">{note}</p>{keyline}</section>'
    )


def byecard(anchor, ribbon, team, note, scale, ribbon_color="var(--gold)"):
    """Friends of Herb runs eleven teams, so somebody sits every week."""
    fill = team["score"] / scale * 100
    tail = team["left"] / scale * 100
    tail_div = (f'<div class="mc-tail" style="left:{fill:.2f}%;width:{tail:.2f}%"></div>'
                if team["left"] > 0 else "")
    return (
        f'<section class="mcard" id="{anchor}" aria-labelledby="{anchor}-h">'
        f'<div class="mc-top"><h3 class="mc-rib" id="{anchor}-h" style="color:{ribbon_color}">{esc(ribbon)}</h3>'
        f'<button class="mc-lnk" type="button" data-a="{anchor}" aria-label="Share or copy a link to {esc(team["team"])} on the bye">Link</button></div>'
        f'<div class="mc-row win bye" id="t-{slug(team["team"])}">'
        f'<span class="mc-name">{esc(team["team"])}</span>'
        f'<span class="mc-score">{num(team["score"])}</span>'
        f'<span class="mc-sub">{esc(team["owner"])} · no opponent</span>'
        f'<span class="mc-left">{"nothing left behind" if team["left"] == 0 else num(team["left"]) + " left behind"}</span>'
        f'<div class="mc-track" aria-hidden="true">'
        f'<div class="mc-fill" style="width:{fill:.2f}%"></div>'
        + tail_div
        + f"</div></div>"
        + f'<p class="mc-note">{note}</p></section>'
    )


def award(kind, title, winner, gil_line, boomer_line):
    """kind: good or bad. Boomer's body text is the only coloured copy."""
    return (
        f'<div class="aw {kind}"><h3>{esc(title)}</h3>'
        f'<p class="win">{esc(winner)}</p>'
        f'<p><span class="who">GIL:</span> {gil_line}</p>'
        f'<p><span class="who">BOOMER:</span> {boomer_line}</p></div>'
    )


def calls_list(items):
    """items: (team, call, support)."""
    lis = "".join(
        f'<li class="call"><p class="call-t"><strong>{esc(t)}.</strong> {esc(c)}</p>'
        f'<p class="call-s">{s}</p></li>'
        for t, c, s in items
    )
    return f'<ol class="calls">{lis}</ol>'


def graded_list(items):
    """items: (team, call, verdict, detail). verdict is RIGHT or WRONG."""
    lis = []
    for team, call, verdict, detail in items:
        v = verdict.upper()
        cls = {"RIGHT": "gr-yes", "WRONG": "gr-no"}.get(v, "gr-open")
        lis.append(
            f'<li class="call"><p class="call-t"><strong>{esc(team)}.</strong> {esc(call)} '
            f'<span class="grade {cls}">{esc(v)}</span></p>'
            f'<p class="call-s">{detail}</p></li>'
        )
    return f'<ol class="calls graded">{"".join(lis)}</ol>'


def ledger(rows, week, season_note=None):
    """rows: (owner, benched, verdict, verdict_class). Styling keys off the
    verdict, not the rank: only a row that actually cost a game goes red."""
    trs = "".join(
        f"<tr><td>{i}</td><th scope=\"row\">{esc(o)}</th><td>{num(b)}</td>"
        f'<td class="led-v{(" " + c) if c else ""}">{esc(v)}</td>'
        f"<td>{num(s)}</td></tr>"
        for i, (o, b, v, c, s) in enumerate(rows, 1)
    )
    cap = f"Week {week}: points left on the bench, whether it actually cost the game, and the running season total"
    extra = f'<p class="mc-note">{season_note}</p>' if season_note else ""
    return (
        f'<table class="led"><caption>{esc(cap)}</caption><thead><tr>'
        f'<th scope="col"><span class="sr">Rank</span></th><th scope="col">Owner</th>'
        f'<th scope="col">Benched</th><th scope="col">Cost him?</th>'
        f'<th scope="col">Season</th></tr></thead><tbody>{trs}</tbody></table>{extra}'
    )


def jump(teams):
    """teams: (team, owner) in alphabetical order by team."""
    opts = "".join(
        f'<option value="t-{slug(t)}">{esc(t)} · {esc(o)}</option>'
        for t, o in sorted(teams, key=lambda x: x[0].lower())
    )
    return (
        '<div class="jump"><label for="jump">Jump to your team</label>'
        f'<select id="jump"><option value="">Pick one…</option>{opts}</select></div>'
    )


NAV = (
    '<nav class="nav" aria-label="Sections"><ul>'
    '<li><a href="#board">The Scoreboard</a></li>'
    '<li><a href="#calls">On The Record</a></li>'
    '<li><a href="#hardware">The Hardware</a></li>'
    '<li><a href="#ledger">The Bench Ledger</a></li>'
    '<li><a href="#wire">The Waiver Wire</a></li>'
    '<li><a href="#next">Next Sunday</a></li></ul></nav>'
)


def page(league, week, headline, dek, sections, meta_desc, og_image, other_link, nav=None):
    """Assemble the whole page. `sections` is the body HTML between the dek and
    the footer, already built by the league module."""
    L = LEAGUES[league]
    title = f"{L['name']}, Week {week} | The Weekly Booth"
    url = f"{SITE}/{L['dir']}/week-{week}.html"
    mark = _asset(L["mark"])
    style = _asset("style.css")
    script = _asset("script.js")
    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta_desc)}">
<meta name="author" content="The Weekly Booth">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#16243c">
<meta property="og:type" content="article">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="The Weekly Booth">
<meta property="og:title" content="{esc(headline)}">
<meta property="og:description" content="{esc(meta_desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(headline)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(headline)}">
<meta name="twitter:description" content="{esc(meta_desc)}">
<meta name="twitter:image" content="{SITE}/og/{og_image}">
<link rel="icon" href="{SITE}/og/booth-icon.png" type="image/png">
<link rel="apple-touch-icon" href="{SITE}/og/booth-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700&display=swap">
<meta property="article:published_time" content="2026-09-24T09:00:00-04:00">
<meta name="twitter:image:alt" content="{esc(headline)}">
<style>{style}{EXTRA_CSS}</style>
<script>document.documentElement.className+=' js';</script>
</head>"""
    body = f"""<body>
<a class="skip" href="#main">Skip to the week</a>
<div id="prog" aria-hidden="true"></div>
<p class="sr" id="cplive" role="status" aria-live="polite"></p>
<main class="wrap" id="main" tabindex="-1">
<header class="mast">{mark}<div class="mt"><p class="m1">The Weekly Booth</p><p class="m2">{esc(L['name'])}</p></div><div class="m3">Week {week} · 2026<br>Gil Prather &amp; Boomer Latour</div></header>
<nav class="crumb" aria-label="Breadcrumb"><a href="{SITE}/">The Weekly Booth</a> <span aria-hidden="true">&#8250;</span> <a href="./">{esc(L['name'])}</a> <span aria-hidden="true">&#8250;</span> <span aria-current="page">Week {week}</span></nav>
{nav or NAV}
<h1>{esc(headline)}</h1>
<p class="dek">{dek}</p>
{sections}
</main>
<footer class="wrap foot">
<p>THE WEEKLY BOOTH: {esc(L['name'])}, Week {week}, 2026. Gil Prather and Boomer Latour. Every number on this page is pulled from the league and checked before it is spoken.</p><p class="note">Scores are computed under each league's own settings, so the same player can be worth different numbers in two different buildings.</p><p><a href="{SITE}/">The Weekly Booth</a> &nbsp; <a href="{SITE}/{L['dir']}/">{esc(L['name'])}, 2026</a> &nbsp; <a href="{other_link[0]}">{esc(other_link[1])}</a></p>
</footer>
<script>
{script}
</script>
</body>
</html>"""
    return head + "\n" + body


def sweep(doc: str) -> None:
    """Hard rule 13 and the punctuation trap from the runbook."""
    bad = []
    if "—" in doc:
        bad.append("em dash (U+2014)")
    if " ," in doc:
        bad.append("space before a comma")
    if "–" in doc:
        bad.append("en dash (U+2013)")
    if bad:
        raise SystemExit("SWEEP FAILED: " + ", ".join(bad))
