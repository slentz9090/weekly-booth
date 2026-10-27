"""Friends of Herb, Week 7. Editorial. The halfway mark.

Boomer runs ULTRA SPICY (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis, clean language, roast cap and Gil defenses apply. Herb content gets reverence.

NEW THIS WEEK: HALFTIME, built from the all-time log (gen2/halftime.py -> docs/data/foh_halftime.json):
what the standings after Week 7 have meant in every ESPN-era season on record (2011 to 2025, fourteen of
them), the luck board (actual record vs all-play, byes excluded), and one random stat from the archive.

Outlier engine, Week 7, HEADLINE tier: Aron Rogers has beaten Aaron Jezioro nine straight times and leads
the series 13-3 (a 1 in 47 series by coin flip); the margin, 75.30, is the 45th-biggest in 1,335 games
since 2011. Support: Michael Turner 1-5 on a 28-32 all-play (1.8 wins unlucky, the unluckiest in the
league); Rogers's 152.12 is the 6th-best game of his 164; Davis's 152.68 beat it by 0.56 for the high
score; Kelly's score has risen six weeks running, tying the longest such run on record; Turner cut Cam
Skattebo for Tre Tucker, Kelly signed Skattebo, they played each other and each man benched his new man
for about twenty; Billy Norton's bench scored zero because every man on it was on bye or out.

Verified against foh_wk7_facts.json, foh_season.json, foh_halftime.json and gen2/data/foh_games.json.
"""
import os

import booth
from booth import award, boomer, byecard, calls_list, gil, graded_list, halftime_board, halftime_tiles, jump, ledger, mcard
from compute import by_owner, ledger_rows, load

NAV = (
    '<nav class="nav" aria-label="Sections"><ul>'
    '<li><a href="#board">The Scoreboard</a></li>'
    '<li><a href="#halftime">Halftime</a></li>'
    '<li><a href="#freiermuth">The Freiermuth Rule</a></li>'
    '<li><a href="#calls">On The Record</a></li>'
    '<li><a href="#hardware">The Hardware</a></li>'
    '<li><a href="#ledger">The Bench Ledger</a></li>'
    '<li><a href="#wire">The Waiver Wire</a></li>'
    '<li><a href="#next">Next Sunday</a></li></ul></nav>'
)

