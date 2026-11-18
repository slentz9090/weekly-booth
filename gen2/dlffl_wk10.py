"""Dewart Lake FFL, Week 10. Editorial.

Boomer runs SCORCHING (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis and never gloats, clean language on the page, roast cap and Gil defenses apply. Mama Beth and DA,
never "Mother" or "Dad". Mama Beth is never the headline, Worst Owner or Boomer's jab target (standing
rule, 2026-11-03). No new segment: the Week 9 structure with THE RACE (stays through the playoff cut)
after the Scoreboard. No series line on the cards, no Owner Spotlight.

Outlier engine, Week 10. HEADLINE tier: Scott Reisert lost with Jahmyr Gibbs's 43.70 (6th-most by one
starter in a loss in 6,349 since 2018); Drake Maye 3.02 on a projection of 23.23 for Spencer Lentz
(13th-worst miss by a projected 10-point starter in 7,736); Christian McCaffrey 49.30 for DA (14th-best
start in 12,711 player-weeks). PROMOTE: Mama Beth lost with Patrick Mahomes's 38.42 (never a jab at
her). SUPPORT: Doug Fields five straight over Reisert; Adam Hershberger lost by 12.68 with 34.90 on the
bench; Kent Frenger lost by 6.64 with 12.50 on the bench; George Pickens 41.00 for Geoff Cavender;
Casey Couture 77.92 (15th-worst of his 256); Cavender 7-3 on a 53-57 all-play; Howard 4-6 on 62-48.
The page leads with the Rams defense: Kent Frenger released it in Week 9 (see the Week 9 page), DA
claimed it in Week 10, it scored 16.00, and DA won by 6.64.

Verified against dlffl_wk10_facts.json, dlffl_season.json, dlffl_wk10_insights.json,
dlffl_race_wk10.json and gen2/data/dlffl_games.json.
"""
import json
import os

import booth
import race
from booth import award, boomer, calls_list, gil, graded_list, jump, ledger, mcard
from compute import DATA, by_owner, ledger_rows, load

