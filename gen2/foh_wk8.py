"""Friends of Herb, Week 8. Editorial.

Boomer runs SCORCHING (standing from Week 6). Gil is the straight man. Nobody is safe, Spencer gets no
alibis, clean language, roast cap and Gil defenses apply. Herb content gets reverence. HALFTIME is retired
(Week 7 one-off; Spencer, 2026-11-03). Spencer's personal life stays off this page.

NEW THIS WEEK, agreed with Spencer 2026-11-03: THE OWNER SPOTLIGHT, one owner per league per week from the
all-time log (gen2/spotlight.py -> docs/data/foh_spotlight_wk8.json), first up Bob Dorsch, the reigning
champion at 2 and 5. And a lifetime series line on every matchup card (gen2/series.py). Friends of Herb's
log starts in 2011 (no weekly scores from the CBS era), so every series line says since 2011. Both are
permanent from here.

Outlier engine, Week 8: nothing cleared HEADLINE or PROMOTE on league-week rarity; a quiet week by the
numbers and a loud one by the stories. SUPPORT: Aaron Jezioro beat Michael Turner by 68.02, the 68th-biggest
margin of 1,340 games since 2011, and took the lead in a series that was 16-16; Turner 1-6 on a 24-39
all-play excluding bye teams (1.7 wins unlucky); Eric Olson's 158.96 is the 4th-best of his 70 games since 2011; Zay Flowers 0.00
on 17.71 for Bob Dorsch (46th-worst miss by a projected starter since 2018); Spencer leads Rahul Pahuja 17-10;
Billy Norton lost with Kirk Cousins's 34.18 (80th-most by one starter in a loss since 2018); Spencer left
Patrick Mahomes on the bench for 32.44 (90th-most by one benched player since 2018); Tyler Allgeier 35.60 on
7.29 for Ryan Kelly; Olson 3 straight over Dorsch, Kelly 3 straight over Norton; Turner's 70.28 is the
147th-lowest of 2,679 team-weeks. Off the engine because byes are excluded: Joe Burrow's 50.48 for Matt Davis
on the bye is the 7th-best quarterback start of 1,216 since 2018 and the 15th-best start of any kind in
10,945, and Davis's 160.38 would have been the 11th-best game of his 242.

League intel (FOHFFL thread after Week 7, filed in the handoff register): Turner quoted the Booth back and
named himself "Napoleon the Magnanimous"; Kelly thanked the Commish for his first W; Eric Olson asked for
the Booth's prompt.

Verified against foh_wk8_facts.json, foh_season.json, foh_spotlight_wk8.json and gen2/data/foh_games.json.
"""
import os

import booth
from booth import award, boomer, byecard, calls_list, gil, graded_list, jump, ledger, mcard, spotlight
from compute import by_owner, ledger_rows, load

NAV = (
    '<nav class="nav" aria-label="Sections"><ul>'
    '<li><a href="#board">The Scoreboard</a></li>'
    '<li><a href="#spotlight">Owner Spotlight</a></li>'
    '<li><a href="#freiermuth">The Freiermuth Rule</a></li>'
    '<li><a href="#calls">On The Record</a></li>'
    '<li><a href="#hardware">The Hardware</a></li>'
    '<li><a href="#ledger">The Bench Ledger</a></li>'
    '<li><a href="#wire">The Waiver Wire</a></li>'
    '<li><a href="#next">Next Sunday</a></li></ul></nav>'
)

