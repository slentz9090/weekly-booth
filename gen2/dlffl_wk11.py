"""Dewart Lake FFL, Week 11. Editorial.

Boomer runs SCORCHING (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis and never gloats, clean language on the page, roast cap and Gil defenses apply. Mama Beth and DA,
never "Mother" or "Dad". Mama Beth is never the headline, Worst Owner or Boomer's jab target (standing
rule, 2026-11-03). No new segment: THE RACE (through the playoff cut) after the Scoreboard. No series
line on the cards, no Owner Spotlight.

Housekeeping note at the top (Spencer, 2026-11-24): the Week 10 teaser was never sent to the group, so
the page opens with Gil linking Week 10 and Boomer taking the blame with a joke.

Outlier engine, Week 11: nothing reached HEADLINE or PROMOTE. SUPPORT: Spencer Lentz by 78.74 (45th
biggest margin of 1,456); Adam Calvelage's first win over Kent Frenger in six; Doug Fields 64.90 (3rd
worst of his 133); Ja'Marr Chase 5.60 on 22.44 (45th-worst miss of 7,801); Calvelage 142.56 and Geoff
Cavender 140.08 (each a 3rd-best career game); Dak Prescott 38.90 for Scott Howard (111th-best start).
The page leads with the fourth playoff spot: DA, Scott Reisert and Calvelage are 6 and 5, and DA holds
the seed on season points, 1,264.06 to 1,262.18, after losing to Reisert by 48.26.

Verified against dlffl_wk11_facts.json, dlffl_season.json, dlffl_wk11_insights.json,
dlffl_race_wk11.json and gen2/data/dlffl_games.json.
"""
import json
import os

import booth
import race
from booth import award, boomer, calls_list, gil, graded_list, jump, ledger, mcard
from compute import DATA, by_owner, ledger_rows, load

