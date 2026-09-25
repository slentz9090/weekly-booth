"""Friends of Herb, Week 2. Editorial.

Eleven teams, so one bye every week. The Freiermuth Rule lives on this page only.
No joke on this page may repeat one from the Dewart Lake page. Spencer reads both.
"""
import os

import booth
from booth import award, boomer, byecard, calls_list, gil, graded_list, jump, ledger, mcard

# Friends of Herb carries one section the other league does not.
NAV = (
    '<nav class="nav" aria-label="Sections"><ul>'
    '<li><a href="#board">The Scoreboard</a></li>'
    '<li><a href="#freiermuth">The Freiermuth Rule</a></li>'
    '<li><a href="#calls">On The Record</a></li>'
    '<li><a href="#hardware">The Hardware</a></li>'
    '<li><a href="#ledger">The Bench Ledger</a></li>'
    '<li><a href="#wire">The Waiver Wire</a></li>'
    '<li><a href="#next">Next Sunday</a></li></ul></nav>'
)
from compute import by_owner, hardware, ledger_rows, load

FACTS = load("foh_wk2_facts.json")
SEASON = load("foh_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 152.30

HEADLINE = "Michael Turner Benched 37 Points In A Game He Was Not Playing"
DEK = (
    "Turner sat Davante Adams and his 37.50 on the one Sunday of the year he had no opponent, which is the safest "
    "possible week to make the worst possible decision. Elsewhere Rahul Pahuja took the week at 130.20, Bob Dorsch "
    "released Pat Freiermuth, and Boomer went 4 and 6."
)
META = (
    "Gil and Boomer call Week 2 of Friends of Herb: Michael Turner benched 37.50 on his bye, Rahul Pahuja led the "
    "league at 130.20, and Bob Dorsch dropped Pat Freiermuth."
)


def card_rows(win_owner, lose_owner):
    w, l = T[win_owner], T[lose_owner]
    return (
        {"team": w["name"], "owner": SEASON["owners"][win_owner]["display"], "score": w["score"], "left": w["left"]},
        {"team": l["name"], "owner": SEASON["owners"][lose_owner]["display"], "score": l["score"], "left": l["left"]},
    )


def build():
    parts = []
    teams = [(t["name"], SEASON["owners"][t["owner"]]["display"]) for t in FACTS["perTeam"]]
    parts.append(jump(teams))
    parts.append('<h2 id="board">The Scoreboard</h2>')

    # ---- 1. the week's best
    w, l = card_rows("Rahul Pahuja", "Eric Olson")
    parts.append(mcard(
        "m-pahuja", "Pahuja takes the week at 130.20", w, l,
        "Jaxon Smith-Njigba 43.00 and Christian McCaffrey 20.60. Eric Olson got 46.82 out of Josh Allen, the "
        "biggest score any player put up in this league this week, and lost.", SCALE, key=True))
    parts.append(gil(
        "Rahul Pahuja wins 130.20 to 111.22, the highest score in the league this week. Smith-Njigba's 43.00 was "
        "27.04 above his projection."))
    parts.append(boomer(
        "Eric Olson had the best football player on the field by a distance. Josh Allen went for 46.82 and he "
        "still went home 1 and 1. There is no justice in this game, only arithmetic."))
    parts.append(gil(
        "Olson left 7.20 behind, the second cleanest lineup of the week. Trey McBride gave him 14.10 and "
        "Christian Watson 12.10."))
    parts.append(boomer(
        "Forty-six points from one man and it bought him nothing. Somebody find this man an opponent who is also "
        "having a bad day.", "good"))

    # ---- 2. the clean one
    w, l = card_rows("Aron Rogers", "Billy Norton")
    parts.append(mcard(
        "m-rogers", "Rogers wins with a quarterback who scored 0.80", w, l,
        "CeeDee Lamb 33.30 and Amon-Ra St. Brown 32.70 for Aron Rogers. Billy Norton left Stefon Diggs and 19.20 "
        "on his bench and started Malik Nabers for 0.60.", SCALE))
    parts.append(gil(
        "Aron Rogers wins 125.20 to 93.18 with Jaxson Dart scoring 0.80 at quarterback, 20.29 under his "
        "projection, the worst miss by any starter in the league."))
    parts.append(boomer(
        "Two receivers gave him 66.00 and his quarterback gave him less than a point. He still left only 3.70 on the "
        "bench, cleanest in the league for the second week running. The man is playing a different sport to the "
        "rest of you and he is winning that one too.", "good"))
    parts.append(gil(
        "Billy Norton is 0 and 2 despite 22.40 from James Cook III and 19.00 from Dalton Kincaid. He has left "
        "28.40 behind across two weeks."))
    parts.append(boomer(
        "Nabers for 0.60 with Diggs on the bench at 19.20. Norton lost by 32.02 and 18.60 of it was sitting "
        "there in his own house wearing a jersey."))

    # ---- 3. the bench cost it
    w, l = card_rows("Michael Smith", "Spencer Lentz")
    parts.append(mcard(
        "m-smith", "Smith wins the one Spencer's bench decided", w, l,
        "Dak Prescott 37.76 and Jonathan Taylor 27.20 for Michael Smith. Spencer Lentz left 22.72 behind and lost "
        "by 18.90, the only bench in the league this week that actually decided a game.", SCALE))
    parts.append(gil(
        "Michael Smith wins 122.66 to 103.76 and is 1 and 1. Dak Prescott, Jonathan Taylor and Travis Kelce all "
        "cleared 22 for him, which nobody else in this league managed on Sunday."))
    parts.append(boomer(
        "Three men over 22 in the same afternoon. He beat the leading scorer in this league and he never needed his "
        "bench to do it, which is more than the leading scorer can say."))
    parts.append(gil(
        "Spencer Lentz started Jalen Hurts for 20.16 with Patrick Mahomes and 35.98 on his bench. His best "
        "possible lineup, 126.48, wins this game by 3.82."))
    parts.append(boomer(
        "Every other loser in this league got beaten. He did not get beaten, he got outvoted by his own roster. "
        "Kenneth Walker III gave him 22.80, Derrick Henry 16.20, and the man who would have won it for him "
        "watched the whole thing in a Kansas City uniform.", "bad"))

    # ---- 4. the low
    w, l = card_rows("Aaron Jezioro", "Ryan Kelly")
    parts.append(mcard(
        "m-jezioro", "Jezioro wins it with 26.82 still on the bench", w, l,
        "Ja'Marr Chase 23.00 for Aaron Jezioro, and Brock Purdy's 32.48 never left the bench. Ryan Kelly's 52.52 "
        "is the lowest score in either league this season.", SCALE))
    parts.append(gil(
        "Aaron Jezioro wins 77.96 to 52.52. He started Trevor Lawrence for 6.16 with Brock Purdy and 32.48 "
        "benched, a 26.32-point swing, and won by 25.44 anyway."))
    parts.append(boomer(
        "I had Ryan Kelly winning this by more than twenty. Instead he put up the lowest score anybody has "
        "managed in this league all year and lost to a man who benched his best quarterback. I was not just "
        "wrong, I was wrong about the wrong team."))
    parts.append(gil(
        "Ryan Kelly scored 52.52 with 65.72 available. De'Von Achane led him at 10.80 and his defense scored "
        "negative one."))
    parts.append(boomer(
        "Nobody in this league has had a Sunday like that yet this season, and he still only lost by 25 because "
        "of who he drew. In a different week that is a 70-point beating. Kelly gets one free pass from me."))

    # ---- 5. Freiermuth
    w, l = card_rows("Matt Davis", "Bob Dorsch")
    parts.append(mcard(
        "m-davis", "Davis wins while Dorsch releases Pat Freiermuth", w, l,
        "Jahmyr Gibbs 20.30 and Joe Burrow 20.18 for Matt Davis. Bob Dorsch got 24.70 from DeVonta Smith and "
        "dropped Freiermuth, who scored 5.40, for a running back who scored 2.50.", SCALE))
    parts.append(gil(
        "Matt Davis wins 122.18 to 92.78 and is 2 and 0. Matthew Stafford scored 35.98 on his bench while Joe "
        "Burrow started for 20.18."))
    parts.append(boomer(
        "Davis left 20.80 behind and won by 29.40, which tells you exactly when a bench bites a man. It bites in the "
        "close ones. His was not close."))
    parts.append(gil(
        "Bob Dorsch is 0 and 2 with the third cleanest lineup of the week, 10.10 left behind. Jaylen Waddle gave "
        "him 19.80 and Sam LaPorta 14.20, and Saquon Barkley scored 2.50 against a projection of 17.15."))
    parts.append(boomer(
        "He turned in a tidy lineup, got nothing from Barkley, and lost. That is football. The other thing he did "
        "gets its own heading, because in this league it has to."))

    # ---- 6. the bye
    t = T["Michael Turner"]
    parts.append(byecard(
        "m-bye", "Turner's bye week, and 30.60 on the bench",
        {"team": t["name"], "owner": SEASON["owners"]["Michael Turner"]["display"], "score": t["score"], "left": t["left"]},
        "Davante Adams scored 37.50 on his bench while Drake London started for 6.90. Eleven teams means somebody "
        "sits every week, and this week it was Napoleon's Army.", SCALE))
    parts.append(gil(
        "Michael Turner had the bye. He scored 85.60 with 116.20 available, benching Davante Adams and his 37.50 "
        "for Drake London and his 6.90, a swing of 30.60 and the largest single sit in the league this week."))
    parts.append(boomer(
        "The one Sunday all season where the scoreboard cannot punish him, and that is the Sunday he picks. If "
        "this man ever gets his weeks the right way round he wins this thing."))

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "The rule is simple and it is older than most of the rosters in this league. Do not leave the answer on "
        "your own bench. This week Bob Dorsch went one better and left it on somebody else's."))
    parts.append(gil(
        "Dorsch dropped Pat Freiermuth, who scored 5.40, to add Kaelon Black, who scored 2.50. He lost by 29.40 "
        "with Chris Godwin Jr. and 7.30 on his bench."))
    parts.append(boomer(
        "Pat Freiermuth. The man the rule is named after, released by the one owner who should know better, in a "
        "week he lost by 29. I did not write the rule. I just read it out when somebody breaks it."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Eleven calls last week, ten of which could settle on Sunday. Four came in, six did not. The Michael "
        "Turner one is still alive until Halloween. Here is every one of them, wrong ones first if you like."))
    parts.append(graded_list([
        ("Balls Deep", "Spencer Lentz posts 150 or more again in Week 2.", "WRONG",
         "103.76, with Patrick Mahomes and his 35.98 sitting on the bench."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson starts Christian Watson in Week 2.", "RIGHT",
         "Watson started for 12.10. The 46.82 from Josh Allen was the part nobody saw coming."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers leaves under five on his bench again.", "RIGHT",
         "3.70 left behind, cleanest in the league for the second week."),
        ("WPB Steel City", "Bob Dorsch wins Week 2 with Pat Freiermuth in his lineup.", "WRONG",
         "He lost by 29.40 and Freiermuth was not on his roster at all."),
        ("Napoleon's Army", "Michael Turner loses another one by under five before Halloween.", "OPEN",
         "He had the bye this week. Still live through Week 8."),
        ("Old Man Smashers", "Ryan Kelly beats Aaron Jezioro by more than twenty.", "WRONG",
         "He lost by 25.44 with 52.52, the lowest score of the season."),
        ("Pack Up", "Rahul Pahuja leaves twenty or more behind again, and it costs him.", "WRONG",
         "Half right is wrong. He left 22.10 and won the week anyway."),
        ("Dallas Dawgs", "Matt Davis gets a receiver into his top three scorers.", "WRONG",
         "Running back, quarterback, kicker. Brandon Aubrey kicked 16.00."),
        ("I Loved You Tom Brady", "Billy Norton scores 130 or more in Week 2.", "WRONG",
         "93.18, with 19.20 of the answer on his bench."),
        ("Midget Grinders", "Michael Smith beats Spencer Lentz on Sunday.", "RIGHT",
         "By 18.90, with 37.76 from Dak Prescott."),
        ("| croup", "Aaron Jezioro beats Ryan Kelly on Sunday.", "RIGHT",
         "By 25.44, while benching a quarterback who scored 32.48."),
    ]))
    parts.append(gil("Four right, six wrong, one still open. Eleven new ones."))
    parts.append(calls_list([
        ("Pack Up", "Rahul Pahuja makes it three straight wins.",
         "130.20 and 114.12 to open the year with Smith-Njigba at 43.00, and he added Jordan Love off the wire for "
         "a 15.90-point swing, the best move in the league this week."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers leaves under ten behind again in Week 3.",
         "2.00 and 3.70 in his first two weeks, 5.70 all season, the tidiest manager in either league. He beats "
         "people with a quarterback who scored 0.80."),
        ("Dallas Dawgs", "Matt Davis gets a receiver into his top three. Again.",
         "I said it last week and I am saying it louder. He owns Xavier Worthy at 11.00 off the bench and Terry "
         "McLaurin at 6.00, and 2 and 0 without receiver production is not a thing that lasts."),
        ("Balls Deep", "Spencer Lentz beats Bob Dorsch on Sunday.",
         "275.68 points scored in two weeks, the most in this league by 18.98, for a 1 and 1 record, and the one week "
         "his bench mattered he sat 35.98 of it. He draws an 0 and 2 team that just released its tight end."),
        ("Colorado Narcoleptic Kestrels", "Josh Allen clears 25 again for Eric Olson.",
         "46.82 on Sunday, 20.50 above projection. Olson has left 40.50 behind on the season, second most behind "
         "Rahul Pahuja, and still sits at 1 and 1 because of what that quarterback keeps doing."),
        ("Midget Grinders", "Michael Smith clears 120 again.",
         "122.66 this week with Prescott at 37.76, Jonathan Taylor at 27.20 and Travis Kelce at 22.60. That is "
         "three players clearing 22 in the same week, which nobody else in this league managed."),
        ("WPB Steel City", "Bob Dorsch clears 110 in Week 3.",
         "0 and 2 with the third cleanest lineup this week and 206.44 points, more than a team that is 1 and 1. "
         "Saquon Barkley scoring 2.50 is not a thing that happens twice."),
        ("I Loved You Tom Brady", "Billy Norton starts Stefon Diggs in Week 3.",
         "Diggs has scored 19.20 on his bench. Malik Nabers started for 0.60. Norton is 0 and 2 and has left 28.40 "
         "behind, and the fix is one line in his own lineup."),
        ("Napoleon's Army", "Michael Turner wins his first, over Billy Norton.",
         "He comes off the bye at 85.60 with Davante Adams, Chris Olave and Lamar Jackson on the roster, against "
         "an 0 and 2 team that has scored 202.02. If he starts Adams this is not close."),
        ("Old Man Smashers", "Ryan Kelly clears 90 in Week 3.",
         "52.52 was the floor of the season for anybody. De'Von Achane, Rashee Rice and TreVeyon Henderson are "
         "better than what they gave him, and Henderson put 13.60 on the bench."),
        ("| croup", "Aaron Jezioro starts Brock Purdy in Week 4.",
         "He has the bye in Week 3, so this one waits. Purdy went 32.48 on his bench while Trevor Lawrence "
         "started for 6.16. Jezioro started 74.4 percent of the points he owned on Sunday, the worst figure of "
         "anybody who had an opponent."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(award(
        "good", "Owner of the Week", "Aron Rogers · Kim Jong Un Pleasure Squad",
        "125.20 scored, 128.90 available, 3.70 left behind, and a starting quarterback who scored 0.80.",
        "He gave up twenty points at the most important position in the game and still won by 32.02. Two weeks, "
        "5.70 wasted in total. Nobody else in this league is inside twenty."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Ryan Kelly · Old Man Smashers",
        "52.52 scored, the lowest in either league this season, with 65.72 available.",
        "His defense scored negative one, his best player got him 10.80, and TreVeyon Henderson put up 13.60 on "
        "the bench, which is a quarter of the whole team's output sitting down."))
    parts.append(award(
        "good", "Start of the Week", "Eric Olson · Josh Allen, 46.82",
        "The highest single score by any player in either league this week, 20.50 above his projection. Jaxon "
        "Smith-Njigba is second at 43.00.",
        "Forty-six points from one man and Olson lost by 18.98. Gil will tell you that is how a schedule works. I "
        "will tell you it is why people quit this hobby in October."))
    parts.append(award(
        "bad", "Sit of the Week", "Michael Turner · Davante Adams, 37.50 on the bench",
        "Drake London started for 6.90 in his place, a swing of 30.60, in the week Turner had no opponent.",
        "The only man in this league who could bench 37 points this week without losing anything is the man who "
        "did it. If that is a system, I want to know what he does with it in November."))
    parts.append(award(
        "bad", "Waste of the Week", "Aaron Jezioro · 77.96 started out of 104.78 available",
        "The lowest score any winner managed this week, with Brock Purdy and 32.48 on his bench.",
        "He won by 25 while sitting on a 32.48 from Brock Purdy. Somewhere Ryan Kelly is looking at that bench and "
        "wondering what a man has to do around here to get 32 points."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All eleven of you, every week, whether you played or not. Rahul Pahuja leads the season at 60.40, which "
        "is a strange thing to say about the man who just won the week."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 2, season_note=(
        "Season totals are Week 1 and Week 2 added together. Rahul Pahuja leads at 60.40, Eric Olson is second at "
        "40.50, Michael Turner third at 34.20. A bye week still counts: the points were on the bench either way.")))
    parts.append(gil(
        "One of eleven this week. Spencer Lentz left 22.72 and lost by 18.90, so his is the only bench that "
        "decided a game."))
    parts.append(boomer(
        "And he leads this league in points scored, so he does not get to blame the schedule for this one. Two "
        "weeks, 275.68, and the one week he needed his bench he left Patrick Mahomes sitting on it."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move:</strong> Rahul Pahuja adding Jordan Love, who scored 17.80, for Quentin Johnston, who "
        "scored 1.90. A 15.90-point swing, the largest in the league."))
    parts.append(gil(
        "<strong>Worst move:</strong> Bob Dorsch dropping Pat Freiermuth, 5.40, to add Kaelon Black, 2.50. Eight "
        "moves went through this week and it is the only one anybody will remember."))
    parts.append(boomer(
        "Aaron Jezioro added Jalen Coker for 10.60 and then benched the quarterback who scored 32.48. Michael Turner "
        "dropped Rico Dowdle, 5.40, to add Tyler Allgeier, 2.90, in a week nobody was playing him. This league "
        "makes its worst decisions with the lights off."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Billy Norton at Michael Turner, Michael Smith at Ryan Kelly, Rahul Pahuja at Aron Rogers, Bob Dorsch at "
        "Spencer Lentz, Matt Davis at Eric Olson. Aaron Jezioro has the bye."))
    parts.append(boomer(
        "Pahuja at Rogers is the one. Both 2 and 0, the man who just put 130.20 on the board against the man who has "
        "wasted 5.70 points all season. Somebody is 3 and 0 on Sunday night and neither of them plans on it "
        "being the other one."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 2, HEADLINE, DEK, build(), META, "foh-week-2.png",
        (f"{booth.SITE}/dlffl/week-2.html", "Dewart Lake FFL, Week 2"), nav=NAV,
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wb", "docs", "foh", "week-2.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
