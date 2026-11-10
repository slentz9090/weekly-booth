"""Dewart Lake FFL, Week 9. Editorial.

Boomer runs SCORCHING (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis and never gloats, clean language on the page, roast cap and Gil defenses apply. Mama Beth and DA,
never "Mother" or "Dad". Mama Beth is never the headline, Worst Owner or Boomer's jab target (standing
rule, 2026-11-03). No new segment this week: the page is the Week 8 structure with THE RACE (stays
through the playoff cut) after the Scoreboard. No series line on the cards, no Owner Spotlight.

Outlier engine, Week 9. HEADLINE tier: Spencer Lentz left C.J. Stroud on the bench for 40.36, the
11th-most points by one benched player in 6,775 since 2018; Geoff Cavender lost with Jordan Love's
39.18, the 17th-most by one starter in a losing lineup in 6,295 since 2018. PROMOTE: Scott Howard has
beaten Mama Beth seven straight (never a jab at her). SUPPORT: Ryan Reed 63.38 (7th-worst of his 84,
75th-lowest of 2,887 team-weeks) and Casey Couture 63.78 (4th-worst of his 255); Howard 148.30 (7th-best
of his 105), 3-6 on a 54-45 all-play; Calvelage 135.28 (5th-best of his 65) snapping DA's four straight
in the series; Cavender 6-3 on a 47-52 all-play; Spencer left 39.10 (49th-most of 1,405 team-weeks);
Doug Fields 91.02, out of the 92 to 106 range for the first time, by 0.98, with a best lineup of 101.72.

Verified against dlffl_wk9_facts.json, dlffl_season.json, dlffl_wk9_insights.json, dlffl_race_wk9.json
and gen2/data/dlffl_games.json.
"""
import json
import os

import booth
import race
from booth import award, boomer, calls_list, gil, graded_list, jump, ledger, mcard
from compute import DATA, by_owner, ledger_rows, load

