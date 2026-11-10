"""Friends of Herb, Week 9. Editorial.

Boomer runs SCORCHING (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis and never gloats, clean language on the page, roast cap and Gil defenses apply. No new segment
this week: the Week 8 structure with THE RACE (stays through the playoff cut) after the Scoreboard. No
series line on the cards, no Owner Spotlight. Nothing on this page refers to any other league.

Outlier engine, Week 9. HEADLINE tier: Rahul Pahuja beat Ryan Kelly by 112.20, the 5th-biggest margin in
1,345 games since 2011; Pahuja's 173.86 is the 2nd-best week of his 243. PROMOTE: Kelly's 61.66 is the
58th-lowest of 2,689 team-weeks (9th-worst of his 241); C.J. Stroud's 46.36 for Pahuja is the 35th-best
start in 11,036 player-weeks since 2018. SUPPORT: Jordan Love 43.18 for Bob Dorsch (61st-best start);
Matt Davis lost with 125.04 (93rd-most in a loss); Spencer Lentz 158.16 (20th-best of his 245), three
straight over Davis, series 15-14; Aron Rogers 83.00 (20th-worst of his 166) with Tyler Shough's 21.70 on
the bench; Jezioro and Pahuja perfect lineups; Turner 1-7 on a 25-47 all-play; Smith 5-3 on 32-40.
Boomer's Week 8 call was Kelly over Pahuja.

Verified against foh_wk9_facts.json, foh_season.json, foh_wk9_insights.json, foh_race_wk9.json and
gen2/data/foh_games.json.
"""
import json
import os

import booth
import race
from booth import award, boomer, byecard, calls_list, gil, graded_list, jump, ledger, mcard
from compute import DATA, by_owner, ledger_rows, load

