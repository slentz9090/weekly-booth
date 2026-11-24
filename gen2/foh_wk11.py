"""Friends of Herb, Week 11. Editorial.

Boomer runs SCORCHING (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis and never gloats, clean language on the page, roast cap and Gil defenses apply. No new segment:
THE RACE (through the playoff cut) after the Scoreboard. No series line on the cards, no Owner
Spotlight. Nothing on this page refers to any other league.

Outlier engine, Week 11. PROMOTE: Michael Turner 54.06 (22nd-lowest of 2,709 team-weeks since 2011);
Eric Olson six straight over Turner. SUPPORT: Matt Davis by 75.10 (47th-biggest margin of 1,355);
Dak Prescott 44.90 for Michael Smith (51st-best start of 11,216); Rahul Pahuja lost with Jonah
Coleman's 34.90; Bob Dorsch 69.00 (6th-worst of his 244); Billy Norton won with 88.00; Smith 7-3 on a
44-46 all-play. The page leads with Turner: last week's ON THE RECORD call named Drake London, Zach
Charbonnet and Josh Jacobs as on the bye, and all three started for him.

Verified against foh_wk11_facts.json, foh_season.json, foh_wk11_insights.json, foh_race_wk11.json and
gen2/data/foh_games.json.
"""
import json
import os

import booth
import race
from booth import award, boomer, byecard, calls_list, gil, graded_list, jump, ledger, mcard
from compute import DATA, by_owner, ledger_rows, load

