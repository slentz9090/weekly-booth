"""Friends of Herb, Week 6. Editorial.

Eleven teams, so one bye every week. The Freiermuth Rule lives on this page only.
No joke on this page may repeat one from the Dewart Lake page. Spencer reads both.
Boomer runs ULTRA SPICY from Week 6 (Spencer, 2026-10-20). Clean language on the page.

Outlier engine top items: Aron Rogers snapped Ryan Kelly's six-game series streak (promote, 1 week in 13),
Bob Dorsch lost by 1.88 with 25.00 on the bench, Germie Bernard 20.20 sat for Zay Flowers 9.70 (promote),
Aaron Jezioro benched Trevor Lawrence's 36.34, 39th-most by one benched player since 2018 (promote).
Supporting: Michael Smith snapped Dorsch's five-game series streak and won by 1.88 (53rd-closest since 2011),
Matt Davis 71.48 is the 3rd-worst of his 241, Billy Norton leads Davis 12-5, Michael Turner 1-4 on a 26-24
all-play, the same all-play as Michael Smith at 4-1. Editorial: Dorsch released Tyler Shough after his
minus 0.16; Aron Rogers signed Shough and started him for 32.96, the top quarterback score in a lineup this
week; the Freiermuth Rule's namesake failed the Freiermuth Rule, with Pat Freiermuth in his lineup. Rahul
Pahuja scored 136.24 on the bye, the most in the league. No new inbox intel this week.
Red team round 1 (2026-10-20) fixed: Davis's bench was three on bye and two out (Judkins, Warren), Kelly
was also winless, Smith's all-play is 26-24 (bye excluded, page convention), Spencer started two of his
adds (Kraft, Panthers), Winston scored 8.48, Rogers fell four straight weeks not five, the curb joke is this
page's alone, Dorsch tellings trimmed.
"""
import os

import booth
from booth import award, boomer, byecard, calls_list, gil, graded_list, jump, ledger, mcard
from compute import by_owner, ledger_rows, load

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

