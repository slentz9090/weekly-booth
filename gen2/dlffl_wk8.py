"""Dewart Lake FFL, Week 8. Editorial.

Boomer runs SCORCHING (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis, clean language on the page, roast cap and Gil defenses apply. Mama Beth and DA, never "Mother" or
"Dad". HALFTIME is retired (Week 7 one-off; Spencer, 2026-11-03).

NEW THIS WEEK, agreed with Spencer 2026-11-03: THE OWNER SPOTLIGHT, one owner per league per week from the
all-time log (gen2/spotlight.py -> docs/data/dlffl_spotlight_wk8.json), first up Casey Couture, the owner with
the most titles in league history. And a lifetime series line on every matchup card (gen2/series.py), since
2009 in this league. Both are permanent from here.

Outlier engine, Week 8. HEADLINE tier: Lamar Jackson was projected 23.46 and gave Scott Howard 0.00, the worst
miss by a projected 10-point starter in 7,600 since 2018; Mama Beth lost by 20.48 with 64.14 on her bench
(started Omar Cooper Jr. for 0, benched Tyler Allgeier for 37.60). PROMOTE: Howard left 50.50 on the bench,
13th-most in 1,393 team-weeks since 2018; Allgeier's 37.60 is the 22nd-most by one benched player in 6,703;
Zay Flowers 0.00 on 18.09 for Mama Beth; Kent Frenger's 163.38 is the 9th-best of his 268 games since 2009;
Joe Burrow's 43.48 for Doug Fields is the 40th-best start in 12,495 player-weeks. SUPPORT: Ryan Reed won with
91.38 (98th-fewest in a win since 2009); Howard 2-6 on a 43-45 all-play (1.9 wins unlucky); Spencer's 159.56
is the 105th-highest of 2,875 team-weeks; the 59.86 margin is the 135th-biggest of 1,438; Mama Beth's 70.90 is
the 10th-worst of her 222; Cavender 6-2 on 43-45 (2.1 wins lucky); DA snapped Hershberger's 3-game run in the
series (7-5); Spencer 3 straight over Howard; Frenger 3 straight over Casey; Casey a perfect lineup; Fields
eight straight weeks between 92.00 and 105.48.

Verified against dlffl_wk8_facts.json, dlffl_season.json, dlffl_spotlight_wk8.json and gen2/data/dlffl_games.json.
"""
import os

import booth
from booth import award, boomer, calls_list, gil, graded_list, jump, ledger, mcard, spotlight
from compute import by_owner, ledger_rows, load

