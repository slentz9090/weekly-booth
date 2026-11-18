"""Friends of Herb, Week 10. Editorial.

Boomer runs SCORCHING (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis and never gloats, clean language on the page, roast cap and Gil defenses apply. No new segment:
the Week 9 structure with THE RACE (stays through the playoff cut) after the Scoreboard. No series line
on the cards, no Owner Spotlight. Nothing on this page refers to any other league.

Outlier engine, Week 10. HEADLINE tier: Rahul Pahuja 173.84 (3rd-best of his 244, a week after 173.86);
Christian McCaffrey 52.30 for Pahuja (9th-best start in 11,126 player-weeks since 2018). PROMOTE: Bob
Dorsch won with 75.10 (16th-fewest in a win in 1,350 games since 2011); Michael Turner 56.56 (32nd-lowest
of 2,699 team-weeks); Aron Rogers 163.62 (4th-best of his 167); Aaron Jezioro lost with Brock Purdy's
38.66; Dak Prescott 45.42 for Michael Smith (43rd-best start). SUPPORT: six perfect lineups among the
ten teams that played; Turner 1-8 on a 25-56 all-play; Smith 6-3 on 37-44. The page leads with Turner:
five starters who did not play (Goedert, Dobbins, the Broncos defense and McLaughlin on the bye, Josh
Jacobs out), a loss by 18.54 with 26.90 on the bench, and a best lineup of 83.46 against Dorsch's 75.10.

Verified against foh_wk10_facts.json, foh_season.json, foh_wk10_insights.json, foh_race_wk10.json and
gen2/data/foh_games.json.
"""
import json
import os

import booth
import race
from booth import award, boomer, byecard, calls_list, gil, graded_list, jump, ledger, mcard
from compute import DATA, by_owner, ledger_rows, load