FACTS = load("foh_wk6_facts.json")
SEASON = load("foh_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 142.38

HEADLINE = "Bob Dorsch Cut Tyler Shough For Scoring Less Than Zero. Aron Rogers Signed Him And He Scored 32.96."
DEK = (
    "Rogers set a perfect lineup, took Owner of the Week, and ended Ryan Kelly's six-game run in their "
    "series. Dorsch lost by 1.88 with Shough's replacement, Germie Bernard, scoring 20.20 on his bench, and "
    "broke the rule named after him. Billy Norton won his first game, over a Matt Davis who scored 71.48 the "
    "week after scoring 170.70. Rahul Pahuja scored 136.24, the most in the league, on his bye."
)
META = (
    "Gil and Boomer call Week 6 of Friends of Herb: Bob Dorsch cuts Tyler Shough and Aron Rogers rides him to "
    "Owner of the Week, Billy Norton beats Matt Davis for his first win, Dorsch breaks the Freiermuth Rule, "
    "and Boomer goes 5 and 6 on his calls."
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

    # ---- 1. the quarterback on the curb
    w, l = card_rows("Michael Smith", "Bob Dorsch")
    parts.append(mcard(
        "m-smith", "Smith by 1.88, and Dorsch benched the winning swap", w, l,
        "Jonathan Taylor 20.10, Tyler Bass 17.00 and DK Metcalf 14.80 for Michael Smith, who left 2.74 behind. "
        "Bob Dorsch started Zay Flowers for 9.70 with Germie Bernard's 20.20 on his bench, and started Pat "
        "Freiermuth for 2.10.", SCALE, key=True))
    parts.append(gil(
        "Michael Smith wins 105.22 to 103.34 and is 4 and 1. Bob Dorsch had won their last five meetings and "
        "still leads the series 13 and 10. Dorsch released Tyler Shough this week, after Shough scored minus "
        "0.16 for him in Week 5, and signed Germie Bernard in his place. Bernard scored 20.20 on Dorsch's "
        "bench. Shough scored 32.96 for Aron Rogers."))
    parts.append(boomer(
        "Bob cut a quarterback for scoring less than nothing, and the quarterback went down the street and "
        "scored 33 for Aron Rogers, the most by any quarterback in a lineup in this league this week. Then the "
        "receiver Bob signed to replace him scored 20 on Bob's bench while Bob lost by two. Gil, that is not a "
        "bad week. That is a man who fired the chef, hired a new one, and locked the new one in the pantry."))
    parts.append(gil(
        "The Freiermuth Rule is named for Bob Dorsch sitting Pat Freiermuth's 13.10 in Week 1 and losing by "
        "0.46. This week Dorsch signed Freiermuth again, started him for 2.10, sat Bernard for 20.20, and lost "
        "by 1.88. Details in the Freiermuth Rule section below."))
    parts.append(boomer(
        "The rule is named after him and he broke it with the guy it is named after in his lineup. That is like "
        "getting a speeding ticket on the street they named for you. Bob, there is a plaque with your name on "
        "it, and you walked into it.", "bad"))
    parts.append(gil(
        "In fairness to Bob Dorsch, he is the reigning champion, and he made seven moves this week, the most in "
        "the league. Two of them started and produced: Jordan Love, signed this week, 22.24, and Chris Boswell, "
        "18.00. Darnell Washington scored 10.50 on the bench. His best possible lineup, 128.34, was the "
        "second-highest of any team that played. For Michael Smith, Tyler Bass, signed this week for Harrison "
        "Mevis, scored 17.00, and Daniel Jones scored 15.76 on his bench behind Dak Prescott's 13.02."))
    parts.append(boomer(
        "Seven moves. He signed a kicker, cut him, and signed a different kicker in the same week. Bob packs "
        "his roster like a man packing for a trip he keeps canceling. And Michael, you are 4 and 1 on a 26 and "
        "24 all-play, the exact same all-play as Michael Turner, who is 1 and 4. Same scores, Gil. One Michael "
        "gets a parade and the other one gets a sympathy card. Your kicker scored 17 and you won by 1.88. Send "
        "Tyler Bass the parade."))

    # ---- 2. the first win
    w, l = card_rows("Billy Norton", "Matt Davis")
    parts.append(mcard(
        "m-norton", "Norton's first win, and the third-worst game of Davis's career", w, l,
        "Malik Nabers 24.50, Kirk Cousins 23.52 and James Cook III 22.80 for Billy Norton, who left 24.30 "
        "behind. Matt Davis set a perfect lineup, because every man on his bench scored zero.", SCALE))
    parts.append(gil(
        "Billy Norton wins 96.22 to 71.48, his first win of the season. He leads Matt Davis 12 and 5 lifetime. "
        "Davis's 71.48 is the third-worst of his 241 games in this league, and it would have lost to all ten "
        "other teams. Joe Burrow and Jahmyr Gibbs had the week off."))
    parts.append(boomer(
        "Matt went 117, 122, 125, 145, 170, up every single week, and then 71. He did not come down the "
        "stairs, Gil. He fell down them holding the laundry. Kyren Williams 8.20, Brandon Aubrey 1.00, Mark "
        "Andrews 0.90. Matt set a perfect lineup because there was nobody on the bench to set it with. Three "
        "of them had the week off, two of them did not play, and the starters joined all five in spirit."))
    parts.append(gil(
        "Last week Billy Norton started three players projected for zero, including his only quarterback. "
        "This week he signed Kirk Cousins, who scored 23.52. He still started DJ Moore at flex, projected for "
        "zero, and Moore scored zero, with Stefon Diggs at 13.40 on the bench."))
    parts.append(boomer(
        "Billy went out and found a quarterback, like I told him. Then he started DJ Moore, who was projected "
        "for zero and scored exactly that, with Diggs and 13 on the bench. Billy, you fixed the quarterback and "
        "kept the zero. That is patching the roof and leaving the front door open. You won by 25. Close the "
        "door anyway.", "good"))
    parts.append(gil(
        "In fairness to Matt Davis, he is still 4 and 2 with 751.84 points, second in the league, and Matthew "
        "Stafford gave him 20.88. Burrow and Gibbs are back next week."))
    parts.append(boomer(
        "Second in points, 4 and 2, and he just lost to a team that had waited five weeks for its first win. "
        "There is no fairness clause for that, Gil. Billy waited five weeks for somebody to show up with a 71, "
        "and Matt brought it over himself, warm, in a dish with his name on the bottom."))

    # ---- 3. the curb pays off
    w, l = card_rows("Aron Rogers", "Ryan Kelly")
    parts.append(mcard(
        "m-rogers", "Rogers 119.46 with Shough, and Kelly's six-game series run ends", w, l,
        "Tyler Shough 32.96, D'Andre Swift 21.00 and George Kittle 15.40 for Aron Rogers, who left nothing "
        "behind. Kyle Pitts Sr. gave Ryan Kelly 20.50 on a projection of 7.30, and Kelly also left nothing "
        "behind.", SCALE))
    parts.append(gil(
        "Aron Rogers wins 119.46 to 87.70 and is 4 and 2. Ryan Kelly had won their last six meetings, and the "
        "series is now 7 and 7. Rogers signed Tyler Shough this week, the quarterback Bob Dorsch released, and "
        "started him for 32.96. Both men set perfect lineups. Rogers's score had fallen four straight weeks, "
        "131, 125, 121, 117, 113, before this one."))
    parts.append(boomer(
        "Four straight weeks going down, and then Aron picked a quarterback up off the curb, the one Bob Dorsch "
        "put out there, and the quarterback scored 33. Bob's trash, Aron's 33 points. The curb does not check "
        "references, Gil, and this week it outscored every quarterback in the league who was in a lineup."))
    parts.append(gil(
        "Ryan Kelly is 0 and 5. Kyle Pitts Sr. gave him 20.50, the biggest beat of a projection by any starter "
        "in the league this week, and his lineup was perfect. He has 339.38 points in games that counted, "
        "about 93 fewer than anyone else."))
    parts.append(boomer(
        "Ryan set a perfect lineup and lost by 32. Last week he started a man on bye and lost by 73. He is "
        "improving at exactly the rate a glacier improves, and the glacier is 0 and 5."))

    # ---- 4. the robot and the human
    w, l = card_rows("Eric Olson", "Aaron Jezioro")
    parts.append(mcard(
        "m-olson", "Olson's perfect lineup · Jezioro sat a 36.34", w, l,
        "Bhayshul Tuten 22.70, Josh Allen 22.30 and Emeka Egbuka 14.30 for Eric Olson, who left nothing "
        "behind. Aaron Jezioro started Brock Purdy for 19.36 with Trevor Lawrence's 36.34 on his bench.", SCALE))
    parts.append(gil(
        "Eric Olson wins 109.00 to 88.86 and is 4 and 2. He leads Aaron Jezioro 6 and 2 lifetime, and they had "
        "not met since 2014. Olson set a perfect lineup. Jezioro left 26.38 behind, and Trevor Lawrence's "
        "36.34 was the highest score by any quarterback in the league this week. It came from a bench."))
    parts.append(boomer(
        "Eric has told this league he built a robot on OpenAI to set his lineup. This week the robot left zero "
        "on the bench. Zero. Meanwhile Aaron, a human being, sat the best quarterback score in the league "
        "behind Brock Purdy. Gil, I have been saying the robots are coming. I did not think the first thing "
        "they would take was the bench."))
    parts.append(gil(
        "In fairness to Aaron Jezioro, Purdy was projected for 26.18 and Lawrence for 21.57. He played the "
        "projection. And his best possible lineup, 115.24, would have beaten Olson by 6.24."))
    parts.append(boomer(
        "He played the projection and the projection played him. Thirty-six points is the 39th-biggest score "
        "left on a bench in this league since 2018, out of more than five thousand. Aaron, they are going to "
        "teach that decision someday, and you are the slide.", "bad"))

    # ---- 5. the phone comes back
    w, l = card_rows("Spencer Lentz", "Michael Turner")
    parts.append(mcard(
        "m-lentz", "Spencer by 23.20, with 25.40 on his bench", w, l,
        "Drake Maye 29.80 and Kenneth Walker III 28.90 for Spencer Lentz, who left 25.40 behind, including "
        "Chuba Hubbard's 20.60. Jayden Daniels gave Michael Turner 26.00, and Turner started two players who "
        "scored zero.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 107.20 to 84.00 and is 4 and 2. He leads Michael Turner 16 and 8. Spencer started "
        "Derrick Henry for 4.50 with Chuba Hubbard at 20.60 on his bench, and Tucker Kraft for 6.20 with "
        "Colston Loveland at 15.50 behind him. Turner started Cam Skattebo and Juwan Johnson, who scored zero "
        "apiece."))
    parts.append(boomer(
        "Last week Spencer left 1.10 on his bench and I said keep his phone hidden. This week he left 25.40. "
        "Somebody gave him the phone back, and the first thing he did with it was bench Chuba Hubbard. "
        "Spencer, 25 points on the bench and a win by 23. You did not win this game. You outlasted it, like a "
        "man who wins an argument because the other guy fell asleep."))
    parts.append(gil(
        "Michael Turner is 1 and 4, and against the whole league he is 26 and 24. He has outscored more teams "
        "than he has lost to, and he keeps drawing the one that beats him. By the numbers he is about a win "
        "and a half short of his scores, the most of anyone in the league."))
    parts.append(boomer(
        "Michael started two zeros and lost by 23, so the zeros were only part of the problem. The rest is the "
        "schedule, and the schedule has his address, his gate code, and a key."))

    # ---- 6. the bye
    t = T["Rahul Pahuja"]
    parts.append(byecard(
        "m-bye", "Pahuja's bye: 136.24, the week's high score, for nobody",
        {"team": t["name"], "owner": SEASON["owners"]["Rahul Pahuja"]["display"], "score": t["score"], "left": t["left"]},
        "Christian McCaffrey 26.20, Bryce Young 23.84 and Jaxon Smith-Njigba 21.40 for Rahul Pahuja, with C.J. "
        "Stroud's 29.98 on his bench.", SCALE))
    parts.append(gil(
        "Rahul Pahuja had the bye and scored 136.24, the highest score in the league this week by 16.78. It "
        "would have beaten all ten teams. He is 4 and 1 and first in the standings."))
    parts.append(boomer(
        "The best score in the league this week belonged to the man who was not playing. Rahul scored 136 for "
        "nobody. He set a lineup, it went off, and it counted exactly as much as my opinions. And I called 110 "
        "on his bye, after swearing off bye calls, and I won. I am a man of no principles and one win on them."))

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "Named for Week 1, when Bob Dorsch sat Pat Freiermuth's 13.10 and lost by 0.46. Do not leave the answer "
        "on your own bench. The test is one swap: a player you sat, for the player you started in his place, "
        "worth more than you lost by. This week the man the rule is named for failed it. Dorsch sat Germie "
        "Bernard, 20.20, for Zay Flowers, 9.70, a swing of 10.50, and lost by 1.88. Pat Freiermuth was in his "
        "lineup, for 2.10."))
    parts.append(gil(
        "Aaron Jezioro came close. Trevor Lawrence for Brock Purdy is worth 16.98, and he lost by 20.14, 3.16 "
        "short of failing. Nobody else lost with a swap that big."))
    parts.append(boomer(
        "The rule has a name on it and the name failed the rule. Bob, we are not renaming it. We are adding a "
        "second line. The Freiermuth Rule, by Bob Dorsch, broken by Bob Dorsch, starring Pat Freiermuth."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Eleven calls came due. Five right, six wrong, and one older call still riding. Season record, 21 and "
        "32. I called Billy Norton's first win and Rahul's bye-week score, so for one week I am a prophet, and "
        "the prophet is still eleven games under .500. Read them all."))
    parts.append(graded_list([
        ("Midget Grinders", "Michael Smith beats Bob Dorsch.", "RIGHT",
         "By 1.88. I said streaks were dropping like flies and told him to swat one. Swatted."),
        ("WPB Steel City", "Bob Dorsch clears 110 in Week 6.", "WRONG",
         "103.34. Germie Bernard scored 20.20 on his bench. Start him and it is 113.84 and a win. Bob, you took "
         "us both down."),
        ("I Loved You Tom Brady", "Billy Norton wins his first game, over Matt Davis.", "RIGHT",
         "By 24.74. I said my type is lost causes. The lost cause signed Kirk Cousins and won by 25."),
        ("Dallas Dawgs", "Matt Davis clears 120 for the fifth straight week.", "WRONG",
         "71.48. I said he could not pick the wrong quarterback if there was only one. He picked the right one "
         "and lost by 25 anyway."),
        ("| croup", "Aaron Jezioro beats Eric Olson.", "WRONG",
         "Lost by 20.14 with Trevor Lawrence on the bench for 36.34. I picked Aaron and Aaron picked Purdy. "
         "Only one of us was wrong on purpose."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson leaves under fifteen on his bench in Week 6.", "RIGHT",
         "Zero. Not a point. Whoever set that lineup, man or machine, set it right, and I know which one I am "
         "betting on."),
        ("Napoleon's Army", "Michael Turner beats Spencer Lentz.", "WRONG",
         "Lost by 23.20. The schedule still owes him one, and now it owes me one too."),
        ("Balls Deep", "Spencer Lentz leaves under five on his bench again.", "WRONG",
         "25.40. Chuba Hubbard, 20.60, on the bench. I called under five. I missed by a Hubbard."),
        ("Old Man Smashers", "Ryan Kelly wins his first game, over Aron Rogers.", "WRONG",
         "Lost by 31.76 with a perfect lineup. Perfect, and 0 and 5."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers leaves under ten on his bench in Week 6.", "RIGHT",
         "Zero. Fifth time in six weeks under ten. Aron signs a quarterback and starts him the same week. The "
         "bench is for other people."),
        ("Pack Up", "Rahul Pahuja clears 110 on his bye.", "RIGHT",
         "136.24. I swore off bye calls, broke the promise, and won. Do not tell the others."),
        ("Napoleon's Army", "Michael Turner loses another one by under five points before Halloween.", "OPEN",
         "Lost by 23.20. Still open. Two weeks left, and the man keeps losing by twenty."),
    ]))
    parts.append(gil(
        "Five right, six wrong, one open. Eleven new ones, with Bob Dorsch's on the bye. The Bills, Chargers, "
        "Commanders and Jaguars have the week off."))
    parts.append(calls_list([
        ("WPB Steel City", "Bob Dorsch starts Germie Bernard in Week 7, bye or no bye.",
         "Bob has the bye, so nothing counts, which makes this the safest week of his life to start the "
         "receiver who scored 20.20 on his bench. Bob, you cannot lose this one. Please do not find a way."),
        ("Pack Up", "Rahul Pahuja starts C.J. Stroud in Week 7.",
         "Stroud scored 29.98 on Rahul's bench while Bryce Young started for 23.84. Rahul leads the standings "
         "and still has a quarterback problem, which is the good kind. Pick the one who scored 30, Rahul."),
        ("Dallas Dawgs", "Matt Davis beats Rahul Pahuja.",
         "Burrow and Gibbs are back. Davis leads the series 12 and 8 and has won the last two. A man does not "
         "score 170 and then 71 and then stay at 71. The elevator is moving again. I just do not know which "
         "button he pushed."),
        ("Midget Grinders", "Michael Smith beats Eric Olson.",
         "The series is 2 and 2, and they last met in 2014. Olson has Josh Allen and Bhayshul Tuten on bye and "
         "no second quarterback on his bench. Michael has Tyler Bass on bye, so he is down a kicker. I will "
         "take down a kicker over down a quarterback."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson clears 100 in Week 7.",
         "No Josh Allen, no Tuten, and no second quarterback on the roster. The robot has work to do. Eric, I "
         "am betting on the robot. Do not make me regret trusting a machine over you."),
        ("I Loved You Tom Brady", "Billy Norton beats Spencer Lentz for the fourth straight time.",
         "Billy leads the series 13 and 9 and has won the last three, one of them in the playoffs. James Cook "
         "III and Dalton Kincaid are on bye, but Billy has Kirk Cousins now and Stefon Diggs is right there "
         "on the bench. My type is lost causes, and Billy just beat the second-best team in the league, so he "
         "barely qualifies anymore. I will take him while he still does."),
        ("Balls Deep", "Spencer Lentz leaves under ten on his bench in Week 7.",
         "25.40 this week, 1.10 the week before, 55.46 the week before that. Spencer's bench goes 55, 1, 25. "
         "There is no pattern, so I am picking a number. Under ten. Hide the phone again."),
        ("| croup", "Aaron Jezioro clears 100 in Week 7.",
         "Trevor Lawrence is on bye, so Brock Purdy starts and nobody has to decide anything. Aaron scored 109, "
         "115 and 132 the three weeks before this one. The only thing that beat him this week was his own "
         "bench, and next week the bench is on bye."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers beats Aaron Jezioro for the ninth straight time.",
         "Eight straight, 12 and 3 lifetime. Rogers has Tyler Shough, Jared Goff back from the bye, and the "
         "cleanest bench in the league. Jezioro has Purdy and a bench that just left 36 points on it. I know "
         "what I am looking at."),
        ("Napoleon's Army", "Michael Turner beats Ryan Kelly.",
         "Kelly leads the series 15 and 10 and won the last one, in the playoffs. But Michael has outscored "
         "the league 26 times in 50 and has one win to show for it, and Ryan is 0 and 5 with 339 points. "
         "Jayden Daniels is on bye for Michael, and Lamar Jackson is projected for zero on his bench. I am "
         "picking the man with no quarterback over the man with no wins, because somebody has to win this "
         "game and I refuse to believe it is Ryan. The close loss can wait a week."),
        ("Old Man Smashers", "Ryan Kelly clears 90 in Week 7.",
         "87.70 this week, and he has not cleared 90 since Week 1. Kyle Pitts Sr. just scored 20 for him on a "
         "projection of seven. Ryan, I need 2.30 more points out of you. Find them anywhere. I am not picky, "
         "and neither is the scoreboard."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "Five trophies, five different owners. Nobody takes two in the same week, and a bye-week score does "
        "not count for a trophy."))
    parts.append(award(
        "good", "Owner of the Week", "Aron Rogers · Kim Jong Un Pleasure Squad",
        "119.46, the high score among the ten teams that played, with a perfect lineup. Rahul Pahuja scored "
        "136.24 on his bye, and a bye does not count. Tyler Shough, signed this week, 32.96.",
        "Aron's third Owner of the Week this season, and the first one he won with somebody else's "
        "quarterback. Bob Dorsch wrapped him, put a bow on him, and left him on the curb, and Aron drove by "
        "slow. Keep him, Aron. Bob is going to come asking."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Matt Davis · Dallas Dawgs",
        "71.48, the lowest score in the league and the third-lowest of his 241 games here. It loses to all ten "
        "teams. His bench was Jahmyr Gibbs, Quinshon Judkins, Joe Burrow, Tyler Warren and Jameson Williams, "
        "every one of them projected for zero: three on bye, two not playing.",
        "Five men on the bench and not one of them in uniform. Matt did not have a bench this week. He had a "
        "waiting room, and the starters took one look at it and decided to wait too. Matt, 170 to 71 in one "
        "week. The elevator did not stop. It went back to the lobby, and the doors would not open."))
    parts.append(award(
        "good", "Start of the Week", "Ryan Kelly · Kyle Pitts Sr., 20.50",
        "Projected for 7.30, so 13.20 over, the biggest beat by any starter in the league this week. His first "
        "piece of hardware since Week 1 that is not a Worst Owner or a Sit of the Week.",
        "Ryan started a tight end projected for seven and got twenty. The trophy says Start of the Week, and "
        "Ryan is 0 and 5, so this is the best thing that has happened to him since the auction. Put it on the "
        "mantle, Ryan, right next to the two Worst Owners. Make it a set."))
    parts.append(award(
        "bad", "Sit of the Week", "Bob Dorsch · Germie Bernard, 20.20 on the bench",
        "Zay Flowers started in his place for 9.70, a swing of 10.50 in a game Dorsch lost by 1.88. Aaron "
        "Jezioro's Trevor Lawrence benching was 6.48 bigger, and it did not cost him the game. One that did "
        "goes first.",
        "Bob, you went to the trouble of signing the man and then kept him in the box. Receivers do not "
        "appreciate in the box."))
    parts.append(award(
        "bad", "Waste of the Week", "Spencer Lentz · 25.40 left behind, and he won",
        "The most left on a bench by any winner. Chuba Hubbard scored 20.60 behind Derrick Henry's 4.50, and "
        "Colston Loveland 15.50 behind Tucker Kraft's 6.20. Billy Norton left 24.30 and also won, 1.10 short of "
        "the trophy.",
        "Spencer took this trophy in Week 4 with 55 points, cleaned up for a week, and is back on the podium "
        "with 25. He won by 23, so it changed nothing, except that it is his second Waste of the Week this "
        "season, and I have started engraving his name in pencil."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "Every bench in Friends of Herb, bye weeks included. New leader: Aaron Jezioro, 125.88, after leaving "
        "26.38 this week with Trevor Lawrence doing most of the sitting. Spencer Lentz is second at 118.88 and "
        "Rahul Pahuja third at 114.54. Aron Rogers has left 31.08 all year and nothing this week. He is the "
        "only man in this league whose bench I would trust with my car."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 6, season_note=(
        "Season totals come from the season ledger through Week 6. Aaron Jezioro leads at 125.88, Spencer Lentz "
        "is second at 118.88, Rahul Pahuja third at 114.54. Aron Rogers has left the fewest, 31.08. A bye week "
        "still counts: the points were on the bench either way.")))
    parts.append(gil(
        "Two benches cost a game this week: Bob Dorsch left 25.00 and lost by 1.88, and Aaron Jezioro left "
        "26.38 and lost by 20.14. Four owners left nothing at all: Matt Davis, Ryan Kelly, Aron Rogers and Eric "
        "Olson. Two of the four lost."))
    parts.append(boomer(
        "Four perfect benches, and half of them lost. Matt Davis and Ryan Kelly set the best lineups they could, "
        "and the best they could was 71 and 87. Gil, a perfect lineup is only a compliment if the roster is."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Aron Rogers adding Tyler Shough, who started and scored "
        "32.96, for Jameis Winston, who scored 8.48. A 24.48-point swing, the biggest of any move in the league "
        "this week."))
    parts.append(gil(
        "<strong>Worst move:</strong> Bob Dorsch releasing Tyler Shough, who scored 32.96 for Aron Rogers, to "
        "add Germie Bernard, who scored 20.20 on Dorsch's bench. A 12.76-point swing against him, and both "
        "players outscored the men Dorsch started in their places."))
    parts.append(boomer(
        "Best move and worst move, same quarterback. Bob threw out a 33 and signed a 20, then benched the 20. "
        "Gil, that is two moves, and only one of them was the idea."))
    parts.append(gil(
        "Twenty-five moves went through. Billy Norton signed Kirk Cousins, who started and scored 23.52, for "
        "Baker Mayfield, who scored zero. Michael Smith signed Tyler Bass for Harrison Mevis, a 17.00-point "
        "swing. Spencer Lentz made four moves and started two of the players he added, Tucker Kraft for 6.20 "
        "and the Panthers defense for 4.00."))
    parts.append(boomer(
        "Billy finally signed a quarterback and the quarterback scored 23. The pool was open all week, like I "
        "said, and Billy walked in and took the one thing off the shelf he needed. Now somebody show him where "
        "they keep the flex players."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Matt Davis at Rahul Pahuja, Eric Olson at Michael Smith, Spencer Lentz at Billy Norton, Aron Rogers at "
        "Aaron Jezioro, and Ryan Kelly at Michael Turner. Bob Dorsch has the bye. The Bills, Chargers, "
        "Commanders and Jaguars have the week off."))
    parts.append(boomer(
        "Bob Dorsch is on bye, which means for one week Bob cannot break the Freiermuth Rule, and neither can "
        "Freiermuth. Billy Norton gets Spencer and I took Billy, because I said my type is lost causes, and a "
        "man has to stick to his type even when the type starts winning. And Eric Olson has no quarterback and "
        "a robot. Eric, if the robot finds one before you do, I want a copy, and so does Bob."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 6, HEADLINE, DEK, build(), META, "foh-week-6.png", nav=NAV,
        published="2026-10-20T11:15:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "week-6.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