FACTS = load("dlffl_wk8_facts.json")
SEASON = load("dlffl_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 166.78

NAV = (
    '<nav class="nav" aria-label="Sections"><ul>'
    '<li><a href="#board">The Scoreboard</a></li>'
    '<li><a href="#spotlight">Owner Spotlight</a></li>'
    '<li><a href="#calls">On The Record</a></li>'
    '<li><a href="#hardware">The Hardware</a></li>'
    '<li><a href="#ledger">The Bench Ledger</a></li>'
    '<li><a href="#wire">The Waiver Wire</a></li>'
    '<li><a href="#next">Next Sunday</a></li></ul></nav>'
)

HEADLINE = "Scott Howard Started Lamar Jackson. Lamar Jackson Did Not Play."
DEK = (
    "Howard's quarterback was projected for 23.46 and scored 0.00, the worst miss by a projected starter in 7,600 "
    "since 2018, and Howard lost by 59.86 with Dak Prescott's 19.80 on his bench. Ryan Reed won with two starters "
    "who did not play. Kent Frenger scored 163.38, the ninth-best of his 268 games here, and three teams sit at 6 and 2. New this week: "
    "a lifetime series line on every card, and THE OWNER SPOTLIGHT, one owner a week from the all-time log. "
    "First up, the man with the most titles in league history, who is currently tenth in points."
)
META = (
    "Gil and Boomer call Week 8 of the Dewart Lake FFL: Scott Howard starts a quarterback who did not play and "
    "loses by 59.86, Ryan Reed wins with two starters who did not play, Kent Frenger's 163.38, three teams at 6 and 2, a "
    "series line on every card, and the first Owner Spotlight: Casey Couture, five titles, tenth in points."
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

    # ---- 1. the quarterback who did not play
    w, l = card_rows("Spencer Lentz", "Scott Howard")
    parts.append(mcard(
        "m-howard", "Spencer by 59.86, and Howard's quarterback did not play", w, l,
        "Tee Higgins 35.50 on a projection of 13.80, Brock Bowers 24.70 and Jaylen Warren 23.80 for Spencer "
        "Lentz, who started Parker Washington for 3.10 and Bijan Robinson for 7.60. Scott Howard started Lamar "
        "Jackson, who did not play and scored zero, with Dak Prescott on his bench for 19.80. Braelon Allen "
        "25.30 and Bucky Irving 24.00 for Howard, Michael Wilson 25.80 on his bench behind Drake London's 1.30.",
        SCALE, key=True, series="Spencer Lentz leads 6-4 since 2019 · Spencer has won the last three"))
    parts.append(gil(
        "Spencer Lentz wins 159.56 to 99.70 and is 6 and 2, six straight wins, first place, and first in points at "
        "1,084.84, eighty clear of anyone. Scott Howard started Lamar Jackson at quarterback. Jackson did not "
        "play. He was projected for 23.46 and scored 0.00, and of the 7,600 starters projected for ten or more "
        "since 2018, that is the worst miss on record. Howard left 50.50 on his bench, the "
        "13th-most by any team in a week since 2018. His best lineup was 150.20. It still loses this game by "
        "9.36."))
    parts.append(boomer(
        "The man started a quarterback who was not in the building. Lamar "
        "Jackson was projected for twenty-three and scored exactly what I scored, and I was in a chair with a "
        "drink. Dak Prescott sat on the bench and threw for nineteen points to nobody. And here is the part "
        "that should keep Scott up at night: if he gets all fifty points back, every one of them, he loses "
        "by nine anyway. He was doomed and he brought a tarp."))
    parts.append(gil(
        "In fairness to Scott Howard, Allen and Irving were 49.30 between them, he has the fifth-most points in "
        "the league at 860.80, and against every other team every week he is 43 and 45, so his 2 and 6 is about "
        "two wins worse than his scores. Spencer's week was not clean either. Bijan Robinson was projected for "
        "19.30 and scored 7.60, Parker Washington scored 3.10, and Tucker Kraft outscored Bijan from the "
        "bench."))
    parts.append(boomer(
        "Spencer's best possible lineup was 166.26, Gil. Kent's was 166.78. Half a point between the two best "
        "rosters in the league, and one of them started Parker Washington. Tee Higgins went for 35 on a "
        "projection of 13, which is the reason that card reads like a rout and not like a missing persons "
        "report for Washington. He also signed a kicker and a defense this week and started both, twelve and "
        "nine, and I want it noted that the two men he found on the street, combined, outscored Bijan Robinson "
        "by thirteen. Six straight, first place, and his third-best running back is a "
        "kicker."))

    # ---- 2. Reed wins with two ghosts
    w, l = card_rows("Ryan Reed", "Beth Couture")
    parts.append(mcard(
        "m-beth", "Reed, with two starters who did not play, over Mama Beth", w, l,
        "Jaxon Smith-Njigba 23.80, Harold Fannin Jr. 21.40 on a projection of 7.11, and Bo Nix 19.28 for Ryan "
        "Reed, who started A.J. Brown and Breece Hall for zero apiece with Jaylen Waddle's 13.40 on his bench. "
        "Mama Beth got 18.00 from Geno Smith, signed this week, and zeros from Omar Cooper Jr. and Zay Flowers, "
        "with Tyler Allgeier's 37.60 on her bench.",
        SCALE, series="Tied 2-2 in four meetings since 2012 · Reed has won the last two"))
    parts.append(gil(
        "Ryan Reed wins 91.38 to 70.90 and is 4 and 4. He started Bo Nix, as Boomer called, and Nix scored "
        "19.28. He also started two players who did not play, A.J. Brown and Breece Hall, plus Emanuel Wilson, "
        "who scored the same zero, and won anyway with the 98th-fewest points in a winning "
        "score since 2009. Mama Beth is 1 and 7. Geno Smith, signed this week, gave her 18.00, Zay Flowers was "
        "projected for 18.09 and scored zero, and Tyler Allgeier scored 37.60 on her bench behind Omar Cooper Jr."))
    parts.append(boomer(
        "The Cooper start was my call, Gil. I said it on this page a week ago, she did it, and the man produced "
        "nothing while Allgeier scored 37 in a folding chair. Put me in the box score under contributing factors. "
        "The story on this card is Ryan. Ryan started two men who were not playing and a third who scored like he "
        "was not playing, and won. The lineup had the same number of absences as a Friday in July."))
    parts.append(gil(
        "In fairness to Mama Beth, the Flowers zero was an absence, not a decision, the 23rd-worst miss since 2018 "
        "by a starter projected for ten or more, and she has three titles here, 2014, 2018 and 2022. Nobody with "
        "three titles stays 1 and 7 for long. Ryan Reed got 21.40 from a "
        "tight end projected for 7.11, Harold Fannin Jr., and released Dominic Zvada for Chad Ryland, who "
        "scored 10.00."))
    parts.append(boomer(
        "Ryan, you won with 91 and two ghosts in the lineup, and Jaylen Waddle scored 13 on your bench behind them. "
        "Three titles on the other sideline, and you beat her with a roster that was half out of town. That one "
        "was awarded, and I am still counting it."))

    # ---- 3. the 163
    w, l = card_rows("Kent Frenger", "Casey Couture")
    parts.append(mcard(
        "m-frenger", "Frenger's 163.38, the high score of the week and the ninth-best of his career, over a perfect lineup", w, l,
        "Bhayshul Tuten 31.90 on a projection of 14.21, Tony Pollard 30.20 and Ja'Marr Chase 28.60 for Kent "
        "Frenger, with Kenneth Walker III at 10.40 and Cam Little, signed this week, at 6.00. Casey Couture set a "
        "perfect lineup: D'Andre Swift 26.90, Kyler Murray 19.90 the week he signed him, the Packers defense "
        "12.00 the week he signed them, and Jonathan Taylor 4.70.", SCALE,
        series="Kent Frenger leads 18-14 since 2009, four in the playoffs · Frenger has won the last three"))
    parts.append(gil(
        "Kent Frenger wins 163.38 to 112.40 and is 6 and 2, five straight wins, second in points at 1,004.76. "
        "The 163.38 is the high score of the week, it beats all eleven teams, and it is the ninth-best game of his "
        "268 in this league since 2009. Tuten and Pollard were projected for 29.10 between them and scored "
        "62.10. Casey Couture left nothing on his bench, scored 112.40, which beats nine of the other eleven teams, "
        "and lost by 50.98. He is 4 and 4. The series is 18 and 14, Frenger, and Frenger has won the last three, "
        "including last December's final."))
    parts.append(boomer(
        "Casey signed a quarterback, a defense and a kicker this week. All three started. All three hit. Murray "
        "twenty, the Packers twelve, Matt Gay ten. Perfect lineup, 112, beats nine teams, loses by fifty-one. "
        "Casey did everything a man can do and got hit by a bus with Kent Frenger's face on the front of it. "
        "That is not a loss, Gil. That is weather, and the champ is the weather."))
    parts.append(gil(
        "In fairness to Casey Couture, Jonathan Taylor was projected for 15.07 and scored 4.70, Ollie Gordon II "
        "was projected for 14.10 and scored 6.90, and he still put up the third-highest score in the league. "
        "Against everyone this week he went 9 and 2. He is 4 and 4 with the tenth-most points, and this is a "
        "man with five titles, which is more than anyone in the history of this league. We have a segment on "
        "him this week. Kent Frenger made three moves, Bryce Young, Cam Little and the Rams defense, and the "
        "Rams scored 11.00."))
    parts.append(boomer(
        "Five straight for the reigning champ, with a running back named Bhayshul who scored 32 and a running "
        "back named Pollard who scored 30, and the one with Kenneth Walker's name on the jersey scored ten. "
        "Kent's roster is a witness protection program. Nobody has heard of half of them and all of them score. "
        "Three at 6 and 2, Gil. One has the points, one has the belt, and one has the horseshoe. We will "
        "get to the horseshoe."))

    # ---- 4. the elder returns
    w, l = card_rows("dennis couture", "Adam Hershberger")
    parts.append(mcard(
        "m-da", "DA by 20.06, with Josh Allen back and a three-game Hershberger run in the series over", w, l,
        "Josh Allen 26.56, Dalton Kincaid 16.60 on a projection of 7.36, Christian Watson 16.30 and the "
        "Commanders defense, claimed this week, 14.00 for DA, with Kyle Pitts Sr. at 1.60. Adam Hershberger got "
        "19.40 from Trevor Lawrence and 17.40 from Matthew Golden, started Zach Charbonnet for 4.40, and left "
        "Jameson Williams's 15.00 on his bench.", SCALE,
        series="DA leads 7-5 since 2014"))
    parts.append(gil(
        "DA wins 110.36 to 90.30 and is 5 and 3, fourth seed, third in points at 955.20. Josh Allen was back "
        "from the Bills' bye and cleared 25, as Boomer called. Adam Hershberger had beaten DA three straight "
        "times, including a December consolation game two years ago, and that run ends. DA leads the series 7 and 5. "
        "Hershberger is 3 and 5 and has had 1,014.96 points scored against him, the most in the league."))
    parts.append(boomer(
        "Josh Allen came home and DA remembered who he was. DA has left 61 points on his bench all season, "
        "third-fewest in the league, and this week he made five moves, Gil. Five. "
        "One of them was signing Dameon Pierce and cutting Dameon Pierce in the same week, so Pierce was on the "
        "roster long enough to find the bathroom and not long enough to use it. The elder got busy, and when "
        "the elder gets busy, somebody named Adam gets a letter."))
    parts.append(gil(
        "In fairness to Adam Hershberger, Lawrence and Golden gave him 36.80 and Blake Corum 13.30, and he "
        "added Antonio Williams this week. The benching hurt: Jameson Williams carried him last week with 23.60, "
        "scored 15.00 this week, and sat behind Charbonnet's 4.40. That swing is 10.60 in a loss by 20.06, so it "
        "did not decide the game. DA still started Kyle Pitts Sr. for 1.60 and Aaron Jones Sr. for 5.00."))
    parts.append(boomer(
        "Adam has had 1,014.96 points scored against him, the most in the league, and he is 36 and 52 against "
        "the room, so half of that is the schedule and the other half is Adam. He also put the man who carried "
        "him last week in the trunk, fifteen on the bench, four in the lineup, and lost by twenty. DA started Kyle Pitts for "
        "one point six and still won by twenty, which is the oldest trick in the Couture book: leave one spot "
        "empty so the other guy thinks he has a chance."))

    # ---- 5. the horseshoe
    w, l = card_rows("Geoff Cavender", "Scott Reisert")
    parts.append(mcard(
        "m-hawk", "Cavender by 8.08, and Reisert's bench had the game by itself", w, l,
        "Jordan Love 21.52, Josh Jacobs 20.20 and Tyler Bass, claimed this week, 16.00 for Geoff Cavender, with "
        "George Pickens at 5.80 and Hunter Henry at 4.50. Scott Reisert got 26.80 from Jahmyr Gibbs and 21.00 "
        "from the Jaguars defense, claimed this week, started Jeremiyah Love for 2.30 and Mark Andrews, signed "
        "this week, for 2.90, and left Wan'Dale Robinson's 12.70 on his bench.", SCALE,
        series="Tied 2-2 in four meetings since 2024"))
    parts.append(gil(
        "Geoff Cavender wins 101.82 to 93.74 and is 6 and 2, third seed on points. He got Josh Jacobs into the "
        "lineup this week for 20.20, after Jacobs scored 17.60 on his bench last week, and Tyler Bass, claimed "
        "for Eddy Pineiro, kicked 16.00. Scott Reisert benched Wan'Dale Robinson for 12.70 and started "
        "Jeremiyah Love for 2.30. That is a 10.40 swing in a game he lost by 8.08, so the bench had the game. "
        "Reisert is 4 and 4 and has lost four of five. The series is 2 and 2, and Reisert won last December's "
        "consolation meeting by 1.28."))
    parts.append(boomer(
        "Geoff is 6 and 2 and the league has outscored him 45 times in 88 tries. That is a participation "
        "trophy with First Place engraved on it. And Scott Reisert made five "
        "moves again this week. One was brilliant, the Jaguars for 21. One was cutting DeMario Douglas, who "
        "then scored 15 as a free agent. Then he benched a 12 and started a 2 and lost by 8. Scott can "
        "beat himself in the same afternoon he beats the wire."))
    parts.append(gil(
        "In fairness to Scott Reisert, Gibbs and the Jaguars were 47.80 between them, the Jaguars claim was the "
        "best defense move in the league this week, and his 51.80 on the bench for the season is still the "
        "fewest of anyone. Javonte Williams was projected for 20.37 and scored 6.20. Geoff Cavender left 0.50 "
        "behind, the second-cleanest week in the league, and he is 6 and 2 on a 43 and 45 all-play, about two "
        "wins ahead of his scores, which is the luckiest record in the league."))
    parts.append(boomer(
        "Geoff's best possible lineup was 102.32, Gil. Four teams scored more than Geoff's ceiling and he is tied "
        "for first. He is not wasting points. He does not have any. Love, Jacobs and a kicker he claimed this "
        "week carried 57 of his 101, and the rest of the roster chipped in a Hunter Henry for four and a half. "
        "Two wins lucky and tied for first. If luck were a stat Geoff would lead the league in it and not know "
        "how."))

    # ---- 6. the band
    w, l = card_rows("Doug Fields", "Adam Calvelage")
    parts.append(mcard(
        "m-fields", "Fields by 12.40 with a 43-point quarterback, and still between 92 and 106 for the eighth straight week", w, l,
        "Joe Burrow 43.48 on a projection of 24.17, James Cook III 17.10 and Derrick Henry 13.00 for Doug "
        "Fields, who started Tre Tucker for zero and Will Reichard for zero with Ladd McConkey's 10.60 and Kirk "
        "Cousins's 28.18 on his bench. Adam Calvelage got 18.40 from Jonah Coleman, claimed this week, started "
        "the Jets defense for minus two and RJ Harvey for zero, and got 14.98 from Jayden Daniels.", SCALE,
        series="Doug Fields leads 4-1 since 2022"))
    parts.append(gil(
        "Doug Fields wins 94.38 to 81.98 and is 4 and 4. Burrow's 43.48 is the 40th-best start by any player in "
        "this league since 2018, and Fields still finished at 94.38, so he has now scored between 92.00 and "
        "105.48 in all eight weeks this season. Boomer's call was 92 to 106 again, and it is right. Adam "
        "Calvelage has lost four straight since starting 3 and 1. He started the Jets defense, who scored "
        "minus two, and RJ Harvey, who did not play. Against everyone this week he went 1 and 10."))
    parts.append(boomer(
        "Burrow's 43 is the 40th-best start anyone in this league has made since 2018, and it bought Doug a 94, "
        "the 131st-fewest points in a win since 2009. One man had the night of the year and the team around "
        "him filed it under Tuesday. Tucker zero, Reichard zero, McConkey on the bench for ten, Kirk Cousins "
        "on the bench for twenty-eight. Eight weeks in the band, Gil. The man is a metronome that had one good night and went right back to "
        "ticking."))
    parts.append(gil(
        "In fairness to Adam Calvelage, Jonah Coleman scored 18.40 the week he claimed him, and Brandon Aubrey "
        "kicked 12.00. Jayden Daniels was projected for "
        "23.88 and scored 14.98. He left 4.70 behind, so the lineup was close to clean. The scores were not "
        "there. Doug Fields left 18.00, most of it McConkey behind Tucker, and he won by 12.40."))
    parts.append(boomer(
        "Negative two is the lowest number any starter in this league put up this week, and Adam chose it. He "
        "went 1 and 10 against the room. Four straight losses. He was 3 and 1, Gil. He was 3 and 1 the way I was once thin. And Doug left eighteen on the "
        "bench and won by twelve, which in Doug's world is a wild Saturday night. Somebody check on Doug. He "
        "scored 94 with a 43-point quarterback and nobody has seen him blink since September."))

    # ---- THE OWNER SPOTLIGHT (new this week)
    parts.append('<h2 id="spotlight">The Owner Spotlight</h2>')
    parts.append(gil(
        "New this week, and permanent from here: one owner, one page, from the all-time log of this league, "
        "which runs back to 2009. Every number below is a real game somebody in this league played. We start "
        "with the owner who has won more titles than anyone and has been in one headline all season, and that "
        "one was about DA."))
    parts.append(spotlight(
        "The Owner Spotlight · Week 8", "Casey Couture · One Under akaThe Mulligan",
        "In the league since 2009 · 254 games in the log · 4 and 4 this season, tenth in points",
        [
            ("5", "titles: 2009, 2011, 2017, 2020 and 2021. The most in league history. Spencer Lentz has four, Mama Beth three, nobody else more than one."),
            ("18-8", "career record in the real playoff bracket, 29 and 11 if you count consolation games, and he does not. Nine finals in seventeen seasons, five won, four lost, the last two in a row: 2024 to Doug Fields, 2025 to Kent Frenger."),
            ("18-2", "lifetime against DA, who raised him. He is also 6 and 0 against Adam Calvelage, 8 and 2 against Ryan Reed, and 13 and 10 against Spencer Lentz."),
            ("204.00", "career high, Week 2 of 2009. Career low 57.80, Week 14 of 2022. Career average 114.44 a week, second among the twelve active owners."),
            ("5-7-1", "his record in 2011, the year he won the title. He was 2 and 5 after seven weeks. Nobody else in league history has won it from two wins at the halfway mark, and only one other champion, 2010 at 6 and 7, won it with a losing record."),
            ("32", "games against Kent Frenger, the most he has played against anyone. Frenger leads 18 and 14, and they have met four times in the playoffs, once in the final, last December."),
        ]))
    parts.append(gil(
        "Casey Couture has the most titles in the history of this league and nobody calls him the "
        "favorite. His best regular season, 12 and 2 in 2024, ended in a final he lost by 68.74 over two "
        "weeks to Doug Fields. His luckiest season was 2010, 8 and 5 on a 43 and 73 all-play, about three wins "
        "ahead of his scores, and he lost the final that year too."))
    parts.append(boomer(
        "Five rings, Gil, and he sets a lineup like a man defusing a bomb in oven mitts. Last week he cut an "
        "eight-point defense for a zero-point defense on purpose and won. This week he got every chair right "
        "and lost by fifty-one. Casey Couture is 18 and 8 in the playoff bracket. Eighteen and eight. That is not "
        "a fantasy record. That is a parole board. He is 18 and 2 against DA, and I have to assume the two "
        "wins were Christmas presents."))
    parts.append(gil(
        "This season he is 4 and 4 with the tenth-most points in the league, 765.62, and a 32 and 56 record "
        "against everyone every week, so he is about a win ahead of his scores. He has made the playoffs in "
        "thirteen of his seventeen completed seasons. The two owners who have ended his last two Decembers, "
        "Doug Fields and Kent Frenger, are both above him in the standings right now, and he plays Frenger "
        "again in the playoffs only if he gets there."))
    parts.append(boomer(
        "Thirteen playoffs in seventeen years from a man who is tenth in points in November, Gil. Casey builds "
        "an alibi for twelve weeks and then shows up in December with a lawyer. "
        "If you are 6 and 2 right now and you are feeling good, look down the standings at the 4 and 4 who is tenth "
        "in points. He has five of the things you want, and only one of them came from a season he led in "
        "points."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls came due. Seven right, five wrong, a winning week, which the record will show does not "
        "happen often. Season record 38 and 46. The Cooper call came in, and that one is on me, not on her. Every "
        "call is below, in ink, including that one."))
    parts.append(graded_list([
        ("The Scranton Strangler", "Scott Howard beats Spencer Lentz.", "WRONG",
         "Lost by 59.86 with a quarterback who did not play. I bet on the weather system and the weather "
         "system started a quarterback who was not in the building. Dak Prescott scored 19.80 in the next chair."),
        ("Balls Deep", "Drake Maye clears 25 again for Spencer Lentz.", "WRONG",
         "22.46. Two and a half short. Spencer won by sixty and I lost the call on his quarterback, which is "
         "the most Spencer thing that has ever happened to me."),
        ("Holy Rollers", "Adam Hershberger beats DA for the fourth straight time.", "WRONG",
         "Lost by 20.06. I said a streak against a Couture is how they find you. They found him, and he had benched "
         "the man who carried him the week before."),
        ("DA The Badenov's", "Josh Allen clears 25 for DA.", "RIGHT",
         "26.56 is the 906th-best start in this league since 2018, Gil. A middling Josh Allen is a career week "
         "for most of these men. Easiest call on the board and I will take it."),
        ("Momma's Boys", "Mama Beth starts Omar Cooper Jr. in Week 8.", "RIGHT",
         "She started him. He scored zero. Tyler Allgeier scored 37.60 on her bench. This is the first call I "
         "have ever won that I would like to give back. The record is the record, so it stays, and the apology "
         "goes to Mama Beth, in ink, same as the call."),
        ("BearDown", "Ryan Reed starts Bo Nix in Week 8.", "RIGHT",
         "Started, 19.28. Then he started two men who were not playing. I asked for Nix to be in the room. I did "
         "not think to ask about the rest of the room."),
        ("An alBum Cover", "Adam Calvelage beats Doug Fields.", "WRONG",
         "Lost by 12.40 with a defense that scored negative two. I bet on Daniels and got 14.98. Four straight "
         "losses for Adam and one for me."),
        ("Cosby Copperheads", "Doug Fields scores between 92 and 106 again.", "RIGHT",
         "94.38 with a 43-point quarterback. Eight for eight. I said I wanted to be there the day Doug Fields "
         "did something. Joe Burrow did something. Doug stayed home."),
        ("Berlin Blitz", "Kent Frenger beats Casey Couture.", "RIGHT",
         "By 50.98. I bet on Kent, and the man across from Kent set a perfect lineup and lost by fifty anyway. First call I have won on Kent in a month, and it took the high score of the week to do it."),
        ("One Under akaThe Mulligan", "Casey Couture leaves under five on his bench again.", "RIGHT",
         "0.00. Last week he left 3.80 and won by 2.36. This week he left nothing at all. The bench is "
         "not the problem, Gil. The problem scored 163."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender beats Scott Reisert.", "RIGHT",
         "By 8.08. I bet on the luck because it had not run out yet. It has not. I am starting to think it is "
         "not luck and I do not like that either."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert leaves under five on his bench in Week 8.", "WRONG",
         "15.80, and 10.40 of it was Wan'Dale Robinson behind Jeremiyah Love in a loss by eight. I said he "
         "would count the silverware right. He counted it. Then he left it in the car."),
    ]))
    parts.append(gil(
        "Seven right, five wrong. Twelve new ones for Week 9, one per team, with the Steelers and Titans off, so "
        "Jaylen Warren, DK Metcalf, Tony Pollard, Chris Boswell and the Pittsburgh defense sit this one out."))
    parts.append(calls_list([
        ("Balls Deep", "Spencer Lentz beats Geoff Cavender.",
         "Geoff leads the series 2 and 1 and has won the last two, including a December consolation game two years ago. "
         "He is also 6 and 2 on a losing all-play record. I bet on his luck last week and it came in. "
         "This week I am betting on the points, because at some point the scoreboard gets a vote."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender scores 110 or more in Week 9.",
         "He scored 110.86 and 101.82 the last two weeks. Love, Jacobs and Amon-Ra St. Brown are on the "
         "roster and he just claimed a kicker who scored 16. I am betting the man finally scores like a 6 "
         "and 2 team, in the week I bet he loses. Both can be true. That is Geoff."),
        ("Berlin Blitz", "Kent Frenger beats Doug Fields.",
         "Fields owns him 10 and 4, and nobody says it out loud because Kent has the ring. "
         "Kent just scored 163 and has won five straight, and Fields has not scored 106 all year. I am betting "
         "the champ against a man who has beaten him ten times in fourteen tries, because I have a short memory and a "
         "long drink."),
        ("Cosby Copperheads", "Doug Fields scores between 92 and 106 again.",
         "Eight for eight. A 43-point quarterback could not get him out of the range. I will ride the dial tone "
         "until somebody picks up."),
        ("DA The Badenov's", "DA beats Adam Calvelage for the fifth straight time.",
         "DA leads the series 4 and 1 and has won four straight, one of them in a December consolation game. Josh Allen is back and "
         "Adam has lost four in a row. The elder has a pattern and Adam Calvelage is in it."),
        ("An alBum Cover", "Jayden Daniels clears 20 for Adam Calvelage.",
         "Daniels scored 14.98 on a 23.88 projection and Brock Purdy is back from the bye, so Adam has a "
         "decision. I am betting he starts Daniels and Daniels remembers how. If he starts Purdy, the call is "
         "dead on arrival, and so is my patience."),
        ("The Scranton Strangler", "Scott Howard beats Mama Beth for the seventh straight time.",
         "Howard leads 7 and 4 and has won six straight meetings. Howard has Dak Prescott, who is playing. I am "
         "betting he notices, and that Mama Beth makes him earn the seventh."),
        ("The Scranton Strangler", "Scott Howard starts Dak Prescott in Week 9.",
         "Dak Prescott scored 19.80 from the next chair and is projected for twenty. Lamar is out again. I am "
         "betting Scott moves one chair to the left."),
        ("BearDown", "Ryan Reed beats Adam Hershberger.",
         "Reed leads 2 and 1. He won this week with two men who did not play, so a full lineup should be an "
         "improvement, and if it is not, Ryan, I am done asking."),
        ("Holy Rollers", "Jameson Williams clears 15 for Adam Hershberger.",
         "He scored 15.00 on Adam's bench and 23.60 in his lineup the week before. The call is that Adam "
         "starts him. Fifteen is the number, and he has to start to count."),
        ("One Under akaThe Mulligan", "Casey Couture beats Scott Reisert.",
         "Casey leads 5 and 2 and won this meeting last year 142.60 to 134.36. He has five rings and a perfect "
         "lineup this week. Reisert has lost four of five and made ten moves in two weeks. I am betting the "
         "man who does less."),
        ("Simba St. Gibbs Lion Kings", "Jahmyr Gibbs clears 20 again for Scott Reisert.",
         "26.80 this week on a 23.98 projection. Gibbs is the one man on that roster Scott has not tried to "
         "replace. I am betting on the one he left alone."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, "
        "then by size. When an owner already holds one, the next name in line takes it."))
    parts.append(award(
        "good", "Owner of the Week", "Kent Frenger · Berlin Blitz",
        "163.38, the high score of the week, the ninth-best game of his 268 in this league, and a win against "
        "all eleven teams. Tuten 31.90, Pollard 30.20, Chase 28.60, and 3.40 left behind. His fifth straight "
        "win.",
        "Five straight for the champ, 163, and the two men who carried him are named Bhayshul and Pollard. Kent, "
        "I have to look up your roster every week and I never once have to look up your score."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Scott Howard · The Scranton Strangler",
        "99.70 in a loss by 59.86. Lamar Jackson, projected for 23.46, did not play and scored 0.00, the worst "
        "miss by a starter projected for ten or more in 7,600 since 2018, with Dak Prescott's 19.80 on the bench. "
        "He also started Drake London for 1.30 over Michael Wilson's 25.80. He left 50.50 on his bench, the "
        "13th-most in a week since 2018, and his best lineup, 150.20, still loses this game by 9.36.",
        "The man started a quarterback who was not in the building, Gil, and the one who was in the building "
        "scored nineteen from the next chair. Projected for twenty-three, scored zero, the biggest miss by a "
        "starter in this league since they started counting. And here is the part he should keep: fifty points "
        "on his bench, and if he gets every one of them back, he loses by nine. The lineup was wrong and it also "
        "did not matter, and I have never had to say both about one man in the same week."))
    parts.append(award(
        "good", "Start of the Week", "Spencer Lentz · Tee Higgins, 35.50",
        "Projected for 13.80, so 21.70 over, the biggest margin over projection by any starter in the league "
        "this week. Joe Burrow's 43.48 for Doug Fields was 19.31 over and second, and Frenger's Tuten 17.69 "
        "over, third.",
        "Spencer started a receiver projected for fourteen and got thirty-five, in a week his headliner "
        "running back scored seven and his other receiver scored three. Take Higgins out and Spencer still wins "
        "by twenty-four. The receiver did not decide the game, Gil. He decided who gets the trophy for it."))
    parts.append(award(
        "bad", "Sit of the Week", "Scott Reisert · Wan'Dale Robinson, 12.70 on the bench",
        "Jeremiyah Love started in his place for 2.30, a 10.40 swing in a game Reisert lost by 8.08. It is the "
        "biggest benching this week that flipped its own game by an owner who does not already hold a trophy. "
        "Mama Beth's Allgeier for Cooper was 37.60, and the booth is not counting it, because Boomer called it and "
        "he can wear it. Scott Howard's Michael Wilson for Drake London was 24.50 in a loss by 59.86, which no "
        "benching flips, and he holds Worst Owner.",
        "Scott made five moves this week, claimed the best defense on the wire, and then lost the game on the "
        "one decision that did not require a transaction. He benched a 12 and started a 2. Scott, you keep "
        "fixing the roster, and the thing that keeps losing is Sunday morning, and you cannot claim a new one of "
        "those."))
    parts.append(award(
        "bad", "Waste of the Week", "Doug Fields · 18.00 left behind, and he won",
        "Ladd McConkey scored 10.60 on his bench behind Tre Tucker's zero, and Will Reichard kicked zero in the "
        "lineup. Kirk Cousins's 28.18 on the bench does not count against him, since Burrow had the quarterback "
        "slot for 43.48. Ryan Reed left 13.40 in his win and DA 8.00.",
        "Doug started a receiver who scored nothing and a kicker who scored nothing and still landed in the "
        "band, because of course he did. Eighteen points on the bench and a 94. If Doug ever starts his best "
        "lineup he might score 107 and the whole league will have to be re-measured."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All twelve of you, every week, all season. Scott Howard leads at 221.30 after adding 50.50 in a week "
        "he lost by 60, which means for the second week running the points on his bench were decorative, just "
        "a lot more of them. Mama Beth added 64.14 and is second at 138.28. Scott Reisert is still the cleanest man in the league at 51.80, and this week the "
        "15.80 he added is the reason he lost."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 8, season_note=(
        "Season totals come from the season ledger through Week 8. Scott Howard leads at 221.30, Mama Beth is "
        "second at 138.28, Ryan Reed third at 132.14. Scott Reisert has left the fewest, 51.80. Casey Couture "
        "left nothing this week.")))
    parts.append(gil(
        "Two benches cost a game this week: Mama Beth left 64.14 and lost by 20.48, and Scott Reisert left 15.80 "
        "and lost by 8.08. Scott Howard left 50.50 and lost by 59.86, so his did not. Casey Couture left "
        "nothing and lost by 50.98. Geoff Cavender left 0.50 and won."))
    parts.append(boomer(
        "Scott Howard's bench has 221 points on it, Gil, more than Reisert, DA and Frenger have left combined "
        "all season. Casey left nothing and lost by fifty. Howard left fifty and lost by sixty. Mama Beth left "
        "sixty-four and lost by twenty. Only one of those three could have won from the couch, Gil, and the man "
        "who could not have won from anywhere is the one holding the trophy this week."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Casey Couture signing Kyler Murray, who started and "
        "scored 19.90, for TreVeyon Henderson, who scored zero. The biggest swing of any move in the league "
        "this week. Scott Reisert's Jaguars defense, claimed for the Dolphins, was 21.00 to 5.00, tied for second with Geoff "
        "Cavender's Tyler Bass for Eddy Pineiro, 16.00 to nothing."))
    parts.append(gil(
        "<strong>Worst move:</strong> Scott Reisert releasing DeMario Douglas, who scored 15.10, to sign "
        "Courtland Sutton, who scored 7.30. A 7.80-point swing against him in a game he lost by 8.08. DA "
        "releasing that same Sutton for Dameon Pierce, whom he cut again before the week was out, was second. "
        "Doug Fields releasing Matt Gay, who kicked 10.00, for the Bengals defense, who scored 4.00, was third, "
        "and Casey Couture picked Gay up and started him."))
    parts.append(boomer(
        "Doug cut a kicker who scored ten so that Casey could start him for ten. Doug is feeding Casey's special teams "
        "now, Gil."))
    parts.append(gil(
        "Thirty moves went through. Scott Reisert made five again: the Jaguars for the Dolphins, Mark Andrews for "
        "Roschon Johnson, KC Concepcion for Jaylin Noel, Jaydon Blue for Kendre Miller, and Sutton for Douglas. "
        "DA made five: the Commanders defense for the Bears, Treylon Burks for Aaron Rodgers, Makai Lemon for "
        "Xavier Worthy, and Dameon Pierce in for Courtland Sutton and out for Samaje Perine. Casey Couture made "
        "four and started three of them: Murray, the Packers defense for the Titans, Matt Gay for Tyler Loop, "
        "and Tyler Shough for Marvin Harrison Jr. Geoff Cavender released Bryce Young for Caleb Douglas, and "
        "Kent Frenger signed Young the same week. Mama Beth signed Geno Smith for Rashod Bateman and claimed "
        "Alvin Kamara for Devaughn Vele."))
    parts.append(boomer(
        "Casey signed four men and three of them started and scored. DA signed five and one of them "
        "did not last the week. Scott signed five and lost by eight. Same wire, Gil, same week. The "
        "difference is Casey picks up a quarterback the way you pick up milk, and Scott picks up a roster "
        "the way you pick up a hobby."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Adam Hershberger at Ryan Reed, Adam Calvelage at DA, Scott Howard at Mama Beth, Kent Frenger at Doug "
        "Fields, Geoff Cavender at Spencer Lentz, and Scott Reisert at Casey Couture. Jacksonville plays at Baltimore on "
        "Thursday night, so Lamar Jackson, Derrick Henry, Zay Flowers, Mark Andrews, Trevor Lawrence, Bhayshul "
        "Tuten, Travis Etienne, Cam Little and the Jaguars defense are all done before Sunday. Cincinnati and Atlanta kick "
        "off at 9:30 Sunday morning, and Buffalo at Minnesota is the Monday night game."))
    parts.append(boomer(
        "Two of the three 6 and 2s play each other. Spencer gets Geoff, who has beaten him twice "
        "running, and Kent gets Doug, who has beaten him ten times, so by Monday night one of the three could be "
        "alone in first and both of them should be looking over a shoulder at Casey Couture, who has five rings and is tenth "
        "in points, which I will keep saying until one of you explains it to me. Howard goes to Mama Beth, where he has won six straight in the series, and if he starts a "
        "quarterback who is playing, he has a chance. Lamar is on Thursday night, Scott."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 8, HEADLINE, DEK, build(), META, "dlffl-week-8.png", nav=NAV,
        published="2026-11-03T07:30:00-05:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "dlffl", "week-8.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