FACTS = load("foh_wk8_facts.json")
SEASON = load("foh_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 161.28

HEADLINE = "Joe Burrow Scored 50.48 For Matt Davis. Matt Davis Had The Week Off."
DEK = (
    "The best quarterback game in Friends of Herb this season happened on a bye. Eric Olson scored 158.96, the "
    "fourth-best game of his career, and beat the reigning champion by 51. Aaron Jezioro beat Michael Turner by "
    "68 and took the lead in a series that was tied at sixteen. Ryan Kelly won a second straight on a backup "
    "running back who scored 35. Spencer Lentz is first in points and first in points left on the bench. New "
    "this week: a lifetime series line on every card, and THE OWNER SPOTLIGHT, starting with the champ at 2 "
    "and 5."
)
META = (
    "Gil and Boomer call Week 8 of Friends of Herb: Joe Burrow's 50.48 on Matt Davis's bye, Eric Olson's "
    "158.96 over the reigning champion, Jezioro by 68 over Turner for the series lead, Kelly's second straight "
    "win, Spencer's 21 points on the bench, a series line on every card, and the first Owner Spotlight: Bob "
    "Dorsch, four titles, 2 and 5."
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

    # ---- 1. the champ gets 51 dropped on him
    w, l = card_rows("Eric Olson", "Bob Dorsch")
    parts.append(mcard(
        "m-olson", "Olson's 158.96, the fourth-best game of his career, over the reigning champion by 51.44", w, l,
        "Bhayshul Tuten 30.90 on a projection of 13.95, Josh Allen 30.56, Michael Wilson 24.80 on a projection "
        "of 10.68 and the Jaguars defense, signed this week, 19.00 for Eric Olson. Bob Dorsch got 27.52 from "
        "Jordan Love and 24.30 from Braelon Allen, started Zay Flowers for zero and Bijan Robinson for 7.60, "
        "and left Rachaad White, claimed this week, on his bench for 13.00.", SCALE, key=True,
        series="Bob Dorsch leads 5-3 since 2011, two in the playoffs · Olson has won the last three, two of them in 2014"))
    parts.append(gil(
        "Eric Olson wins 158.96 to 107.52 and is 6 and 2, second in points at 1,005.98, five and a half behind "
        "the lead. The 158.96 is the fourth-best game of his 70 in this league since 2011, and it beats every other "
        "team that played. He signed the Jaguars defense this week for the Patriots and got 19.00. Bob "
        "Dorsch, the reigning champion, is 2 and 5 and has lost three straight. He left 5.40 behind, and he "
        "made five moves this week, two of them on the same defense: he claimed the Buccaneers for Jordan "
        "Addison, then released the Buccaneers for the Texans, who were on bye. The Buccaneers scored 16.00."))
    parts.append(boomer(
        "The champ is 2 and 5 and this week he signed a defense, cut the defense, and the defense he cut "
        "scored sixteen for nobody. Bob also cut Jaylen Waddle, who scored thirteen, to sign KC Concepcion, who "
        "scored five, and then benched the running back he claimed, who scored thirteen, for Bijan Robinson, "
        "who scored seven. Five moves, Gil, and three of them were a man walking the wrong way up an "
        "escalator. We have a whole segment on Bob this week, and it is going to say he is great, and he is, "
        "and he is also 2 and 5."))
    parts.append(gil(
        "In fairness to Bob Dorsch, Love and Allen were 51.82 between them and the Steelers defense scored 17.00, "
        "and Zay Flowers was projected for 17.71 and gave him nothing, the 46th-worst miss since 2018 by a "
        "starter in this league projected for ten or more. Against the nine other teams that played this week he "
        "went 4 and 5, and for the season he is 30 and 33, so his 2 and 5 is more than a win worse than his "
        "scores. Eric Olson released Bo Nix this week with Josh Allen back, and Nix scored 23.28 on the wire."))
    parts.append(boomer(
        "Eric released a quarterback who scored 23 and it did not matter because the one he kept scored 30 and "
        "the running back he started scored 31 and the receiver he started on a projection of ten scored 25. "
        "Eric asked for this booth's instructions last week. Eric, here they are: score 159. And he has the bye "
        "next week, which means the only man who can stop Eric Olson right now is the schedule, and the "
        "schedule got him."))

    # ---- 2. the series lead
    w, l = card_rows("Aaron Jezioro", "Michael Turner")
    parts.append(mcard(
        "m-turner", "Jezioro by 68.02, and the lead in a series that was tied at sixteen", w, l,
        "Ja'Marr Chase 27.60, Trevor Lawrence 25.40, Brock Bowers 24.70 and Jaylen Warren 22.80 for Aaron "
        "Jezioro, with Kenny Gainwell, signed this week, at 16.00 and Will Reichard at 1.00. Michael Turner got "
        "20.20 from Josh Jacobs and 16.98 from Jayden Daniels, started Drake London for 1.30, J.K. Dobbins for "
        "1.30 and Tre Tucker for zero, and had Lamar Jackson, out, on his bench.", SCALE,
        series="Aaron Jezioro leads 17-16 since 2011 · Jezioro has won the last two"))
    parts.append(gil(
        "Aaron Jezioro wins 138.30 to 70.28 and is 3 and 4. The margin, 68.02, is the 68th-biggest of 1,340 games "
        "in this league since 2011. These two had played 32 times and split them, 16 and 16, and Boomer's call "
        "was that Turner would take the lead. Jezioro took it instead. Michael Turner is 1 and 6, five straight "
        "losses, with the low score of the week, which loses to all nine teams that played. Three of his nine starters "
        "scored 1.30 or less."))
    parts.append(boomer(
        "Napoleon the Magnanimous, by his own decree last week, scored 70 and lost by 68. He named himself after "
        "a man who lost an empire, Gil, and then went out and lost a province to Aaron Jezioro, who is 3 and 4 "
        "and had lost three of the previous four to him. Drake London scored 1.30. J.K. Dobbins scored 1.30. "
        "Tre Tucker scored nothing. Michael started three men and got 2.60 out of them, which is less than a field goal."))
    parts.append(gil(
        "In fairness to Michael Turner, he is 1 and 6 on a 24 and 39 all-play, which is almost two wins unlucky, "
        "the most of anyone in the league, and Lamar Jackson was out, so the quarterback decision made itself. "
        "Jacobs and Daniels did their part. Aaron Jezioro's 138.30 is the 20th-best game of his 239 here, he "
        "got 16.00 from Gainwell the week he signed him, and he released Jalen Coker, who scored 8.60 for Rahul "
        "Pahuja's bench after Pahuja claimed him off waivers."))
    parts.append(boomer(
        "Jezioro cut a receiver, Rahul picked him up, and the receiver scored eight on Rahul's bench. That is "
        "the most Friends of Herb transaction of the year: two men, one player, zero points used. And Jezioro "
        "still scored 138, because Chase, Lawrence, Bowers and Warren put up 100 by themselves and left the "
        "rest of the roster to argue about who had to bring the kicker. Reichard scored one. The argument "
        "continues."))

    # ---- 3. first in points, first in points on the bench
    w, l = card_rows("Spencer Lentz", "Rahul Pahuja")
    parts.append(mcard(
        "m-lentz", "Spencer by 10.40 with 21.18 on his bench, over a perfect Pahuja lineup", w, l,
        "Tee Higgins 34.50 on a projection of 13.59, Drake Maye 26.46 and Tucker Kraft 14.30 for Spencer Lentz, "
        "who started Javonte Williams for 6.20 with Chuba Hubbard's 21.40 on his bench, started Jason Myers, "
        "signed this week, for zero, and left Patrick Mahomes at 32.44. Rahul Pahuja left nothing behind: "
        "Jaxon Smith-Njigba 23.80, Jonah Coleman 18.40 the week he signed him, Matthew Golden 17.40, and Bryce "
        "Young 12.36.", SCALE,
        series="Spencer Lentz leads 17-10 since 2011, two in the playoffs"))
    parts.append(gil(
        "Spencer Lentz wins 113.96 to 103.56 and is 6 and 2, first on points at 1,011.48. He left 21.18 on his "
        "bench, the most in the league this week, and he now leads the season bench ledger at 151.36. Hubbard "
        "for Javonte Williams was a 15.20 swing, the biggest benching in the league this week. Mahomes scored "
        "32.44 behind Maye's 26.46, the 90th-most points by one benched player in this league since 2018. He "
        "signed Jason Myers this week for Dominic Zvada, and Myers scored zero. Rahul Pahuja set a perfect "
        "lineup with Christian McCaffrey and C.J. Stroud on bye and lost by 10.40. Spencer leads the series 17 "
        "and 10."))
    parts.append(boomer(
        "Spencer is first in points and first in points he did not use. He signed a kicker this week and the "
        "kicker scored nothing, he benched a running back who scored 21 for one who scored 6, and his backup "
        "quarterback outscored his starting quarterback by six from the parking lot. He won by ten. Rahul set a "
        "perfect lineup with half his roster on vacation and lost to a man who left 21 at home. Rahul, "
        "you were out-rostered by a man who was trying to lose."))
    parts.append(gil(
        "In fairness to Rahul Pahuja, Coleman gave him 18.40 the week he signed him for Marvin Harrison Jr., the "
        "biggest swing of any move in the league this week, and he is 4 and 3 in fifth. Bryce Young was projected "
        "for 20.56 and scored 12.36, and Tyler Loop kicked 2.00. Spencer's 84.3% lineup efficiency, meaning he "
        "scored 84.3% of what his roster had, was the worst in the league this week. Tee Higgins has now scored "
        "25.80 and 34.50 in back-to-back weeks for him."))
    parts.append(boomer(
        "Worst lineup efficiency in the league and first place, Gil. Spencer started a kicker who scored zero, "
        "left Mahomes and Hubbard on the bench for fifty-four between them, and won by ten anyway. The lineup "
        "card was filled out in the dark, and the dark is 6 and 2."))

    # ---- 4. the backup
    w, l = card_rows("Ryan Kelly", "Billy Norton")
    parts.append(mcard(
        "m-kelly", "Kelly by 6.10 on a backup running back who scored 35; Norton's 34-point quarterback lost anyway", w, l,
        "Tyler Allgeier 35.60 on a projection of 7.29, Caleb Williams 15.98 and Rashee Rice 14.80 for Ryan "
        "Kelly, who started Emanuel Wilson for zero and Kyle Pitts Sr. for 1.60 with Kyler Murray's 23.90 on "
        "his bench. Billy Norton got 34.18 from Kirk Cousins, 17.10 from James Cook III and 16.10 from DeMario "
        "Douglas, started the Jets defense for minus two, and left nothing behind.", SCALE,
        series="Ryan Kelly leads 11-7 since 2011, one in the playoffs · Kelly has won the last three"))
    parts.append(gil(
        "Ryan Kelly wins 111.08 to 104.98 and is 2 and 5, two straight wins after an 0 and 5 start. Allgeier's "
        "35.60 on a projection of 7.29 is the biggest margin over projection by any starter in the league this "
        "week. Kelly left 11.32 behind, most of it Kyler Murray's 23.90 behind Caleb Williams, and won by 6.10 "
        "anyway. Billy Norton set a perfect lineup, got 34.18 from Kirk Cousins, which is the 80th-most by one "
        "starter in a loss in this league since 2018, and lost. He is 1 and 6. Kelly leads the series 11 and 7 "
        "and has won the last three."))
    parts.append(boomer(
        "Ryan Kelly thanked the Commish last week for his first win. This week he won again on a backup running "
        "back projected for seven who scored 35, and I want to know who to thank for that, because it was not "
        "Ryan. Ryan started a running back who scored zero and a tight end who scored one and a half and "
        "benched a 24-point quarterback, and he is on a two-game winning streak. The Old Man Smashers have "
        "four titles, Gil, and this is how all four of them happened. Nobody can explain any of it."))
    parts.append(gil(
        "In fairness to Billy Norton, there was nothing to fix. Cousins, Cook and Douglas were 67.38 between "
        "them, his bench was Malik Nabers on bye, Ladd McConkey, RJ Harvey, Jaylin Noel and Kendre Miller, and "
        "his best possible lineup was the one he played. The Jets defense scored minus two and his tight end, "
        "Juwan Johnson, was on bye with no replacement. Billy has four titles and is 1 and 6."))
    parts.append(boomer(
        "Billy played a perfect lineup and lost by six, and the six points that decided it were the Jets missing "
        "their projection by eight. Billy did not lose to Ryan Kelly. He lost to the New York Jets, which is a "
        "sentence that has ended a lot of Sundays in this country, Gil, but rarely in fantasy, where the Jets "
        "are usually somebody else's problem."))

    # ---- 5. the zero at defense
    w, l = card_rows("Aron Rogers", "Michael Smith")
    parts.append(mcard(
        "m-rogers", "Rogers by 21.04 with a zero at defense, over a perfect Smith lineup that scored 89", w, l,
        "Tony Pollard 29.20 on a projection of 14.54, D'Andre Swift 26.90 and T.J. Hockenson, signed this "
        "week, 13.80 for Aron Rogers, whose Chiefs defense scored zero and whose quarterback, Jared Goff, "
        "scored 11.04. Michael Smith left nothing behind: Dak Prescott 21.80, Puka Nacua 19.50, Tyler Bass "
        "16.00, and Jonathan Taylor 4.70 on a projection of 14.82.", SCALE,
        series="Aron Rogers leads 11-7 since 2011, one in the playoffs"))
    parts.append(gil(
        "Aron Rogers wins 110.14 to 89.10 and is 6 and 2, third in points at 991.00. Pollard cleared 20 again, as "
        "Boomer called, and Swift gave him 26.90. He released Harrison Butker this week for T.J. Hockenson, who "
        "started at tight end and scored 13.80 with George Kittle on bye. His defense scored zero and he still "
        "won by 21. Michael Smith set a perfect lineup and scored 89.10, which beats one of the other nine teams "
        "that played. He is 4 and 3."))
    parts.append(boomer(
        "Aron cut his kicker to sign a tight end and the tight end scored 14, which is a thing you can do when "
        "your two running backs score 56 between them. His defense scored zero and he won by 21. And Michael "
        "Smith played a perfect lineup and scored 89. A perfect 89. That is a man ironing a shirt with a hole "
        "in it, Gil. Every crease is right and you can still see his undershirt."))
    parts.append(gil(
        "In fairness to Michael Smith, Dak Prescott, Nacua and Bass were 57.30 between them, and his bench was "
        "Mike Evans, Deebo Samuel Sr., Woody Marks and Christian Kirk, all zeros, and Daniel Jones. Jonathan "
        "Taylor was projected for 14.82 and scored 4.70, and DK Metcalf was projected for 10.59 and scored 0.90. "
        "Against the nine other teams that played this week, Smith went 1 and 8. Aron Rogers has left 38.08 on his bench all season, "
        "the fewest in the league by 17."))
    parts.append(boomer(
        "Aron has left 38 points on the bench all year. Spencer left 21 on Sunday. Aron is the only man in "
        "this league who reads his lineup before he sends it, and his reward is 6 and 2 and third in points "
        "and nobody in the thread ever mentions him. I am mentioning him. Aron, you are the quietest "
        "contender in the history of this league, and if you keep it up, I am going to have to learn how you "
        "spell your first name without looking."))

    # ---- 6. the bye
    d = T["Matt Davis"]
    parts.append(byecard(
        "m-bye", "Davis on the bye: 160.38, Joe Burrow 50.48, and none of it counts",
        {"team": d["name"], "owner": "Matt Davis", "score": d["score"], "left": d["left"]},
        "Joe Burrow 50.48 on a projection of 28.90, Jahmyr Gibbs 25.80, Bucky Irving 23.00 and Jameson "
        "Williams 15.00 for Matt Davis, who left 0.90 behind, Tyler Warren's 3.80 behind Mark Andrews's 2.90. "
        "Bye-week scores never take a trophy and do not count in all-play.", SCALE))
    parts.append(gil(
        "Matt Davis had the week off and scored 160.38, which would have been the high score of the week by "
        "1.42 and the 11th-best game of his 243 in this league. Burrow's 50.48 would be the seventh-best game by a "
        "quarterback in this league since 2018, out of 1,217 quarterback starts, and the 15th-best start by any "
        "player out of 10,946. Davis is 5 and 2 and fourth in the standings, with the fourth-most points at "
        "904.52 and the second-fewest points against, 751.22."))
    parts.append(boomer(
        "Fifty points from his quarterback and the standings did not move a hair. Matt Davis just played the "
        "second-best game of his season in an empty stadium. The one week all year his bench was quiet too, "
        "there was nobody to play, and nobody saw it but Matt, in his kitchen, refreshing the app "
        "like a man who hit a hole in one with nobody else on the course. And he still benched the right tight "
        "end for the wrong one by 0.90, so even on a week off, the lineup card found a way."))

    # ---- THE OWNER SPOTLIGHT (new this week)
    parts.append('<h2 id="spotlight">The Owner Spotlight</h2>')
    parts.append(gil(
        "New this week, and permanent from here: one owner, one page, from the all-time log of this league, "
        "which on ESPN runs back to 2011. The CBS era before it left champions and finishes but no weekly "
        "scores, so every number below says since 2011 unless it says otherwise. We start with the reigning "
        "champion, because he is 2 and 5 and somebody should say out loud who he is."))
    parts.append(spotlight(
        "The Owner Spotlight · Week 8", "Bob Dorsch · WPB Steel City",
        "In the league since the CBS era · 241 games in the ESPN log · 2 and 5 this season, sixth in points, reigning champion",
        [
            ("4", "titles across both eras: 2010 on CBS, then 2012, 2015 and 2025. Tied for the most in league history with Ryan Kelly and Billy Norton, who are 2 and 5 and 1 and 6."),
            ("1,853.02", "points last regular season, 11 and 3. The most anyone has scored in a season on record, 1.82 ahead of Aron Rogers in 2021."),
            ("19-8", "against Spencer Lentz since 2011. He is also 16 and 6 against Billy Norton and 15 and 6 against Aaron Jezioro."),
            ("8-15", "against Matt Davis, the one man in the league who owns him. He beat Davis in last December's final, 158.90 to 100.28."),
            ("6", "finals since 2011, 3 and 3: lost to Kelly in 2011, beat Spencer in 2012, beat Turner in 2015, lost to Smith in 2020, lost to Davis in 2023, beat Davis in 2025."),
            ("116.31", "points a week for his career since 2011, second among the eleven active owners behind Eric Olson's 118.48. Career high 189.14, Week 6 of last season."),
        ]))
    parts.append(gil(
        "Bob Dorsch has made the playoffs in eleven of his fifteen completed seasons since 2011, and his one truly bad "
        "year before this one was 2014, when he went 4 and 9. The scores have cut both ways for him: 2011 was 9 "
        "and 4 on a 54 and 63 all-play, three wins better than he played, and he lost the final to Ryan Kelly; "
        "2013 was 6 and 8 on a 96 and 58, a 9 and 5 team by the scores that missed the playoffs. This season he is 2 and 5 on a 30 and 33, so about a win and a third unlucky, with the "
        "sixth-most points in the league and three straight losses."))
    parts.append(boomer(
        "Four rings, the biggest season on record, and he is 19 and 8 against the man in first "
        "place. Spencer Lentz has lost to Bob Dorsch more than he has lost to any human being, and Spencer is "
        "in first and Bob is 2 and 5 with a bench full of running backs he keeps meaning to start. Bob won the "
        "title last December by 58 over the one man who owns him, and then opened this season by losing to "
        "Rahul Pahuja by 0.46. That is not a slump, Gil. That is a man who left the trophy at the venue and has not "
        "been back for it."))
    parts.append(gil(
        "Bob Dorsch had never been 2 and 5 after seven games in the ESPN era until this season. His worst start since 2011 was 3 "
        "and 4, three times, and one of those years, 2017, he finished 8 and 5 and made the playoffs. He "
        "plays Aron Rogers next, whom he leads 10 and 7, and then the schedule turns toward December, where "
        "he is 13 and 8 in the bracket for his career."))
    parts.append(boomer(
        "Thirteen and eight in the playoff bracket and four rings, and right now he cannot beat Eric Olson, who has "
        "won the last three meetings and the first two of those were in 2014, when Bob was last this bad. "
        "Olson has been waiting twelve years to finish the job, Gil. Bob, the file says four rings and the "
        "biggest season on record. The standings say you are eighth. One of "
        "them is going to be right in December, and the file has a better record than the standings."))

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "The rule: do not leave the answer on your own bench. For the second straight week nobody lost a game "
        "that his bench would have won. The closest was nobody: Dorsch left 5.40 in a loss by 51.44, Turner 4.40 "
        "in a loss by 68.02, Smith, Pahuja and Norton nothing at all. The spirit of the rule took a beating from "
        "the winners instead: Spencer Lentz left 21.18 and Ryan Kelly 11.32, both in wins."))
    parts.append(boomer(
        "Three of the five losers played perfect lineups and the two biggest benches in the league both won. "
        "The Freiermuth Memorial Rule is undefeated this week because nobody could be bothered to break it "
        "properly. Spencer and Ryan, you left 32 points on the bench between you and won by 16. The rule does "
        "not care, Gil. The rule only comes out when you lose, and the rule has a long memory."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Eleven calls came due. Eight right, three wrong, which in this booth counts as a parade, "
        "and I would like it noted that two of the three I missed were me betting on Michael Turner and Michael "
        "Smith, which is a lesson about betting on men named Michael that I will forget by the next time one of them is on the board. Season "
        "record 34 and 42. Every call is below."))
    parts.append(graded_list([
        ("Dallas Dawgs", "Matt Davis clears 130 on his bye.", "RIGHT",
         "160.38, with fifty from Burrow. I bet on a man to show up for a game that did not exist and he brought "
         "the second-best game of his season. Matt, I apologize for every chatbot joke. For this week."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Bob Dorsch.", "RIGHT",
         "By 51.44, with 158.96. Olson signed Bo Nix for Josh Allen's bye and cut him this week with Allen back, "
         "and won by fifty anyway. The man who cut Pat Freiermuth lost by fifty. The rule keeps score."),
        ("WPB Steel City", "Bob Dorsch starts Rhamondre Stevenson in Week 8.", "WRONG",
         "He started Bijan Robinson for 7.60 and benched Stevenson for 10.50 and Rachaad White for 13.00. Two "
         "running backs on the bench who outscored the one in the lineup, and the one in the lineup was the "
         "headliner. I bet on the wrong one of the right ones."),
        ("Balls Deep", "Spencer Lentz beats Rahul Pahuja.", "RIGHT",
         "By 10.40, with 21 on the bench and a kicker who scored zero. I got the call. Spencer got the win. "
         "Neither of us earned it."),
        ("Pack Up", "Rahul Pahuja leaves under ten on his bench in Week 8.", "RIGHT",
         "Zero. A perfect lineup, with McCaffrey and Stroud on bye. The man had fewer choices and made all of "
         "them right, which is the only recipe that has ever worked for him."),
        ("Kim Jong Un Pleasure Squad", "Tony Pollard clears 20 again for Aron Rogers.", "RIGHT",
         "29.20, after 37.00 last week. The call writes itself and I am taking credit for the handwriting."),
        ("Midget Grinders", "Michael Smith beats Aron Rogers.", "WRONG",
         "Lost by 21.04 with a perfect lineup that scored 89. I bet on Smith's lineup discipline and got exactly "
         "that: a disciplined 89."),
        ("Old Man Smashers", "Ryan Kelly beats Billy Norton.", "RIGHT",
         "By 6.10, on a 35 from a backup running back and a negative two from Billy's defense. I called the "
         "winner. I could not have called the how in a hundred tries."),
        ("I Loved You Tom Brady", "Billy Norton clears 90 in Week 8.", "RIGHT",
         "104.98, a perfect lineup, 34 from Cousins, and a loss. Right about the points, and the points were "
         "the only thing that went right for Billy."),
        ("Napoleon's Army", "Michael Turner beats Aaron Jezioro and takes the lead in the series.", "WRONG",
         "Lost by 68.02. The series is 17 and 16, Jezioro. I bet on the emperor and he scored 70. Napoleon the "
         "Magnanimous is now also Napoleon the Trailing."),
        ("| croup", "Aaron Jezioro starts Ja'Marr Chase in Week 8.", "RIGHT",
         "Started, 27.60, and 138 for the team. I asked for one thing and he did it and then did eight more. If "
         "I had asked him to start the kicker too he might have found one who scored."),
    ]))
    parts.append(gil(
        "Eight right, three wrong. Eleven new ones for Week 9, one per team. Eric Olson has the bye, and the "
        "Steelers and Titans have the week off, so Tony Pollard, Jaylen Warren, Kenny Gainwell, DK Metcalf, "
        "Chris Boswell and the Pittsburgh defense sit this one out."))
    parts.append(calls_list([
        ("Dallas Dawgs", "Matt Davis beats Spencer Lentz.",
         "Twenty-eight games between them since 2011, four of them in the playoffs, and the series is 14 and "
         "14. Spencer won the last two. Davis just scored 160 on a bye with 50 from Burrow, and left 0.90 on his "
         "bench. Spencer left 21.18 and a kicker who scored zero. I am betting the man who sets the lineup."),
        ("Balls Deep", "Tee Higgins clears 20 again for Spencer Lentz.",
         "25.80 and 34.50 the last two weeks, and Cincinnati plays Atlanta at 9:30 Sunday morning, so by the "
         "time the rest of you wake up this call will be decided. Spencer may lose the game. Higgins is not "
         "the reason."),
        ("WPB Steel City", "Bob Dorsch beats Aron Rogers.",
         "Dorsch leads the series 10 and 7, he is the champ, he is 2 and 5 on three straight losses, and he has "
         "just read his own file on this page. Pollard is on bye for Rogers. A man with four rings does not "
         "lose a fourth straight the week the booth puts his name in lights. If he does, I will put it in "
         "bigger lights."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers leaves under five on his bench in Week 9.",
         "He has left 38.08 on the bench all season, the fewest in the league by 17. With Pollard on bye the "
         "lineup has one fewer decision in it. I am betting on the man who gets fewer of those wrong than anyone "
         "in the league."),
        ("Old Man Smashers", "Ryan Kelly beats Rahul Pahuja.",
         "Rahul has won the last three meetings, including last December's consolation game, 162.00 to 81.24. Kelly has won "
         "two straight and his backup running back just scored 35. Kelly still leads the series 13 and 12. I am betting the hot hand "
         "against the hotter one, which is how every Ryan Kelly title has started, and there are four."),
        ("Pack Up", "Rahul Pahuja leaves under five on his bench in Week 9.",
         "He left nothing this week with McCaffrey and Stroud on bye. Now they are back, and so are the "
         "decisions. I am betting he makes them right. Rahul, that is a compliment, and it is also a trap."),
        ("Midget Grinders", "Michael Smith beats Michael Turner.",
         "Turner leads the series 13 and 12, but he is 1 and 6 on five straight losses and just scored 70. Smith "
         "set a perfect lineup and scored 89, which is sad, and 89 beats 70, which is math."),
        ("Napoleon's Army", "Michael Turner clears 100 in Week 9.",
         "He averaged 110 a week before Sunday. Lamar Jackson plays Thursday night, or does not, and either way "
         "there are eight other slots. One hundred. This call is for you, Michael, and it is the kindest thing I "
         "have done all season."),
        ("| croup", "Aaron Jezioro beats Billy Norton.",
         "Norton leads the series 16 and 8. Jezioro won the last one, a December consolation game, by 47, and just scored 138. Billy has four titles and is 1 and 6. I am "
         "betting the man who is scoring."),
        ("I Loved You Tom Brady", "Kirk Cousins clears 20 again for Billy Norton.",
         "34.18 this week in a loss. The quarterback is not the problem. I am betting on the quarterback and "
         "not the team around him, which, Billy, is also how the team got built."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson clears 120 on his bye.",
         "Davis did 160 on his. Olson is the man who built a robot to set his lineup, and the robot does not "
         "know what a bye is. Josh Allen plays Monday night in Minnesota, so this one goes the distance."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. Sit of the Week goes first to a benching that cost a game, "
        "then by size. When an owner already holds one, the next name in line takes it. Bye-week scores never "
        "take a trophy."))
    parts.append(award(
        "good", "Owner of the Week", "Eric Olson · Colorado Narcoleptic Kestrels",
        "158.96, the high score among the ten teams that played, the fourth-best game of his 70 in this league "
        "since 2011, and a win by 51.44 over the reigning champion. Tuten 30.90, Allen 30.56, Wilson 24.80, the "
        "Jaguars defense 19.00 the week he signed them, and 1.00 left behind.",
        "Eric signed a defense this week, the defense scored 19, and he kept it, which in this league this week "
        "counts as a strategy. One point on the bench, 159 on the field, and the "
        "robot gets the week off next Sunday, which is the first time all year Eric Olson and his lineup have "
        "had the same schedule."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Michael Turner · Napoleon's Army",
        "70.28, the low score of the week, which loses to all nine teams that played, in a loss by 68.02 that handed Aaron "
        "Jezioro the series lead. Drake London 1.30, J.K. Dobbins 1.30, Tre Tucker 0.00, the Broncos defense "
        "2.00. Five straight losses.",
        "Seventy points and the series lead gone in one afternoon. Michael started three men who combined for "
        "2.60, and he left 4.40 on the bench, so there were no right ones to pick. Napoleon, the army is the "
        "problem."))
    parts.append(award(
        "good", "Start of the Week", "Ryan Kelly · Tyler Allgeier, 35.60",
        "Projected for 7.29, so 28.31 over, the biggest margin over projection by any starter in the league this "
        "week. Joe Burrow's 50.48 for Matt Davis was 21.58 over and came on a bye. Tee Higgins's 34.50 for "
        "Spencer Lentz was 20.91 over and third.",
        "A backup running back projected for seven scored 35 in Ryan Kelly's flex, and I would give Ryan credit "
        "for the start if the rest of his lineup did not include a running back who scored zero and a tight "
        "end who scored one and a half. Allgeier found Ryan, Gil, the way the four titles did."))
    parts.append(award(
        "bad", "Sit of the Week", "Spencer Lentz · Chuba Hubbard, 21.40 on the bench",
        "Javonte Williams started at flex in his place for 6.20, a 15.20 swing, the biggest benching in the "
        "league this week. Patrick Mahomes's 32.44 sat behind Drake Maye's 26.46 on the same bench. Spencer "
        "won by 10.40, so the benching flipped nothing but the trophy. Kelly's Kyler Murray for Caleb Williams "
        "was 7.92 and second.",
        "Spencer benched 21 and 32 in the same week and won, which means the only thing he lost on Sunday was "
        "the argument. First in points, first in points left on the bench, and the Sit of the Week. Spencer, "
        "the trophy case is starting to look like a ledger."))
    parts.append(award(
        "bad", "Waste of the Week", "Aron Rogers · 7.00 left behind, and he won",
        "Rico Dowdle scored 11.60 on his bench behind George Pickens's 5.80 at flex, and Josh Downs's 10.30 sat "
        "behind Amon-Ra St. Brown's 9.10. Spencer Lentz left 21.18 and Ryan Kelly 11.32 in their wins, and both "
        "already hold a trophy.",
        "Seven points. Aron Rogers won the Waste of the Week with seven points because the two men ahead of him "
        "already had hardware and nobody else was left. It is the cleanest Waste ever awarded. Aron, you got "
        "a trophy for being the third-worst at something you are the best at. Hang it crooked."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All eleven of you, every week, all season. Spencer Lentz added 21.18 and took the lead at 151.36, "
        "passing Aaron Jezioro at 148.28, and Rahul Pahuja added nothing and sits third at 133.34. Aron Rogers "
        "has left 38.08 all year. The three men at the top of the standings are first, sixth and last on "
        "this list, Gil, which tells you exactly how much the bench matters until December, when it is the "
        "whole thing."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 8, season_note=(
        "Season totals come from the season ledger through Week 8. Spencer Lentz leads at 151.36, Aaron Jezioro "
        "is second at 148.28, Rahul Pahuja third at 133.34. Aron Rogers has left the fewest, 38.08. Matt "
        "Davis's 0.90 came on his bye and counts in his season total, not in any result.")))
    parts.append(gil(
        "No bench cost a game this week. Three owners left nothing: Rahul Pahuja, Michael Smith and Billy "
        "Norton, and all three lost. The two biggest benches, Spencer Lentz at 21.18 and Ryan Kelly at 11.32, "
        "both won."))
    parts.append(boomer(
        "Every perfect lineup lost and the two sloppiest ones won. I have been doing this a long time, Gil, and the "
        "only lesson in that is that the scoreboard grades the roster, not the homework."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Rahul Pahuja signing Jonah Coleman, who started and "
        "scored 18.40, for Marvin Harrison Jr., who scored zero. The biggest swing of any move in the league "
        "this week. Aaron Jezioro's Kenny Gainwell for Brian Robinson Jr., 16.00 to zero, was second, and Eric "
        "Olson's Jaguars defense for the Patriots, 19.00 to 7.00, third."))
    parts.append(gil(
        "<strong>Worst move:</strong> Bob Dorsch releasing the Buccaneers defense, who scored 16.00, for the "
        "Texans defense, who were on bye and scored zero, after claiming the Buccaneers for Jordan Addison the "
        "same week. A 16.00-point swing against him. Eric Olson releasing Bo Nix, who scored 23.28, for Antonio "
        "Williams, who scored 7.90, was second on paper, and it did not matter with Josh Allen back."))
    parts.append(boomer(
        "Bob claimed a defense and cut the same defense inside one week, and the defense scored sixteen for "
        "nobody. He cut Waddle, who scored thirteen, for a man who scored five. He claimed a "
        "running back who scored thirteen and sat him. Bob made five moves and the best of them was the one "
        "that did not count. The reigning champion, Gil. We did a whole segment."))
    parts.append(gil(
        "Twenty-four moves went through. Bob Dorsch made five: Spencer Shrader for Germie Bernard, Rachaad White "
        "for Baker Mayfield, the Buccaneers for Addison, KC Concepcion for Jaylen Waddle, and the Texans for the "
        "Buccaneers. Rahul Pahuja made four: Coleman for Harrison, the Bears defense for the Seahawks, Hunter "
        "Henry for Roschon Johnson, and Jalen Coker, released by Jezioro, for David Montgomery. Spencer Lentz "
        "made four, three of them defenses: the Bengals for the Panthers, then the Vikings for the Bengals, the "
        "Seahawks for the Texans, and Jason Myers for Dominic Zvada at kicker. Matt Davis claimed the Rams defense "
        "for the Vikings, and Spencer claimed the Vikings. Aron Rogers released Harrison Butker for T.J. "
        "Hockenson. Ryan Kelly signed the Patriots defense for the Giants, and Michael Smith signed Kimani Vidal "
        "for Ka'imi Fairbairn."))
    parts.append(boomer(
        "Spencer changed defenses three times in one week and started the one that scored six, with the one "
        "that scored two on his bench, and his kicker scored zero. Rahul picked up Jezioro's receiver and did "
        "not use him. Davis cut the Vikings, Spencer claimed the Vikings. This league passes players around like "
        "a bowl at Thanksgiving, Gil, and nobody takes any."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Spencer Lentz at Matt Davis, Aron Rogers at Bob Dorsch, Ryan Kelly at Rahul Pahuja, Michael Turner at "
        "Michael Smith, and Aaron Jezioro at Billy Norton. Eric Olson has the bye. The Steelers and Titans have "
        "the week off. Jacksonville plays at Baltimore on Thursday night, so Trevor Lawrence, Derrick Henry, "
        "Lamar Jackson, Zay Flowers, Mark Andrews, Isaiah Likely, Parker Washington and the Jaguars and Ravens "
        "defenses are done before Sunday. "
        "Cincinnati and Atlanta kick off at 9:30 on Sunday morning. Buffalo plays at Minnesota on Monday night."))
    parts.append(boomer(
        "Spencer and Davis, 14 and 14 after twenty-eight games, and one of them walks out ahead. Rogers goes to Dorsch, and Bob has read his own page, so "
        "either he wins or we find out it was fiction. Kelly and Rahul meet for the first time since Rahul took "
        "last December's consolation game 162.00 to 81.24, Rahul has won three straight in it, and Kelly is hot, which in this league lasts about as "
        "long as a two-game winning streak. Turner needs a hundred and a win and I have bet him for one of them. And Billy "
        "Norton, four rings, 1 and 6, gets Jezioro and his 138. Set your lineups, and Bob, start the running "
        "backs. All of them. I do not care which."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 8, HEADLINE, DEK, build(), META, "foh-week-8.png", nav=NAV,
        published="2026-11-03T07:30:00-05:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "week-8.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