FACTS = load("foh_wk7_facts.json")
SEASON = load("foh_season.json")
HALF = load("foh_halftime.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 158.78

HEADLINE = "Aron Rogers Beat Aaron Jezioro By 75 Points. It Was The Ninth Straight."
DEK = (
    "Halftime in Friends of Herb. Aron Rogers set a perfect lineup, scored 152.12, beat Aaron Jezioro 152.12 to "
    "76.82 for the ninth straight time, and finished second in the league for the week by 0.56. Michael Turner "
    "cut Cam Skattebo and signed Tre Tucker. Ryan Kelly signed Skattebo. They played each other, each man "
    "benched his new man for about twenty points, and Kelly won his first game of the year. The booth opens the "
    "archive on what the halfway mark has meant since 2011, and Herb is in it."
)
META = (
    "Gil and Boomer call Week 7 of Friends of Herb, the halfway mark: Aron Rogers beats Aaron Jezioro by 75 for "
    "the ninth straight time, Turner and Kelly swap a running back and both bench twenty, Ryan Kelly's first "
    "win, Matt Davis starts Joe Burrow this time, and a new segment on what the halfway standings have meant "
    "in every season since 2011."
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

    # ---- 1. nine straight
    w, l = card_rows("Aron Rogers", "Aaron Jezioro")
    parts.append(mcard(
        "m-rogers", "Rogers's ninth straight over Jezioro, by 75.30, with a perfect lineup", w, l,
        "Tony Pollard 37.00 on a projection of 13.64, Jared Goff 23.02, CeeDee Lamb 21.90 and Amon-Ra St. Brown "
        "21.70 for Aron Rogers, who left nothing behind. Aaron Jezioro started Jalen Coker for 1.40 and the "
        "Ravens defense for minus two, with Ja'Marr Chase's 14.70 on his bench.", SCALE, key=True))
    parts.append(gil(
        "Aron Rogers wins 152.12 to 76.82 and is 5 and 2. It is the ninth straight time he has beaten Aaron "
        "Jezioro, and he leads the series 13 and 3. If every game were a coin flip, a series that lopsided "
        "comes up about once in 47 tries. The "
        "margin, 75.30, is the 45th-biggest in 1,335 games in this league since 2011. Rogers set a perfect "
        "lineup for the second week in a row and has left 31.08 on his bench all year, the fewest in the "
        "league."))
    parts.append(boomer(
        "Thirteen and three. Nine straight. Seventy-five points. Aron Rogers does not have a rivalry with Aaron "
        "Jezioro, Gil. He has a standing appointment, and Jezioro keeps showing up early. And the thing about Rogers is the bench: 31 points left "
        "behind all season, in seven weeks. Some men in this league leave 31 by halftime Sunday. Rogers sets a "
        "lineup like a man folding a flag."))
    parts.append(gil(
        "In fairness to Aaron Jezioro, Jaylen Warren gave him 17.20 and Will Reichard 13.00, and Brock Purdy was "
        "projected for 24.69 and scored 14.02. His 76.82 is the 40th-worst of his 238 games here. He started "
        "Coker over Chase, a 13.30 swing, and the Ravens defense cost him two more."))
    parts.append(boomer(
        "He benched Ja'Marr Chase for Jalen Coker. On purpose. He looked at the best receiver in the sport and "
        "the fourth receiver in Carolina and said, I like the kid's energy. Aaron, Chase would not have saved "
        "you. You lost by seventy-five. But a man drowning in the ocean should still not take off his shoes."))

    # ---- 2. the running back they passed between them
    w, l = card_rows("Ryan Kelly", "Michael Turner")
    parts.append(mcard(
        "m-kelly", "Kelly's first win: he benched the running back Turner cut, Turner benched the receiver he cut him for", w, l,
        "Caleb Williams 27.12, Emanuel Wilson 20.00 and Blake Corum 16.60 for Ryan Kelly, with Cam Skattebo, "
        "signed this week, on his bench for 20.60 behind Tyler Allgeier's 6.40. Michael Turner got 17.60 from "
        "Josh Jacobs, also signed this week, started Garrett Wilson for 3.60, and left Tre Tucker, also signed "
        "this week, on his bench for 20.80.", SCALE))
    parts.append(gil(
        "Ryan Kelly wins 117.12 to 92.58 for his first win of the season and is 1 and 5. The order of events, "
        "from the league's transaction log: Michael Turner released Cam Skattebo to claim Tre Tucker. Kelly "
        "signed Skattebo and released Kenny Gainwell. Then the two of them played each other, Turner benched "
        "Tucker for 20.80, and Kelly benched Skattebo for 20.60. Kelly leads the series 16 and 10."))
    parts.append(boomer(
        "Turner cut a man, Kelly picked him up, and then both of them sat both of them. Forty-one points on two "
        "benches, in the same game, and it is the same transaction. That is not two lineup mistakes, Gil. That "
        "is one mistake with a layover. Ryan Kelly has four titles here and he just won his first game of the "
        "year with the guy he signed to start sitting next to him in street clothes."))
    parts.append(gil(
        "In fairness to Ryan Kelly, his score has gone up five weeks in a row: 52.52, 54.52, 67.78, 76.86, 87.70 "
        "and now 117.12, six straight scores each higher than the last, which ties the longest run of "
        "week-over-week improvement by any owner on record here. For Michael Turner, Josh Jacobs scored 17.60 on his first week in the lineup, and against the "
        "whole league this season Turner is 28 and 32, so his 1 and 5 is almost two wins worse than his "
        "scores. That is the unluckiest record in the league."))
    parts.append(boomer(
        "Six straight scores, each one higher than the last, from 52 to 117. Ryan Kelly is the only man in this "
        "league whose season reads better upside down. He still has the fewest points in the league. He is "
        "just getting there slower than everybody else and from much further away. And Turner: 1 and 5 on an "
        "all-play record that is almost even. Turner is cursed, Gil, which is worse than bad, because you "
        "cannot fix cursed on the waiver wire, and he has tried, five times this week."))

    # ---- 3. Burrow, this time
    w, l = card_rows("Matt Davis", "Rahul Pahuja")
    parts.append(mcard(
        "m-davis", "Davis's 152.68, the high score of the week by 0.56, with Joe Burrow in the lineup this time", w, l,
        "Joe Burrow 36.88, Bucky Irving 25.50 and Jameson Williams 23.60 for Matt Davis, with Matthew Stafford's "
        "23.50 on his bench. Rahul Pahuja got 28.80 from Jaxon Smith-Njigba and 23.70 from Luther Burden III, "
        "started Bryce Young for 7.42 with C.J. Stroud's 20.52 on his bench, and started Roschon Johnson, "
        "signed this week, for 1.30.", SCALE))
    parts.append(gil(
        "Matt Davis wins 152.68 to 104.32 and is 5 and 2, first place, with the most points in the league at "
        "904.52. It is the high score of the week by 0.56 over Rogers. He has beaten Rahul Pahuja three straight "
        "times and leads the series 13 and 8. In Week 3 Davis benched Burrow for Stafford and lost by 0.76. "
        "This week Burrow started and scored 36.88, the most by any quarterback in the league."))
    parts.append(boomer(
        "Four weeks ago, in Week 3, the man asked a chatbot who to start, sat Burrow for Stafford, and lost by "
        "less than a point. This week "
        "he started Burrow himself and scored 152. Matt learned the lesson the way this league learns every "
        "lesson, Gil: a month late and by less than a point. And Rahul: Stroud on the bench for 20, Bryce Young in the lineup for seven, and he released a "
        "tight end who scored ten to sign a running back who scored one. Rahul is 4 and 2, and the standings "
        "are the only thing on his team that has not been benched."))
    parts.append(gil(
        "In fairness to Rahul Pahuja, Smith-Njigba and Burden were 52.50 between them, and he is 4 and 2 with a "
        "winning all-play record. He released Harold Fannin Jr., who scored 10.10, and started Isaiah Likely at "
        "tight end for 2.20. Davis left 6.10 behind, Quinshon Judkins at 22.90 behind Jahmyr Gibbs at 16.80, and "
        "Gibbs was projected for 24.38."))
    parts.append(boomer(
        "Matt Davis has scored 170 and 71 and 152 in his last three games. The man has two settings and neither "
        "one is a dimmer. Rahul, you have left 133 points on your bench this season, second in the league, and "
        "this week the answer was Stroud, and Stroud was on your roster, and you knew his name. You did not "
        "need a chatbot. You needed to read your own depth chart out loud."))

    # ---- 4. the bench that scored zero
    w, l = card_rows("Spencer Lentz", "Billy Norton")
    parts.append(mcard(
        "m-lentz", "Spencer by 38.24, and Norton's entire bench scored zero", w, l,
        "Drake Maye 32.44, Tee Higgins 25.80 and Javonte Williams 23.50 for Spencer Lentz, who started Nico "
        "Collins for 1.60 and Derrick Henry for 5.40 and left Colston Loveland's 16.40 behind. Billy Norton set "
        "a perfect lineup: James Cook III, Omarion Hampton, Ladd McConkey, DJ Moore and Stefon Diggs were all on "
        "his bench, and all five scored zero.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 115.24 to 77.00 and is 5 and 2, four straight wins, second place on points. Norton "
        "had won their last three meetings and still leads the series 13 and 10. Norton's 77.00 was a perfect "
        "lineup, since the five men on his bench were on bye or out and scored nothing between them. It is the "
        "21st-worst score of his 209 games here. Spencer left 11.30 behind, Loveland behind Tucker Kraft, and "
        "Boomer's call was under ten."))
    parts.append(boomer(
        "Billy Norton played a perfect lineup and scored 77. Think about that. He could not have done a single "
        "thing differently and he still lost by 38. His bench was five men and a folding chair. Billy has four "
        "titles and 1 and 5, and against the whole league he is 12 and 48, and the only man below him is Ryan "
        "Kelly, who just won. Billy is having a bad year with no witnesses, Gil."))
    parts.append(gil(
        "In fairness to Billy Norton, Kirk Cousins gave him 24.40 and Malik Nabers 16.60, and he scored 96.22 "
        "last week in his first win. His 77.00 was the first clean bench of his season. For Spencer, Collins "
        "and Henry were 7.00 between them in his lineup, two starters outscored by Billy's kicker."))
    parts.append(boomer(
        "Spencer started a receiver for 1.60 and a running back for 5.40 and won by 38, because Billy was "
        "playing with a bench that had been evacuated. Spencer, you left Loveland on the bench for 16, which is "
        "a tight end outscoring the one you started by 3.60 while you were busy starting a receiver for 1.60. Four straight wins, second in points, and you still cannot get through a Sunday "
        "without leaving a tight end in the lot. You beat Billy. Next week it is Rahul, who has 133 on his "
        "bench, so between you there will be enough points sitting down to field a third team."))

    # ---- 5. the quarterback he signed for one week
    w, l = card_rows("Eric Olson", "Michael Smith")
    parts.append(mcard(
        "m-olson", "Olson by 14.00 with a quarterback he signed this week, and two perfect lineups", w, l,
        "Bo Nix 28.18 on a projection of 18.95, Trey McBride 24.10 and Ollie Gordon II 18.80 for Eric Olson, "
        "who left nothing behind. Michael Smith got 29.28 from Dak Prescott and 18.00 from Jonathan Taylor, "
        "left nothing behind either, and his two running backs behind Taylor scored 11.70 between them.", SCALE))
    parts.append(gil(
        "Eric Olson wins 118.78 to 104.78 and is 5 and 2, fourth place. Josh Allen had the week off, so Olson "
        "released Travis Etienne Jr. and signed Bo Nix, who started and scored 28.18, the biggest swing of any "
        "move in the league this week. Both men set perfect lineups. Olson leads the series 3 and 2 and has "
        "won the last two."))
    parts.append(boomer(
        "Olson needed a quarterback for one week and signed one who scored 28 on a projection of 19. The man "
        "borrows a quarterback better than most of this league drafts one. Meanwhile Michael Smith is 4 and 2 on a 31 and 29 "
        "all-play, which is a long way of saying the league has outscored him about half the time and he "
        "keeps winning anyway. Michael Smith is the only man in the league whose schedule deserves a trophy."))
    parts.append(gil(
        "In fairness to Michael Smith, Prescott's 29.28 was the third-best quarterback score in the league this "
        "week, and he has left 55.64 behind all year, the second-fewest in the league, with 28.20 of that on "
        "his bye week. Aaron Jones Sr. was projected for 11.14 and scored 3.10."))
    parts.append(boomer(
        "Two perfect lineups, 27 points left behind in the six games he played, and 4 and 2. Michael Smith has "
        "the discipline of a monk and the roster of a monastery. Everybody shows up on time and nobody scores. Eric, you did the Bo Nix thing "
        "once. Do not get a taste for it. The last man in this league who got clever with one-week "
        "quarterbacks asked a chatbot, and the chatbot got a nickname."))

    # ---- 6. the bye
    d = T["Bob Dorsch"]
    parts.append(byecard(
        "m-bye", "Dorsch on the bye, 104.26, and 24.60 left behind",
        {"team": d["name"], "owner": "Bob Dorsch", "score": d["score"], "left": d["left"]},
        "Zay Flowers 26.70 and Jordan Love 20.96 for Bob Dorsch, who started Germie Bernard for 4.20 with "
        "Rhamondre Stevenson's 21.00 and Braelon Allen's 18.40 on his bench. He released Pat Freiermuth this "
        "week. Bye-week scores never take a trophy and do not count in all-play.", SCALE))
    parts.append(gil(
        "Bob Dorsch had the week off and scored 104.26, which would have beaten three of the ten teams that "
        "played. He left 24.60 behind, the most in the league this week: Stevenson for 21.00 and Allen for "
        "18.40 sat while Bernard started for 4.20. Boomer's call was that he would "
        "start Bernard, bye or no bye, and he did. Dorsch is 2 and 4 and had lost two straight going into "
        "the bye."))
    parts.append(boomer(
        "I called it and I am not proud of it. Last week Bob benched Bernard and Bernard scored twenty. This week "
        "he started Bernard, Bernard scored four, and Stevenson sat there for twenty-one. Bob is one week "
        "behind his own roster, every week, and this time it did not even count. He practiced the mistake. "
        "On a week off. And he cut Pat Freiermuth, Gil, the man the rule is named for, so the rule is now a "
        "memorial. We will get to that."))

    # ---- HALFTIME (new this week)
    parts.append('<h2 id="halftime">Halftime</h2>')
    parts.append(gil(
        "Seven weeks played, seven to go, and for the first time this season the booth opens the archive: every "
        "ESPN-era season on record in this league, 2011 through 2025, fourteen of the fifteen (2018 has no "
        "bracket on record), and what the standings "
        "looked like after Week 7 against how the year ended. Then the luck board, which is each owner's "
        "actual record beside his all-play record, meaning his score against every other team, every week, "
        "with bye weeks left out. The gap between the two is luck, counted in wins."))
    parts.append(halftime_tiles([
        ("4 of 14", "halfway leaders, meaning the team in first place on record after Week 7, who went on to win the title. Matt Davis is one, 6 and 1 in 2023."),
        ("13 of 14", "halfway leaders who at least made the playoffs. The one who did not: Aron Rogers, 6 and 1 in 2024."),
        ("36 of 38", "teams with five or more wins at halftime that made the playoffs. The two misses were both Aron Rogers, 2023 and 2024."),
        ("18 of 34", "teams with four wins at halftime that made the playoffs, 53%. Five of them won the title, more than any other group."),
        ("1 of 29", "teams with two wins at halftime that made the playoffs: Aron Rogers, 2 and 5 in 2020."),
        ("1 of 13", "teams with one win at halftime that made the playoffs: Herb Schumann, 1 and 6 in 2013."),
    ]))
    rows = []
    for c in HALF["current"]:
        rows.append({"display": c["display"], "team": c["team"], "w": c["w"], "l": c["l"], "pfRank": c["pfRank"],
                     "allPlayW": c["allPlayW"], "allPlayL": c["allPlayL"], "luck": c["luck"], "me": False})
    parts.append(halftime_board(rows,
        "The luck board, through Week 7, in standings order. All-play is your score against every other team, "
        "every week, bye weeks left out, so 70 games for the four teams whose bye is still to come and 60 for "
        "the rest. Lucky means more wins than that pace, counted in wins; even means within a quarter of a win "
        "either way."))
    parts.append(gil(
        "Aron Rogers is 5 and 2 and third. Thirty-eight teams in the history of this league have had five or "
        "more wins at halftime. Thirty-six of them made the playoffs. The two that did not were Rogers, 5 and "
        "2 in 2023 and 6 and 1 in 2024, when he was the halfway leader and the only halfway leader ever to miss."))
    parts.append(boomer(
        "Every team that has ever been where Aron Rogers is right now made the playoffs, except Aron Rogers, "
        "twice, in a row. He is the only exception to the rule and he is also the rule's most recent "
        "evidence. Aron, you are 5 and 2 with the best bench discipline in the league and the archive says "
        "you are the one man it cannot vouch for. Every other 5 and 2 team in history gets a reference letter, "
        "Gil. Aron gets a file."))
    parts.append(gil(
        "Matt Davis leads on record and on points. The team leading on record at halftime has won four of "
        "fourteen titles and the team leading on points has won six, and Davis did both at once in 2023 from "
        "6 and 1. Rahul Pahuja and Michael Smith are "
        "both 4 and 2 with a game in hand, and four-win teams at halftime have made the playoffs about half the "
        "time, 18 of 34, but five of this league's fourteen champions came from that group, more than from any "
        "other record. Three of the five were Ryan Kelly."))
    parts.append(boomer(
        "Four wins at halftime is where the titles live. Five of fourteen. Ryan Kelly has won from there three "
        "times, and Ryan Kelly is 1 and 5 with the fewest points in the league, so Rahul and Michael, that "
        "group's best player is not in it this year. You are in a good neighborhood and the only man who "
        "knew how to get out of it moved."))
    parts.append(gil(
        "Michael Turner, Billy Norton and Ryan Kelly are 1 and 5. One team in the history of this league has "
        "made the playoffs from one win at halftime. In 2013 Herb Schumann was 1 and 6 after seven weeks, with "
        "the second-fewest points of twelve teams, and he made it. Nobody else has, in twelve tries."))
    parts.append(boomer(
        "Herb did it. From 1 and 6, with nothing, in a twelve-team league. The whole precedent for the bottom "
        "three is one man, and it is the man the league is named for, and I am not touching that with a joke, "
        "Gil. I will say this: if you are 1 and 5 and you need a reason to set your lineup this week, the "
        "reason has a name on the door."))
    parts.append(gil(
        "The luck board has Michael Turner at almost two wins unlucky, the worst in the league, and Bob Dorsch "
        "a full win short of his scores at 2 and 4. Michael Smith is nearly a win ahead of his. And one more "
        "from the archive: the highest Week 7 score in league history is 185.46, Matt Davis in 2020, against "
        "Michael Turner, who scored 60.40 that day. It is also the biggest Week 7 margin ever, 125.06. The "
        "lowest Week 7 score on record is 55.20, Matt Horak in 2015."))
    parts.append(boomer(
        "The biggest Week 7 in league history was Matt Davis putting 185 on Michael Turner and winning by 125, and six years later "
        "Turner is the unluckiest man in the league. Some curses have a date on them, Gil. This one has a box "
        "score."))

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "The rule: do not leave the answer on your own bench. This week nobody lost a game that his bench would "
        "have won. The closest was Michael Turner, who left Tre Tucker's 20.80 behind and lost by 24.54, so "
        "even with Tucker in for Garrett Wilson he falls 7.34 short. And the rule's namesake is gone: Bob "
        "Dorsch released Pat Freiermuth this week to sign the Steelers defense."))
    parts.append(boomer(
        "Bob Dorsch cut Pat Freiermuth. Six weeks after Bob benched the right tight end for the wrong one and "
        "lost by half a point and got a rule named after it, he cut the wrong one. The rule outlived the man, "
        "Gil. From here on it is the Freiermuth Memorial Rule, and the first man to break it in his honor "
        "gets the tight end's old locker."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Eleven calls came due, plus the Turner one from Week 1 that has been open since September. Five right, "
        "seven wrong. Season record 26 and 39. The one I got most right was Dorsch starting Germie Bernard on "
        "his bye, which means my best call of the week was a man making a mistake on a week off. Every call "
        "is below."))
    parts.append(graded_list([
        ("Napoleon's Army", "Michael Turner loses another one by under five points before Halloween.", "WRONG",
         "Made in Week 1. Halloween is Saturday, no Week 8 game ends before it, so it closes today. His losses "
         "since: 5.08, 50.84, 23.20 and 24.54. Five point zero eight, Gil. I bet on Turner losing close and he "
         "missed it by eight hundredths of a point and then stopped trying."),
        ("WPB Steel City", "Bob Dorsch starts Germie Bernard in Week 7, bye or no bye.", "RIGHT",
         "Bernard started, 4.20, with Stevenson sitting there for 21.00. Right about the man. Wrong to be "
         "proud of it."),
        ("Pack Up", "Rahul Pahuja starts C.J. Stroud in Week 7.", "WRONG",
         "Bryce Young started and scored 7.42. Stroud scored 20.52 on the bench. I was betting on Rahul to "
         "read his own roster, and that horse has never once come in."),
        ("Dallas Dawgs", "Matt Davis beats Rahul Pahuja.", "RIGHT",
         "By 48.36, with Burrow in the lineup. The chatbot and I agree on Matt now. It took four weeks."),
        ("Midget Grinders", "Michael Smith beats Eric Olson.", "WRONG",
         "Lost by 14.00 to a quarterback Olson signed that week. Smith played a perfect lineup and so did "
         "Olson, and Olson's perfect was fourteen better."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson clears 100 in Week 7.", "RIGHT",
         "118.78 without Josh Allen. The easy half of the Olson week, and I will take easy."),
        ("I Loved You Tom Brady", "Billy Norton beats Spencer Lentz for the fourth straight time.", "WRONG",
         "Lost by 38.24 with a perfect lineup and a bench that scored zero. I bet on a streak and the streak "
         "did not have any players."),
        ("Balls Deep", "Spencer Lentz leaves under ten on his bench in Week 7.", "WRONG",
         "11.30. Loveland for 16.40 behind Kraft. Missed by a tight end, which for Spencer is the usual "
         "margin."),
        ("| croup", "Aaron Jezioro clears 100 in Week 7.", "WRONG",
         "76.82, with Chase on the bench. I bet on the roster. The roster was there. The owner sat part of it."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers beats Aaron Jezioro for the ninth straight time.", "RIGHT",
         "By 75.30. Nine straight. I am going to keep making this call until one of them retires."),
        ("Napoleon's Army", "Michael Turner beats Ryan Kelly.", "WRONG",
         "Lost by 24.54 after cutting the running back Kelly signed. I picked a man against his own "
         "transaction."),
        ("Old Man Smashers", "Ryan Kelly clears 90 in Week 7.", "RIGHT",
         "117.12, his best score of the year and his first win, six straight scores each higher than the last. "
         "I had him at 90 and he beat it by 27 with 20 on the bench."),
    ]))
    parts.append(gil(
        "Five right, seven wrong. Eleven new ones for Week 8, one per team, with Matt Davis on the bye. The "
        "Saints, Giants, 49ers and Texans have the week off, so Brock Purdy, Christian McCaffrey, George "
        "Kittle, C.J. Stroud, Nico Collins, Malik Nabers, Cam Skattebo and Chris Olave are all out of lineups."))
    parts.append(calls_list([
        ("Dallas Dawgs", "Matt Davis clears 130 on his bye.",
         "He has cleared 145 in three of his last four. Bye-week scores never take a trophy and do not count "
         "in all-play, so this one is for the record and nothing else. Matt, a week off is the only week "
         "nobody can ask you who to start."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Bob Dorsch.",
         "They have not played since 2014. Dorsch leads the series 5 and 2 and won both playoff meetings, in "
         "2011 and 2012. Olson has Josh Allen back and has won three straight. Twelve years is a "
         "long time to hold a grudge, and I am betting Eric held it."),
        ("WPB Steel City", "Bob Dorsch starts Rhamondre Stevenson in Week 8.",
         "Twenty-one on the bench this week, behind Bernard for four. Bob has started the wrong one of those two "
         "for two weeks running, and the wrong one keeps changing. Bob, the man is not hiding. He is on your "
         "roster, next to the one you keep picking."),
        ("Balls Deep", "Spencer Lentz beats Rahul Pahuja.",
         "Spencer leads the series 16 and 10, Rahul won the last one, and Rahul has Stroud and McCaffrey both "
         "on bye. Spencer has Collins and his defense on bye, so both of them are short-handed, and the man "
         "with 897 points usually wins the short-handed games. I am betting on the points."),
        ("Pack Up", "Rahul Pahuja leaves under ten on his bench in Week 8.",
         "He has left 133 behind this season, second in the league, and 18.80 this week. Stroud is on bye, so "
         "the quarterback decision cannot hurt him for once. The bench gets smaller. I am betting the "
         "mistakes do too."),
        ("Kim Jong Un Pleasure Squad", "Tony Pollard clears 20 again for Aron Rogers.",
         "37.00 this week on a projection of 13.64. George Kittle is on bye, so the lineup leans harder on the "
         "running backs, and Pollard is the one Rogers does not have to think about."),
        ("Midget Grinders", "Michael Smith beats Aron Rogers.",
         "Smith won the last meeting, Rogers leads the series 10 and 7, and Rogers has Kittle on bye. Smith is "
         "4 and 2 on a 31 and 29 all-play, which means the luck has carried him about a win. Rogers without a "
         "tight end is the closest thing to an even fight Smith will get all year, and Smith wins the even "
         "ones."),
        ("Old Man Smashers", "Ryan Kelly beats Billy Norton.",
         "Kelly leads the series 10 and 7 and has won the last two. Six straight scores, each higher than the "
         "last, and "
         "Norton's receivers are Nabers on bye and whoever is left. Two 1 and 5 teams, and I am taking the one "
         "whose line on the chart goes up."),
        ("I Loved You Tom Brady", "Billy Norton clears 90 in Week 8.",
         "He scored 77 with a perfect lineup this week, which means the roster has no more room to be wrong. "
         "Nabers and Kendre Miller are on bye. I am betting Cousins gets him there mostly by himself."),
        ("Napoleon's Army", "Michael Turner beats Aaron Jezioro and takes the lead in the series.",
         "Sixteen and sixteen, thirty-two meetings, the most-played rivalry in the league's ESPN years, and ten "
         "of them in the playoffs. Jezioro won the last one. Turner is the unluckiest man in the league and "
         "Jezioro has Purdy on bye, so the luck finally has something to push against."),
        ("| croup", "Aaron Jezioro starts Ja'Marr Chase in Week 8.",
         "He sat Chase for Jalen Coker this week and Coker scored 1.40. Purdy is on bye too, so Trevor Lawrence "
         "starts at quarterback by default, and Chase starts at receiver by common sense. I am betting on the "
         "second one, which in this league is the bigger bet."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, "
        "then by size. A bye-week score never takes a trophy. When an owner already holds one, the next name "
        "in line takes it."))
    parts.append(award(
        "good", "Owner of the Week", "Matt Davis · Dallas Dawgs",
        "152.68, the high score of the week, by 0.56 over Aron Rogers's 152.12. Joe Burrow 36.88, Bucky Irving "
        "25.50, Jameson Williams 23.60. His second Owner of the Week, one week after his first Worst Owner.",
        "He won it by half a point over a man who left nothing on his bench, while leaving six. Matt Davis beat a "
        "perfect lineup with an imperfect one, which is the Davis career in one sentence. Matt, the margin "
        "was 0.56. You have now taken the high score of a week by half a point and lost a game by three "
        "quarters of a point this season, and both times the swing was a quarterback you were already holding."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Aaron Jezioro · | croup",
        "76.82, the low score of the week among the ten teams that played, in a loss by 75.30. He started Jalen "
        "Coker for 1.40 with Ja'Marr Chase's 14.70 on his bench, and the Ravens defense for minus two. Billy "
        "Norton's 77.00 was 0.18 higher, with a perfect lineup.",
        "He lost to Billy Norton's score by 0.18, and Billy's bench was five guys on bye. Aaron benched Chase "
        "and still only finished 0.18 behind a man who had no decisions to make. That is the trophy, Gil. "
        "He took the hard road to the same place and arrived last."))
    parts.append(award(
        "good", "Start of the Week", "Aron Rogers · Tony Pollard, 37.00",
        "Thirty-seven on a projection of 13.64, 23.36 over, more than any other starter in the league beat his "
        "number by this week. Jameson Williams's 23.60 for Matt Davis was 14.40 over, and Davis already has a "
        "trophy.",
        "Thirty-seven from a running back, in a lineup with nothing on the bench. Aron gets exactly what he "
        "wrote down, Gil, every week, like a man who has never once been surprised by his own mail. The last time anything surprised the man was Aaron Jezioro "
        "beating him by four hundredths of a point in 2021, and he has not let it happen since."))
    parts.append(award(
        "bad", "Sit of the Week", "Michael Turner · Tre Tucker, 20.80 on the bench",
        "Signed this week. Garrett Wilson started in his place for 3.60, a swing of 17.20 in a game Turner lost "
        "by 24.54. Bob Dorsch's Stevenson for Bernard was 16.80 on the bye, and bye weeks never take a trophy.",
        "He cut Skattebo to sign Tucker, then sat Tucker for Garrett Wilson, who scored 3.60. "
        "Michael made the move, Gil. He just forgot to make the move. He is a man who orders the steak and "
        "falls asleep before it gets to the table."))
    parts.append(award(
        "bad", "Waste of the Week", "Ryan Kelly · 14.20 left behind, and he won",
        "Cam Skattebo, signed this week, scored 20.60 on his bench behind Tyler Allgeier's 6.40. Spencer Lentz "
        "left 11.30 and Matt Davis 6.10 in their wins, and Davis already holds a trophy.",
        "Ryan signed Skattebo to use him and then used him as a paperweight. You won by 24, Ryan, so it took "
        "nothing from the result but the trophy, and the trophy says Waste. Four titles on that shelf, Gil, "
        "and this is the first Waste next to them."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All eleven of you, every week, all season. Aaron Jezioro leads at 144.28 and added 18.40, most of it "
        "Ja'Marr Chase. Rahul Pahuja is second at 133.34, Spencer third at 130.18, and the three of them have "
        "left more than 400 points sitting down between them. Aron Rogers has left 31.08, Gil. All season. "
        "Jezioro left 32.00 in Week 3 alone."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 7, season_note=(
        "Season totals come from the season ledger through Week 7. Aaron Jezioro leads at 144.28, Rahul Pahuja "
        "is second at 133.34, Spencer Lentz third at 130.18. Aron Rogers has left the fewest, 31.08. Bob "
        "Dorsch's 24.60 came on his bye and counts in his season total, not in any result.")))
    parts.append(gil(
        "No bench cost a game this week. Michael Turner's 17.20 fell 7.34 short of his margin, Jezioro's 18.40 "
        "fell 56.90 short, and Pahuja's 18.80 fell 29.56 short. Four owners left nothing: Rogers, Olson, Smith "
        "and Norton, and two of the four lost."))
    parts.append(boomer(
        "Four perfect lineups and two of them lost. Billy Norton and Michael Smith did everything right and got "
        "a loss for it, and Jezioro did everything wrong and got the same loss, only bigger. The lesson, Gil, "
        "is that there is no lesson. There is only the roster, and the roster does not read this page."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Eric Olson signing Bo Nix, who started and scored 28.18 "
        "with Josh Allen on bye, for Travis Etienne Jr., who scored zero. The biggest swing of any move in the "
        "league this week, and the difference in a game Olson won by 14.00."))
    parts.append(gil(
        "<strong>Worst move:</strong> Rahul Pahuja releasing Harold Fannin Jr., who scored 10.10, to sign Roschon "
        "Johnson, who started and scored 1.30. An 8.80-point swing against him, with Isaiah Likely at 2.20 in "
        "the tight end slot Fannin used to hold."))
    parts.append(boomer(
        "Rahul cut a tight end who scored ten and started a running back who scored one, at the same time he "
        "had a 20-point quarterback on the bench. Rahul had a bad week everywhere, Gil, and the wire is where "
        "it started."))
    parts.append(gil(
        "Twenty-five moves went through. Billy Norton made six, all of them for players who scored 9.00 or "
        "less. Michael Turner made five: Josh Jacobs, who started and scored 17.60; Tre Tucker, for Cam "
        "Skattebo; Aaron Rodgers, who started and scored 15.08; and Jayden Daniels, claimed and then released "
        "for a kicker, Chase McLaughlin, who scored 12.00. Bob Dorsch made three, including releasing Pat "
        "Freiermuth, who scored 3.00, for the Steelers defense, who scored 7.00. Michael Smith claimed Ka'imi "
        "Fairbairn, who started and scored 11.00."))
    parts.append(boomer(
        "Billy made six moves and the best one scored nine. Six trips to the well, Gil, and he came back with a "
        "cup. Turner claimed a quarterback and cut him for a kicker in the same week, which is the fantasy "
        "football version of adopting a dog and keeping the leash. And Bob cut Freiermuth. We covered that. We will be covering it for years."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Bob Dorsch at Eric Olson, Rahul Pahuja at Spencer Lentz, Michael Smith at Aron Rogers, Billy Norton at "
        "Ryan Kelly, and Aaron Jezioro at Michael Turner. Matt Davis has the bye. The Saints, Giants, 49ers "
        "and Texans have the week off. Carolina plays at Green Bay on Thursday night."))
    parts.append(boomer(
        "Olson and Dorsch have not played since 2014, which means the last time these two met, half this league "
        "still had Herb at quarterback in their heart and a flip phone in their pocket. Turner and Jezioro play "
        "for the lead in a series that is 16 and 16 after thirty-two games, and one of them is going to walk "
        "out of there ahead, and the other one is going to say it does not matter. Kelly gets Norton, two 1 and 5 teams, one of them "
        "going up, one of them already on the floor. And Davis sits, which means for one Sunday nobody in "
        "this league can ask a chatbot about him. Halftime is over, Gil. The archive is open, and it has "
        "Herb's name in it, so set your lineup."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 7, HEADLINE, DEK, build(), META, "foh-week-7.png", nav=NAV,
        published="2026-10-27T11:00:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "week-7.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