FACTS = load("dlffl_wk10_facts.json")
SEASON = load("dlffl_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 187.54

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

HEADLINE = "Kent Frenger Cut The Rams Defense. It Scored 16 For DA, Who Beat Him By 6.64."
DEK = (
    "The champ's six-game winning streak ended against a defense he released a week ago, with 13.50 on his bench behind a receiver who scored 1.00. Adam Hershberger benched 44.30 points of running back and lost by 12.68. Doug Fields scored between 92 and 106 for eight straight weeks, then 91, then 131. The man who runs this booth left 36.02 on his bench after Boomer bet he would leave under ten. Boomer went 4 and 8."
)
META = (
    "Gil and Boomer call Week 10 of the Dewart Lake FFL: DA beats Kent Frenger by 6.64 with the Rams defense Frenger released, Adam Hershberger benches 44.30 points of running back in a loss by 12.68, Doug Fields scores 131.06, and the race for four playoff spots with four weeks left."
)


def card_rows(win_owner, lose_owner):
    w, l = T[win_owner], T[lose_owner]
    return (
        {"team": w["name"], "owner": SEASON["owners"][win_owner]["display"], "score": w["score"], "left": w["left"]},
        {"team": l["name"], "owner": SEASON["owners"][lose_owner]["display"], "score": l["score"], "left": l["left"]},
    )


def race_section():
    """THE RACE: data from the FantasyPros pull after the ESPN roll, copy from race_wk10_copy.py."""
    p = os.path.join(DATA, "dlffl_race_wk10.json")
    if not os.path.exists(p):
        return '<h2 id="race">The Race</h2>'
    import race_wk10_copy
    return race.render(json.load(open(p)), race_wk10_copy.DL_COPY)


def build():
    parts = []
    teams = [(t["name"], SEASON["owners"][t["owner"]]["display"]) for t in FACTS["perTeam"]]
    parts.append(jump(teams))
    parts.append('<h2 id="board">The Scoreboard</h2>')

    # ---- 1. the defense he cut
    w, l = card_rows("dennis couture", "Kent Frenger")
    parts.append(mcard(
        "m-da", "DA by 6.64, with the defense Kent Frenger released a week ago", w, l,
        "Christian McCaffrey 49.30 on a projection of 20.30, Josh Allen 22.34 and the Rams defense 16.00 the week he claimed it for DA. Ja'Marr Chase 32.60, Tony Pollard 19.90 and Bhayshul Tuten 18.80 for Kent Frenger, who started Germie Bernard for 1.00 with Jordyn Tyson's 13.50 on his bench.",
        SCALE, key=True))
    parts.append(gil(
        "DA wins 128.34 to 121.70 and is 6 and 4, alone in the fourth playoff spot, one game clear of three teams at 5 and 5. It ends Kent Frenger's winning streak at six. Christian McCaffrey's 49.30 is the 14th-best start in this league since 2018, out of 12,711. The Rams defense scored 16.00 for DA the week he claimed it. Kent Frenger released that defense a week ago, and the Packers defense he claimed this week scored 4.00 in his lineup. DA leads the series 15 and 11."))
    parts.append(boomer(
        "Last week I said the champ packed for the trip and left the suitcase on the porch. The suitcase was the Rams defense. DA walked by, picked it up, and beat him over the head with it. Sixteen from the Rams. Four from the Packers. That is a twelve-point swing in a game Kent lost by 6.64. And it gets worse, Gil. Kent released three players last week. The Rams scored 16 for DA. Cam Little kicked 19 for Spencer. Bryce Young started for Ryan Reed. Kent Frenger is running a job placement office for the rest of this league."))
    parts.append(gil(
        "In fairness to Kent Frenger, Kenneth Walker III did not play and Caleb Williams and the Broncos defense were on their bye, so three of his regular starters were unavailable, and Jacoby Brissett, signed this week, gave him 14.80. He is 7 and 3 and second in the league in points at 1,256.02. He also left 12.50 on his bench and lost by 6.64: Germie Bernard scored 1.00 in the flex with Jordyn Tyson's 13.50 and Malik Washington's 11.86 behind him. His best lineup was 134.20."))
    parts.append(boomer(
        "Two receivers on the bench with 13.50 and 11.86, and the man in the lineup scored one point. One. Either of them wins the game. Chase gave him 32.60 and the flex gave him one. Kent had 25 points of receiver on the bench and started the only one who could not find two. And DA? The elder got 49.30 from McCaffrey and 4.20 from Kyren Williams and 5.20 from Christian Watson, and it did not matter, because he read the waiver wire and Kent wrote it."))

    # ---- 2. the running backs on the bench
    w, l = card_rows("Adam Calvelage", "Adam Hershberger")
    parts.append(mcard(
        "m-adams", "Calvelage by 12.68, over a bench that held 44.30 points of running back", w, l,
        "Brock Purdy 36.66 on a projection of 21.91, CeeDee Lamb 16.70 and Garrett Wilson 15.10 for Adam Calvelage. Trevor Lawrence 29.78, Blake Corum 22.40 and the Colts defense 14.00 for Adam Hershberger, who left Chase Brown's 24.30 and Omarion Hampton's 20.00 on his bench and started Denzel Boston for 2.10.", SCALE))
    parts.append(gil(
        "Adam Calvelage wins 118.96 to 106.28 and is 5 and 5 with two straight wins. He started Brock Purdy over Jayden Daniels again, and Purdy scored 36.66 to Daniels's 20.76. Adam Hershberger left 34.90 on his bench and lost by 12.68. Chase Brown scored 24.30 and Omarion Hampton 20.00 behind Zach Charbonnet's 9.40 and Denzel Boston's 2.10. His best lineup was 141.18, which would have been the second-highest score in the league this week. He is 4 and 6. The series is 4 and 4, and Calvelage has won the last three."))
    parts.append(boomer(
        "Forty-four point three, Gil. Two running backs. On the bench. Together. Adam Hershberger had the second-best score in the league sitting on his roster and turned in the ninth-best one. Chase Brown was right there. Omarion Hampton was right there. Denzel Boston got the start and scored 2.10. I picked Hershberger to win this game, and he had it won on paper. He just had it won on the wrong side of the roster."))
    parts.append(gil(
        "In fairness to Adam Hershberger, Brown was projected for 11.42, only 0.15 more than Boston, and Hampton for 7.54, well under Charbonnet's 14.32, Colston Loveland and Rome Odunze were on their bye, and he has had 1,197.30 points scored against him, still the most in the league. The Colts defense he signed this week scored 14.00. In fairness to Calvelage, he left 4.30 on his bench, and Purdy over Daniels has now been the right call two weeks running."))
    parts.append(boomer(
        "Calvelage is 5 and 5. I told him to start Jayden Daniels two weeks ago, he has started Purdy both weeks since, and Purdy has scored 25 and 36. I am going to keep giving Adam advice. It is clearly working, just not in the direction I intended."))

    # ---- 3. through the roof
    w, l = card_rows("Doug Fields", "Scott Reisert")
    parts.append(mcard(
        "m-fields", "Fields scores 131.06, his high of the season, and is 5 and 0 against Reisert", w, l,
        "Joe Burrow 37.16, Isaiah Likely 27.20 and Drake London 16.90 for Doug Fields, with Seth McGowan's 13.70 on his bench for the second straight week. Jahmyr Gibbs 43.70 on a projection of 22.91 and Jared Goff 24.42 for Scott Reisert, with Dominic Zvada at 2.00 and the Jaguars defense at 3.00.", SCALE))
    parts.append(gil(
        "Doug Fields wins 131.06 to 112.62 and is 5 and 5. The 131.06 is his high score of the season and the second-highest score in the league this week, a 10 and 1 day against the field. He scored between 92.00 and 105.48 in each of the first eight weeks, then 91.02, then this. Isaiah Likely and Drake London, who arrived in the trade with Scott Howard, scored 44.10 between them. Fields has beaten Scott Reisert all five times they have played. Reisert is 5 and 5 and lost with Jahmyr Gibbs's 43.70, the sixth-most points by one starter in a losing lineup since 2018, out of 6,349."))
    parts.append(boomer(
        "Last week Doug left the range through the basement, so I bet he would walk back up the stairs. He took the elevator to the roof. A hundred and thirty-one. I have now been wrong about Doug Fields being boring in both directions in consecutive weeks, and I would like the league office to look into it. And Scott Reisert got 43.70 from Gibbs and lost, because his kicker scored two. The same kicker who scored 17 last week. Zvada giveth, Gil."))
    parts.append(gil(
        "In fairness to Scott Reisert, he left 4.20 on his bench, tied for the least in the league, so there was no better lineup to set. Javonte Williams was projected for 14.15 and scored 7.20. Fields, for his part, started Tre Tucker for 1.40 and Audric Estime for 1.60 with Seth McGowan's 13.70 on the bench. McGowan scored 10.70 on that bench a week ago."))
    parts.append(boomer(
        "Seth McGowan has scored 24.40 on Doug's bench in two weeks and Doug keeps starting the men next to him. Doug won by 18, so I will say it quietly. I picked Reisert to finally beat him. Five and oh. Reisert is now 5 and 5, tied with two other teams, and looking up at DA. Doug spent eight weeks between 92 and 106 against everybody else and saved the 131 for Scott."))

    # ---- 4. the quarterback
    w, l = card_rows("Spencer Lentz", "Casey Couture")
    parts.append(mcard(
        "m-lentz", "Spencer by 73.60, with 3.02 at quarterback and 36.02 on his bench", w, l,
        "Emmett Johnson 35.10 the week he signed him, Chuba Hubbard 31.70, Jaxon Smith-Njigba 31.10 and Cam Little 19.00 for Spencer Lentz, with Drake Maye at 3.02 and Parker Washington's 27.70 and C.J. Stroud's 20.44 on his bench. Stefon Diggs 17.30 and Fernando Mendoza 13.92 for Casey Couture, who started Jordan Addison, who did not play.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 151.52 to 77.92 and is 8 and 2, alone in first place by a game, with eight straight wins. It is the high score of the week. Drake Maye left his game on the first drive with an ankle injury and scored 3.02 on a projection of 23.23, the 13th-worst miss by a starter projected for ten or more in this league since 2018, out of 7,736. C.J. Stroud scored 20.44 on the bench behind him. Parker Washington scored 27.70 on the bench behind Tee Higgins's 9.10. Spencer left 36.02 behind, the most in the league. Casey Couture's 77.92 is the low score of the week. Casey still leads the series 13 and 11."))
    parts.append(boomer(
        "I bet, in ink, that the man who runs this booth would leave under ten points on his bench. He left 36.02. Last week Stroud scored 40 on that bench behind Maye. This week Stroud scored 20 on it behind a 3.02. Two weeks, 60 points of quarterback, none of it started. And Parker Washington scored 27.70 behind a man who scored 9.10. He signed three defenses this week and they scored four, minus one and minus seven. Spencer's best lineup was 187.54. He turned in 151.52."))
    parts.append(gil(
        "In fairness to Casey Couture, Jonathan Taylor was projected for 17.26 and scored 11.30, Chris Olave was projected for 13.55 and scored 4.50, and D'Andre Swift was on his bye. His best lineup was 88.92. He did start Jordan Addison, who was out, in the flex with Pat Freiermuth's 10.50 on his bench. He is 4 and 6 and has lost three straight."))
    parts.append(boomer(
        "Casey has five rings and started a man who was ruled out, so even the great ones have a Sunday. I called fifteen for Jonathan Taylor. He scored 11.30. Taylor scored 6.90 the week before that. I bet on the bounce and Taylor declined the invitation."))

    # ---- 5. the receiver who did not play last week
    w, l = card_rows("Geoff Cavender", "Beth Couture")
    parts.append(mcard(
        "m-cavender", "Cavender by 21.78 behind George Pickens's 41.00", w, l,
        "George Pickens 41.00 on a projection of 10.30 and Amon-Ra St. Brown 24.80 for Geoff Cavender, with Jordan Love at 10.80 and Matthew Stafford's 19.76 on his bench. Patrick Mahomes 38.42 and the Vikings defense 21.00 for Mama Beth, with Saquon Barkley and Luther Burden III on their bye.", SCALE))
    parts.append(gil(
        "Geoff Cavender wins 120.60 to 98.82 and is 7 and 3, third in the standings. George Pickens, who did not play a week ago, scored 41.00 on a projection of 10.30, the biggest margin over projection by any starter in the league this week. Cavender is 3 and 0 against Mama Beth. Mama Beth got 38.42 from Patrick Mahomes and 21.00 from the Vikings defense, the best quarterback and the best defense in the league this week, and is 1 and 9."))
    parts.append(boomer(
        "Last week Geoff started George Pickens and Pickens did not play. This week Pickens scored 41. Geoff Cavender does not manage a roster, he stands under it and waits for things to fall. He is 7 and 3 and against the whole league, every week, he is 53 and 57. Jordan Love scored 39 for him in a loss and 10.80 for him in a win. Nothing about this man's season is connected to anything else about this man's season."))
    parts.append(gil(
        "In fairness to Mama Beth, Justin Jefferson was projected for 16.57 and scored 11.90, Saquon Barkley and Luther Burden III were off, and nobody in the league got more from quarterback and defense combined than her 59.42. In fairness to Geoff Cavender, he is 7 and 3 and has left 87.70 on his bench all season, the fourth-fewest in the league. Against the whole league she is 27 and 83, about a win and a half better than her record."))
    parts.append(boomer(
        "I called fifteen for Jefferson and he scored 11.90, so that one is on me and on him, in that order. Mama Beth had the best quarterback and the best defense in the building and lost to a man whose receiver scored four times his projection. I have no lineup advice for that. Call it weather."))

    # ---- 6. attendance
    w, l = card_rows("Scott Howard", "Ryan Reed")
    parts.append(mcard(
        "m-howard", "Howard by 23.72 with 4.20 on his bench, his third win in four weeks", w, l,
        "Dak Prescott 37.42 on a projection of 17.40, James Cook III 25.70 and Deebo Samuel Sr. 25.40 the week he claimed him for Scott Howard. Cam Skattebo 25.70, Nico Collins 19.90 and Harold Fannin Jr. 12.60 for Ryan Reed, with Bryce Young at 8.10 on a projection of 20.09.", SCALE))
    parts.append(gil(
        "Scott Howard wins 126.12 to 102.40 and is 4 and 6, with three wins in his last four games. He left 4.20 on his bench, tied for the least in the league. Deebo Samuel Sr., claimed this week, scored 25.40 in his lineup. Howard has the fifth-most points in the league, 1,135.22, and against the whole league he is 62 and 48. He has beaten Ryan Reed three straight times and leads the series 3 and 1. Reed is 4 and 6."))
    parts.append(boomer(
        "Scott Howard leads this league in points left on the bench for the season, 233.80, and this week he left 4.20. Four point two. I do not know who this man is. He claimed a receiver, started him, and the receiver scored 25. He started his quarterback and the quarterback scored 37. Scott, where was this in September? You are 4 and 6 with a 62 and 48 team."))
    parts.append(gil(
        "In fairness to Ryan Reed, all nine of his starters played this week, Bo Nix was on his bye, and A.J. Brown returned from injury and scored 3.70. Bryce Young, claimed to cover for Nix, was projected for 20.09 and scored 8.10. Reed left 17.70 behind: DK Metcalf's 14.40 and the Seahawks defense's 12.00 sat behind Brown and the Texans defense's 5.00."))
    parts.append(boomer(
        "I asked Ryan for one thing last week. Attendance. Nine men in uniform. He delivered, he scored 102, and my call came home. So I am proud of him, and I am also going to point out that he carries two defenses and started the one that scored five while the one on the bench scored twelve. Baby steps, Ryan. Everybody showed up. Next week we work on which ones."))

    # ---- THE RACE
    parts.append(race_section())

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls came due. Four right, eight wrong. Season record 46 and 62. I had DA over the champ, which is the one I will be bringing up all week. Every call is below, in ink."))
    parts.append(graded_list([
        ("DA The Badenov's", "DA beats Kent Frenger.", "RIGHT",
         "By 6.64. I said the elder needed it more than the champ did, and then the champ handed him a defense to do it with."),
        ("Berlin Blitz", "Kenneth Walker III clears 20 again for Kent Frenger.", "WRONG",
         "He did not play. I said I was betting on the one piece of that roster I knew was playing. I did not know."),
        ("Balls Deep", "Spencer Lentz leaves under ten on his bench in Week 10.", "WRONG",
         "36.02. He left Parker Washington's 27.70 behind a 9.10 and C.J. Stroud's 20.44 behind a 3.02."),
        ("One Under akaThe Mulligan", "Jonathan Taylor clears 15 for Casey Couture.", "WRONG",
         "11.30 on a projection of 17.26. Close does not count, and it was not that close."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender beats Mama Beth.", "RIGHT",
         "By 21.78, with a receiver who scored 41. I bet on Geoff's luck one more time and it showed up dressed as George Pickens."),
        ("Momma's Boys", "Justin Jefferson clears 15 for Mama Beth.", "WRONG",
         "11.90. I bet he would remember who he plays for. He remembered about three quarters of it."),
        ("The Scranton Strangler", "Scott Howard beats Ryan Reed.", "RIGHT",
         "By 23.72 with 4.20 on the bench. I bet the points would finally count, and for once he started all of them."),
        ("BearDown", "Ryan Reed scores 90 or more in Week 10.", "RIGHT",
         "102.40, with nine starters who played. Attendance was the whole call, and attendance was taken."),
        ("An alBum Cover", "CeeDee Lamb clears 20 again for Adam Calvelage.", "WRONG",
         "16.70. Purdy scored 36.66 next to him, so Adam did not need it. I did."),
        ("Holy Rollers", "Adam Hershberger beats Adam Calvelage.", "WRONG",
         "Lost by 12.68 with 34.90 on his bench. I picked the right Adam and he picked the wrong running backs."),
        ("Cosby Copperheads", "Doug Fields scores between 92 and 106 in Week 10.", "WRONG",
         "131.06. Under the range last week, over it this week. Doug has found both exits."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert beats Doug Fields for the first time.", "WRONG",
         "Lost by 18.44 with Gibbs at 43.70. Fields is 5 and 0 against him, and I bet against a 4 and 0."),
    ]))
    parts.append(gil(
        "Four right, eight wrong. Twelve new ones for Week 11, one per team. The Falcons, Patriots, Packers, Seahawks, Rams and Browns are off, so Bijan Robinson, Jaxon Smith-Njigba, Jordan Love, Matthew Stafford, Kyren Williams, Christian Watson, Quinshon Judkins and Drake London sit this one out."))
    parts.append(calls_list([
        ("Balls Deep", "C.J. Stroud clears 20 for Spencer Lentz.",
         "Stroud has scored 40.36 and 20.44 on that bench the last two weeks. The Patriots are off, so there is nobody left to start in front of him. Houston is home to the Colts. I am betting the points finally land in the lineup, mostly because there is no other chair."),
        ("Cosby Copperheads", "Doug Fields beats Spencer Lentz.",
         "Spencer leads the series 6 and 4 and has won eight straight this season. He is also missing Bijan Robinson and Jaxon Smith-Njigba to the bye, and Doug just scored 131 with Joe Burrow at 37. I am betting against the man who runs this booth. Somebody write that down."),
        ("Berlin Blitz", "Kent Frenger beats Adam Calvelage.",
         "Kent is 5 and 0 against him. Caleb Williams and the Broncos defense are back from the bye, and Kenneth Walker III is listed as questionable. The champ lost by 6.64 with a one-point flex. I am betting he reads his own bench this week."),
        ("An alBum Cover", "Brock Purdy clears 20 again for Adam Calvelage.",
         "25.28 and 36.66 the last two weeks, and San Francisco is home to Minnesota. I have stopped telling Adam who to start at quarterback. He has picked Purdy twice. I am standing behind Purdy."),
        ("BearDown", "Ryan Reed beats Geoff Cavender.",
         "They have never played. Geoff has two quarterbacks, Jordan Love and Matthew Stafford, and both are on the bye, along with Quinshon Judkins. Ryan gets Bo Nix back. I am betting on the man who has a quarterback."),
        ("Hawk Tua Tagovailoa", "Amon-Ra St. Brown clears 15 for Geoff Cavender.",
         "24.80 this week, and Detroit is home to Tampa Bay. Geoff needs a quarterback by Sunday, but he does not need help at receiver. I am betting on the part of that roster that is not on vacation."),
        ("DA The Badenov's", "DA beats Scott Reisert.",
         "DA leads the series 5 and 1 and is one game up on Reisert for the last playoff spot. He loses Kyren Williams, Christian Watson and that Rams defense to the bye. He still has Josh Allen at home to Miami and Christian McCaffrey off a 49. I am betting the elder keeps the chair."),
        ("Simba St. Gibbs Lion Kings", "Jahmyr Gibbs clears 20 again for Scott Reisert.",
         "43.70 this week, and Detroit is home to Tampa Bay. Scott has lost with Gibbs at 43 and won with Gibbs at 13, so I have no idea what this does for him. I am just betting on Gibbs."),
        ("Momma's Boys", "Mama Beth beats Casey Couture.",
         "She leads the series 12 and 10, though Casey has won the last two. Barkley and Burden are back from the bye, and she just got 38 from Mahomes. Casey has scored 63 and 77 the last two weeks. She has won this league three times. I am betting she gets one."),
        ("One Under akaThe Mulligan", "Casey Couture scores 90 or more in Week 11.",
         "63.78 and 77.92 the last two weeks. D'Andre Swift is back from the bye and Jonathan Taylor is at Houston. Five rings do not stay under 80 three weeks in a row."),
        ("The Scranton Strangler", "Scott Howard beats Adam Hershberger.",
         "Howard leads the series 5 and 3 and has won three of his last four. Dak Prescott is home to Tennessee and James Cook III is home to Miami. Howard has the fifth-most points in the league and four wins. I am betting the record keeps catching up."),
        ("Holy Rollers", "Chase Brown starts for Adam Hershberger in Week 11.",
         "24.30 on the bench this week. Cincinnati is at Washington. Zach Charbonnet, Blake Corum and Matthew Golden are all on the bye, so three of this week's starters are unavailable. I am betting the schedule makes the decision for him."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, then by size. When an owner already holds one, the next name in line takes it."))
    parts.append(award(
        "good", "Owner of the Week", "DA · DA The Badenov's",
        "128.34, a win over the team that had won six straight, and a 9 and 2 day against the field. He claimed the Rams defense this week and it scored 16.00 in a game decided by 6.64. He left 7.80 on his bench and has left 69.50 all season, the fewest in the league. Doug Fields's 131.06 was the higher score, and Spencer Lentz's 151.52 came with 36.02 left behind.",
        "The elder beat the champ with the champ's own defense. Kent held the door for the Rams and they walked into DA's lineup and scored 16 on him. DA is alone in fourth with the cleanest bench in the league, and he did it the week Kyren Williams and Christian Watson gave him 9.40 between them. Somebody get this man his hardware."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Casey Couture · One Under akaThe Mulligan",
        "77.92, the low score of the week and a loss to all eleven teams. Jordan Addison started in the flex and did not play, with Pat Freiermuth's 10.50 on the bench. He released J.J. McCarthy, who scored 18.12, for Fernando Mendoza, who started and scored 13.92. It is his third straight loss.",
        "Last week Casey cut Tyler Shough for J.J. McCarthy, and Shough outscored him. This week he cut McCarthy for Fernando Mendoza, and McCarthy outscored him. Casey is not picking quarterbacks, he is launching their careers on the way out the door. Five rings. I know. I have seen the rings. Start a man who is playing, Casey."))
    parts.append(award(
        "good", "Start of the Week", "Geoff Cavender · George Pickens, 41.00",
        "Projected for 10.30, so 30.70 over, the biggest margin over projection by any starter in the league this week. Christian McCaffrey's 49.30 for DA was 29.00 over and second, and DA holds Owner of the Week. Jahmyr Gibbs's 43.70 for Scott Reisert was 20.79 over and third.",
        "Geoff won this trophy last week for starting his quarterback. He wins it this week for starting a receiver who did not play the week before. Two weeks, two trophies, and I could not tell you one decision he made. Geoff, whatever you are not doing, keep not doing it."))
    parts.append(award(
        "bad", "Sit of the Week", "Adam Hershberger · Chase Brown, 24.30 on the bench",
        "Denzel Boston started in the flex for 2.10, a 22.20 swing in a game he lost by 12.68. Omarion Hampton's 20.00 was on the same bench. Two benchings cost a game this week. Kent Frenger's Jordyn Tyson behind Germie Bernard was 12.50 in a loss by 6.64 and second.",
        "Adam had 44.30 points of running back sitting down and lost by 12.68. Either one of them wins it alone. He has had the most points scored against him in the league all year, and this week he decided to help."))
    parts.append(award(
        "bad", "Waste of the Week", "Spencer Lentz · 36.02 left behind, and he won",
        "Parker Washington scored 27.70 on his bench behind Tee Higgins's 9.10, and C.J. Stroud 20.44 behind Drake Maye's 3.02. His best lineup was 187.54. Doug Fields left 12.30 in his win and Geoff Cavender 10.76 in his.",
        "Fourth Waste of the Week, and he held Sit of the Week last week. Parker Washington scored 27.70 and watched a 9.10 do his job. Spencer sees every number on this page before you do and still cannot find his own bench."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All twelve of you, every week, all season. Scott Howard still leads at 233.80 and added 4.20, which for Scott is a quiet week. Adam Hershberger added 34.90 in one afternoon and jumped Ryan Reed for second, 174.30 to 163.84. The man who runs this booth added 36.02 and is fifth at 156.68. DA is still the cleanest man in the league at 69.50."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 10, season_note=(
        "Season totals come from the season ledger through Week 10. Scott Howard leads at 233.80, Adam Hershberger is second at 174.30, Ryan Reed third at 163.84. DA has left the fewest, 69.50.")))
    parts.append(gil(
        "Two benches cost a game this week, after none did a week ago. Adam Hershberger left 34.90 and lost by 12.68. Kent Frenger left 12.50 and lost by 6.64. Spencer Lentz left 36.02 and won. Scott Howard and Scott Reisert each left 4.20, the least in the league, and Adam Calvelage left 4.30."))
    parts.append(boomer(
        "Scott Howard left 4.20 and Scott Reisert left 4.20. Two Scotts, 8.40 between them. One won, and one lost with Gibbs at 43.70, so a clean bench is a start and not a finish."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Spencer Lentz signing Emmett Johnson, who started and scored 35.10, for Jonathon Brooks, who has not played. Scott Howard's claim of Deebo Samuel Sr., 25.40 in his lineup, was second. Adam Hershberger's Colts defense for the Cowboys was 14.00 to minus 7.00 and third, and DA's Rams defense for the Bills was 16.00 to 10.00 in a game decided by 6.64."))
    parts.append(gil(
        "<strong>Worst move that made a lineup:</strong> Casey Couture releasing J.J. McCarthy, who scored 18.12, for Fernando Mendoza, who started and scored 13.92. DA released Samaje Perine, who scored 11.90, for Chris Rodriguez Jr., who scored 0.50 on his bench. Spencer Lentz made seven moves this week and signed three defenses: the Commanders started for 4.00, and the 49ers and Steelers scored minus 1.00 and minus 7.00 on his bench."))
    parts.append(boomer(
        "Seven moves, Gil. The man made seven moves in one week. He found a running back who scored 35 and then kept going, through three defenses that combined for minus four. And Kent's three releases from last week, the Rams, Cam Little and Bryce Young, all started for somebody else this week."))
    parts.append(gil(
        "Twenty-six moves went through. The trade noted on last week's page is final: Jaxon Smith-Njigba went from Ryan Reed to Spencer Lentz for Jaylen Warren and Nico Collins. In their first week, Smith-Njigba scored 31.10 for Lentz, and Collins and Warren scored 19.90 and 6.60 for Reed."))
    parts.append(boomer(
        "That one still involves the man who runs this booth, so Gil read the numbers and my hands are still folded."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Adam Hershberger at Scott Howard, Kent Frenger at Adam Calvelage, Geoff Cavender at Ryan Reed, Scott Reisert at DA, Casey Couture at Mama Beth, and Spencer Lentz at Doug Fields. The Falcons, Patriots, Packers, Seahawks, Rams and Browns are off. Four weeks remain in the regular season."))
    parts.append(boomer(
        "Reisert at DA is the game. Fourth place against the first man out, 5 and 1 lifetime for the elder, and DA without Kyren Williams or the defense that just won him a week. Geoff Cavender goes to Ryan Reed with both of his quarterbacks on the bye, and I cannot wait to see who he does not pick. Mama Beth gets Casey, and she leads that series 12 and 10. And the first-place team walks into Doug Fields without Bijan Robinson or Jaxon Smith-Njigba, the week after Doug found the roof."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 10, HEADLINE, DEK, build(), META, "dlffl-week-10.png", nav=NAV,
        published="2026-11-17T21:00:00-05:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "dlffl", "week-10.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