FACTS = load("dlffl_wk9_facts.json")
SEASON = load("dlffl_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 163.76

NAV = (
    '<nav class="nav" aria-label="Sections"><ul>'
    '<li><a href="#board">The Scoreboard</a></li>'
    '<li><a href="#race">The Race</a></li>'
    '<li><a href="#calls">On The Record</a></li>'
    '<li><a href="#hardware">The Hardware</a></li>'
    '<li><a href="#ledger">The Bench Ledger</a></li>'
    '<li><a href="#wire">The Waiver Wire</a></li>'
    '<li><a href="#next">Next Sunday</a></li></ul></nav>'
)

HEADLINE = "Spencer Lentz Benched C.J. Stroud. C.J. Stroud Scored 40."
DEK = (
    "The man who runs this booth left 40.36 on his bench at quarterback, the 11th-most by one benched player in this league since 2018, and started the wrong kicker and the wrong defense beside it. Scott Howard went from Worst Owner to the high score of the week. Ryan Reed started two men who did not play, for the second week running. Doug Fields left the 92 to 106 range for the first time all season, by 0.98. Boomer went 4 and 8."
)
META = (
    "Gil and Boomer call Week 9 of the Dewart Lake FFL: Spencer Lentz benches C.J. Stroud's 40.36, Scott Howard goes from Worst Owner to the high score of the week, Ryan Reed starts two more players who did not play, Doug Fields misses his range by 0.98, and the race for four playoff spots with five weeks left."
)


def card_rows(win_owner, lose_owner):
    w, l = T[win_owner], T[lose_owner]
    return (
        {"team": w["name"], "owner": SEASON["owners"][win_owner]["display"], "score": w["score"], "left": w["left"]},
        {"team": l["name"], "owner": SEASON["owners"][lose_owner]["display"], "score": l["score"], "left": l["left"]},
    )


def race_section():
    """THE RACE: data from the FantasyPros pull after the ESPN roll, copy from race_wk9_copy.py."""
    p = os.path.join(DATA, "dlffl_race_wk9.json")
    if not os.path.exists(p):
        return '<h2 id="race">The Race</h2>'
    import race_wk9_copy
    return race.render(json.load(open(p)), race_wk9_copy.DL_COPY)


def build():
    parts = []
    teams = [(t["name"], SEASON["owners"][t["owner"]]["display"]) for t in FACTS["perTeam"]]
    parts.append(jump(teams))
    parts.append('<h2 id="board">The Scoreboard</h2>')

    # ---- 1. the forty on the bench
    w, l = card_rows("Spencer Lentz", "Geoff Cavender")
    parts.append(mcard(
        "m-lentz", "Spencer by 30.48, with a 40-point quarterback on his bench", w, l,
        "Bijan Robinson 26.70, Brock Bowers 21.80 and Drake Maye 18.26 for Spencer Lentz, who left C.J. Stroud's 40.36 on his bench, along with the better kicker and the better defense. Jordan Love 39.18 on a projection of 18.37 for Geoff Cavender, who got 0.50 from Josh Jacobs and started George Pickens, who did not play.",
        SCALE, key=True))
    parts.append(gil(
        "Spencer Lentz wins 124.66 to 94.18 and is 7 and 2, seven straight wins, first place on points over Kent Frenger, 1,209.50 to 1,134.32. He also left 39.10 on his bench, the most in the league this week, and all of it came at quarterback, kicker and defense. C.J. Stroud scored 40.36 behind Drake Maye's 18.26. Chase McLaughlin kicked 10.00 behind Jason Myers's 6.00. The Browns defense scored 8.00 behind the Patriots, who scored minus five. Stroud's 40.36 is the 11th-most points by one benched player in this league since 2018, out of 6,775."))
    parts.append(boomer(
        "The man who runs this booth had a quarterback score forty on his bench. Forty, Gil. Last week I laughed at Scott Howard on this page for less. He had two quarterbacks, two kickers and two defenses, and he went oh for three, which is hard to do with a coin. The Patriots defense scored minus five. At defense he would have been better off starting nobody and taking the zero. His best lineup was 163.76 and he turned in 124.66. He won the game and lost the week."))
    parts.append(gil(
        "In fairness to Geoff Cavender, Jordan Love's 39.18 was 20.81 over his projection, the biggest margin by any starter in the league this week, and it is the 17th-most points by one starter in a losing lineup since 2018. The other eight starters gave him 55.00. Josh Jacobs was projected for 15.10 and scored 0.50, George Pickens did not play, and Caleb Douglas scored 10.00 on the bench behind him. Cavender is 6 and 3 and holds the third seed with the sixth-most points in the league, 944.34. The series is 2 and 2."))
    parts.append(boomer(
        "Jordan Love was 42% of Geoff's points this week. One man carried the piano and the other eight brought 55 between them. I said he would score 110. He scored 94, and Love was 39 of it."))

    # ---- 2. the quarterback who played
    w, l = card_rows("Scott Howard", "Beth Couture")
    parts.append(mcard(
        "m-howard", "Howard's 148.30, the high score of the week, a week after he was Worst Owner", w, l,
        "Puka Nacua 31.00, Bucky Irving 26.50, Dak Prescott 22.50 and James Cook III 19.70 for Scott Howard, with DeMario Douglas's 15.70 on his bench the week he signed him. Luther Burden III 18.20, Patrick Mahomes 16.48 and the Chiefs defense 12.00 for Mama Beth.", SCALE))
    parts.append(gil(
        "Scott Howard wins 148.30 to 88.08 and is 3 and 6. The 148.30 is the high score of the week, it beats all eleven teams, and it is the seventh-best game of his 105 in this league. He started Dak Prescott, as Boomer called, and Prescott scored 22.50. James Cook III, who arrived in a trade with Doug Fields, scored 19.70 in his first start for Howard. It is his seventh straight win over Mama Beth, and he leads the series 8 and 4. Mama Beth is 1 and 8."))
    parts.append(boomer(
        "Seven days ago this man was Worst Owner. This week he moved one chair to the left, like I asked, and scored 148. Scott has the fifth-most points in the league and he is 3 and 6. Against the whole room, every week, he is 54 and 45. He has also left 229.60 on his bench this season, so some of that is homemade, but this week the bench was eight points and the scoreboard was a hundred and forty-eight, and for once I have nothing to yell at him about, which I do not enjoy."))
    parts.append(gil(
        "In fairness to Mama Beth, Justin Jefferson was projected for 16.05 and scored 7.30, Saquon Barkley scored 8.20, and she left only 6.80 on her bench. Tyler Allgeier, who scored 37.60 on her bench a week ago, started this week and scored 5.60. She signed Cairo Santos, who kicked 9.00. Against the whole league she is 26 and 73, about a win and a half better than her record."))
    parts.append(boomer(
        "She did the reasonable thing. Allgeier scored 37.60 on her bench last week, so she started him this week, and he went back to being Allgeier. Mama Beth, the lineup was fine. The players should apologize."))

    # ---- 3. two more ghosts
    w, l = card_rows("Adam Hershberger", "Ryan Reed")
    parts.append(mcard(
        "m-reed", "Hershberger by 44.10 over the low score of the week, and two more Reed starters who did not play", w, l,
        "Matthew Golden 30.40 on a projection of 15.48, Jake Bates 15.00 and Trevor Lawrence 14.58 for Adam Hershberger, with Rome Odunze's 14.00 and Denzel Boston's 12.80 on his bench. Bo Nix 15.68 and the Texans defense 12.00 for Ryan Reed, who started Cam Skattebo and Kendre Miller for zero apiece.", SCALE))
    parts.append(gil(
        "Adam Hershberger wins 107.48 to 63.38 and is 4 and 5. Matthew Golden's 30.40 was nearly double his projection. Ryan Reed's 63.38 is the low score of the week, it loses to all eleven teams, and it is the seventh-worst game of his 84 in this league. For the second week in a row he started two players who did not play: Cam Skattebo, and Kendre Miller, whom he signed this week. Jake Ferguson scored 9.10 on his bench, and so did Devin Singletary, also signed this week, for 4.90. He carries three defenses, and the two that played, the Texans and the Seahawks, scored 12.00 and 10.00. The series is 2 and 2."))
    parts.append(boomer(
        "Ryan, last week you started two men who were not playing and won, and I said if a full lineup was not an improvement I was done asking. So I am done asking. I am telling the people. He signed a running back this week, started him, and the running back did not play. He signed a second running back the same week, benched that one, and that one scored. Three defenses on the roster and one spot to start them in."))
    parts.append(gil(
        "In fairness to Ryan Reed, he is 4 and 5 and one game out of the last playoff spot, A.J. Brown is out, DK Metcalf and the Steelers defense were on their bye, and Jaxon Smith-Njigba was projected for 20.28 and scored 8.60. His best possible lineup was 77.38, which still loses by 30.10. Adam Hershberger left 15.60 behind, most of it Odunze and Boston on the bench while Jameson Williams scored 4.50 and Malik Nabers 6.80 in the lineup, and he has had 1,078.34 points scored against him, still the most in the league."))
    parts.append(boomer(
        "Hershberger benched a 14 and a 12.80, started a 4.50, and won by 44, so nobody is going to bring it up except me, right now. I called fifteen for Jameson Williams. Adam started him, the way I asked, and he scored four and a half. Matthew Golden scored thirty. I did not call that. Nobody called that. I am not sure Matthew Golden called that."))

    # ---- 4. out of the band
    w, l = card_rows("Kent Frenger", "Doug Fields")
    parts.append(mcard(
        "m-frenger", "Frenger's sixth straight, and Doug Fields leaves the 92 to 106 range by 0.98", w, l,
        "Kenneth Walker III 37.30 on a projection of 22.78, Ja'Marr Chase 29.50 and Ka'imi Fairbairn 17.00 for Kent Frenger, with Malik Washington at 3.10. Joe Burrow 29.54 for Doug Fields, who got 13.80 from Isaiah Likely and 9.30 from Drake London, both new this week by trade, started Ladd McConkey for zero, and left Seth McGowan's 10.70 on his bench.", SCALE))
    parts.append(gil(
        "Kent Frenger wins 129.56 to 91.02 and is 7 and 2, six straight wins, second on points. Doug Fields scored 91.02, and that ends the run: he had scored between 92.00 and 105.48 in each of the first eight weeks, and he missed the bottom of that range by 0.98. His best lineup was 101.72. He is 4 and 5. Fields still leads the series 10 and 5, and Frenger has won the last two."))
    parts.append(boomer(
        "Nine weeks I have been waiting for Doug Fields to do something. I pictured a 140. I pictured fireworks. He went out the bottom, Gil, by ninety-eight hundredths of a point. And his best lineup was 101.72, right in the middle of the range, so the only way Doug could get out was to bench the one man who would have kept him in. Seth McGowan, 10.70, on the bench. Ladd McConkey, zero, in the lineup. Doug finally escaped, and he did it through the basement."))
    parts.append(gil(
        "In fairness to Doug Fields, he gave up James Cook III in the trade with Scott Howard and got 23.10 back from Likely and London against Cook's 19.70, so the deal came out ahead on the day. Derrick Henry was projected for 14.19 and scored 5.58. Kent Frenger made three moves this week: he released Cam Little, who kicked 17.00, Bryce Young, who scored 20.34, and the Rams defense, who scored 11.00, for three players who combined for 17.30. None of the six was in his lineup."))
    parts.append(boomer(
        "Kent cut a kicker who scored 17 and started a different kicker who scored 17. Even his mistakes break even. He cut 48 points, signed 17, and won by 38. Six straight. But I looked ahead, Gil. His quarterback is Caleb Williams, and the Bears are off next week. The other quarterback on that roster was Bryce Young, until Kent showed him the door. His defense is Denver, also off next week. The other defense was the Rams. Same door. The champ packed for the trip and left the suitcase on the porch."))

    # ---- 5. the other Adam
    w, l = card_rows("Adam Calvelage", "dennis couture")
    parts.append(mcard(
        "m-da", "Calvelage by 25.72, his first win since Week 4, over the cleanest lineup in the league", w, l,
        "CeeDee Lamb 31.50, Brock Purdy 25.28, Jonah Coleman 16.80 and Travis Kelce 15.30 for Adam Calvelage, with the Giants defense at 14.00 the week he signed them and Garrett Wilson, who did not play, in the flex. Christian Watson 29.60 on a projection of 13.69, Christian McCaffrey 21.70 and the Bills defense 15.00 for DA, with Josh Allen at 12.86 and Ryan Fitzgerald at 2.00.", SCALE))
    parts.append(gil(
        "Adam Calvelage wins 135.28 to 109.56 and is 4 and 5. It ends a four-game losing streak, it is the fifth-best game of his 65 in this league, and against everyone this week he went 10 and 1. He started Brock Purdy over Jayden Daniels, and Purdy scored 25.28 to Daniels's 14.56. DA had won four straight in the series and still leads it 4 and 2. DA is 5 and 4, the fourth seed, third in points at 1,064.76. He left 0.70 on his bench, the least in the league."))
    parts.append(boomer(
        "I told Adam on this page that if he started Purdy, my call was dead on arrival and so was my patience. He started Purdy. Purdy scored 25. Daniels scored 14 on the bench. Adam Calvelage read my advice, did the opposite, and had the fifth-best day of his career. There is a lesson in that and I refuse to learn it. And DA left seven tenths of a point on his bench. Seven tenths. The elder turned in the cleanest lineup in the league and lost by 25, which is what happens when the lineup is clean and Josh Allen is not."))
    parts.append(gil(
        "In fairness to DA, Josh Allen was projected for 20.84 and scored 12.86, Kyren Williams scored 7.60 on a projection of 15.81, and the Bills defense he signed this week gave him 15.00. He has left 61.70 on his bench all season, now the fewest in the league. Calvelage did start Garrett Wilson, who did not play, with Jakobi Meyers's 8.50 on his bench."))
    parts.append(boomer(
        "DA is 5 and 4 with the third-most points in the league, and Scott Reisert is 5 and 4 right behind him for the last playoff chair. Thirty-four points separate them. That is one Josh Allen afternoon, in either direction. And Adam: 3 and 1, then four straight losses, then 135. I do not know which Adam shows up next week, and neither does the other Adam, who he plays."))

    # ---- 6. the milk
    w, l = card_rows("Scott Reisert", "Casey Couture")
    parts.append(mcard(
        "m-casey", "Reisert by 32.62 with a zero and a minus in his lineup, over the fourth-worst game of Casey Couture's career", w, l,
        "Javonte Williams 23.40, KC Concepcion 17.80 and Dominic Zvada 17.00 the week he signed him for Scott Reisert, with Jared Goff at 5.30, Adonai Mitchell at zero and Mike Washington Jr. at minus 0.30. Chris Olave 13.30 for Casey Couture, with Jonathan Taylor at 6.90 on a projection of 19.42 and D'Andre Swift at 3.10 on a projection of 18.04.", SCALE))
    parts.append(gil(
        "Scott Reisert wins 96.40 to 63.78 and is 5 and 4, level with DA for the fourth playoff spot and behind him on points. Dominic Zvada, signed this week, kicked 17.00. Casey Couture's 63.78 is the fourth-worst game of his 255 in this league, and it beat one team this week. Jonathan Taylor, D'Andre Swift and Ollie Gordon II were projected for 54.05 between them and scored 16.90. Casey is 4 and 5 and has lost two straight. He leads the series 5 and 3."))
    parts.append(boomer(
        "Last week I said Casey picks up a quarterback the way you pick up milk. This week the milk turned. He cut Tyler Shough, who scored 19.70, for J.J. McCarthy, who scored 7.28 in his lineup. He cut the Packers defense, who scored 11, for the Saints, who scored 4. Five rings, and he spent the week swapping good groceries for bad ones. And I picked him to win. Of course I picked him."))
    parts.append(gil(
        "In fairness to Casey Couture, he left 2.30 on his bench, so the lineup was nearly clean, and no lineup he had beats 96.40. Kyler Murray, last week's quarterback, did not play. Scott Reisert started Adonai Mitchell for zero and Mike Washington Jr. for minus 0.30, both signed this week, with Courtland Sutton's 13.00 and Keenan Allen's 4.60 on his bench. Jahmyr Gibbs was projected for 25.80 and scored 13.40."))
    parts.append(boomer(
        "Scott signed three men this week and started all three. The kicker scored 17. The other two combined for negative three tenths of a point. He left 17.90 on the bench and won by 32. Last week his bench beat him. This week it tried again and could not get there. Reisert is 5 and 4, Gil, and he got there on a week when a kicker named Zvada outscored Jahmyr Gibbs."))

    # ---- THE RACE
    parts.append(race_section())

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls came due. Four right, eight wrong. Season record 42 and 54. Three of the four I got right were Scott Howard or the champ. Every call is below, in ink."))
    parts.append(graded_list([
        ("Balls Deep", "Spencer Lentz beats Geoff Cavender.", "RIGHT",
         "By 30.48, with forty points of quarterback on the bench. I bet on the points. The points showed up. Most of them started."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender scores 110 or more in Week 9.", "WRONG",
         "94.18. Jordan Love scored 39.18 by himself, so the other eight starters needed 71 and brought 55. I said he would finally score like a 6 and 2 team. He scored like Jordan Love and eight guys."),
        ("Berlin Blitz", "Kent Frenger beats Doug Fields.", "RIGHT",
         "By 38.54. Fields still leads the series 10 and 5, and I still have a short memory. Six straight for Kent."),
        ("Cosby Copperheads", "Doug Fields scores between 92 and 106 again.", "WRONG",
         "91.02. Eight for eight, and the one week I bet on boring, he missed boring by 0.98, with the 10.70 that saves the call on his bench."),
        ("DA The Badenov's", "DA beats Adam Calvelage for the fifth straight time.", "WRONG",
         "Lost by 25.72 with seven tenths of a point on his bench. The elder had a pattern. Adam Calvelage had CeeDee Lamb."),
        ("An alBum Cover", "Jayden Daniels clears 20 for Adam Calvelage.", "WRONG",
         "He did not start. Purdy did, for 25.28. Daniels scored 14.56 on the bench, so I was wrong sitting down and wrong standing up."),
        ("The Scranton Strangler", "Scott Howard beats Mama Beth for the seventh straight time.", "RIGHT",
         "By 60.22. Seven straight in the series. I said he would have to earn it, and he earned it with the high score of the week."),
        ("The Scranton Strangler", "Scott Howard starts Dak Prescott in Week 9.", "RIGHT",
         "Started, 22.50. One chair to the left. I have never been prouder of a man for doing the obvious."),
        ("BearDown", "Ryan Reed beats Adam Hershberger.", "WRONG",
         "Lost by 44.10 with the low score of the week. Matthew Golden scored 30 for the other side and I had not accounted for Matthew Golden."),
        ("Holy Rollers", "Jameson Williams clears 15 for Adam Hershberger.", "WRONG",
         "He started, which was the hard part, and scored 4.50, which was the other part."),
        ("One Under akaThe Mulligan", "Casey Couture beats Scott Reisert.", "WRONG",
         "Lost by 32.62 with the fourth-worst score of his career. I bet on the man who does less. He did less."),
        ("Simba St. Gibbs Lion Kings", "Jahmyr Gibbs clears 20 again for Scott Reisert.", "WRONG",
         "13.40 on a projection of 25.80. The one man on that roster Scott left alone, and he took the afternoon off without leaving the field."),
    ]))
    parts.append(gil(
        "Four right, eight wrong. Twelve new ones for Week 10, one per team. The Eagles, Buccaneers, Bears and Broncos are off, so Saquon Barkley, Bucky Irving, Caleb Williams, D'Andre Swift, Bo Nix and the Bears and Broncos defenses sit this one out."))
    parts.append(calls_list([
        ("Balls Deep", "Spencer Lentz leaves under ten on his bench in Week 10.",
         "He left 39.10 this week at quarterback, kicker and defense. He leads the league in points and he has now left 120.66 behind on the season. I am betting a man can only go oh for three at the one-chair positions once. Flip the coin if you have to, Spencer, but look at it when it lands."),
        ("One Under akaThe Mulligan", "Jonathan Taylor clears 15 for Casey Couture.",
         "Projected for 19.42 this week, scored 6.90. Casey leads Spencer 13 and 10 lifetime, five of those in the playoffs, and has won the last two. Swift is off with the Bears. If Casey is going to make it three, it starts with the man he drafted to carry him."),
        ("Berlin Blitz", "Kenneth Walker III clears 20 again for Kent Frenger.",
         "37.30 this week, and Kansas City is at Atlanta. Kent needs him, because his quarterback and his defense are both off and he cut the spares. I am betting on the one piece of that roster I know is playing."),
        ("DA The Badenov's", "DA beats Kent Frenger.",
         "DA leads the series 14 and 11, one of those in the playoffs, though Kent has won the last two. Kent has won six straight and does not have a quarterback for Sunday as of this page. Josh Allen is at the Jets. The elder is fourth by 34 points and needs this one more than the champ does."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender beats Mama Beth.",
         "Geoff is 2 and 0 against her. His defense is the Bears, who are off, so the Ravens come off his bench, and she loses Barkley, Goedert, Burden and her kicker to the bye. I am betting on Geoff's luck one more time, and I would be happy to lose this one."),
        ("Momma's Boys", "Justin Jefferson clears 15 for Mama Beth.",
         "Projected for 16.05, scored 7.30. Minnesota is at Green Bay. She has three titles, and the best receiver in her building has been quiet. I am betting he remembers who he plays for."),
        ("The Scranton Strangler", "Scott Howard beats Ryan Reed.",
         "Howard leads 2 and 1 and just scored 148. Puka Nacua is listed as doubtful, and Bucky Irving and his defense are on the bye. Ryan loses Bo Nix. Scott has the fifth-most points in the league and three wins. I am betting the points finally count."),
        ("BearDown", "Ryan Reed scores 90 or more in Week 10.",
         "He has started two men who did not play in back-to-back weeks and scored 91 and 63. I am betting nine players who are playing gets him to 90. That is the whole call, Ryan. Attendance."),
        ("An alBum Cover", "CeeDee Lamb clears 20 again for Adam Calvelage.",
         "31.50 this week, and Dallas is home to San Francisco. Adam just ignored my advice and scored 135, so this time I am calling the one thing on his roster that does not need any."),
        ("Holy Rollers", "Adam Hershberger beats Adam Calvelage.",
         "Hershberger leads the series 4 and 3, and Calvelage has won the last two. Hershberger has had the most points scored against him in the league and is still 4 and 5. Loveland is off with the Bears, so he needs a tight end. I am betting on the Adam who has had the harder road."),
        ("Cosby Copperheads", "Doug Fields scores between 92 and 106 in Week 10.",
         "He went out through the basement with his best lineup sitting in the middle of the range. I am betting he comes back up the stairs."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert beats Doug Fields for the first time.",
         "Fields is 4 and 0 against him. Reisert is 5 and 4, level with DA for the last playoff chair, and he just won with a zero and a minus in his lineup. I am betting on the man who has never done it, because he has never needed it more."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, then by size. When an owner already holds one, the next name in line takes it."))
    parts.append(award(
        "good", "Owner of the Week", "Scott Howard · The Scranton Strangler",
        "148.30, the high score of the week, a win against all eleven teams, and the seventh-best game of his 105 in this league. Nacua 31.00, Irving 26.50, Prescott 22.50, Cook 19.70, and 8.30 left behind. He was Worst Owner on this page a week ago.",
        "Worst Owner to Owner of the Week in seven days. Scott, you are 3 and 6 with the fifth-most points in the league and 229.60 on your bench for the season. Fix the second number and the first one follows."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Ryan Reed · BearDown",
        "63.38, the low score of the week, a loss to all eleven teams, and a loss by 44.10. Cam Skattebo and Kendre Miller started and did not play, the second straight week with two such starters, and Miller was signed this week. Jake Ferguson's 9.10 and Devin Singletary's 4.90 sat on the bench, 14.00 left behind, with three defenses on a roster that can start one.",
        "Two weeks, four starters who did not play. He has three defenses and started two running backs who were not in uniform. Ryan, I am begging you. Before Sunday, open the app, find the word OUT next to a name, and believe it."))
    parts.append(award(
        "good", "Start of the Week", "Geoff Cavender · Jordan Love, 39.18",
        "Projected for 18.37, so 20.81 over, the biggest margin over projection by any starter in the league this week. Christian Watson's 29.60 for DA was 15.91 over and second, and Matthew Golden's 30.40 for Adam Hershberger 14.92 over and third. Love's 39.18 is the 17th-most points by one starter in a losing lineup since 2018.",
        "Geoff gets a trophy for starting his own quarterback, and I am handing it over with a straight face, because the man lost by 30 and should carry something home. Thirty-nine from Love. Half a point from Josh Jacobs. Geoff, the trophy is real."))
    parts.append(award(
        "bad", "Sit of the Week", "Spencer Lentz · C.J. Stroud, 40.36 on the bench",
        "Drake Maye started in his place for 18.26, a 22.10 swing, the biggest benching in the league this week and the 11th-most points by one benched player since 2018, out of 6,775. No benching cost a game this week, so the award goes by size. Scott Reisert's Courtland Sutton behind Adonai Mitchell was 13.00 and second.",
        "He has two quarterbacks and they take turns being the wrong one. Stroud scored 25.98 on that bench in Week 6 and 40.36 on it this week. Spencer, you are first in points with seven straight wins, and you benched forty. The lineup is 7 and 2. The man setting it went oh for three on Sunday with two options at every spot."))
    parts.append(award(
        "bad", "Waste of the Week", "Scott Reisert · 17.90 left behind, and he won",
        "Courtland Sutton scored 13.00 on his bench behind Adonai Mitchell's zero, and Keenan Allen 4.60 behind Mike Washington Jr.'s minus 0.30. Spencer Lentz left 39.10 in his win and already holds a trophy. Adam Hershberger left 15.60 in his.",
        "Scott held Sit of the Week last week and Waste of the Week this week, so he is working his way down the shelf. Last week the bench beat him. This week he outran it. Scott, the wire handed you a kicker who scored 17 and two men who combined for less than zero, and you started all three."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All twelve of you, every week, all season. Scott Howard still leads at 229.60, and for once he added almost nothing, 8.30 in the high score of the week. Ryan Reed is second at 146.14 and Mama Beth third at 145.08. The man who runs this booth added 39.10 in one afternoon, more than Frenger, DA, Howard, Casey and Mama Beth left behind put together. And there is a new cleanest man in the league: DA, 61.70, who passed Scott Reisert and Kent Frenger by leaving seven tenths of a point."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 9, season_note=(
        "Season totals come from the season ledger through Week 9. Scott Howard leads at 229.60, Ryan Reed is second at 146.14, Mama Beth third at 145.08. DA has left the fewest, 61.70.")))
    parts.append(gil(
        "No bench cost a game this week. In each of the last four weeks at least one did. The closest was Geoff Cavender, who left 14.50 and lost by 30.48. Ryan Reed left 14.00 and lost by 44.10. Spencer Lentz left 39.10 and won. DA left 0.70 and lost."))
    parts.append(boomer(
        "DA left seven tenths and lost by 25. Spencer left 39 and won by 30. If I were DA I would stop reading this section."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Scott Reisert signing Dominic Zvada, who started and kicked 17.00, for Chris Boswell, whose Steelers were off. The biggest swing of any move in the league this week. Adam Calvelage's Giants defense for the Jets was 14.00 to 2.00 and second, and DA's Bills defense for the Commanders was 15.00 to 5.00 and third."))
    parts.append(gil(
        "<strong>Worst move that made a lineup:</strong> Casey Couture releasing Tyler Shough, who scored 19.70, for J.J. McCarthy, who started and scored 7.28, a 12.42 swing against him. His Saints defense for the Packers was 4.00 to 11.00, another 7.00. Kent Frenger's three releases, Cam Little, Bryce Young and the Rams defense, scored 48.34 between them against 17.30 for the three players he signed. The biggest single swing of the week was his Elijah Mitchell for Cam Little, 4.10 to 17.00, and none of it touched his lineup."))
    parts.append(boomer(
        "Ryan Reed cut J.J. McCarthy. Casey Couture picked McCarthy up, started him, and cut Tyler Shough to do it. Shough then outscored McCarthy by twelve from the street. Casey looked at a quarterback another team did not want and cut a better one to get him."))
    parts.append(gil(
        "Eighteen moves went through, and one trade. Scott Howard got James Cook III from Doug Fields for Drake London and Isaiah Likely, the first trade completed in this league since 2024. Cook scored 19.70 for Howard, and London and Likely scored 23.10 for Fields. A second trade has been accepted and is in the league's review window: Ryan Reed would send Jaxon Smith-Njigba to Spencer Lentz for Jaylen Warren and Nico Collins. It is not final, so it is not graded here."))
    parts.append(boomer(
        "That one involves the man who runs this booth, so Gil read it and I am keeping my hands folded."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Adam Calvelage at Adam Hershberger, Ryan Reed at Scott Howard, DA at Kent Frenger, Mama Beth at Geoff Cavender, Doug Fields at Scott Reisert, and Spencer Lentz at Casey Couture. The Eagles, Buccaneers, Bears and Broncos are off. Washington plays at the Giants on Thursday night, so Jayden Daniels, J.J. McCarthy, Malik Nabers, Isaiah Likely, Dominic Zvada and the Giants defense are done before Sunday. New England and Detroit kick off at 9:30 Sunday morning. The Chargers play at Baltimore on Monday night."))
    parts.append(boomer(
        "DA at Kent is the game. Fourth place against a share of first, the elder against the champ, 14 and 11 lifetime, and one of them does not have a quarterback yet. Reisert gets Doug Fields, who has beaten him all four times, with a playoff chair on the table. Spencer goes to Casey, who has five rings, a 13 and 10 lead on him, and the fourth-worst score of his life fresh in the mirror. Casey off a 63 is either the most dangerous man in this league or the least, and nobody has ever been able to tell which until it is over. And Scott Howard, fresh off 148, gets Ryan Reed with both of them missing starters to the bye."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 9, HEADLINE, DEK, build(), META, "dlffl-week-9.png", nav=NAV,
        published="2026-11-10T04:00:00-05:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "dlffl", "week-9.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