FACTS = load("foh_wk9_facts.json")
SEASON = load("foh_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 173.86

NAV = (
    '<nav class="nav" aria-label="Sections"><ul>'
    '<li><a href="#board">The Scoreboard</a></li>'
    '<li><a href="#race">The Race</a></li>'
    '<li><a href="#freiermuth">The Freiermuth Rule</a></li>'
    '<li><a href="#calls">On The Record</a></li>'
    '<li><a href="#hardware">The Hardware</a></li>'
    '<li><a href="#ledger">The Bench Ledger</a></li>'
    '<li><a href="#wire">The Waiver Wire</a></li>'
    '<li><a href="#next">Next Sunday</a></li></ul></nav>'
)

HEADLINE = "Rahul Pahuja Beat Ryan Kelly By 112.20. Boomer Picked Kelly."
DEK = (
    "Pahuja scored 173.86 with a perfect lineup, the second-best week of his 243 in this league, and won by the fifth-biggest margin in 1,345 games since 2011. Boomer had the other side, in ink. Bob Dorsch beat Aron Rogers while the quarterback Dorsch cut before Week 6 scored 21.70 on Rogers's bench. Boomer also had Matt Davis in a series that was 14 and 14. Boomer went 4 and 7."
)
META = (
    "Gil and Boomer call Week 9 of Friends of Herb: Rahul Pahuja beats Ryan Kelly by 112.20 with a perfect lineup, Bob Dorsch beats Aron Rogers with Tyler Shough on the wrong bench, a 14 and 14 series gets broken, three teams tie for the last playoff spot, and Boomer goes 4 and 7."
)


def card_rows(win_owner, lose_owner):
    w, l = T[win_owner], T[lose_owner]
    return (
        {"team": w["name"], "owner": SEASON["owners"][win_owner]["display"], "score": w["score"], "left": w["left"]},
        {"team": l["name"], "owner": SEASON["owners"][lose_owner]["display"], "score": l["score"], "left": l["left"]},
    )


def race_section():
    """THE RACE: data from the FantasyPros pull after the ESPN roll, copy from race_wk9_copy.py."""
    p = os.path.join(DATA, "foh_race_wk9.json")
    if not os.path.exists(p):
        return '<h2 id="race">The Race</h2>'
    import race_wk9_copy
    return race.render(json.load(open(p)), race_wk9_copy.FOH_COPY)


def build():
    parts = []
    teams = [(t["name"], SEASON["owners"][t["owner"]]["display"]) for t in FACTS["perTeam"]]
    parts.append(jump(teams))
    parts.append('<h2 id="board">The Scoreboard</h2>')

    # ---- 1. the 112
    w, l = card_rows("Rahul Pahuja", "Ryan Kelly")
    parts.append(mcard(
        "m-pahuja", "Pahuja by 112.20, the fifth-biggest margin since 2011, with a perfect lineup", w, l,
        "C.J. Stroud 46.36 on a projection of 20.37, Matthew Golden 29.40, Christian McCaffrey 21.70 and Luther Burden III 20.20 for Rahul Pahuja, who left nothing on his bench that belonged in the lineup. Caleb Williams 16.76 and Blake Corum 11.80 for Ryan Kelly, who started Cam Skattebo, who did not play, and got zero from the Patriots defense.",
        SCALE, key=True))
    parts.append(gil(
        "Rahul Pahuja wins 173.86 to 61.66 and is 5 and 3. The margin, 112.20, is the fifth-biggest in the 1,345 games in this league's log since 2011, and the biggest since 2023. The 173.86 is the second-best week of his 243 here, behind the 174.84 he scored in Week 8 last season, and he set a perfect lineup: Bryce Young scored 26.34 on his bench, and C.J. Stroud scored 46.36 in front of him. Stroud's 46.36 is the 35th-best start by any player in this league since 2018. Ryan Kelly's 61.66 is the ninth-worst game of his 241. He is 2 and 6."))
    parts.append(boomer(
        "I picked Ryan Kelly. In ink. On this page. I said Kelly was hot, and I would like the record to show that he lost by a hundred and twelve points. Rahul had two quarterbacks, one scored 46 and one scored 26, and he started the 46. Perfect lineup. C.J. Stroud and Luther Burden outscored Ryan's entire team by themselves, 66.56 to 61.66. Ryan scored 61."))
    parts.append(gil(
        "In fairness to Ryan Kelly, he had won two straight, Cam Skattebo is out, and Justin Jefferson was projected for 15.77 and scored 7.30. Tyler Allgeier, who scored 35.60 for him last week, scored 5.60. His best lineup was 70.16. The series is 13 and 13 after 26 meetings, and Pahuja has won the last four."))
    parts.append(boomer(
        "Thirteen and thirteen, Gil. Twenty-six games dead even, and the twenty-sixth was by 112. Rahul started a kicker he signed this week who scored three. Three. His kicker was the weak link, and if you take the kicker off the field entirely he wins by 109. Rahul, I did not see you coming. Ryan saw you coming and it did not help."))

    # ---- 2. the tie is broken
    w, l = card_rows("Spencer Lentz", "Matt Davis")
    parts.append(mcard(
        "m-lentz", "Spencer by 33.12, and a series that was 14 and 14 has a leader", w, l,
        "Kenneth Walker III 36.30 on a projection of 22.35, Drake Maye 24.26, Javonte Williams 22.40 and Ka'imi Fairbairn 17.00 the week he signed him for Spencer Lentz, with Patrick Mahomes's 20.48 and Parker Washington's 16.10 on his bench. Joe Burrow 35.54 and Bucky Irving 26.50 for Matt Davis, with Jahmyr Gibbs at 13.40 on a projection of 25.27 and Mark Andrews at 2.90.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 158.16 to 125.04 and is 7 and 2, six straight wins, alone in first place and first in points at 1,169.64. The 158.16 is the second-highest score of the week and the 20th-best game of his 245 here. These two were 14 and 14 after 28 games. It is 15 and 14 now, and Spencer has won the last three. Matt Davis is 5 and 3 and holds the fourth playoff spot on points over Rahul Pahuja and Michael Smith, who are also 5 and 3."))
    parts.append(boomer(
        "I picked Davis, so file that one with the other six. Now. Spencer's best move of the week was a kicker. He signed Ka'imi Fairbairn, and the kicker scored 17, which is more than his tight end, his defense, or Chuba Hubbard gave him. Seven and two, first in points, and the transaction that looked smartest was a man whose whole job is one leg. He also left Parker Washington's 16 on the bench behind a 13 and an 11, because it would not be a Spencer lineup without something good left on the bench."))
    parts.append(gil(
        "In fairness to Matt Davis, against everyone this week he went 5 and 4. Burrow and Irving gave him 62.04. Jahmyr Gibbs was projected for 25.27 and scored 13.40, and Jameson Williams scored 4.50. He left 9.00 behind, most of it Omar Cooper Jr.'s 9.80 and Tyler Warren's 6.40 on the bench, with Mark Andrews at tight end for 2.90."))
    parts.append(boomer(
        "Matt started Mark Andrews over Tyler Warren again. Two point nine in the lineup, six point four on the bench. He did the same thing on his bye last week, when it did not count, so I let it go. This week it counted. It did not decide anything, Matt lost by 33, but a man with Joe Burrow and Jahmyr Gibbs should not be losing arguments to his own tight ends. Fifteen and fourteen after 29 games, Gil, and my pick was on the fourteen."))

    # ---- 3. the quarterback on the wrong bench
    w, l = card_rows("Bob Dorsch", "Aron Rogers")
    parts.append(mcard(
        "m-dorsch", "Dorsch by 50.68, with the quarterback he cut scoring 21.70 on the other bench", w, l,
        "Jordan Love 43.18 on a projection of 20.89, Bijan Robinson 25.70 and Spencer Shrader 16.00 for Bob Dorsch, with KC Concepcion's 19.80 on his bench behind Zay Flowers's 3.80. CeeDee Lamb 31.50 for Aron Rogers, who got 5.30 from Jared Goff with Tyler Shough's 21.70 on his bench, 3.10 from D'Andre Swift, and started George Pickens, who did not play.", SCALE))
    parts.append(gil(
        "Bob Dorsch wins 133.68 to 83.00 and is 3 and 5. Jordan Love's 43.18 is the 61st-best start by any player in this league since 2018. Aron Rogers's 83.00 is the 20th-worst game of his 166 here. He left 20.60 on his bench, the most in the league this week, and 16.40 of it was Tyler Shough behind Jared Goff. Rogers is 6 and 3, third in the standings behind Eric Olson's 6 and 2, and second in points at 1,074.00. Dorsch leads the series 11 and 7."))
    parts.append(boomer(
        "Stay with me, Gil, because this one has a family tree. Before Week 6, Bob Dorsch cut Tyler Shough. Aron Rogers signed him and he scored 33 that week. It was the headline on this page. This week Aron played Bob, sat Shough on the bench for 21.70, started Jared Goff for 5.30, and lost to the man who cut him. Bob Dorsch has now beaten Tyler Shough coming and going. Bob cut him and Aron got 33 out of it. Then Aron benched him against Bob, of all people, and handed the favor back."))
    parts.append(gil(
        "In fairness to Aron Rogers, the benching did not decide it. He lost by 50.68, and his best lineup was 103.60. George Pickens did not play, D'Andre Swift was projected for 17.75 and scored 3.10, and Goff was projected for 24.17. Rogers had left 38.08 on his bench all season before this week, the fewest in the league, and at 58.68 he still has the fewest. Bob Dorsch left 16.00 of his own, KC Concepcion behind Zay Flowers."))
    parts.append(boomer(
        "I told Bob last week to start the running backs, all of them, I did not care which. He started Bijan for 25.70 and won by fifty. I am 38 and 49 on the year and that one I am framing. And Aron: you signed a running back this week, Mike Washington Jr., cut T.J. Hockenson to do it, started him, and he scored minus 0.30. The cleanest bench in the league picked this week to leave twenty on it."))

    # ---- 4. two straight for croup
    w, l = card_rows("Aaron Jezioro", "Billy Norton")
    parts.append(mcard(
        "m-jezioro", "Jezioro by 48.14 with a perfect lineup, his second straight week over 134", w, l,
        "Ja'Marr Chase 29.50, Brock Purdy 29.28 and Brock Bowers 20.80 for Aaron Jezioro, who left nothing on his bench that belonged in the lineup. James Cook III 18.70, DeMario Douglas 14.70 and Kirk Cousins 14.64 for Billy Norton, who left 1.50 behind.", SCALE))
    parts.append(gil(
        "Aaron Jezioro wins 134.48 to 86.34 and is 4 and 4. He scored 138.30 last week and 134.48 this week, both wins, and this one came with a perfect lineup: Trevor Lawrence's 15.58 sat on the bench behind Brock Purdy's 29.28. Against everyone this week he went 7 and 2. Billy Norton is 1 and 7 and left 1.50 behind, so the lineup was not the issue. Norton still leads the series 16 and 9, and Jezioro has won the last two."))
    parts.append(boomer(
        "Last week I said I had seen Aaron's lineups. I had. He has left 148.28 on his bench this season, second-most in the league, and this week he left zero, which for Aaron is like watching a dog walk on its hind legs. You do not ask how well. Four and four, 272 points in two weeks, and one game out of the last playoff spot. Billy, four titles, 1 and 7, and you did nothing wrong on Sunday except own this roster."))
    parts.append(gil(
        "In fairness to Billy Norton, his best lineup was 87.84, and it loses this game by 46.64. Malik Nabers was projected for 14.86 and scored 6.80, and Ladd McConkey, RJ Harvey, Jaylin Noel and Kendre Miller gave him four zeros on a five-man bench. He has scored 700.54 points this season, tenth of eleven."))
    parts.append(boomer(
        "Four zeros on a five-man bench, Gil. Billy's bench is a waiting room and nobody is getting called. Kirk Cousins needed twenty for my call and brought 14.64, so add Kirk to the list of people who let Billy down this week, right under me."))

    # ---- 5. six straight
    w, l = card_rows("Michael Smith", "Michael Turner")
    parts.append(mcard(
        "m-smith", "Smith by 31.04 and into a three-way tie for the last playoff spot", w, l,
        "Puka Nacua 30.00, Dak Prescott 24.50 and Travis Kelce 15.30 for Michael Smith, with Jonathan Taylor at 6.90 and Aaron Jones Sr. at 2.60. Jayden Daniels 16.56 and Chris Olave 13.30 for Michael Turner, who got 0.50 from Josh Jacobs on a projection of 14.94 and left Breece Hall's 10.20 on his bench.", SCALE))
    parts.append(gil(
        "Michael Smith wins 107.00 to 75.96 and is 5 and 3, level with Matt Davis and Rahul Pahuja for the fourth playoff spot and behind both on points. Nacua, Prescott and Kelce gave him 69.80 of the 107. Michael Turner is 1 and 7 and has lost six straight. Josh Jacobs was projected for 14.94 and scored 0.50, with Breece Hall's 10.20 on the bench. The series is 13 and 13 after 26 meetings."))
    parts.append(boomer(
        "Two series in this league got to 13 and 13 on the same Sunday and neither game was close. Smith is 5 and 3 with the seventh-most points in the league. Against everyone, all season, he is 32 and 40. The man is a game and a half ahead of his own scoreboard and one tiebreaker from a playoff spot, and he got there this week with a running back who scored 2.60 and a flex who scored 4.10. Michael, I do not know how you are doing this and I would like you to never explain it."))
    parts.append(gil(
        "In fairness to Michael Turner, against the whole league he is 25 and 47, nearly two wins better than 1 and 7, and Lamar Jackson has been out. He left 14.50 behind this week: Hall behind Jacobs, and Tre Tucker's 7.50 behind J.K. Dobbins's 2.70. His best lineup was 90.46, and it still loses by 16.54."))
    parts.append(boomer(
        "I called a hundred for Michael Turner and he gave me 76. Josh Jacobs, half a point in the lineup. Six straight losses, Gil, and the best running back Michael had on Sunday watched from the bench."))

    # ---- the bye
    o = T["Eric Olson"]
    parts.append(byecard(
        "m-bye", "Olson on the bye: 102.36, and the receiver he released scored 13.00",
        {"team": o["name"], "owner": "Eric Olson", "score": o["score"], "left": o["left"]},
        "Christian Watson 28.60 on a projection of 13.44, Cam Little 17.00 and Josh Allen 14.86 for Eric Olson, who started Jaylen Waddle for 2.70 the week he signed him. Bye-week scores never take a trophy and do not count in all-play.", SCALE))
    parts.append(gil(
        "Eric Olson had the week off and scored 102.36. He is 6 and 2 and holds the second seed. He released Courtland Sutton, who scored 13.00, to sign Jaylen Waddle, who started and scored 2.70, and Michael Wilson's 9.00 sat on his bench. None of it counts."))
    parts.append(boomer(
        "I called 120 for Eric on his bye and he scored 102. The one week nothing counts, Eric cut a 13 for a 2.70 and started the 2.70. That is a dress rehearsal where the lead forgets his lines. Get it out of your system, Eric. Aron Rogers is next, the second seed goes with it, and Aron is in a mood."))

    # ---- THE RACE
    parts.append(race_section())

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "The rule: do not leave the answer on your own bench. For the third straight week nobody lost a game that his bench would have won. Aron Rogers came closest to the spirit of it, 20.60 left behind in a loss by 50.68. Michael Turner left 14.50 in a loss by 31.04, Matt Davis 9.00 in a loss by 33.12, Ryan Kelly 8.50 in a loss by 112.20, and Billy Norton 1.50 in a loss by 48.14."))
    parts.append(boomer(
        "Five losers and five benches that could not have saved them. The smallest gap was Turner, who needed 31 and had 14 and a half. The rule is having the quietest month of its life, Gil. Nobody is breaking it because nobody is getting close enough to. You have to be in a game to throw it away."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Eleven calls came due. Four right, seven wrong. Season record 38 and 49. One of the seven was Ryan Kelly over Rahul Pahuja, which missed by 112.20. I have been wrong before, Gil. I have never been wrong by twelve and a half points per starter. Every call is below."))
    parts.append(graded_list([
        ("Dallas Dawgs", "Matt Davis beats Spencer Lentz.", "WRONG",
         "Lost by 33.12. I took the fourteen in a 14 and 14 series and it is 15 and 14 the other way. Burrow gave me 35.54 and Gibbs gave me half of what he was projected for."),
        ("Balls Deep", "Tee Higgins clears 20 again for Spencer Lentz.", "WRONG",
         "17.70. Two point three short. Spencer won by 33 and I still found a way to lose a call inside his lineup."),
        ("WPB Steel City", "Bob Dorsch beats Aron Rogers.", "RIGHT",
         "By 50.68. I bet four titles against a 6 and 2 record, and Jordan Love made me look smart for 43.18 points."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers leaves under five on his bench in Week 9.", "WRONG",
         "20.60, the most in the league. He had left 38 all season. I called the cleanest bench in the league clean and it picked this week to spill."),
        ("Old Man Smashers", "Ryan Kelly beats Rahul Pahuja.", "WRONG",
         "Lost by 112.20. I have nothing to add. The number is the comment."),
        ("Pack Up", "Rahul Pahuja leaves under five on his bench in Week 9.", "RIGHT",
         "0.00, a perfect lineup with a 26-point quarterback on the bench behind a 46. I got the bench right and the game wrong by 112, so call it a split."),
        ("Midget Grinders", "Michael Smith beats Michael Turner.", "RIGHT",
         "By 31.04. Five and three, 32 and 40 against the room. I have stopped asking."),
        ("Napoleon's Army", "Michael Turner clears 100 in Week 9.", "WRONG",
         "75.96. Even his best lineup was 90.46. The hundred was not on the roster."),
        ("| croup", "Aaron Jezioro beats Billy Norton.", "RIGHT",
         "By 48.14 with a perfect lineup. I bet on the 138 showing up twice, and it showed up as 134.48."),
        ("I Loved You Tom Brady", "Kirk Cousins clears 20 again for Billy Norton.", "WRONG",
         "14.64. He needed twenty. Billy's bench had four zeros on it, so there was nobody else to ask."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson clears 120 on his bye.", "WRONG",
         "102.36. He released a receiver who scored 13 for one who scored 2.70. It does not count for him. It counts for me."),
    ]))
    parts.append(gil(
        "Four right, seven wrong. Eleven new ones for Week 10, one per team. Spencer Lentz has the bye. The Eagles, Buccaneers, Bears and Broncos are off, so Saquon Barkley, Bucky Irving, Caleb Williams, D'Andre Swift, Luther Burden III and the Bears and Broncos defenses sit this one out."))
    parts.append(calls_list([
        ("Balls Deep", "Spencer Lentz clears 120 on his bye.",
         "I called 120 for Eric Olson on his bye and he scored 102. Spencer leads the league in points and in points left on the bench, 155.86. Nothing counts this week. I am betting he scores anyway."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers starts Tyler Shough in Week 10.",
         "Shough scored 21.70 on his bench this week and 32.96 in his lineup in Week 6. Jared Goff scored 5.30. I am betting Aron reads this page."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Aron Rogers.",
         "Olson is 6 and 2, Rogers is 6 and 3, and the second seed is at stake. Rogers just scored 83 and loses D'Andre Swift to the bye. Olson made his mistakes on a week that did not count. I am betting on the rested man."),
        ("Old Man Smashers", "Ryan Kelly clears 80 in Week 10.",
         "He scored 61.66, and his quarterback, Caleb Williams, is off with the Bears, so this is not a gift. But he scored 117.12 and 111.08 in the two weeks before this one. I am betting 61 was the bottom."),
        ("Dallas Dawgs", "Matt Davis beats Ryan Kelly.",
         "Davis leads the series 17 and 12, four of those in the playoffs, and won the last meeting 165.04 to 69.52. He loses Bucky Irving to the bye and still has Burrow, Gibbs and Kyren Williams. He is fourth on a tiebreaker with two teams on his shoulder. He cannot drop this one."),
        ("Napoleon's Army", "Breece Hall starts for Michael Turner in Week 10.",
         "He scored 10.20 on the bench behind Josh Jacobs's 0.50. Turner also loses Goedert, Dobbins, his kicker and his defense to the bye, so he has to open the lineup anyway. While you are in there, Michael."),
        ("WPB Steel City", "Bob Dorsch beats Michael Turner.",
         "Dorsch leads 15 and 11, three of those in the playoffs, and has won the last two. He is 3 and 5, two games out with five weeks to play, and Turner is missing four starters to the bye. Bob loses Barkley. I am betting on the man with Jordan Love and a reason."),
        ("| croup", "Aaron Jezioro clears 120 for the third straight week.",
         "138.30 and 134.48. Chase, Purdy and Bowers are all playing, and Rome Odunze and Kenny Gainwell are on the bye. I am betting on the man who just found his lineup card."),
        ("Pack Up", "Rahul Pahuja beats Aaron Jezioro.",
         "Pahuja leads the series 18 and 11. He loses Luther Burden, Jonah Coleman and his defense to the bye, and he still has two quarterbacks who scored 46 and 26. Both of these men can be right on Sunday. One of them gets the win, and I am betting on the 173."),
        ("I Loved You Tom Brady", "Billy Norton beats Michael Smith.",
         "Norton leads this series 13 and 5 and has won the last two. He is 1 and 7 with four titles. Smith is 5 and 3 on a 32 and 40 record against the room. If the standings are ever going to even out for both of these men on the same afternoon, this is the game."),
        ("Midget Grinders", "Dak Prescott clears 20 again for Michael Smith.",
         "24.50 this week, and Dallas is home to San Francisco. Puka Nacua is listed as doubtful, so the 30 he scored this week may not be on the field. Smith is in a three-way tie for the last playoff spot, and his quarterback has to cover it."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, then by size. When an owner already holds one, the next name in line takes it. Bye-week scores never take a trophy."))
    parts.append(award(
        "good", "Owner of the Week", "Rahul Pahuja · Pack Up",
        "173.86, the high score of the week, the second-best week of his 243 in this league, a perfect lineup, and a win by 112.20, the fifth-biggest margin in the league's log since 2011. Stroud 46.36, Golden 29.40, McCaffrey 21.70, Burden 20.20.",
        "A perfect lineup with a 26-point quarterback on the bench, because the one in front of him scored 46. Rahul, you are 5 and 3, tied for the last playoff spot, and you just beat a man by nearly twice what he scored. I picked against you. Do it again next week so I can be wrong on purpose."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Ryan Kelly · Old Man Smashers",
        "61.66, the low score of the week, a loss to all nine teams that played, and a loss by 112.20. It is the ninth-worst game of his 241 in this league. Cam Skattebo started and did not play, with Jakobi Meyers's 8.50 on the bench, and the Patriots defense scored zero.",
        "Ryan had Start of the Week on this page seven days ago. That is Ryan Kelly's season in two issues: a backup running back scores 35 for him, and the next week the same man scores 5.60 and Ryan loses by a number you usually see on a highway sign. Four titles, Ryan. I picked you. We both have to live with that."))
    parts.append(award(
        "good", "Start of the Week", "Bob Dorsch · Jordan Love, 43.18",
        "Projected for 20.89, so 22.29 over, the biggest margin over projection by a starter whose owner does not already hold a trophy. C.J. Stroud's 46.36 for Rahul Pahuja was 25.99 over and first, and Pahuja holds Owner of the Week. Christian Watson's 28.60 for Eric Olson was 15.16 over and came on a bye.",
        "Bob Dorsch, 3 and 5, four titles, and a quarterback who just scored 43. Bob, the standings and the roster are describing two different men, and this week the roster won the argument."))
    parts.append(award(
        "bad", "Sit of the Week", "Aron Rogers · Tyler Shough, 21.70 on the bench",
        "Jared Goff started in his place for 5.30, a 16.40 swing, the biggest benching in the league this week. Bob Dorsch's KC Concepcion behind Zay Flowers was 16.00 and second, and Dorsch holds Start of the Week. Rogers lost by 50.68, so the benching flipped nothing.",
        "Aron, you rescued that quarterback off Bob Dorsch's curb, he scored 33 for you, and the week you play Bob you leave him in the garage. Twenty-one seven on the bench. Five three in the lineup. You have the cleanest bench in this league and the one stain on it is shaped like Tyler Shough."))
    parts.append(award(
        "bad", "Waste of the Week", "Michael Smith · 5.30 left behind, and he won",
        "Woody Marks scored 7.90 on his bench behind Aaron Jones Sr.'s 2.60. Bob Dorsch left 16.00 in his win and already holds a trophy. Spencer Lentz left 4.50 in his, and the other two winners left nothing.",
        "Last week Aron Rogers won this trophy with seven points and I called it the cleanest Waste ever awarded. That record lasted one week. Five point three, Michael. You won the Waste of the Week by benching a man who scored eight. The five winners in this league left 25.80 on their benches combined, and sixteen of it was Bob."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All eleven of you, every week, all season. Spencer Lentz still leads at 155.86 and added only 4.50, so somebody else finally did the work this week. Aaron Jezioro is second at 148.28 and left nothing. Rahul Pahuja is third at 133.34 and left nothing. The three biggest benches in the league went a combined 3 and 0 and left four and a half points between them. Aron Rogers, who has left the fewest all season, left 20.60 and lost."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 9, season_note=(
        "Season totals come from the season ledger through Week 9. Spencer Lentz leads at 155.86, Aaron Jezioro is second at 148.28, Rahul Pahuja third at 133.34. Aron Rogers has left the fewest, 58.68.")))
    parts.append(gil(
        "No bench cost a game this week. Aron Rogers left the most, 20.60, in a loss by 50.68. Rahul Pahuja and Aaron Jezioro left nothing and won."))
    parts.append(boomer(
        "Rahul and Aaron Jezioro have left 281 points on their benches this season between them, and both turned in perfect lineups on the same Sunday. I do not know what happened. I checked the water. Do not get used to it."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Spencer Lentz signing Ka'imi Fairbairn, who started and kicked 17.00, for Jason Myers, who kicked 6.00. An 11.00 swing, the biggest of any move in the league this week. Michael Smith's Keenan Allen for Christian Kirk was 4.60 to nothing and second."))
    parts.append(gil(
        "<strong>Worst move:</strong> Eric Olson releasing Courtland Sutton, who scored 13.00, for Jaylen Waddle, who started and scored 2.70, a 10.30 swing against him on a bye week. Aron Rogers releasing T.J. Hockenson, who scored 5.30, for Mike Washington Jr., who started and scored minus 0.30, was second, and that one counted."))
    parts.append(boomer(
        "The best move in the league this week was a kicker and the worst one did not count. Nine moves, Gil, and that is the podium."))
    parts.append(gil(
        "Nine moves went through. Bob Dorsch made three: Dalton Kincaid for Chris Boswell, then Ryan Flournoy for Kincaid, and Jordan Addison for Rachaad White. Rahul Pahuja signed Chad Ryland for Tyler Loop and picked up White for Hunter Henry."))
    parts.append(boomer(
        "Bob signed Dalton Kincaid and cut Dalton Kincaid in the same week, and Kincaid scored 4.30 for nobody. Then Bob cut Rachaad White, and Rahul picked White up and benched him. Bob's roster moves are the only waiver wire some of these teams have."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Eric Olson at Aron Rogers, Matt Davis at Ryan Kelly, Bob Dorsch at Michael Turner, Rahul Pahuja at Aaron Jezioro, and Michael Smith at Billy Norton. Spencer Lentz has the bye. The Eagles, Buccaneers, Bears and Broncos are off. Washington plays at the Giants on Thursday night, so Jayden Daniels, Malik Nabers and Isaiah Likely are done before Sunday. New England and Detroit kick off at 9:30 Sunday morning, so Jared Goff, Amon-Ra St. Brown, Jahmyr Gibbs and Jameson Williams go early. The Chargers play at Baltimore on Monday night."))
    parts.append(boomer(
        "Olson at Rogers for the second seed, 6 and 2 against 6 and 3. Davis, Rahul and Smith are all 5 and 3 for one chair, and all three play somebody below them, so this could be a three-way tie at 6 and 3 a week from now or a mess. Rahul gets Jezioro, 173 against two straight weeks over 134, and I have a call on each of them. And the man in first place has the week off, so for one Sunday whatever he leaves on the bench hurts nobody. Set a lineup anyway, Spencer."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 9, HEADLINE, DEK, build(), META, "foh-week-9.png", nav=NAV,
        published="2026-11-10T04:00:00-05:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "week-9.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