FACTS = load("foh_wk10_facts.json")
SEASON = load("foh_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 201.32

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

HEADLINE = "Michael Turner Started Five Players Who Did Not Play. Bob Dorsch Beat Him With Just 75.10."
DEK = (
    "Four of Turner's starters were on the bye and a fifth was out, and the lineup that beats Dorsch was sitting on his bench. Rahul Pahuja scored 173.84 a week after scoring 173.86, both with perfect lineups. Six of the ten teams that played left nothing on the bench. Matt Davis finally moved on from Mark Andrews, the week Andrews scored 12.20. Spencer Lentz used his bye to bench 46.42 at quarterback. Boomer went 7 and 4."
)
META = (
    "Gil and Boomer call Week 10 of Friends of Herb: Michael Turner starts five players who did not play and loses to Bob Dorsch's 75.10, Rahul Pahuja scores 173.84 a week after 173.86, six perfect lineups in one week, four teams at 6 and 3 for two playoff spots, and Boomer goes 7 and 4."
)


def card_rows(win_owner, lose_owner):
    w, l = T[win_owner], T[lose_owner]
    return (
        {"team": w["name"], "owner": SEASON["owners"][win_owner]["display"], "score": w["score"], "left": w["left"]},
        {"team": l["name"], "owner": SEASON["owners"][lose_owner]["display"], "score": l["score"], "left": l["left"]},
    )


def race_section():
    """THE RACE: data from the FantasyPros pull after the ESPN roll, copy from race_wk10_copy.py."""
    p = os.path.join(DATA, "foh_race_wk10.json")
    if not os.path.exists(p):
        return '<h2 id="race">The Race</h2>'
    import race_wk10_copy
    return race.render(json.load(open(p)), race_wk10_copy.FOH_COPY)


def build():
    parts = []
    teams = [(t["name"], SEASON["owners"][t["owner"]]["display"]) for t in FACTS["perTeam"]]
    parts.append(jump(teams))
    parts.append('<h2 id="board">The Scoreboard</h2>')

    # ---- 1. five empty chairs
    w, l = card_rows("Bob Dorsch", "Michael Turner")
    parts.append(mcard(
        "m-dorsch", "Dorsch by 18.54 with 75.10, over a lineup with five starters who did not play", w, l,
        "Bijan Robinson 15.70, Jordan Love 12.80 and Jadarian Price 10.90 for Bob Dorsch, whose bench had nothing better. Jayden Daniels 26.76 and Drake London 15.90 for Michael Turner, who started Dallas Goedert, J.K. Dobbins, Josh Jacobs, Chase McLaughlin and the Broncos defense for zero apiece and left Garrett Wilson's 14.10 and Breece Hall's 12.80 on his bench.",
        SCALE, key=True))
    parts.append(gil(
        "Bob Dorsch wins 75.10 to 56.56 and is 4 and 5. The 75.10 is the 16th-fewest points in a win in this league since 2011, out of 1,350 games, and it was a perfect lineup: nothing on his bench would have added a point. Michael Turner started five players who did not play. Dallas Goedert, J.K. Dobbins, Chase McLaughlin and the Broncos defense were on the bye, and Josh Jacobs was out. Turner's 56.56 is the 32nd-lowest score of 2,699 team-weeks since 2011. He left 26.90 on his bench and lost by 18.54. His best lineup was 83.46. Dorsch leads the series 16 and 11 and has won the last three."))
    parts.append(boomer(
        "Last week, on this page, I told Michael Turner he was losing a tight end, a running back, a kicker and a defense to the bye and would have to open his lineup. He did not open his lineup. Five empty chairs, Gil. He played four against nine and lost by 18. Garrett Wilson and Breece Hall were on his bench with 26.90 between them, and that alone wins the game. Bob Dorsch scored 75 and it was enough. Bob could have scored 57 and it was enough."))
    parts.append(gil(
        "In fairness to Michael Turner, Lamar Jackson is on injured reserve, he had no second tight end, kicker or defense on his roster, and against the whole league this season he is 25 and 56, nearly two wins better than his 1 and 8 record. In fairness to Bob Dorsch, Saquon Barkley and DeVonta Smith were on the bye, and he started the best nine he had."))
    parts.append(boomer(
        "Bob set a perfect lineup and it scored 75.10. That was the best nine he had, Gil. Germie Bernard started for one point because nobody on the bench could beat him. Sam LaPorta gave him 2.10. Four titles, a perfect lineup, the 13th-worst score of his 243 in this league, and a win. Bob Dorsch has been in this league long enough to know you do not hand those back."))

    # ---- 2. two hundredths
    w, l = card_rows("Rahul Pahuja", "Aaron Jezioro")
    parts.append(mcard(
        "m-pahuja", "Pahuja's 173.84, a week after 173.86, over a perfect lineup that lost by 44.28", w, l,
        "Christian McCaffrey 52.30 on a projection of 20.02, Jaxon Smith-Njigba 32.10, Isaiah Likely 28.20 and C.J. Stroud 26.44 for Rahul Pahuja. Brock Purdy 38.66, Ja'Marr Chase 32.60 and Chase Brown 24.30 for Aaron Jezioro, with Trevor Lawrence's 33.78 on his bench behind Purdy.", SCALE))
    parts.append(gil(
        "Rahul Pahuja wins 173.84 to 129.56 and is 6 and 3. He scored 173.86 last week. Those are the second-best and third-best games of his 244 in this league, two hundredths of a point apart, and both were perfect lineups. Christian McCaffrey's 52.30 is the ninth-best start in this league since 2018, out of 11,126. Aaron Jezioro also set a perfect lineup, scored 129.56, the 49th-most points in a loss since 2011, and is 4 and 5. Pahuja leads the series 19 and 11."))
    parts.append(boomer(
        "A hundred seventy-three point eight six. Then a hundred seventy-three point eight four. Rahul is not having hot weeks, he is running a machine, and the machine slipped by two hundredths. Perfect lineup both times. The man has not left a point on his bench in two weeks. And Jezioro, bless him. Three straight weeks over 129, a perfect lineup of his own, and he lost by 44. Aaron did everything right and got run over by a truck that was also doing everything right."))
    parts.append(gil(
        "In fairness to Aaron Jezioro, he chose Brock Purdy over Trevor Lawrence and Purdy outscored him, 38.66 to 33.78, so the 33.78 on the bench was the right decision. Brock Bowers was projected for 12.89 and scored 2.80, and Denzel Boston was projected for 11.14 and scored 2.10. He has left 148.28 on his bench this season, second-most in the league, and none of it came this week."))
    parts.append(boomer(
        "Jezioro had two quarterbacks score 72 between them and picked the right one. I have spent ten weeks yelling at this man about his bench. He fixes it, sets three good lineups in a row, and goes 2 and 1. I called 120 for him and he cleared it. He was 23% to make the playoffs a week ago, per FantasyPros, and he is 4% now. Aaron finally stopped beating himself, so the schedule sent Rahul to do it."))

    # ---- 3. the second seed
    w, l = card_rows("Aron Rogers", "Eric Olson")
    parts.append(mcard(
        "m-rogers", "Rogers by 61.48, the fourth-best game of his 167, for the second seed", w, l,
        "George Pickens 40.00 on a projection of 10.19, Jared Goff 27.42 and Amon-Ra St. Brown 26.80 for Aron Rogers. Josh Allen 24.34, Cam Little 19.00 and Bhayshul Tuten 18.80 for Eric Olson, with A.J. Brown at 3.70 and Christian Watson at 5.20.", SCALE))
    parts.append(gil(
        "Aron Rogers wins 163.62 to 102.14 and is 7 and 3, second in the standings. It is the fourth-best game of his 167 in this league and a perfect lineup. Jared Goff started over Tyler Shough and outscored him, 27.42 to 11.98. Eric Olson is 6 and 3, one of four teams with that record. He scored 102.36 on his bye a week ago and 102.14 this week."))
    parts.append(boomer(
        "I picked Olson. I said the rested man. The rested man scored 102.14, which is 22 hundredths less than he scored on his week off. Eric took a bye, came back, and reproduced the bye. I also called for Aron to start Tyler Shough. Aron started Jared Goff, who scored 27, and Shough scored 12 on the bench. Rogers heard both of my opinions about his team and scored 163."))
    parts.append(gil(
        "In fairness to Eric Olson, A.J. Brown was projected for 11.08 and scored 3.70 in his return from injury, Christian Watson was projected for 13.44 and scored 5.20, and Jaylen Waddle did not play. He left 4.90 on his bench. No lineup he had gets within 56 points."))
    parts.append(boomer(
        "Rogers has left 58.68 on his bench all season, the fewest in the league. He goes on the bye next week at 7 and 3 with the second seed in his pocket. Olson scored 102 two weeks in a row and fell from second to fifth. The number never moved. Everybody else did."))

    # ---- 4. the tight end
    w, l = card_rows("Matt Davis", "Ryan Kelly")
    parts.append(mcard(
        "m-davis", "Davis by 27.86 with two players over 42, in a game where both lineups were perfect", w, l,
        "Jahmyr Gibbs 42.70, Joe Burrow 42.16 and the Rams defense 14.00 for Matt Davis, with Tyler Warren at 1.40. Cam Skattebo 25.70, Blake Corum 21.40 and Drew Lock 19.60 the week he signed him for Ryan Kelly.", SCALE))
    parts.append(gil(
        "Matt Davis wins 142.06 to 114.20 and is 6 and 3, third in the standings on points. Jahmyr Gibbs and Joe Burrow scored 84.86 between them. Both teams set perfect lineups. Ryan Kelly's 114.20 is his third score over 110 in four weeks, and he is 2 and 7. He signed Drew Lock this week and Lock scored 19.60. Davis leads the series 18 and 12."))
    parts.append(boomer(
        "For weeks I have been on Matt about starting Mark Andrews over Tyler Warren. So this week Matt cut Mark Andrews. Released him. Gone. And Andrews went out and scored 12.20 for nobody, and Tyler Warren scored 1.40 in the lineup. Matt Davis finally took my advice and it immediately exploded. He won by 28 because Gibbs and Burrow scored 85, and nobody will ever ask about the tight end. I am asking about the tight end."))
    parts.append(gil(
        "In fairness to Matt Davis, his lineup was perfect: no one on his bench would have helped, and Matthew Stafford's 25.76 sat behind Burrow's 42.16. Kyren Williams was projected for 17.45 and scored 4.20. In fairness to Ryan Kelly, his best nine scored 114.20 and he started all nine. He has had 1,099.36 points scored against him, the second-most in the league."))
    parts.append(boomer(
        "Ryan Kelly did nothing wrong. Perfect lineup, signed a quarterback who scored 19.60, got 47 from two running backs, and lost by 28 to a man with two forties. I picked Davis and I picked Kelly to clear 80, and both came in. When Ryan Kelly and I are both right in the same week, check the sky."))

    # ---- 5. same record
    w, l = card_rows("Michael Smith", "Billy Norton")
    parts.append(mcard(
        "m-smith", "Smith by 23.44 behind Dak Prescott's 45.42", w, l,
        "Dak Prescott 45.42 on a projection of 19.96 and Deebo Samuel Sr. 24.40 for Michael Smith, with the Cowboys defense at zero. James Cook III 23.70, Kirk Cousins 19.38 and Omarion Hampton 19.00 for Billy Norton, who started DeMario Douglas for 0.90 with Stefon Diggs's 17.30 on his bench.", SCALE))
    parts.append(gil(
        "Michael Smith wins 125.52 to 102.08 and is 6 and 3, level with Matt Davis, Rahul Pahuja and Eric Olson. Dak Prescott's 45.42 is the 43rd-best start in this league since 2018, out of 11,126. Smith left 1.60 on his bench. Against the whole league this season he is 37 and 44, nearly two wins worse than his record. Billy Norton is 1 and 8 and still leads the series 13 and 6."))
    parts.append(boomer(
        "Davis and Rahul are 6 and 3 too. FantasyPros gives them a 76% and a 67% chance to make the playoffs and gives Smith 13%, because he is 37 and 44 against the room. He just won with a defense that scored zero and a quarterback who scored 45, and for one more week FantasyPros can sit there and be wrong."))
    parts.append(gil(
        "In fairness to Billy Norton, Stefon Diggs was projected for 8.44, slightly under DeMario Douglas's 8.63, and Malik Nabers was projected for 13.61 and scored 4.90. He left 16.40 behind and lost by 23.44, so the bench did not decide it. Ladd McConkey did not play."))
    parts.append(boomer(
        "I picked Billy. Billy leads this series 13 and 6 and that is why I picked him, and it turns out the series does not suit up. DeMario Douglas, nine tenths of a point, with 17.30 sitting right behind him. Billy Norton has four titles and one win, and I keep betting on the first number."))

    # ---- the bye
    o = T["Spencer Lentz"]
    parts.append(byecard(
        "m-bye", "Spencer Lentz on the bye: 147.12, with 46.42 at quarterback on his bench",
        {"team": o["name"], "owner": "Spencer Lentz", "score": o["score"], "left": o["left"]},
        "Emmett Johnson 34.10 the week he signed him, Chuba Hubbard 31.70 and Parker Washington 26.70 for Spencer Lentz, with Drake Maye at 3.02 and Patrick Mahomes's 46.42 on his bench. Bye-week scores never take a trophy and do not count in all-play.", SCALE))
    parts.append(gil(
        "Spencer Lentz had the bye and is 7 and 2, still first. His lineup scored 147.12. Drake Maye left his game on the first drive with an ankle injury and scored 3.02, with Patrick Mahomes's 46.42 on the bench. Colston Loveland started at tight end with the Bears on their bye, and there was no other tight end on the roster: Tucker Kraft was released this week for the 49ers defense, which scored 2.00 on the bench. He left 54.20 behind. None of it counts."))
    parts.append(boomer(
        "I called 120 for him on the bye and he cleared it, so thank you, Spencer, for the win. Now. Forty-six on the bench at quarterback behind a three. He could have known the Bears were not playing, because it was on the schedule, and he started their tight end anyway after cutting the other one for a second defense. His best lineup was 201.32. On a week with no opponent he still found a way to lose 54 points."))

    # ---- THE RACE
    parts.append(race_section())

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "The rule: do not leave the answer on your own bench. For the first time in four weeks, somebody broke it. Michael Turner left 26.90 behind and lost by 18.54. Garrett Wilson's 14.10 and Breece Hall's 12.80 would have replaced two starters who scored zero, and his best lineup, 83.46, beats Bob Dorsch's 75.10 by 8.36. Billy Norton left 16.40 in a loss by 23.44 and Eric Olson 4.90 in a loss by 61.48. Aaron Jezioro and Ryan Kelly lost with nothing on the bench at all."))
    parts.append(boomer(
        "Usually this rule is about a hard choice. Two receivers, pick one, pick wrong. This one was easy. Breece Hall played and sat behind Josh Jacobs, who did not. The answer was standing on Turner's bench, waving."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Eleven calls came due. Seven right, four wrong. Season record 45 and 53. Seven right. I will take it. Every call is below, in ink."))
    parts.append(graded_list([
        ("Napoleon's Army", "Breece Hall starts for Michael Turner in Week 10.", "WRONG",
         "He scored 12.80 on the bench behind two running backs who did not play. I said Michael had to open the lineup anyway. He did not open the lineup."),
        ("WPB Steel City", "Bob Dorsch beats Michael Turner.", "RIGHT",
         "By 18.54, with 75.10. I bet on the man with Jordan Love and a reason. All he needed was a pulse."),
        ("Pack Up", "Rahul Pahuja beats Aaron Jezioro.", "RIGHT",
         "By 44.28 with 173.84. I said both of these men could be right on Sunday. Both set perfect lineups. One of them had McCaffrey."),
        ("| croup", "Aaron Jezioro clears 120 for the third straight week.", "RIGHT",
         "129.56 with a perfect lineup, in a loss. He found his lineup card and then ran into Rahul."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Aron Rogers.", "WRONG",
         "Lost by 61.48. He scored 102.36 on his week off and 102.14 on his week back. I should have bet on the 102."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers starts Tyler Shough in Week 10.", "WRONG",
         "He started Jared Goff, who scored 27.42. Shough scored 11.98 on the bench. Aron was right and I was loud."),
        ("Dallas Dawgs", "Matt Davis beats Ryan Kelly.", "RIGHT",
         "By 27.86, with Gibbs and Burrow both over 42. I said he still had Burrow, Gibbs and Kyren Williams. Two out of three."),
        ("Old Man Smashers", "Ryan Kelly clears 80 in Week 10.", "RIGHT",
         "114.20 with a perfect lineup. I set the bar at 80 for a man who has now cleared 110 three times in four weeks. Ryan has earned a higher bar."),
        ("Midget Grinders", "Dak Prescott clears 20 again for Michael Smith.", "RIGHT",
         "45.42. I set the bar at 20 and he cleared it twice."),
        ("I Loved You Tom Brady", "Billy Norton beats Michael Smith.", "WRONG",
         "Lost by 23.44 with Stefon Diggs's 17.30 on the bench. I bet on a 13 and 5 series, and it is now 13 and 6."),
        ("Balls Deep", "Spencer Lentz clears 120 on his bye.", "RIGHT",
         "147.12, with another 54.20 on the bench. I bet he would score anyway. He scored anyway, and then some, and then some more that did not start."),
    ]))
    parts.append(gil(
        "Seven right, four wrong. Eleven new ones for Week 11, one per team. Aron Rogers has the bye. The Falcons, Patriots, Packers, Seahawks, Rams and Browns are off, so Bijan Robinson, Jaxon Smith-Njigba, Jordan Love, Matthew Stafford, Kyren Williams, Drake London, Christian Watson and Quinshon Judkins sit this one out."))
    parts.append(calls_list([
        ("Balls Deep", "Patrick Mahomes clears 25 for Spencer Lentz.",
         "46.42 on the bench this week. Kansas City is home to Arizona, and he is the only quarterback on that roster with a game. I am betting 25 of it counts this time."),
        ("Old Man Smashers", "Caleb Williams starts for Ryan Kelly in Week 11.",
         "Drew Lock scored 19.60 for him this week, and Seattle is off. Caleb Williams is back from the bye, home to the Saints. Ryan just set a perfect lineup, so I am betting he reads the schedule too."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Michael Turner.",
         "Olson leads the series 5 and 1, and they have not played since 2014. Eric loses A.J. Brown and Christian Watson to the bye. He still has Josh Allen home to Miami, and he is fifth with four teams on the same record. I am betting he does not score 102 a third time."),
        ("Napoleon's Army", "Michael Turner clears 90 in Week 11.",
         "Drake London, Zach Charbonnet and Josh Jacobs are on the bye. Jayden Daniels, Breece Hall, Garrett Wilson and Chris Olave are not. I am betting on nine men who are playing, Michael, and I have checked: you have nine."),
        ("Dallas Dawgs", "Matt Davis beats Aaron Jezioro.",
         "The series is 12 and 12, and Davis has won the last three. He loses Kyren Williams, Quinshon Judkins and the Rams defense to the bye, so he needs a defense by Sunday. He still has Burrow and Gibbs off a pair of 42s. I am betting on the two forties."),
        ("| croup", "Ja'Marr Chase clears 20 again for Aaron Jezioro.",
         "32.60 this week, and Cincinnati is at Washington. Aaron has cleared 129 three straight weeks and lost the last one by 44. I am betting on Chase and hoping for the owner."),
        ("I Loved You Tom Brady", "Billy Norton beats Bob Dorsch.",
         "Dorsch leads the series 16 and 6. He also loses Bijan Robinson, Jordan Love, Jadarian Price and KC Concepcion to the bye, and Love is the only quarterback on his roster. Billy has James Cook III home to Miami. I picked Billy last week and lost. I am picking him again, because this time the other side has to find a quarterback first."),
        ("WPB Steel City", "Saquon Barkley clears 12 for Bob Dorsch.",
         "Back from the bye, home to Pittsburgh. Bob just won with 75 and is about to lose four starters to the schedule. I am betting the one who comes back does his share."),
        ("Pack Up", "Rahul Pahuja beats Michael Smith.",
         "Pahuja leads the series 18 and 10, though Smith won the last one. Rahul loses Jaxon Smith-Njigba and Matthew Golden to the bye. He has also scored 173 twice in a row. Two teams at 6 and 3, and I am betting on the one that got there on points."),
        ("Midget Grinders", "Dak Prescott clears 25 for Michael Smith.",
         "45.42 this week, and Dallas is home to Tennessee. I set the bar at 20 last week and he doubled it. Smith needs every bit of it against Rahul, so I moved the bar up."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers clears 130 on his bye.",
         "163.62 this week with a perfect lineup, and none of his starters are off. Nothing counts for him on Sunday. I am betting a man who has left the fewest points in the league on his bench does not start now."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, then by size. When an owner already holds one, the next name in line takes it. Bye-week scores never take a trophy."))
    parts.append(award(
        "good", "Owner of the Week", "Rahul Pahuja · Pack Up",
        "173.84, the high score of the week, a win against all nine other teams that played, and a perfect lineup. It is the third-best game of his 244 in this league, and the second-best was a week ago. McCaffrey 52.30, Smith-Njigba 32.10, Likely 28.20, Stroud 26.44. This is his second straight Owner of the Week.",
        "Back to back. Same score, same perfect lineup, same trophy. Rahul was 4 and 3 two weeks ago and scrapping for the last spot. He has scored 347.70 since. If he does it a third time I am checking the machine for a plug."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Michael Turner · Napoleon's Army",
        "56.56, the low score of the week and the 32nd-lowest of 2,699 team-weeks since 2011. Five starters did not play: Dallas Goedert, J.K. Dobbins, Chase McLaughlin and the Broncos defense on the bye, and Josh Jacobs out. Garrett Wilson's 14.10 and Breece Hall's 12.80 were on the bench, and the best lineup he had, 83.46, wins the game by 8.36.",
        "Michael Turner lost to 75 points. With the win on his bench. With a week's warning, in writing, on this page. Napoleon's Army marched into Sunday with four soldiers. Michael, the bye weeks are printed in advance. They print them in the spring."))
    parts.append(award(
        "good", "Start of the Week", "Aron Rogers · George Pickens, 40.00",
        "Projected for 10.19, so 29.81 over, the biggest margin over projection by a starter whose owner does not already hold a trophy. Christian McCaffrey's 52.30 for Rahul Pahuja was 32.28 over and first, and Pahuja holds Owner of the Week. Dak Prescott's 45.42 for Michael Smith was 25.46 over and third.",
        "Aron put George Pickens in the flex and got forty. He also sat Tyler Shough against my advice and was right about that too. A perfect lineup, the fourth-best day of his career, and the second seed. Aron, I would tell you to keep it up, but you do better when I tell you nothing."))
    parts.append(award(
        "bad", "Sit of the Week", "Billy Norton · Stefon Diggs, 17.30 on the bench",
        "DeMario Douglas started in his place for 0.90, a 16.40 swing, the biggest benching in a game that counted by an owner who does not already hold a trophy. Michael Turner's benchings cost him a game, and he holds Worst Owner. Spencer Lentz left Patrick Mahomes's 46.42 behind Drake Maye's 3.02 on his bye, and bye weeks never take a trophy.",
        "The projections had Douglas ahead by 0.19. Billy took the 0.19 and it ran 16.40 the other way. Four titles, one win, and now the projections are in on it."))
    parts.append(award(
        "bad", "Waste of the Week", "Michael Smith · 1.60 left behind, and he won",
        "Five teams won this week and four of them left nothing on the bench. Smith is the only winner who left anything: Keenan Allen's 8.60 behind Woody Marks's 7.00. It is his second straight Waste of the Week, after 5.30 a week ago.",
        "One point six. Everybody else who won was perfect, so Smith gets the hardware for the only blemish among the winners, two weeks running. He is 6 and 3 and keeps winning the wrong awards."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All eleven of you, every week, all season. Six of the ten teams that played this week left nothing on the bench: Pahuja, Rogers, Davis, Kelly, Jezioro and Dorsch. A perfect lineup happens about one team-week in eight in this league since 2018, and six of you did it in the same week. Then there is the leader. Spencer Lentz added 54.20 on his bye and now sits at 210.06 for the season, 61.78 clear of Aaron Jezioro in second."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 10, season_note=(
        "Season totals come from the season ledger through Week 10 and include bye weeks. Spencer Lentz leads at 210.06, Aaron Jezioro is second at 148.28, Rahul Pahuja third at 133.34. Aron Rogers has left the fewest, 58.68.")))
    parts.append(gil(
        "One bench cost a game this week: Michael Turner left 26.90 and lost by 18.54. Billy Norton left 16.40 and lost by 23.44. Eric Olson left 4.90 and Michael Smith 1.60. The other six teams that played left 0.00."))
    parts.append(boomer(
        "Six zeroes on the ledger, and the man at the top of it left 54 on a week off. Spencer has left more than three times as much on his bench this season as Aron Rogers has. He is also in first place, which is the most annoying sentence I have had to read on this broadcast."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Ryan Kelly signing Drew Lock, who started and scored 19.60, for Kyler Murray, who did not play. Rahul Pahuja's Bills defense, 11.00 in his lineup, for Jalen Coker was second. Kelly's Lions defense for the Patriots was 10.00 to 3.00 and third. Spencer Lentz signed Emmett Johnson, who scored 34.10 in his lineup, on a bye week that did not count."))
    parts.append(gil(
        "<strong>Worst move that made a lineup:</strong> Matt Davis releasing Mark Andrews, who scored 12.20, for Audric Estime, who scored 1.60 on his bench, which left Tyler Warren to start at tight end for 1.40. Bob Dorsch released Ryan Flournoy, who scored 16.10, for Jadarian Price, who started and scored 10.90. Eric Olson released Antonio Williams, who scored 11.20, for Travis Etienne Jr., who scored 4.90 on his bench."))
    parts.append(boomer(
        "Bob Dorsch signed Bo Nix this week. The Broncos were on the bye. Then Bob released Bo Nix, the same week, without Nix ever touching the lineup or a football. Bob picked up a quarterback on the quarterback's week off and put him back before he got home. Seventeen moves in the league this week and that one was a round trip to nowhere."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Ryan Kelly at Spencer Lentz, Michael Turner at Eric Olson, Aaron Jezioro at Matt Davis, Billy Norton at Bob Dorsch, and Michael Smith at Rahul Pahuja. Aron Rogers has the bye. The Falcons, Patriots, Packers, Seahawks, Rams and Browns are off. Four weeks remain in the regular season."))
    parts.append(boomer(
        "Smith at Pahuja is the game. Two teams at 6 and 3, one that got there on 173s and one that got there on a 37 and 44 team, and somebody leaves at 6 and 4 in a four-way knot. Davis and Jezioro are 12 and 12 lifetime and Davis has to find a defense. Bob Dorsch has to replace four starters. And the first-place team comes off its bye against Ryan Kelly, who just set a perfect lineup and lost, which makes him the most dangerous 2 and 7 team I have ever seen."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 10, HEADLINE, DEK, build(), META, "foh-week-10.png", nav=NAV,
        published="2026-11-17T21:00:00-05:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "week-10.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
