"""THE RACE (added Week 8, 2026-11-03).

Every team's chance to make the playoffs and to win the title, from FantasyPros'
League Analyzer (getProjectedStandings), plus the bracket if the season ended today.
Data file: docs/data/<league>_race_wk<N>.json, written by the weekly run from the
FantasyPros pull (public odds only; nothing from the private waiver run).

render(data, copy) -> HTML string for the section. Reuses the .ht tiles and the
.led table CSS already on every page. No em dashes anywhere.
"""
import html as _h


def _e(s):
    return _h.escape(str(s), quote=True)


def _pct(v):
    v = str(v).strip()
    if v.startswith("<"):
        return "under 1%"
    return v if v.endswith("%") else v + "%"


def render(data, copy):
    """data: {league, week, spots, weeksLeft, rounds, teams:[{owner, team, w, l, playoffs, title, projW, projL, projRank}], bracket:[[a,b],[c,d]]}
    copy: {gilIntro, tiles:[[big, small],...], gilAfter, boomer1, gilFair, boomer2}"""
    out = []
    out.append('<h2 id="race">The Race</h2>')
    out.append('<p><span class="who">GIL:</span> %s</p>' % copy["gilIntro"])
    tiles = "".join('<div><b>%s</b><span>%s</span></div>' % (_e(b), s) for b, s in copy["tiles"])
    out.append('<div class="ht">%s</div>' % tiles)
    rows = []
    teams = sorted(data["teams"], key=lambda t: t["projRank"])
    for i, t in enumerate(teams, 1):
        rows.append(
            '<tr><td>%d</td><th scope="row">%s</th><td>%d and %d</td><td>%s</td><td>%s</td></tr>'
            % (i, _e(t["owner"]), t["w"], t["l"], _pct(t["playoffs"]), _pct(t["title"]))
        )
    out.append(
        '<table class="led"><caption>%s</caption><thead><tr>'
        '<th scope="col"><span class="sr">Rank</span></th><th scope="col">Owner</th>'
        '<th scope="col">Record</th><th scope="col">Playoffs</th><th scope="col">Title</th>'
        '</tr></thead><tbody>%s</tbody></table>' % (copy["caption"], "".join(rows))
    )
    out.append('<p><span class="who">GIL:</span> %s</p>' % copy["gilAfter"])
    out.append('<div class="bcom"><p><span class="who">BOOMER:</span> %s</p></div>' % copy["boomer1"])
    out.append('<p><span class="who">GIL:</span> %s</p>' % copy["gilFair"])
    out.append('<div class="bcom"><p><span class="who">BOOMER:</span> %s</p></div>' % copy["boomer2"])
    s = "".join(out)
    assert "—" not in s, "em dash in THE RACE"
    return s


NAV_ITEM = '<li><a href="#race">The Race</a></li>'


def insert(page_html, section_html):
    """Insert the section before the Owner Spotlight and add the nav item after The Scoreboard."""
    anchor = '<h2 id="spotlight">'
    assert page_html.count(anchor) == 1, "spotlight anchor"
    page_html = page_html.replace(anchor, section_html + anchor)
    nav_anchor = '<li><a href="#board">The Scoreboard</a></li>'
    assert page_html.count(nav_anchor) == 1, "nav anchor"
    if NAV_ITEM not in page_html:
        page_html = page_html.replace(nav_anchor, nav_anchor + NAV_ITEM)
    return page_html
