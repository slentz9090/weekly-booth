"""Dewart Lake FFL, Week 7. Editorial. The halfway mark.

Boomer runs ULTRA SPICY (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis, clean language on the page, roast cap and Gil defenses apply. Mama Beth and DA, never "Mother" or
"Dad".

NEW THIS WEEK: HALFTIME. Seven games in, seven to go, so the page carries a new segment built from the
all-time log (gen2/halftime.py -> docs/data/dlffl_halftime.json): what the standings after Week 7 have
meant in every season on record (2009 to 2025), the luck board (actual record vs all-play), and one
random stat from the archive. It sits right after the scoreboard because forward-looking content at the
bottom of the page is never reached.

Outlier engine, Week 7: a quiet week. Promote tier only: Casey Couture has beaten Adam Calvelage six
straight (every meeting), and Casey is 4-3 on a 23-54 all-play (1.9 wins lucky, the luckiest in the
league). Support: Ryan Reed left Bo Nix's 28.18 on his bench and lost by 16.46 (the Nix-for-McCarthy swap
alone is 18.00); Mama Beth claimed Omar Cooper Jr., benched him for 23.00, started Justin Jefferson for
6.40 and lost by 10.20; Scott Howard's 135.68 is the high score of the week from eleventh place; Doug
Fields set a perfect lineup and his seven scores sit in a 13.48-point band, the tightest seven-week start
by any owner since 2009; Kent Frenger's Tony Pollard scored 38.00 on a projection of 14.00.

Verified against dlffl_wk7_facts.json, dlffl_season.json, dlffl_halftime.json and gen2/data/dlffl_games.json.
"""
import os

import booth
from booth import award, boomer, calls_list, gil, graded_list, halftime_board, halftime_tiles, jump, ledger, mcard
from compute import ledger_rows, load, by_owner