FACTS = load("foh_wk11_facts.json")
SEASON = load("foh_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  

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

HEADLINE = "Boomer Named Three Players On The Bye. Michael Turner Started All Three And Scored 54.06."
DEK = (
    "Last week this page listed Drake London, Zach Charbonnet and Josh Jacobs as off. All three were in Turner's lineup on Sunday, with Breece Hall's 17.50 on his bench. Matt Davis won by 75.10 with a perfect lineup and is 2.68 season points behind first place. Dak Prescott scored 44.90 a week after 45.42. Rahul Pahuja set a third straight perfect lineup and lost. Four teams are 7 and 3 with three weeks left. Boomer went 8 and 3."
)
META = (
    "Gil and Boomer call Week 11 of Friends of Herb: Michael Turner starts three players on the bye and scores 54.06, Matt Davis wins by 75.10 with a perfect lineup, Dak Prescott scores 44.90 for Michael Smith, four teams are 7 and 3, and the race for four playoff spots with three weeks left."
)

def card_rows(win_owner, lose_owner):
    w, l = T[win_owner], T[lose_owner]
    return (
        {"team": w["name"], "owner": SEASON["owners"][win_owner]["display"], "score": w["score"], "left": w["left"]},
        {"team": l["name"], "owner": SEASON["owners"][lose_owner]["display"], "score": l["score"], "left": l["left"]},
    )


def race_section():
    """THE RACE: data from the FantasyPros pull after the ESPN roll, copy from race_wk11_copy.py."""
    p = os.path.join(DATA, "foh_race_wk11.json")
    if not os.path.exists(p):
        return '<h2 id="race">The Race</h2>'
    import race_wk11_copy
    return race.render(json.load(open(p)), race_wk11_copy.FOH_COPY)




def build():
    parts = []
    teams = [(t["name"], SEASON["owners"][t["owner"]]["display"]) for t in FACTS["perTeam"]]
    parts.append(jump(teams))

    parts.append('<h2 id="board">The Scoreboard</h2>')

    # ---- 1. the three names
    w, l = card_rows("Eric Olson", "Michael Turner")
    parts.append(mcard(
        "m-olson", "Olson by 37.90 with 91.96, over a lineup with three starters on the bye", w, l,
        "Ashton Jeanty 28.40 on a projection of 12.16 and Cam Little 13.00 for Eric Olson, with Josh Allen at 15.16 on a projection of 27.14. Jayden Daniels 17.06, Chris Olave 16.70 and the Broncos defense 13.00 for Michael Turner, who started Drake London, Zach Charbonnet and Josh Jacobs on their bye with Breece Hall's 17.50 on his bench.",
        SCALE, key=True))
    parts.append(gil(
        "Eric Olson wins 91.96 to 54.06 and is 7 and 3. Michael Turner's 54.06 is the low score of the week and the 22nd-lowest of 2,709 team-weeks in this league since 2011. Three of his starters were on the bye, Drake London, Zach Charbonnet and Josh Jacobs, and a fourth, J.K. Dobbins, scored zero. Breece Hall scored 17.50 on his bench and Aaron Rodgers 17.98. He left 29.82 behind, the most in the league, and has lost eight straight. Olson has beaten him six straight times."))
    parts.append(boomer(
        "I am going to read from last week's page, Gil. My words. Quote. Drake London, Zach Charbonnet and Josh Jacobs are on the bye. Unquote. I named them. I named the men who were playing, too. I said, I have checked, you have nine. And Michael Turner read that, or did not, and started Drake London, Zach Charbonnet and Josh Jacobs. That is eight starters in two weeks who were not at the stadium. He has scored 110.62 in those two weeks combined. Rahul Pahuja did that by himself on Sunday."))
    parts.append(gil(
        "In fairness to Michael Turner, Lamar Jackson is on injured reserve, and his best lineup this week was 83.88, which still loses by 8.08. Against the whole league this season he is 25 and 65, nearly two wins better than his 1 and 9 record. In fairness to Eric Olson, he left 4.80 behind and Josh Allen finished 11.98 under his projection."))
    parts.append(boomer(
        "And Olson. Eric scored 91.96, the tenth-worst game he has ever had in this league, and won by 38. His last three weeks are 102.36, 102.14 and 91.96, and he is 7 and 3 and holding a playoff spot. He signed Courtland Sutton this week, started him, and got zero. Eric is walking into the playoffs backwards and nobody on his schedule has been able to stop him."))

    # ---- 2. the defense
    w, l = card_rows("Matt Davis", "Aaron Jezioro")
    parts.append(mcard(
        "m-davis", "Davis by 75.10 with a perfect lineup, and a defense and a flex he signed this week", w, l,
        "Jahmyr Gibbs 25.80, Joe Burrow 24.90, Jameson Williams 20.30, David Montgomery 15.90 and the Texans defense 13.00 for Matt Davis, with Tyler Warren at 2.70. Brock Purdy 28.20 and Carnell Tate 15.80 for Aaron Jezioro, with Ja'Marr Chase at 5.60 on a projection of 22.03 and Brock Bowers, who did not play, in the lineup.",
        SCALE))
    parts.append(gil(
        "Matt Davis wins 146.20 to 71.10 and is 7 and 3, second in the standings. The margin, 75.10, is the 47th-largest in 1,355 games in this league since 2011. It was a perfect lineup. He signed David Montgomery and the Texans defense this week and both started, for 28.90 between them. He has 1,317.82 points on the season, 2.68 behind Spencer Lentz for the most in the league. Davis has beaten Aaron Jezioro four straight times and leads the series 13 and 12. Jezioro is 4 and 6."))
    parts.append(boomer(
        "Last week I told Matt he needed a defense by Sunday, because his was on the bye. So Matt went looking. He came back with a defense that scored 13 and a running back that scored 15.90 and put both of them in a perfect lineup. Seven wins, and the whole roster is finally awake. Except the tight end. Tyler Warren scored 1.40 last week and 2.70 this week. That is 4.10 in two weeks from the position Matt cleared out Mark Andrews to fix."))
    parts.append(gil(
        "In fairness to Aaron Jezioro, he chose Brock Purdy over Trevor Lawrence for the second straight week and was right again, 28.20 to 15.74. Ja'Marr Chase finished 16.43 under his projection and Jaylen Warren 11.07 under his. He left 4.00 behind. Brock Bowers did not play, and Jezioro had no other tight end on the roster."))
    parts.append(boomer(
        "Jezioro scored 138, 134 and 129 the three weeks before this and I finally stopped yelling at him. Then 71.10. He started a tight end who was not playing because there was not another one on the roster, and the one move he made at receiver was releasing Khalil Shakir, who scored 14.80 for nobody, for a man who scored zero on his bench. I called twenty for Chase. Chase scored 5.60. Jezioro and I can split that one."))

    # ---- 3. ninety in two weeks
    w, l = card_rows("Michael Smith", "Rahul Pahuja")
    parts.append(mcard(
        "m-smith", "Smith by 18.54 behind Dak Prescott's 44.90, over a third straight perfect lineup", w, l,
        "Dak Prescott 44.90 on a projection of 27.27, Travis Kelce 22.40, Mike Evans 21.90 and Tyler Bass 18.00 for Michael Smith, who started Woody Marks, who did not play. Jonah Coleman 34.90, C.J. Stroud 26.46 and the Bears defense 15.00 for Rahul Pahuja, with Jaxon Smith-Njigba and Matthew Golden on the bye.",
        SCALE))
    parts.append(gil(
        "Michael Smith wins 129.40 to 110.86 and is 7 and 3 with three straight wins. Dak Prescott's 44.90 is the 51st-best start in this league since 2018, out of 11,216, and he scored 45.42 a week ago. Rahul Pahuja set a perfect lineup for the third straight week and lost. Jonah Coleman's 34.90 is the 74th-most by one starter in a losing lineup since 2018, out of 5,413. Pahuja is 6 and 4 and sixth in the standings. He leads the series 18 and 11, and Smith has won the last two."))
    parts.append(boomer(
        "A hundred seventy-three. A hundred seventy-three. A hundred ten. The machine did not break, Gil. Somebody took two parts out of it. Smith-Njigba and Golden were on the bye, Rahul set the best lineup he had for the third week in a row, and the best lineup he had was 63 points lighter. I picked him. I would pick him again. Three perfect lineups in three weeks and the man is in sixth place."))
    parts.append(gil(
        "In fairness to Rahul Pahuja, he has the third-most points in the league, 1,259.20, and nothing on his bench would have helped. Luther Burden III was projected for 12.92 and scored 2.30. In fairness to Michael Smith, he left 12.50 behind: Woody Marks did not play in the flex with Kimani Vidal's 6.40 on the bench, and DK Metcalf scored 0.70."))
    parts.append(boomer(
        "Dak Prescott has scored 90.32 for Michael Smith in two weeks. Ninety. Smith started a running back who was not playing and a receiver who scored seven tenths of a point and won by 18, because when your quarterback is scoring 45 every week you can leave a seat empty. He is 7 and 3. Against the whole league he is 44 and 46. Michael Smith has a losing record against everybody and a winning record against whoever shows up."))

    # ---- 4. one week behind
    w, l = card_rows("Billy Norton", "Bob Dorsch")
    parts.append(mcard(
        "m-norton", "Norton by 19.00 with 88.00, his first win since Week 6", w, l,
        "DJ Moore 19.10, James Cook III 16.20 and Malik Nabers 15.00 for Billy Norton, with Ladd McConkey's 18.20 on his bench and Juwan Johnson at zero. Saquon Barkley 13.50, Bo Nix 13.50 on a projection of 25.06 and Zay Flowers 12.40 for Bob Dorsch, with Bijan Robinson and Jordan Love on the bye.",
        SCALE))
    parts.append(gil(
        "Billy Norton wins 88.00 to 69.00 and is 2 and 8, ending a four-game losing streak. The 88.00 is the 65th-fewest points in a win in 1,355 games in this league since 2011. Bob Dorsch's 69.00 is the sixth-worst game of his 244. He is 4 and 6. Dorsch still leads the series 16 and 7."))
    parts.append(boomer(
        "I picked Billy two weeks running and this time he came through. Now look at how. Last week Billy benched Stefon Diggs and Diggs scored 17.30. So this week he started Stefon Diggs, and Diggs scored 6.50, and Ladd McConkey scored 18.20 on the bench behind him. Billy Norton is managing last week's team. He is exactly seven days behind his own roster. Start McConkey next week, Billy, I am begging you, unless that is the week he scores four."))
    parts.append(gil(
        "In fairness to Bob Dorsch, Bijan Robinson, Jordan Love and Rhamondre Stevenson were on the bye, and he left 5.40 behind in a game he lost by 19.00. Bo Nix finished 11.56 under his projection. In fairness to Billy Norton, Kirk Cousins was projected for 18.00 and scored 7.40, and he won anyway."))
    parts.append(boomer(
        "Bob and Bo Nix. Last week Bob signed Bo Nix on Nix's week off and released him without a start. This week Bob signed him again, started him, and got 13.50. And to make room for Bo Nix, Bob released the Texans defense. Matt Davis signed the Texans defense. It scored 13 for Matt in a perfect lineup. Bob started the Steelers defense for five. Four titles, Gil. He let a 13 walk across the street so he could start a 5."))

    # ---- 5. the first-place bench
    w, l = card_rows("Spencer Lentz", "Ryan Kelly")
    parts.append(mcard(
        "m-lentz", "Spencer Lentz by 71.32, with a zero at defense and 14.00 of defense on his bench", w, l,
        "Patrick Mahomes 31.96, Chuba Hubbard 28.00, Emmett Johnson 24.30 and Javonte Williams 22.60 for Spencer Lentz, with the Vikings defense at zero and the 49ers defense's 14.00 and Derrick Henry's 17.10 on his bench. Caleb Williams 18.34 and Chris Boswell 13.00 for Ryan Kelly, with Cam Skattebo at 4.30 on a projection of 13.58.",
        SCALE))
    parts.append(gil(
        "Spencer Lentz wins 150.86 to 79.54 and is 8 and 2, first in the standings, with seven straight wins. It is the high score of the week. He left 17.00 behind: the 49ers defense scored 14.00 on his bench behind a zero from the Vikings, and Nico Collins scored 14.30 behind Tee Higgins's 11.30. Ryan Kelly is 2 and 8 and has lost three straight. Spencer leads the series 12 and 10."))
    parts.append(boomer(
        "The man who runs this booth carries two defenses. One scored 14 and one scored zero. I will let you guess which one he started. He has left 227.06 points on his bench this season, which is 69 more than anybody else in the league. Sixty-nine. The man runs a website about lineups. I called 25 for Mahomes and Mahomes scored 31.96, so I got mine. He left his on the bench."))
    parts.append(gil(
        "In fairness to Ryan Kelly, he left 2.80 behind, Blake Corum, Kyle Pitts Sr. and Drew Lock were on the bye, and TreVeyon Henderson is on injured reserve. Justin Jefferson was projected for 17.21 and scored 10.20. He started Caleb Williams, who scored 18.34."))
    parts.append(boomer(
        "Ryan started the right quarterback, like I said he would, and set close to the best lineup he had, and lost by 71. I have nothing for him this week. Some Sundays you do your homework and the other kid's dad built his volcano."))

    # ---- the bye
    o = T["Aron Rogers"]
    parts.append(byecard(
        "m-bye", "Aron Rogers on the bye: 136.86, the third-best score in the league, on a week off",
        {"team": o["name"], "owner": "Aron Rogers", "score": o["score"], "left": o["left"]},
        "CeeDee Lamb 26.70, Jared Goff 24.36 and George Pickens 22.30 for Aron Rogers, with Jacory Croskey-Merritt's 14.70 on his bench behind Rico Dowdle's 5.40. Bye-week scores never take a trophy and do not count in the standings.",
        SCALE))
    parts.append(gil(
        "Aron Rogers had the bye and is 7 and 3, third in the standings. His lineup scored 136.86, which only Spencer Lentz and Matt Davis beat this week. He left 9.30 behind. He has left 67.98 all season, the fewest in the league."))
    parts.append(boomer(
        "I called 130 for Rogers on his week off and he gave me 136.86, so thank you, Rogers, that is a win for the booth. It is the only thing that score did for anybody. A hundred thirty-six on a Sunday that did not count. He would have beaten eight of the ten teams that played, and instead he beat my over."))

    # ---- THE RACE
    parts.append(race_section())

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "The rule: do not leave the answer on your own bench. Nobody broke it this week. Michael Turner came closest. He left 29.82 behind and lost by 37.90, so his best lineup, 83.88, was 8.08 short. Billy Norton left 11.70 and won. Spencer Lentz left 17.00 and won. Matt Davis and Rahul Pahuja left 0.00."))
    parts.append(boomer(
        "Turner broke this rule last week and missed breaking it this week by eight points. The answer was on his bench again. It was just the wrong answer. That is the nicest thing I can say about a 54."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Eleven calls came due. Eight right, three wrong. Season record 53 and 56. That is fifteen right out of the last twenty-two, and I am three games from even. Do not tell me it does not matter. Every call is below, in ink."))
    parts.append(graded_list([
        ("Napoleon's Army", "Michael Turner clears 90 in Week 11.", "WRONG",
         "54.06. I listed the three men on the bye. He started the three."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Michael Turner.", "RIGHT",
         "By 37.90, with 91.96. I bet on the man who had to win. He did not have to do much."),
        ("Dallas Dawgs", "Matt Davis beats Aaron Jezioro.", "RIGHT",
         "By 75.10. I said he needed a defense by Sunday. He found one, and it scored 13."),
        ("| croup", "Ja'Marr Chase clears 20 again for Aaron Jezioro.", "WRONG",
         "5.60 on a projection of 22.03. I bet on Chase and hoped for the owner. I got neither."),
        ("Pack Up", "Rahul Pahuja beats Michael Smith.", "WRONG",
         "Lost by 18.54 with a perfect lineup. I bet on the one who scored 173 twice. He was missing 63 of it."),
        ("Midget Grinders", "Dak Prescott clears 25 for Michael Smith.", "RIGHT",
         "44.90. I moved the bar from 20 to 25 and he cleared it by almost twenty. I am out of bars."),
        ("I Loved You Tom Brady", "Billy Norton beats Bob Dorsch.", "RIGHT",
         "By 19.00. I picked Billy two weeks in a row and went one for two. Billy would take one for two."),
        ("WPB Steel City", "Saquon Barkley clears 12 for Bob Dorsch.", "RIGHT",
         "13.50. He did his share. It was the rest of the 69 that came up short."),
        ("Balls Deep", "Patrick Mahomes clears 25 for Spencer Lentz.", "RIGHT",
         "31.96, in the lineup this time. I bet 25 of it would count. All of it did."),
        ("Old Man Smashers", "Caleb Williams starts for Ryan Kelly in Week 11.", "RIGHT",
         "He started and scored 18.34. Ryan read the schedule."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers clears 130 on his bye.", "RIGHT",
         "136.86. I asked for 130 on a week off and he gave me six extra that nobody can use."),
    ]))
    parts.append(gil(
        "Eight right, three wrong. Eleven new ones for Week 12, one per team. Ryan Kelly has the bye. No NFL team is off. It is Thanksgiving week: the Packers and Rams play Wednesday, six teams play Thursday, and the Broncos and Steelers play Friday, so lineups lock early."))
    parts.append(calls_list([
        ("Napoleon's Army", "Michael Turner clears 80 in Week 12.",
         "No NFL team is on the bye this week, Turner. None. I am not listing names again, because I saw what happened to the last list. Jayden Daniels is at Arizona and Breece Hall is at Miami. Eighty. I believe in you more than the evidence does."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers beats Michael Turner.",
         "Rogers leads the series 9 and 5 and won 131.50 to 131.16 in Week 1. Rogers comes off the bye with CeeDee Lamb and George Pickens home to Philadelphia on Thursday. I am betting on the man with the fewest points left on his bench in the league."),
        ("Dallas Dawgs", "Matt Davis beats Michael Smith.",
         "Davis leads the series 14 and 7 and has won seven straight. Both are 7 and 3. Kyren Williams and the Rams defense are back from the bye, and Joe Burrow is home to the Saints. I am betting on the 44 and 46 team finally meeting somebody who makes it count."),
        ("Midget Grinders", "Dak Prescott clears 25 again for Michael Smith.",
         "45.42 and 44.90 the last two weeks. Dallas is home to Philadelphia on Thursday. I set the bar at 20, then 25, and he has cleared both by about twenty. I am leaving it at 25 because I am scared to go higher."),
        ("Pack Up", "Rahul Pahuja beats Bob Dorsch.",
         "Dorsch leads the series 14 and 8, and Rahul has won the last five. Jaxon Smith-Njigba and Matthew Golden are back from the bye, so the machine gets its parts back. He is in sixth with the third-most points in the league. I am betting he is not in sixth for long."),
        ("WPB Steel City", "Bob Dorsch scores 100 or more in Week 12.",
         "75.10 and 69.00 the last two weeks. Bijan Robinson, Jordan Love and Rhamondre Stevenson are all back from the bye. Bob made seven roster moves this week to score 69. I am betting that getting his own players back works better."),
        ("Colorado Narcoleptic Kestrels", "Josh Allen clears 20 for Eric Olson.",
         "15.16 this week on a projection of 27.14. Buffalo is home to Kansas City on Thursday. Eric has not cleared 103 in three weeks and is still 7 and 3. I am betting the quarterback remembers who he is before the playoffs do."),
        ("I Loved You Tom Brady", "Ladd McConkey starts for Billy Norton in Week 12.",
         "18.20 on the bench this week. The Chargers are home to New England. Billy benched Diggs the week Diggs scored 17 and started him the week he scored 6. I am betting Billy catches up to his roster by one week."),
        ("| croup", "Brock Purdy clears 20 again for Aaron Jezioro.",
         "38.66 and 28.20 the last two weeks, and San Francisco is home to Seattle. Jezioro has picked Purdy over Trevor Lawrence twice and been right twice. I am betting on the one decision on that roster that keeps working."),
        ("Balls Deep", "Spencer Lentz leaves under ten on his bench in Week 12.",
         "17.00 this week, 54.20 on his bye, 227.06 on the season. Nobody has left more. I am asking the man who runs this booth to look at his own bench one time. I do not expect to win this one."),
        ("Old Man Smashers", "Ryan Kelly clears 100 on his bye.",
         "114.20 a week ago and 79.54 this week. Nothing counts for him on Sunday. Blake Corum is back from the bye and Justin Jefferson is home to Atlanta. I am betting Ryan has a good day when it cannot help him, because that is the kind of year it has been."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, then by size. When an owner already holds one, the next name in line takes it. Bye-week scores never take a trophy."))
    parts.append(award(
        "good", "Owner of the Week", "Matt Davis · Dallas Dawgs",
        "146.20 with a perfect lineup, a win by 75.10, and an 8 and 1 day against the field. He signed David Montgomery and the Texans defense this week, started both, and got 28.90 from them. It is the 26th-best game of his 245 in this league. Spencer Lentz's 150.86 was the higher score and came with 17.00 left behind.",
        "Matt needed a defense and a flex. He went and got a defense and a flex. They scored 13 and 15.90. That is the whole story, and in this league that makes him a genius. Third Owner of the Week. He is 2.68 points out of the league lead in scoring and I think he knows it."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Michael Turner · Napoleon's Army",
        "54.06, the low score of the week, a loss to all nine other teams that played, and the 22nd-lowest score of 2,709 team-weeks since 2011. Drake London, Zach Charbonnet and Josh Jacobs started on their bye. Breece Hall's 17.50 and Aaron Rodgers's 17.98 were on his bench. He scored 56.56 a week ago with five starters who did not play.",
        "Second straight week, third Worst Owner of the season. Fifty-six, then fifty-four. Turner is getting worse at a thing I did not think had a floor. I gave him the names. I do not know what else a broadcaster can do. Next week I am going to call him."))
    parts.append(award(
        "good", "Start of the Week", "Michael Smith · Dak Prescott, 44.90",
        "Projected for 27.27, so 17.63 over, the biggest margin over projection by any starter in the league this week. Jonah Coleman's 34.90 for Rahul Pahuja was 16.55 over and second. Ashton Jeanty's 28.40 for Eric Olson was 16.24 over and third.",
        "Michael Smith won Waste of the Week two weeks running. This is a better shelf. Dak has scored 45.42 and 44.90, and all Smith has to do is not bench him, and so far he has not benched him. Do not get clever, Michael Smith. You are one clever idea from sixth place."))
    parts.append(award(
        "bad", "Sit of the Week", "Billy Norton · Ladd McConkey, 18.20 on the bench",
        "Stefon Diggs started in his place for 6.50, an 11.70 swing. No benching cost a game this week. Michael Turner's Breece Hall behind J.K. Dobbins was 17.50 and first, and Turner holds Worst Owner. Spencer Lentz's 49ers defense behind the Vikings was 14.00 and second, and Lentz holds Waste of the Week.",
        "Second straight Sit of the Week for Billy, and this time he won the game. Diggs on the bench for 17.30, then Diggs in the lineup for 6.50. Billy is not making bad decisions. He is making last week's good decision, a week late."))
    parts.append(award(
        "bad", "Waste of the Week", "Spencer Lentz · 17.00 left behind, and he won",
        "The 49ers defense scored 14.00 on his bench behind the Vikings defense's zero, and Nico Collins 14.30 behind Tee Higgins's 11.30. His best lineup was 167.86. Michael Smith left 12.50 in his win and Billy Norton 11.70 in his.",
        "Third Waste of the Week. He left 54 on his bench on the bye and 17 more this week. He started a defense that scored zero with 14 sitting behind it. He builds a page every week that tells eleven people to check their bench, and he has not read it."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All eleven of you, every week, all season. Spencer Lentz leads at 227.06. Michael Turner added 29.82 and moved into second at 157.62, past Aaron Jezioro at 152.28. Aron Rogers is still the cleanest at 67.98, and that includes 9.30 on a week off."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 11, season_note=(
        "Season totals come from the season ledger through Week 11 and include bye weeks. Spencer Lentz leads at 227.06, Michael Turner is second at 157.62, Aaron Jezioro third at 152.28. Aron Rogers has left the fewest, 67.98.")))
    parts.append(gil(
        "No bench cost a game this week. Michael Turner left 29.82 and lost by 37.90. Spencer Lentz left 17.00, Michael Smith 12.50 and Billy Norton 11.70, and all three won. Matt Davis and Rahul Pahuja left 0.00."))
    parts.append(boomer(
        "Three of the five winners left double digits behind, and the one man who set a perfect lineup and lost is in sixth place. This was a week when it did not matter what you did with your bench unless your bench was the only part of your team that was playing."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Matt Davis signing David Montgomery, who started and scored 15.90, for Audric Estime. His Texans defense, 13.00 in the lineup, for Omar Cooper Jr. was second. Ryan Kelly's Chig Okonkwo also started, for 8.60 at tight end."))
    parts.append(gil(
        "<strong>Worst move that made a lineup:</strong> Eric Olson signing Courtland Sutton, who started and scored zero. Bob Dorsch released Germie Bernard, who scored 7.00, for Xavier Hutchinson, who started for 2.30. Aaron Jezioro released Khalil Shakir, who scored 14.80, for Konata Mumpfield, who was on the bye. Matt Davis released Xavier Worthy, who scored 10.80, for Jordyn Tyson, 1.50 on his bench."))
    parts.append(boomer(
        "Fifteen moves went through this week and Bob Dorsch made seven of them. He signed Adonai Mitchell and released Adonai Mitchell. He signed Kaelon Black and released Kaelon Black. He released Rhamondre Stevenson and signed Rhamondre Stevenson back. Seven moves, and six of them cancelled each other out. Bob spent the week rearranging the furniture and scored 69 in the living room."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Aron Rogers at Michael Turner, Spencer Lentz at Aaron Jezioro, Eric Olson at Billy Norton, Matt Davis at Michael Smith, and Bob Dorsch at Rahul Pahuja. Ryan Kelly has the bye. No NFL team is off, and with games on Wednesday, Thursday and Friday, check your lineup before the holiday. Three weeks remain in the regular season."))
    parts.append(boomer(
        "Circle Davis at Smith. Two teams at 7 and 3, one that has beaten the other seven straight times, and a quarterback who has scored 90 in two weeks standing in the middle of it. Rahul gets his two receivers back and Bob Dorsch across from him, and needs it, because he is the one good team on the wrong side of the line. Olson gets Billy Norton, who is on a one-game winning streak and feeling dangerous. And Aron Rogers comes off the bye to play Michael Turner. Check the lineup, Turner. I am asking as a friend."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 11, HEADLINE, DEK, build(), META, "foh-week-11.png", nav=NAV,
        published="2026-11-24T05:00:00-05:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "week-11.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