FACTS = load("dlffl_wk11_facts.json")
SEASON = load("dlffl_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  

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

HEADLINE = "DA Scored 70.96, Lost By 48, And Still Holds The Last Playoff Spot. By 1.88 Points."
DEK = (
    "Three teams are 6 and 5 for the fourth playoff spot with three weeks left, and season points break the tie: DA 1,264.06, Scott Reisert 1,262.18. Adam Calvelage beat Kent Frenger for the first time in six tries with 22.94 on his bench. Doug Fields scored 131 last week and 64.90 this week. Casey Couture has the fewest points in the league and is one game out of the playoffs. Boomer bet on two quarterbacks to clear 20. Both did, from the bench. Boomer went 4 and 8."
)
META = (
    "Gil and Boomer call Week 11 of the Dewart Lake FFL: Scott Reisert beats DA by 48.26 and pulls within 1.88 season points of the last playoff spot, Adam Calvelage beats Kent Frenger for the first time, Doug Fields scores 64.90 a week after 131.06, and the race for four playoff spots with three weeks left."
)

def card_rows(win_owner, lose_owner):
    w, l = T[win_owner], T[lose_owner]
    return (
        {"team": w["name"], "owner": SEASON["owners"][win_owner]["display"], "score": w["score"], "left": w["left"]},
        {"team": l["name"], "owner": SEASON["owners"][lose_owner]["display"], "score": l["score"], "left": l["left"]},
    )


def race_section():
    """THE RACE: data from the FantasyPros pull after the ESPN roll, copy from race_wk11_copy.py."""
    p = os.path.join(DATA, "dlffl_race_wk11.json")
    if not os.path.exists(p):
        return '<h2 id="race">The Race</h2>'
    import race_wk11_copy
    return race.render(json.load(open(p)), race_wk11_copy.DL_COPY)




def build():
    parts = []
    teams = [(t["name"], SEASON["owners"][t["owner"]]["display"]) for t in FACTS["perTeam"]]
    parts.append(jump(teams))

    # ---- housekeeping: Week 10 was published and never reached the group
    parts.append(gil(
        'One piece of housekeeping. The Week 10 show was published last Tuesday and never reached the group chat. It is still up, and some of what follows grades calls made on it: <a href="week-10.html">Week 10, right here</a>.'))
    parts.append(boomer(
        "That one is on me. Gil gave me one job, and the job was to send you the link. I wrote the link on my hand so I would not forget it. Then I washed my hands, because I am a professional. By the time I figured out where it went, it was Sunday. Go read it. DA beats the champ with the champ's own defense in it, and after this week DA could use the memory."))

    parts.append('<h2 id="board">The Scoreboard</h2>')

    # ---- 1. 1.88
    w, l = card_rows("Scott Reisert", "dennis couture")
    parts.append(mcard(
        "m-reisert", "Reisert by 48.26, and within 1.88 season points of the last playoff spot", w, l,
        "Jahmyr Gibbs 25.80, Cam Ward 23.22 the week he claimed him, Javonte Williams 22.60 and George Kittle 16.90 for Scott Reisert, with Courtland Sutton at zero. Khalil Shakir 15.80, Josh Allen 15.16 on a projection of 24.35 and Christian McCaffrey 13.20 for DA, with Kyren Williams and Christian Watson on the bye.",
        SCALE, key=True))
    parts.append(gil(
        "Scott Reisert wins 119.22 to 70.96. Both teams are 6 and 5, and so is Adam Calvelage. Season points break the tie, and DA has 1,264.06 to Reisert's 1,262.18. DA led that count by 50.14 a week ago and leads it by 1.88 now, so he keeps the fourth playoff spot. His 70.96 beat one team in the league this week. Reisert set a perfect lineup: he claimed Cam Ward, started him over Jared Goff, and Ward won that choice 23.22 to 21.36. DA still leads the series 5 and 2."))
    parts.append(boomer(
        "One point eight eight. That is a field goal that hit the upright and a short kickoff return. That is what DA has left of the playoffs. Last week I gave the elder the trophy for beating the champ with the champ's own defense. This week the Rams were on the bye, so he signed four new people, started all four, and got 16 points out of the whole group. Dawson Knox, 4.10. Xavier Hutchinson, 2.30. Ryan Flournoy, 1.60. The Jets defense carried the other three in on its back with an eight."))
    parts.append(gil(
        "In fairness to DA, Kyren Williams and Christian Watson were on the bye, Woody Marks and Dalton Kincaid did not play, and Josh Allen and Christian McCaffrey finished 14.34 under their projections between them. His best lineup was 80.16, so the bench did not decide it. He left 9.20 behind: Aaron Jones Sr. scored 10.80 behind Ryan Flournoy's 1.60. He beat Reisert twice last season."))
    parts.append(boomer(
        "And Reisert did it with a receiver who scored zero. Courtland Sutton, in the lineup, nothing. Perfect lineup anyway, because the bench behind him was on vacation. Reisert found a quarterback on the wire, benched Jared Goff for him, and was right by 1.86. I picked DA. I said the elder keeps the chair. He is still in the chair, Gil. There is just somebody else's coat on the back of it now."))

    # ---- 2. first time
    w, l = card_rows("Adam Calvelage", "Kent Frenger")
    parts.append(mcard(
        "m-calvelage", "Calvelage's first win over Frenger in six tries, with 22.94 on his bench", w, l,
        "Jonah Coleman 35.90 on a projection of 18.59, CeeDee Lamb 27.70 and Travis Kelce 22.40 for Adam Calvelage, with Brock Purdy's 22.20 and Jacory Croskey-Merritt's 14.70 on his bench. DJ Moore 19.10 and David Montgomery 16.90 for Kent Frenger, with Ja'Marr Chase at 5.60 on a projection of 22.44.",
        SCALE))
    parts.append(gil(
        "Adam Calvelage wins 142.56 to 105.04 and is 6 and 5 with three straight wins. He was 0 and 5 against Kent Frenger before this. The 142.56 is the third-best game of his 67 in this league and the second-highest score of the week. He left 22.94 on his bench, the most in the league: Brock Purdy scored 22.20 behind Jayden Daniels's 17.06, and Jacory Croskey-Merritt 14.70 behind Kaelon Black's 2.00. Kent Frenger, the defending champion, is 7 and 4 and has lost two straight. Ja'Marr Chase's 5.60 on a projection of 22.44 is the 45th-worst miss by a starter projected for ten or more in this league since 2018, out of 7,801."))
    parts.append(boomer(
        "Follow me here. Three weeks ago I told Adam Calvelage to start Jayden Daniels. He started Brock Purdy. Purdy scored 25, then 36. So last week I stood up on this page and said fine, I am standing behind Purdy. Calvelage heard that, walked over to Purdy, and benched him. Purdy scored 22.20 from the bench and my call lost with him. I am not giving that man advice anymore, Gil. I am going to start saying the opposite of what I think and see if he can find me."))
    parts.append(gil(
        "In fairness to Kent Frenger, Kenneth Walker III did not play for the second straight week, and Chase, Tony Pollard, Bhayshul Tuten and Caleb Williams all finished under their projections. He is still second in the league in points at 1,361.06. He left 8.80 behind, Justice Hill's 15.60 behind Tuten's 6.80, in a game he lost by 37.52. In fairness to Calvelage, Daniels was projected for 20.59 to Purdy's 18.60."))
    parts.append(boomer(
        "Kent won six straight, and since then he has lost to a defense he cut and to a man who had never beaten him. Chase gave him 5.60. That is a tight end's bad day from the best receiver on the roster. And Calvelage left 22.94 on the bench and still won by 37. He sat one defense for another and they both scored six. Nothing he did mattered and all of it worked."))

    # ---- 3. no quarterbacks
    w, l = card_rows("Geoff Cavender", "Ryan Reed")
    parts.append(mcard(
        "m-cavender", "Cavender by 51.78, the third-best game of his 39, with a quarterback he signed this week", w, l,
        "Ashton Jeanty 26.40 on a projection of 12.27, George Pickens 23.30, and 17.00 each from Tyler Bass and the Bears defense for Geoff Cavender, with Mike Evans's 22.90 on his bench. Breece Hall 17.50 and the Texans defense 17.00 for Ryan Reed, with Bo Nix at 11.50 on a projection of 21.71.",
        SCALE))
    parts.append(gil(
        "Geoff Cavender wins 140.08 to 88.30 and is 8 and 3, alone in second place. Jordan Love was on the bye, so he signed Aaron Rodgers, who started and scored 15.98. Samaje Perine, also signed this week, started for 11.70. It was the first meeting between these two. Ryan Reed is 4 and 7 and has lost three straight. Bo Nix scored 11.50 for him with Bryce Young's 15.96 on the bench, and Jaylen Warren scored 3.90 on a projection of 15.25."))
    parts.append(boomer(
        "I bet on Ryan because Ryan had a quarterback and Geoff did not. Then Geoff went and got one off the wire and it outscored Ryan's. Aaron Rodgers, 15.98. Bo Nix, 11.50. Geoff Cavender spent the week with no quarterback and still won the quarterback matchup. He left Mike Evans's 22.90 on the bench and won by 51. The kicker scored 17. The defense scored 17. I have been calling this luck for eleven weeks, and at some point I have to consider that the man just lives like this."))
    parts.append(gil(
        "In fairness to Ryan Reed, Nix was projected for 21.71 to Young's 18.37, so the start was the reasonable one, and he left only 4.56 behind. Cam Skattebo scored 4.30 on a projection of 13.81. In fairness to Geoff Cavender, he is 8 and 3. Against the whole league, every week, he is 62 and 59, about two and a half wins better than that would predict."))
    parts.append(boomer(
        "Sixty-two and 59, and second place. I called fifteen for Amon-Ra St. Brown and he scored 12.20 while Mike Evans scored 22.90 right next to him, so Geoff beat my call with his own bench. Ryan Reed, two of your running backs gave you 8.20 between them. I have had sandwiches do more."))

    # ---- 4. three and a half
    w, l = card_rows("Casey Couture", "Beth Couture")
    parts.append(mcard(
        "m-casey", "Casey by 3.52, the closest game of the week", w, l,
        "Fernando Mendoza 23.88 on a projection of 15.17 and Chris Olave 17.70 for Casey Couture, with Jonathan Taylor at 4.70 on a projection of 16.00. Patrick Mahomes 27.96, Saquon Barkley 13.50 and Chris Boswell 13.00 for Mama Beth, with Luther Burden III at 2.30 and the Vikings defense at zero.",
        SCALE))
    parts.append(gil(
        "Casey Couture wins 91.98 to 88.46 and is 5 and 6, ending a three-game losing streak. He has beaten Mama Beth three straight times, and she leads the series 12 and 11. Mama Beth left 1.90 on her bench, and her best lineup was 90.36, so there was no lineup that wins it. Patrick Mahomes gave her 27.96. The Vikings defense, which scored 21.00 for her a week ago, scored zero."))
    parts.append(boomer(
        "I picked Mama Beth and she did her part. She left 1.90 on the bench. There was no better lineup on that roster, I checked, and the defense that scored 21 last week showed up with nothing. That loss goes on my record, not hers. Now, Casey. Casey Couture has scored 999.30 points this season. That is the fewest in the league. Twelfth of twelve. He is 5 and 6 and one game out of a playoff spot. Five titles, last in points, still in it. I do not know how he does it and I do not think he does either."))
    parts.append(gil(
        "In fairness to Casey Couture, Jonathan Taylor was projected for 16.00 and scored 4.70, and D'Andre Swift and Ollie Gordon II were both under their projections. He left 2.90 behind. Fernando Mendoza, the quarterback he signed a week ago, scored 23.88, the best game by anyone in his lineup. Against the whole league this season Casey is 37 and 84."))
    parts.append(boomer(
        "I called 90 for Casey and he scored 91.98, so I will take the win and the two points of breathing room. Jonathan Taylor has given him 6.90, 11.30 and 4.70 the last three weeks. Casey is winning games around Jonathan Taylor like a man carrying a couch up the stairs by himself."))

    # ---- 5. the running backs, started
    w, l = card_rows("Scott Howard", "Adam Hershberger")
    parts.append(mcard(
        "m-howard", "Howard by 12.16 for his third straight win, over a perfect lineup", w, l,
        "Dak Prescott 38.90 on a projection of 23.15, Bucky Irving 17.50 and James Cook III 16.20 for Scott Howard, with Spencer Shrader at 1.00. Jameson Williams 18.30, Trevor Lawrence 15.74 and Malik Nabers 15.00 for Adam Hershberger, with Chase Brown at 6.10 and Omarion Hampton at 9.80.",
        SCALE))
    parts.append(gil(
        "Scott Howard wins 110.00 to 97.84 and is 5 and 6 with three straight wins and four in his last five. Dak Prescott has scored 37.42 and 38.90 for him the last two weeks. Howard has the fifth-most points in the league, 1,245.22, and leads this series 6 and 3. Adam Hershberger set a perfect lineup and lost. He is 4 and 7 and has had 1,307.30 points scored against him, the most in the league."))
    parts.append(boomer(
        "Last week Adam Hershberger left Chase Brown and Omarion Hampton on the bench and they scored 44.30. I yelled. The whole booth yelled. So this week he started both of them, and they scored 15.90. Together. That is 28 points that got lost somewhere between his bench and his lineup. Hershberger did everything right and it handed him a 6.10. The lineup was perfect, Gil. The players were not."))
    parts.append(gil(
        "In fairness to Adam Hershberger, Zach Charbonnet, Blake Corum, Matthew Golden and Denzel Boston were all on the bye, so the bench had nothing to offer, and no lineup he could have set wins the game. In fairness to Scott Howard, he left 5.20 behind after leaving 4.20 a week ago. He still leads the league in points left on the bench for the season, at 239.00."))
    parts.append(boomer(
        "Scott Howard has left 9.40 on his bench in two weeks. He left 46 in Week 1 alone. I called this one and I am taking it. His kicker scored one point and he still won by twelve. He is 5 and 6 with the fifth-most points in the league and three wins in a row, and nobody at 6 and 5 should be sleeping well."))

    # ---- 6. the range
    w, l = card_rows("Spencer Lentz", "Doug Fields")
    parts.append(mcard(
        "m-lentz", "Fields scores 64.90 a week after 131.06, and Spencer Lentz benches Boomer's quarterback again", w, l,
        "Chuba Hubbard 29.00, Emmett Johnson 25.30 and Justin Herbert 22.44 the week he signed him for Spencer Lentz, with C.J. Stroud's 20.46 and the 49ers defense's 14.00 on his bench. Joe Burrow 22.90 and Derrick Henry 17.10 for Doug Fields, with Ladd McConkey's 18.20 on his bench behind Keon Coleman's 2.70.",
        SCALE))
    parts.append(gil(
        "Spencer Lentz wins 143.64 to 64.90 and is 9 and 2, with nine straight wins. The margin, 78.74, is the 45th-largest in 1,456 games in this league since 2009. Doug Fields's 64.90 is the low score of the week and the third-worst game of his 133. He scored 131.06 a week ago, so this is less than half of it. He left 16.10 behind, 15.50 of it Ladd McConkey behind Keon Coleman. Spencer leads the series 7 and 4."))
    parts.append(boomer(
        "Doug Fields lived between 92 and 106 for eight weeks. Then 91. Then 131. Now 64.90. He left the range through the basement, took the elevator to the roof, and this week he fell off the roof. And for two weeks I told him Seth McGowan was scoring on his bench. So he started Seth McGowan. One point three. I am sorry, Doug. I did that. I also picked you to win this game, in ink, and you lost by 78.74, so we have both had better weeks."))
    parts.append(gil(
        "In fairness to Doug Fields, Drake London and Rhamondre Stevenson were on the bye, Isaiah Likely was projected for 10.53 and scored 4.00, and his best lineup was 81.00, which does not win either. He is 5 and 6 and one game out of the fourth spot."))
    parts.append(boomer(
        "And the man who runs this booth. I bet C.J. Stroud would clear 20 for him, because the Patriots were off and there was nobody left to start in front of Stroud. So he went out and signed Justin Herbert to start in front of Stroud. Stroud scored 20.46. On the bench. Again. That is 40.36, 20.44 and 20.46 in three weeks, 81.26 points of quarterback, none of it in the lineup. He also sat a defense that scored 14 for one that scored 7. He will not start Stroud for me and I am starting to take it personally."))

    # ---- THE RACE
    parts.append(race_section())

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls came due. Four right, eight wrong, same as last week. Season record 50 and 70. Two of the eight were quarterbacks who cleared my number from the bench, and I want that noted somewhere, even though it does not count. Every call is below, in ink."))
    parts.append(graded_list([
        ("Balls Deep", "C.J. Stroud clears 20 for Spencer Lentz.", "WRONG",
         "20.46, on the bench, behind Justin Herbert's 22.44. He cleared it. He just did it sitting down."),
        ("Cosby Copperheads", "Doug Fields beats Spencer Lentz.", "WRONG",
         "Lost by 78.74 with 64.90. I bet against the man who runs this booth and asked somebody to write it down. Somebody did."),
        ("Berlin Blitz", "Kent Frenger beats Adam Calvelage.", "WRONG",
         "Lost by 37.52. He was 5 and 0 in the series, and I bet on the 5 and 0. Chase scored 5.60."),
        ("An alBum Cover", "Brock Purdy clears 20 again for Adam Calvelage.", "WRONG",
         "22.20, on the bench, behind Jayden Daniels's 17.06. I stood behind Purdy and Calvelage sat him down in front of me."),
        ("BearDown", "Ryan Reed beats Geoff Cavender.", "WRONG",
         "Lost by 51.78. I bet on the man who had a quarterback. The other man found one."),
        ("Hawk Tua Tagovailoa", "Amon-Ra St. Brown clears 15 for Geoff Cavender.", "WRONG",
         "12.20. Mike Evans scored 22.90 on the bench next to him. I picked the wrong receiver on a roster that did not need either."),
        ("DA The Badenov's", "DA beats Scott Reisert.", "WRONG",
         "Lost by 48.26. I said the elder keeps the chair. He kept it by 1.88 points."),
        ("Simba St. Gibbs Lion Kings", "Jahmyr Gibbs clears 20 again for Scott Reisert.", "RIGHT",
         "25.80. I said I was just betting on Gibbs. Gibbs is the only one on this list who has never let me down."),
        ("Momma's Boys", "Mama Beth beats Casey Couture.", "WRONG",
         "Lost by 3.52 with 1.90 on her bench and no better lineup available. She did everything right. The miss is mine."),
        ("One Under akaThe Mulligan", "Casey Couture scores 90 or more in Week 11.", "RIGHT",
         "91.98. Clear by 1.98, in a win by 3.52. Nothing Casey does this year has any room in it."),
        ("The Scranton Strangler", "Scott Howard beats Adam Hershberger.", "RIGHT",
         "By 12.16, his third straight. I bet the record would keep catching up to the points, and it is."),
        ("Holy Rollers", "Chase Brown starts for Adam Hershberger in Week 11.", "RIGHT",
         "He started and scored 6.10. I was right that he would start. I would like to be clear that I promised nothing else."),
    ]))
    parts.append(gil(
        "Four right, eight wrong. Twelve new ones for Week 12, one per team. Nobody is on the bye. It is Thanksgiving week: the Packers and Rams play Wednesday, six teams play Thursday, and the Broncos and Steelers play Friday, so lineups lock early."))
    parts.append(calls_list([
        ("Balls Deep", "C.J. Stroud starts for Spencer Lentz in Week 12.",
         "I am done betting on the points. 40.36, 20.44 and 20.46 on that bench the last three weeks. Houston is home to Baltimore. All I am asking for is the chair. Put the man in the chair."),
        ("DA The Badenov's", "DA beats Spencer Lentz.",
         "Spencer leads the series 22 and 11 and has won nine straight this season. DA has also beaten him three straight times, including 156.86 to 114.02 in Week 1. Kyren Williams and Christian Watson are back from the bye. I bet against the man who runs this booth last week and lost by 78.74. I am doing it again."),
        ("Berlin Blitz", "Kent Frenger beats Adam Hershberger.",
         "Hershberger leads the series 11 and 9, and Kent has won the last two. Kenneth Walker III is listed as out again. Ja'Marr Chase is home to the Saints and is not scoring 5.60 twice. I am betting the champ does not lose three in a row."),
        ("Holy Rollers", "Trevor Lawrence clears 20 for Adam Hershberger.",
         "15.74 this week on a projection of 20.41. Jacksonville is home to Tennessee. Hershberger set a perfect lineup and lost, and he gets his bye-week players back. I am betting the quarterback does his share this time."),
        ("The Scranton Strangler", "Scott Howard beats Geoff Cavender.",
         "The series is 3 and 3. Howard has won three straight and is 69 and 52 against the whole league. Cavender is 62 and 59. Dak Prescott is home to Philadelphia on Thursday off a 37 and a 38. I am betting on the points over the luck, and I know how that has gone."),
        ("Hawk Tua Tagovailoa", "George Pickens clears 15 for Geoff Cavender.",
         "41.00 and 23.30 the last two weeks, and Dallas is home to Philadelphia on Thursday. Geoff gets Jordan Love back, so he has two quarterbacks again. I am betting on the receiver and staying out of the rest of it."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert beats Adam Calvelage.",
         "Reisert leads the series 5 and 2, and they are both 6 and 5. The winner is still in the fight for fourth and the loser needs help. Jahmyr Gibbs is home to Chicago on Thursday. Reisert has the fewest points scored against him in the league and just set a perfect lineup. I am betting on the man 1.88 back."),
        ("An alBum Cover", "Jonah Coleman clears 15 for Adam Calvelage.",
         "35.90 this week. Denver is at Pittsburgh on Friday. I have no call on which quarterback Calvelage starts. I have retired from that. I am betting on the running back, who has never been benched to spite me."),
        ("One Under akaThe Mulligan", "Casey Couture beats Ryan Reed.",
         "Casey leads the series 8 and 2 and has won the last four, including 129.44 to 108.26 in Week 1. A win puts the last-place scoring team in the league at 6 and 6. I am betting it happens, because of course it does."),
        ("BearDown", "Ryan Reed scores 95 or more in Week 12.",
         "63.38, 102.40 and 88.30 the last three weeks. Nobody on his roster is on the bye, and Bo Nix was 10 points under his projection. I am betting on a full roster and an ordinary day."),
        ("Momma's Boys", "Mama Beth beats Doug Fields.",
         "She leads the series 12 and 6 and beat him 149.12 to 96.96 in Week 1. Patrick Mahomes has given her 38.42 and 27.96 the last two weeks. Doug just scored 64.90. I picked her last week and she lost by 3.52 through no fault of her own. I am picking her again."),
        ("Cosby Copperheads", "Doug Fields scores 90 or more in Week 12.",
         "He cleared 90 in each of the first ten weeks of the season before the 64.90. Joe Burrow is home to the Saints, and Drake London and Rhamondre Stevenson are back from the bye. I am betting Doug finds the stairs."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, then by size. When an owner already holds one, the next name in line takes it."))
    parts.append(award(
        "good", "Owner of the Week", "Scott Reisert · Simba St. Gibbs Lion Kings",
        "119.22 with a perfect lineup, a win by 48.26, and an 8 and 3 day against the field. He claimed Cam Ward this week and started him over Jared Goff, and Ward was the right choice by 1.86. The win pulled him level with DA at 6 and 5 and within 1.88 season points of the fourth playoff spot. Three teams scored more: Spencer Lentz 143.64, Adam Calvelage 142.56 with 22.94 left behind, and Geoff Cavender 140.08 with 10.70.",
        "Reisert had to pick between a quarterback he has started all year and one he met this week, and he picked the stranger and was right. He has left 73.90 on his bench all season, the fewest in the league, and he passed DA for that this week too. A week ago he lost with Gibbs at 43. This week he won with a receiver at zero. Third Owner of the Week this year. Take the hardware, Reisert, and go get the other 1.88."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Doug Fields · Cosby Copperheads",
        "64.90, the low score of the week, a loss to all eleven teams and the third-worst game of his 133 in this league. Ladd McConkey scored 18.20 on his bench behind Keon Coleman's 2.70. The Bengals defense scored zero and Will Reichard 3.00. His best lineup was 81.00.",
        "Last week Doug had the second-best score in the league. This week he had the worst one by six points. Same roster. Same man. He sat an 18 for a 2.70, and the 2.70 was not even the problem, because a kicker, a defense, a tight end and a running back gave him 8.30 put together. Doug, I liked you better when you were boring."))
    parts.append(award(
        "good", "Start of the Week", "Scott Howard · Dak Prescott, 38.90",
        "Projected for 23.15, so 15.75 over, and the 111th-best start in this league since 2018, out of 12,819. Jonah Coleman's 35.90 for Adam Calvelage was 17.31 over and first, and Calvelage holds Waste of the Week. Ashton Jeanty's 26.40 for Geoff Cavender was 14.13 over and third.",
        "Scott Howard has the most Sit of the Week trophies in this league. Three of them. This is his first one for starting somebody. Dak has given him 76.32 in two weeks, and for two weeks Howard has had him in the lineup to receive it. Growth, Gil. In November, but growth."))
    parts.append(award(
        "bad", "Sit of the Week", "Geoff Cavender · Mike Evans, 22.90 on the bench",
        "Amon-Ra St. Brown started in his place for 12.20, a 10.70 swing. No benching cost a game this week. Doug Fields's Ladd McConkey behind Keon Coleman was 15.50 and first, and Fields holds Worst Owner. Adam Calvelage's Jacory Croskey-Merritt behind Kaelon Black was 12.70 and second, and Calvelage holds Waste of the Week.",
        "Geoff benched 22.90, won by 51.78 and moved into second place. Giving this man a trophy for a mistake is like giving a cat a detention. He does not know it happened and it is not going to change anything."))
    parts.append(award(
        "bad", "Waste of the Week", "Adam Calvelage · 22.94 left behind, and he won",
        "Brock Purdy scored 22.20 on his bench behind Jayden Daniels's 17.06, and Jacory Croskey-Merritt 14.70 behind Kaelon Black's 2.00. He also sat the Giants defense's 6.00 for the Lions defense's 6.00, which changed nothing. His best lineup was 165.50. Geoff Cavender left 10.70 in his win and Spencer Lentz 7.00 in his.",
        "Calvelage's best lineup was 165.50 and he turned in 142.56, and it was still the third-best day of his career. He claimed a running back, the running back scored 14.70, and he started a different running back who scored two. First win over Kent, first Waste of the Week. Frame them together."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All twelve of you, every week, all season. Scott Howard still leads at 239.00, and he has added 9.40 in two weeks, which for Howard is a monastery. Adam Hershberger is second at 174.30 and added nothing. Ryan Reed is third at 168.40. The man who runs this booth is fourth at 163.68. And there is a new name at the bottom: Scott Reisert has left 73.90 all season and passed DA, at 78.70, for the cleanest bench in the league. That is the second thing Reisert took from DA this week."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 11, season_note=(
        "Season totals come from the season ledger through Week 11. Scott Howard leads at 239.00, Adam Hershberger is second at 174.30, Ryan Reed third at 168.40. Scott Reisert has left the fewest, 73.90.")))
    parts.append(gil(
        "No bench cost a game this week, after two did a week ago. Adam Calvelage left 22.94 and won by 37.52. Doug Fields left 16.10 and lost by 78.74. Adam Hershberger and Scott Reisert each left 0.00, and Mama Beth left 1.90 in a game she lost by 3.52."))
    parts.append(boomer(
        "Two perfect lineups this week. Reisert's scored 119 and won by 48. Hershberger's scored 97 and lost by 12. Same grade on the test, Gil. Different class."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Scott Reisert claiming Cam Ward, who started and scored 23.22, for Wan'Dale Robinson. Spencer Lentz signing Justin Herbert, 22.44 in his lineup, for the Commanders defense was second. Geoff Cavender signing Aaron Rodgers, 15.98 in his lineup, for Matthew Stafford was third, and his Samaje Perine started for 11.70."))
    parts.append(gil(
        "<strong>Worst move that made a lineup:</strong> DA signed the Jets defense, Dawson Knox, Xavier Hutchinson and Ryan Flournoy and started all four for 16.00 combined. Two of the players he released for them, Chris Rodriguez Jr. and Treylon Burks, scored 4.60 and 4.00. Kent Frenger released Jacoby Brissett, who scored 14.74, and started Caleb Williams for 14.34."))
    parts.append(boomer(
        "Here is the life of the Rams defense. Two weeks ago Kent cut it. Last week it scored 16 for DA and won him a game and a trophy. This week it was on the bye, so DA cut it too. That defense has been fired by two playoff teams in three weeks and the only thing it has done wrong is take a week off. I have been fired for less, Gil, but not by much."))
    parts.append(gil(
        "Twenty-six moves went through, the same number as a week ago."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Kent Frenger at Adam Hershberger, Scott Howard at Geoff Cavender, Adam Calvelage at Scott Reisert, Ryan Reed at Casey Couture, DA at Spencer Lentz, and Mama Beth at Doug Fields. Nobody is on the bye. Thanksgiving week has one game Wednesday, three Thursday and one Friday, so set lineups before the turkey. Three weeks remain in the regular season."))
    parts.append(boomer(
        "Calvelage at Reisert is the game. Two of the three teams at 6 and 5, and the third one, DA, has to go through the first-place team with a 1.88 lead in the tiebreaker. Somebody is leaving Week 12 in fourth place and I could not tell you who. Howard at Cavender is the points against the luck. Casey gets Ryan Reed and a chance to be 6 and 6 with the fewest points in the league, which I would like to see just to know it can be done. And Mama Beth gets Doug Fields, who she beat 149.12 to 96.96 in Week 1, the week after he fell off the roof. I am on her side of that one."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 11, HEADLINE, DEK, build(), META, "dlffl-week-11.png", nav=NAV,
        published="2026-11-24T05:00:00-05:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "dlffl", "week-11.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