FACTS = load("dlffl_wk7_facts.json")
SEASON = load("dlffl_season.json")
HALF = load("dlffl_halftime.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 143.12

NAV = (
    '<nav class="nav" aria-label="Sections"><ul>'
    '<li><a href="#board">The Scoreboard</a></li>'
    '<li><a href="#halftime">Halftime</a></li>'
    '<li><a href="#calls">On The Record</a></li>'
    '<li><a href="#hardware">The Hardware</a></li>'
    '<li><a href="#ledger">The Bench Ledger</a></li>'
    '<li><a href="#wire">The Waiver Wire</a></li>'
    '<li><a href="#next">Next Sunday</a></li></ul></nav>'
)

HEADLINE = "Scott Howard Scored The Most Points In The League This Week. He Is In Eleventh Place."
DEK = (
    "Halftime in Dewart Lake. Scott Howard put up 135.68, the high score of the week, and is 2 and 5 with the "
    "fifth-most points in the league. Casey Couture is 4 and 3 with the fewest. Ryan Reed signed a quarterback, "
    "started him over Bo Nix, and lost by less than Nix scored on his bench. Mama Beth claimed a receiver, sat "
    "him for 23, and lost by 10. The booth opens the archive on what the halfway mark has meant since 2009."
)
META = (
    "Gil and Boomer call Week 7 of the Dewart Lake FFL, the halfway mark: Scott Howard's 135.68 from eleventh "
    "place, Casey Couture 4 and 3 with the fewest points in the league, Ryan Reed benches Bo Nix, Mama Beth "
    "benches a 23, and a new segment on what the halfway standings have meant in every season since 2009."
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

    # ---- 1. the high score, from eleventh
    w, l = card_rows("Scott Howard", "Scott Reisert")
    parts.append(mcard(
        "m-howard", "Howard's 135.68, the high score of the week, from eleventh place", w, l,
        "Bucky Irving 26.50, the Buccaneers defense 26.00 on a projection of 4.65, and Dak Prescott 23.28 for "
        "Scott Howard. Scott Reisert got 24.50 from Javonte Williams and 21.02 from Jared Goff, and left Rico "
        "Dowdle's 11.60 behind Kendre Miller's 4.30.", SCALE, key=True))
    parts.append(gil(
        "Scott Howard wins 135.68 to 100.82 and is 2 and 5. It is the high score of the week, and it would have "
        "beaten all eleven teams. He has the fifth-most points in the league, 761.10, and he sits eleventh in "
        "the standings. The series with Reisert is 3 and 3."))
    parts.append(boomer(
        "Two and five with the fifth-most points in the league. Scott Howard is the best-dressed man at the bus stop. "
        "Two weeks ago he scored 173 and won. Last week he scored 99 with a perfect lineup and lost by 38. This "
        "week he scored 136 and won by 35. Scott, you do not have a team. You have a weather system."))
    parts.append(gil(
        "In fairness to Scott Reisert, he started the year 3 and 0 with scores of 142.08 and 160.76 in there, and "
        "he is still fourth in points. Jahmyr Gibbs was projected for 24.82 and scored 17.80. His kicker swap, "
        "Chris Boswell in for Nick Folk, produced exactly 11.00 either way."))
    parts.append(boomer(
        "He cut a kicker who scored eleven and signed a kicker who scored eleven. Scott Reisert ran a full "
        "transaction to change the name on the jersey, a man rearranging the furniture in a house that is on "
        "fire. Three losses in four, and the one win was by 58 over Mama Beth."))

    # ---- 2. the quarterback he signed
    w, l = card_rows("Spencer Lentz", "Ryan Reed")
    parts.append(mcard(
        "m-lentz", "Spencer by 16.46, and Reed's benched quarterback outscored the gap by himself", w, l,
        "Drake Maye 30.44 and Tee Higgins 26.80 for Spencer Lentz, with Nico Collins at 1.60 in his lineup and "
        "C.J. Stroud's 16.52 on his bench. Ryan Reed signed J.J. McCarthy this week and started him for 10.18. "
        "Bo Nix scored 28.18 on Reed's bench.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 123.04 to 106.58 and is 5 and 2, five straight wins, first place, and the most "
        "points in the league at 925.28. Ryan Reed released Jacoby Brissett this week, who scored 16.48, signed "
        "J.J. McCarthy, who scored 10.18, and left Bo Nix on the bench for 28.18. Nix for McCarthy is an 18.00 "
        "swing in a game Reed lost by 16.46. He left 27.50 behind in all, the most in the league this week."))
    parts.append(boomer(
        "Three quarterbacks, Gil. Ryan cut the one who scored 16, started the one who scored 10, and benched the "
        "one who scored 28. Ryan ran a quarterback tournament and gave the trophy to the guy who lost in the first "
        "round. Nix was projected for 16.81, McCarthy for 17.33. Ryan saw half a point of projection and it "
        "turned into eighteen the other way."))
    parts.append(gil(
        "In fairness to Ryan Reed, Jaxon Smith-Njigba scored 29.80, as Boomer called, Cam Skattebo gave him 21.60 "
        "on a projection of 7.63 and Emanuel Wilson 21.00 on a projection of 10.57. Against the whole league "
        "this season he is 39 and 38, so his 3 and 4 is about what his scores have earned. Spencer started "
        "Nico Collins for 1.60, and Stroud outscored six of his nine starters from "
        "the bench."))
    parts.append(boomer(
        "Spencer is in first place with the most points in the league, and he has now left Stroud on the bench "
        "for 25.98 and 16.52 in back-to-back weeks. Nico Collins scored 1.60 in his lineup. One point six. "
        "Spencer, Nico Collins scored 1.60 and Reed's kicker scored 1.00. The two of them should split a cab. First "
        "place is a nice view, and you are standing on a ladder somebody else is holding."))

    # ---- 3. the claim she benched
    w, l = card_rows("Adam Hershberger", "Beth Couture")
    parts.append(mcard(
        "m-hershberger", "Hershberger by 10.20 with a quarterback he signed this week; Mama Beth benched a 23", w, l,
        "Jameson Williams 23.60, Malik Nabers 17.60 and Blake Corum 16.60 for Adam Hershberger, with Kyler "
        "Murray, signed this week, at 13.90. Mama Beth got 26.70 from Zay Flowers and 24.70 from Luther Burden "
        "III, started Justin Jefferson for 6.40, and left Omar Cooper Jr., claimed this week, on her bench for "
        "23.00.", SCALE))
    parts.append(gil(
        "Adam Hershberger wins 115.80 to 105.60 and is 3 and 4. Trevor Lawrence had the week off and there was no "
        "other quarterback on Hershberger's roster, so he claimed Kyler Murray, who gave him 13.90. Mama Beth claimed "
        "Omar Cooper Jr. this week and released Jalen Hurts to make room. Cooper scored 23.00 on her bench. She "
        "started Justin Jefferson for 6.40 and lost by 10.20. She leads the series 6 and 3, and has lost the last "
        "two."))
    parts.append(boomer(
        "She went and got the man. She cut a quarterback to make room for him. Then she looked at him and said, "
        "not today, son. Twenty-three points. Mama Beth lost by ten with a sixteen-point mistake "
        "sitting in a chair she pulled out herself. Mama Beth drove to the airport to pick the man up and "
        "drove home alone."))
    parts.append(gil(
        "In fairness to Mama Beth, Flowers and Burden gave her 51.40 between them, her two best receivers this "
        "week by a distance, and Patrick Mahomes was projected for 16.37 and scored 6.00. She has three titles "
        "here, and she started the year as Owner of the Week with 149.12. Adam Hershberger has now scored "
        "over 100 three weeks running after opening the year with four weeks under it, and he still has 904.60 "
        "points scored against him, the most in the league by 45."))
    parts.append(boomer(
        "Adam is 3 and 4 and the league has dropped 904 points on his head. He has been the away team at his own "
        "house all year. He finally found a receiver, Jameson Williams, 23.60 on a projection of 9.27, and the "
        "reward is DA next week, who he has beaten three straight times. Adam, careful. In this league a streak "
        "against a Couture is how they find you."))

    # ---- 4. six straight, fewest points
    w, l = card_rows("Casey Couture", "Adam Calvelage")
    parts.append(mcard(
        "m-casey", "Casey's sixth straight over Calvelage, by 2.36, every meeting they have played", w, l,
        "Ollie Gordon II 19.80, Jonathan Taylor 18.00 and D'Andre Swift 17.00 for Casey Couture, whose new Titans "
        "defense scored zero. Adam Calvelage got 21.90 from CeeDee Lamb and 14.00 from Brandon Aubrey, with "
        "Jayden Daniels on bye and Brock Purdy at 12.02.", SCALE))
    parts.append(gil(
        "Casey Couture wins 90.68 to 88.32 and is 4 and 3. He has beaten Adam Calvelage six straight times, which "
        "is every meeting they have played. Casey has the fewest points in the league, 653.22, and he is tied on "
        "record with the fourth seed. This week he released the Colts defense, who scored 8.00, for the Titans "
        "defense, who scored zero, and won by 2.36 anyway."))
    parts.append(boomer(
        "Fewest points in the league, 4 and 3, two tiebreakers from the playoffs. The man cut an eight-point defense for "
        "a zero-point defense on purpose and won by two. Casey does not play fantasy football, Gil. He plays "
        "roulette, and the wheel knows his family by name."))
    parts.append(gil(
        "In fairness to Adam Calvelage, Lamb cleared 20 and his kicker scored 14.00, and he left just 0.90 "
        "behind. His bench scored 4.50 in total. He was 3 and 1 after four weeks and has lost three straight, by "
        "71.46, by 16.72 and by 2.36."))
    parts.append(boomer(
        "Three and one to three and four. Adam's bench scored four and a half points. His bench is a waiting room "
        "with the magazines taken away. Daniels on bye, Purdy for 12, a defense for zero, and he still only lost "
        "by two to a team that has scored fewer points than anybody. Adam, you lost a fight to a man who was "
        "asleep."))

    # ---- 5. the metronome
    w, l = card_rows("Doug Fields", "dennis couture")
    parts.append(mcard(
        "m-fields", "Fields by 13.20 with a perfect lineup, over the low score of the week", w, l,
        "Joe Burrow 28.88, Tre Tucker 21.80 and Rhamondre Stevenson 20.00 for Doug Fields, who left nothing "
        "behind. Derrick Henry gave him 5.40. DA got 19.00 from Christian McCaffrey and 17.10 from Kyren "
        "Williams, with Aaron Rodgers at 13.08, Xavier Worthy at 2.60 and Ryan Fitzgerald, signed this week, "
        "at 1.00.", SCALE))
    parts.append(gil(
        "Doug Fields wins 96.48 to 83.28 and is 3 and 4. He started Tre Tucker, as Boomer called, and Tucker "
        "scored 21.80. DA's 83.28 is the low score of the week and loses to all eleven teams. DA leads the "
        "series 8 and 4. Fields has scored between 92.00 and 105.48 every week this season, a 13.48-point band, "
        "and that is the tightest seven-week start by any owner in this league since 2009."))
    parts.append(boomer(
        "Seventeen seasons, every owner who ever played here, and nobody has ever opened a year as flat as Doug "
        "Fields. Ninety-two to a hundred and five, seven straight weeks. The man is a dial tone. And this week "
        "the dial tone beat DA, because DA scored 83 with Aaron Rodgers at quarterback, a kicker he signed this "
        "week for one point, and Xavier Worthy for 2.60. DA has gone 151, 92, 83 in three weeks, "
        "Gil. The man is walking down a staircase in the dark and calling it a slump."))
    parts.append(gil(
        "In fairness to DA, Josh Allen, Khalil Shakir and Dalton Kincaid all had the week off with the Bills, "
        "McCaffrey and Kyren Williams were 36.10 between them, and he is still second in the league in points "
        "with 844.84. He is 4 and 3 and holds the fourth seed on points. Doug Fields is now 3 and 4 with the "
        "league's cleanest week, and his first bench of the season with nothing on it."))
    parts.append(boomer(
        "Second in points, fourth seed, and he just lost to a 96. DA and Mama Beth are 5 and 9 between them, "
        "Gil. Spencer and Casey are 9 and 5. Somewhere in that house there is a Thanksgiving table where "
        "nobody is passing anything."))

    # ---- 6. Pollard
    w, l = card_rows("Kent Frenger", "Geoff Cavender")
    parts.append(mcard(
        "m-frenger", "Frenger's fourth straight win, and Tony Pollard's 38.00 on a projection of 14.00", w, l,
        "Tony Pollard 38.00, Caleb Williams 25.12 and Trey McBride 25.10 for Kent Frenger, with Kenneth Walker "
        "III at 7.70. Geoff Cavender got 22.90 from Quinshon Judkins and 22.70 from Amon-Ra St. Brown, started "
        "Carnell Tate for 7.40 with Josh Jacobs's 17.60 on his bench, and his Ravens defense, signed this week, "
        "scored minus three.", SCALE))
    parts.append(gil(
        "Kent Frenger wins 133.52 to 110.86 and is 5 and 2, four straight wins, the second seed on the points "
        "tiebreaker. He has "
        "beaten Geoff Cavender in all three meetings. Pollard's 38.00 is the biggest start in the league this "
        "week against its projection. Frenger released Tyler Shough this week for T.J. Hockenson, so Boomer's "
        "call that he would start Shough is wrong by the whole roster."))
    parts.append(boomer(
        "I bet the man would start his quarterback and he cut him. I cannot win a call on Kent Frenger. I bet on "
        "Shough's points, Kent sat him. I bet on Kent's finger, Kent cut him. If I bet on Kent showing up "
        "Sunday, the man will move the game. The reigning champ has won four straight with Caleb Williams at "
        "quarterback, which is how you know the rings are real. Nobody fakes that."))
    parts.append(gil(
        "In fairness to Geoff Cavender, Judkins and St. Brown were 45.60 between them and he is 5 and 2 with a "
        "share of first place. He signed the Ravens defense this week for the Rams, who scored 1.00. The Ravens "
        "scored minus three. Jordan Love was projected for 21.10 and scored 16.96."))
    parts.append(boomer(
        "Geoff signed a defense that scored negative three and benched a running back who scored seventeen and "
        "a half. He is 5 and 2 and the whole league has outscored him more often than not. Geoff, the standings "
        "say you are a contender. The scoreboard says you are a rumor. One of them is lying, and I have been "
        "doing this for forty years and it is never the scoreboard."))

    # ---- HALFTIME (new this week)
    parts.append('<h2 id="halftime">Halftime</h2>')
    parts.append(gil(
        "Seven games played, seven to go. For the first time this season the booth opens the archive: every "
        "season on record in this league, 2009 through 2025, seventeen of them, and what the standings looked "
        "like after Week 7 against how the year ended. Then the luck board, which is each owner's actual "
        "record beside his all-play record, meaning his score against every other team, every week. The gap "
        "between the two is luck, counted in wins."))
    tiles = [
        ("4 of 17", "halfway leaders, meaning the team in first place on record after Week 7, who went on to win the title. Spencer Lentz owns two of the four, 2010 and 2019."),
        ("16 of 17", "halfway leaders who at least made the playoffs. The one who did not: Kent Frenger, 5 and 2 in 2023."),
        ("31 of 44", "teams with exactly five wins at halftime that made the playoffs, 70%. Eleven of them won the title."),
        ("23 of 42", "teams with four wins at halftime that made the playoffs, 55%. Three went on to win it."),
        ("3 of 31", "teams with two wins at halftime that made the playoffs. One won the title: Casey Couture, 2 and 5 in 2011."),
        ("0 of 14", "teams with one win at halftime that made the playoffs."),
    ]
    parts.append(halftime_tiles(tiles))
    rows = []
    for c in HALF["current"]:
        rows.append({"display": c["display"], "team": c["team"], "w": c["w"], "l": c["l"], "pfRank": c["pfRank"],
                     "allPlayW": c["allPlayW"], "allPlayL": c["allPlayL"], "luck": c["luck"],
                     "me": False})
    parts.append(halftime_board(rows,
        "The luck board, through Week 7, in standings order. All-play is your score against every other team, "
        "every week, 77 games each. Lucky means more wins than that pace, counted in wins; even means within a "
        "quarter of a win either way. Casey Couture's 23 and 54 is worth about two wins. He has four."))
    parts.append(gil(
        "Spencer Lentz is first on record and first on points. The team leading on record at halftime has won "
        "four of seventeen titles, and the team leading on points has won six. Spencer has led the points at "
        "halftime five times before this one and won twice from there, in 2010 and 2016; his 2019 title came "
        "from first on record with Ryan Couture ahead of him on points. Kent Frenger is "
        "second, and in 2023 he was the only halfway leader in the history of this league to miss the "
        "playoffs. Last year he was 4 and 3 and sixth at halftime, and he won it all."))
    parts.append(boomer(
        "Kent Frenger is the only man alive who has missed the playoffs from first place and won the title from "
        "sixth. The man is a cautionary tale with a ring. And Spencer, two of the four leaders who finished "
        "the job are you, and three of your five points-leader seasons ended with somebody else wearing the "
        "ring. First place in October is a reservation, Gil. The table still goes to whoever shows up in "
        "December."))
    parts.append(gil(
        "Casey Couture is 4 and 3 with the fewest points in the league. There is exactly one precedent. In 2022 "
        "Doug Fields was 4 and 3 at halftime with the fewest points of all twelve teams, and he made the "
        "playoffs. Casey also owns the only title ever won from two wins at halftime: 2 and 5 in 2011, ninth "
        "of ten, champion."))
    parts.append(boomer(
        "Casey has scored fewer points than anybody and he is tied with the fourth seed, and the one man who ever did that and "
        "made the playoffs is Doug Fields, who is currently the flattest line in league history. Casey, your "
        "entire playoff case is a Doug Fields season. You are planning a wedding around somebody else's "
        "weather."))
    parts.append(gil(
        "Scott Howard is 2 and 5 with the fifth-most points in the league. Against every other team every week "
        "he is 37 and 40, so his record is about a win and a half worse than his scores. Teams with two wins "
        "at halftime have made the playoffs three times in thirty-one tries. Mama Beth is 1 and 6, and no team "
        "with one win at halftime has ever made it, in fourteen tries. She has won three titles here, and in "
        "every one of those years she was 5 and 2 at the break."))
    parts.append(boomer(
        "Scott Howard needs the 2011 Casey Couture miracle and he needs it from eleventh. Mama Beth needs "
        "something that has never happened in this league, and I have watched her claim a receiver and bench "
        "him for 23, so I am not ruling it out. She has done the impossible before, Gil. Usually to herself."))
    parts.append(gil(
        "Geoff Cavender is the luckiest man in the top three, 5 and 2 on a 36 and 41 all-play, about a win and "
        "three quarters ahead of his scores. And one more from the archive: the highest Week 7 score in league "
        "history is 185.00, Spencer Lentz in 2010. The lowest is 37.84, Adam Hershberger in 2019. Hershberger "
        "scored 115.80 this Week 7 and won."))
    parts.append(boomer(
        "Adam Hershberger holds the record for the worst Week 7 anybody has ever played here, 37.84. This year "
        "he tripled it. That is growth, Gil. Seventeen years from now somebody is going to read this archive "
        "and find out Geoff Cavender was 5 and 2 with a losing all-play record, and they are going to assume "
        "the data is wrong. It is not. It is just Geoff."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls came due. Four right, eight wrong. Season record 31 and 41, a .431 batting average, which "
        "in baseball is a statue and in this booth is a Tuesday. I bet on a man to start a quarterback and he cut the "
        "quarterback. I bet on Mama Beth against a man with no quarterback and the man went and found one. "
        "Every call is below, in ink."))
    parts.append(graded_list([
        ("Momma's Boys", "Mama Beth beats Adam Hershberger.", "WRONG",
         "Lost by 10.20 with a 23-point receiver on her bench that she claimed this week. I said if this one "
         "missed I was done picking the parents. I am a man of my word, and the word lasted until the bottom "
         "of this page."),
        ("Holy Rollers", "Malik Nabers clears 20 again for Adam Hershberger.", "WRONG",
         "17.60. Jameson Williams carried him instead with 23.60. Right about Adam getting carried, wrong about "
         "who was doing the lifting."),
        ("Cosby Copperheads", "Doug Fields starts Tre Tucker in Week 7.", "RIGHT",
         "Started, 21.80. Doug listened to me and set a perfect lineup and won. Doug, this is a trap and you "
         "walked straight into it: now I expect it."),
        ("DA The Badenov's", "DA beats Doug Fields with Aaron Rodgers at quarterback.", "WRONG",
         "Rodgers started and scored 13.08. DA scored 83 and lost. I praised the elder for planning ahead. The "
         "plan was Aaron Rodgers. I should have read it twice."),
        ("Balls Deep", "Spencer Lentz beats Ryan Reed by twenty or more.", "WRONG",
         "Won by 16.46. Three and a half points short, and Nico Collins scored 1.60 in his lineup. Spencer, you "
         "cost me a call with your own receiver and I am holding you to it."),
        ("BearDown", "Jaxon Smith-Njigba clears 20 again for Ryan Reed.", "RIGHT",
         "29.80. The one man on that roster you can set a watch by, and he did it while his owner benched a "
         "28-point quarterback. I got the easy half."),
        ("One Under akaThe Mulligan", "Casey Couture beats Adam Calvelage for the sixth straight time.", "RIGHT",
         "By 2.36, with the fewest points in the league and a zero-point defense he signed on purpose. I bet on "
         "the family and the family came through. The family always comes through."),
        ("An alBum Cover", "Brock Purdy clears 20 for Adam Calvelage.", "WRONG",
         "12.02. I said the quarterback decision would make itself. It did, and it made the wrong one."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert clears 120 in Week 7.", "WRONG",
         "100.82 with Gibbs and Goff back in the lineup. I told him to put the flyer guys back in the drawer. He "
         "did. The Lions showed up and scored 38.82 between them, and it still was not enough."),
        ("The Scranton Strangler", "Scott Howard beats Scott Reisert.", "RIGHT",
         "By 34.86 with the high score of the week. I bet on the law of averages and for once it answered the "
         "phone."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender beats Kent Frenger for the first time.", "WRONG",
         "Lost by 22.66. Now 0 and 3 against Kent. I said Geoff would prove one of us wrong. He picked me."),
        ("Berlin Blitz", "Kent Frenger starts Tyler Shough in Week 7.", "WRONG",
         "Kent cut Shough this week. I bet on the man's finger and he used it to delete the player. I am 0 "
         "and 2 on Tyler Shough since Week 5, and the quarterback is not even on the team anymore."),
    ]))
    parts.append(gil(
        "Four right, eight wrong. Twelve new ones for Week 8, one per team. The Saints, Giants, 49ers and Texans "
        "have the week off, so Brock Purdy, Christian McCaffrey, C.J. Stroud, Nico Collins, Malik Nabers and "
        "Chris Olave are all out of lineups this week."))
    parts.append(calls_list([
        ("The Scranton Strangler", "Scott Howard beats Spencer Lentz.",
         "Howard just scored 136 and Spencer's receivers are Tee Higgins and the Texans' bye week. Spencer leads "
         "the series 5 and 4, so it is close to a coin flip, and the coin is 2 and 5 with the fifth-most "
         "points in the league. I am betting on the weather system."),
        ("Balls Deep", "Drake Maye clears 25 again for Spencer Lentz.",
         "30.44 this week, 23.80 the week before. Stroud is on bye, so for once there is no 25 waiting on "
         "Spencer's bench to embarrass him. Maye is the one thing on that roster that keeps showing up on "
         "the right side of the line."),
        ("Holy Rollers", "Adam Hershberger beats DA for the fourth straight time.",
         "Three straight over DA, Trevor Lawrence back from the bye, and DA just scored 83 without Josh Allen, who "
         "is also back this week. Malik Nabers is on bye, so Jameson Williams has to do it twice. The "
         "streak against a Couture never ends well, and I am betting it lasts one more week."),
        ("DA The Badenov's", "Josh Allen clears 25 for DA.",
         "Allen is back from the bye, and DA scored 83 without him with Aaron Rodgers at 13.08. Allen gave DA "
         "33.50 in Week 5 and 18.30 in Week 6. DA does not need a new lineup. He needs the one he had before "
         "the Bills took the week off, and Sunday he gets it back."),
        ("Momma's Boys", "Mama Beth starts Omar Cooper Jr. in Week 8.",
         "She claimed him, she benched him, he scored 23. I am betting she learned the lesson the same way I "
         "learn mine: the second time."),
        ("BearDown", "Ryan Reed starts Bo Nix in Week 8.",
         "Twenty-eight on the bench behind a quarterback he signed this week, in a loss by sixteen. Cam "
         "Skattebo is on bye, so Ryan has fewer places to hide his points. Start the man, Ryan. I am not "
         "asking him to score. I am asking him to be in the room."),
        ("An alBum Cover", "Adam Calvelage beats Doug Fields.",
         "Fields has scored between 92 and 106 every week of his life, and Adam has cleared 100 in four of "
         "seven. Purdy is on bye, so Jayden Daniels starts, and Daniels has 35.26 and 24.00 in his last two "
         "games on this roster, one of them from the bench. Adam cannot sit him this week. That is the whole "
         "bet."),
        ("Cosby Copperheads", "Doug Fields scores between 92 and 106 again.",
         "Seven for seven. The tightest start in league history. I am betting the dial tone holds, and if it "
         "does not, I want it on the record that I was there the day Doug Fields did something."),
        ("Berlin Blitz", "Kent Frenger beats Casey Couture.",
         "Kent leads the series 17 and 14 and has won the last two, including a playoff game last December. "
         "He has won four straight and Casey has the fewest points in the league. I have lost three calls in a "
         "row on Kent by betting on his lineup. This time I am betting on the man across from him, and the man "
         "across from him is Casey. I know."),
        ("One Under akaThe Mulligan", "Casey Couture leaves under five on his bench again.",
         "3.80 this week, 1.30 the week before, after 110 left behind in the first five weeks. The lineups have "
         "been clean since the family Sunday. Chris Olave "
         "is on bye, so the roster gets smaller and the lineup gets easier. I will take the half I can win."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender beats Scott Reisert.",
         "Reisert leads the series 2 and 1 but has lost three of four, and Geoff is 5 and 2 with the universe on "
         "retainer. Josh Jacobs comes off the bench or Geoff gets another seventeen-point reminder. I am "
         "betting on the luck, because it has not run out yet and I want to be there when it does."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert leaves under five on his bench in Week 8.",
         "He left 7.30 this week, all of it Rico Dowdle behind Kendre Miller. George Kittle is on bye, so the "
         "decisions get simpler. Scott counts the silverware every week, Gil. This week I am betting he counts "
         "it right."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, "
        "then by size. When an owner already holds one, the next name in line takes it."))
    parts.append(award(
        "good", "Owner of the Week", "Scott Howard · The Scranton Strangler",
        "135.68, the high score of the week, from eleventh place. It beats all eleven teams. Bucky Irving 26.50, "
        "the Buccaneers defense 26.00 on a projection of 4.65, Dak Prescott 23.28. His first Owner of the Week "
        "after three Sits, a Waste and a Worst.",
        "Scott Howard has five pieces of bad hardware on the shelf and now one good one. It is the first trophy "
        "in that house that is not a warning. Enjoy it, Scott. Your defense outscored your tight end by "
        "23.80, and the defense is the one you forgot to bench."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "DA · DA The Badenov's",
        "83.28, the low score of the week, which loses to all eleven teams. Aaron Rodgers 13.08 on a projection "
        "of 20.53, Xavier Worthy 2.60, and Ryan Fitzgerald, signed this week, 1.00. Two weeks ago DA scored "
        "151.10.",
        "The man signed a kicker this week and the kicker made one point. One. DA's Week 7 was a trip to the "
        "store for milk that ended with the car in a lake. He is still second in the league in points, which "
        "means the first five weeks were real and the last two are the sequel nobody asked for."))
    parts.append(award(
        "good", "Start of the Week", "Kent Frenger · Tony Pollard, 38.00",
        "Projected for 14.00, so 24.00 over, the biggest margin over projection by any starter in the league "
        "this week. Scott Howard's Buccaneers defense was 21.35 over, and Howard already has a trophy.",
        "Kent cut his quarterback and started a running back for 38. The reigning champ makes examples, Gil. "
        "Pollard was projected for fourteen. Everybody else who started a running back projected for fourteen "
        "got fourteen and a long drive home."))
    parts.append(award(
        "bad", "Sit of the Week", "Ryan Reed · Bo Nix, 28.18 on the bench",
        "J.J. McCarthy, signed this week, started in his place for 10.18, a swing of 18.00 in a game Reed lost by "
        "16.46. It is the biggest benching in the league this week that flipped its game by itself. Mama Beth's "
        "Omar Cooper Jr. for Justin Jefferson was a 16.60 swing in a loss by 10.20, and it was second.",
        "Ryan signed a quarterback and the quarterback's first act as a member of BearDown was to lose Ryan the "
        "game from the field while Bo Nix won it from the bench. Ryan, you benched the result. Somewhere there "
        "is a man who locks a gate on a field with no fence, and this week that man is you."))
    parts.append(award(
        "bad", "Waste of the Week", "Spencer Lentz · 4.80 left behind, and he won",
        "Tucker Kraft scored 12.80 on his bench behind Brock Bowers's 10.30, a 2.50 swing, and Bowers at flex "
        "over Chuba Hubbard's 8.00 is the other 2.30. Kent Frenger left 9.60 and Scott Howard 7.30, and both "
        "already hold a trophy.",
        "Four point eight, Gil. It is the smallest Waste anybody has won all season and Spencer still got it, "
        "because he is in first place and nobody else was left. He left Stroud on the bench for the second "
        "straight week, 25.98 and then 16.52, and both weeks Stroud outscored half the men in his lineup. "
        "Spencer, your bench quarterback outscored six of the eleven starting quarterbacks in this league this "
        "week. Six men would have started your backup, and you are the one who will not."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All twelve of you, every week, all season. Scott Howard leads at 170.80 and added 7.30 in a week he won "
        "by 35, so for once the points on his bench were decorative. Ryan Reed added 27.50 and jumped to "
        "118.74, and his 27.50 is the biggest entry this week that cost a game. Scott Reisert "
        "is still the cleanest man in the league at 36.00, and he is 4 and 3, so cleanliness, Gil, is next to "
        "nothing."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 7, season_note=(
        "Season totals come from the season ledger through Week 7. Scott Howard leads at 170.80, Ryan Reed is "
        "second at 118.74, Casey Couture third at 115.28. Scott Reisert has left the fewest, 36.00.")))
    parts.append(gil(
        "Two benches cost a game this week: Ryan Reed left 27.50 and lost by 16.46, and Mama Beth left 16.60 and "
        "lost by 10.20. Doug Fields left nothing, and won. Adam Calvelage left 0.90 and lost by 2.36, which is "
        "the one bench in the league this week that was close to the margin and still short of it."))
    parts.append(boomer(
        "Two losses, two benches, and both of them were a player the owner went out and got this week and then "
        "would not look at on Sunday. These two did the hard part, Gil. They scouted, they claimed, they made "
        "room. Then they got to the easy part and sat down."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Adam Hershberger claiming Kyler Murray, who started for "
        "13.90, for Dameon Pierce. With Trevor Lawrence on bye and no other "
        "quarterback on the roster, the move filled an empty slot, and Hershberger won by 10.20."))
    parts.append(gil(
        "<strong>Worst move:</strong> Ryan Reed releasing Jacoby Brissett, who scored 16.48, to sign J.J. "
        "McCarthy, who started and scored 10.18. A 6.30-point swing against him, in a game he lost by 16.46, "
        "with Bo Nix on his bench for 28.18 the whole time."))
    parts.append(boomer(
        "Ryan needed one quarterback. He had Nix. He cut Brissett, who outscored the man he replaced him with, "
        "and then he benched Nix behind the man he signed, which cost him eighteen. Eighteen points of "
        "self-inflicted quarterback, Gil, in a loss by sixteen."))
    parts.append(gil(
        "Twenty moves went through. Scott Reisert made five: Chris Boswell for Nick Folk at kicker, 11.00 for "
        "11.00; the Dolphins defense for the Patriots, which gained him 4.00; Roschon Johnson for Jameis "
        "Winston; DeMario Douglas for Terry McLaurin; and Jaylin Noel for Austin Ekeler. Kent Frenger shuffled "
        "Dameon Pierce and Chris Godwin Jr. through the same slot and ended with Godwin, who scored 4.70 in "
        "his lineup. Casey Couture released the Colts defense, who scored 8.00, for the Titans, who scored "
        "zero."))
    parts.append(boomer(
        "Scott Reisert made five moves and the biggest one was worth four points. The man alphabetized his "
        "roster, Gil. Kent signed Pierce, cut Pierce, signed Godwin, and Godwin scored 4.70, which "
        "is the sound of a man changing his mind in a revolving door. And Casey cut an eight for a "
        "zero and won. In this league the moves do not matter. The last name does."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "DA at Adam Hershberger, Mama Beth at Ryan Reed, Doug Fields at Adam Calvelage, Spencer Lentz at Scott "
        "Howard, Casey Couture at Kent Frenger, and Scott Reisert at Geoff Cavender. The Saints, Giants, 49ers "
        "and Texans have the week off. Carolina plays at Green Bay on Thursday night."))
    parts.append(boomer(
        "First place goes to Scranton, where Scott Howard is 2 and 5 and just scored 136, and I have taken Howard, "
        "because somebody has to and Spencer fell three and a half short of my number this week with a "
        "receiver who scored 1.60. Hershberger gets DA for a fourth straight, and if he wins it, the Coutures "
        "hold a meeting. Mama Beth starts Cooper this "
        "week or I eat the call on the air, which I have done, Gil, and it tastes like a laminated card. Seven "
        "down, seven to go, and the three men at 5 and 2 are the reigning champ, the points leader, and a man "
        "the whole league has outscored. One of those is not like the others, and he is sitting third with a "
        "share of first."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 7, HEADLINE, DEK, build(), META, "dlffl-week-7.png", nav=NAV,
        published="2026-10-27T11:00:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "dlffl", "week-7.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
