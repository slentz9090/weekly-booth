"""Dewart Lake FFL, Week 4. Editorial.

Outlier engine top items this week: Geoff Cavender 4-0 on an 18-26 all-play record (headline tier,
season luck), Scott Howard lost by 2.54 with 29.62 on the bench (promote). Supporting: Scott Reisert's
137.68 is the 44th-most in a loss since 2009, Spencer Lentz's 165.18 is the season high.
"""
import os

import booth
from booth import award, boomer, calls_list, gil, graded_list, jump, ledger, mcard
from compute import ledger_rows, load, by_owner

FACTS = load("dlffl_wk4_facts.json")
SEASON = load("dlffl_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 194.66

HEADLINE = "Geoff Cavender Is 4 And 0 And Nobody He Has Played Has Scored 93"
DEK = (
    "His four opponents put up 80.26, 58.86, 76.18 and 92.92. In the weeks he drew them they went a combined "
    "3 and 41 against the league. Elsewhere Spencer Lentz hung 165.18 on a previously unbeaten "
    "Scott Reisert, Scott Howard lost by 2.54 with two winning answers on his bench, and Boomer had his first "
    "winning week."
)
META = (
    "Gil and Boomer call Week 4 of the Dewart Lake FFL: Geoff Cavender is 4 and 0 without facing a 93, Spencer "
    "Lentz scored 165.18, Scott Howard lost by 2.54, and Boomer went 7 and 5 on his calls."
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

    # ---- 1. the schedule
    w, l = card_rows("Geoff Cavender", "Doug Fields")
    parts.append(mcard(
        "m-cavender", "Cavender is the last unbeaten team", w, l,
        "Bryce Young 24.46, Carnell Tate 20.00 and Quinshon Judkins 18.60 for Geoff Cavender, with 1.60 left behind. "
        "Doug Fields got 27.72 from Joe Burrow and had Kirk Cousins at 25.60 on his bench.", SCALE, key=True))
    parts.append(gil(
        "Geoff Cavender wins 117.26 to 92.92 and is 4 and 0, the only unbeaten team left. He is seventh in the "
        "league in points. His four opponents have scored 80.26, 58.86, 76.18 and 92.92 against him, 308.22 in "
        "all, the fewest any team here has faced."))
    parts.append(boomer(
        "Last week I said Geoff's schedule was 3 and 0, not Geoff. I went and checked the schedule's work. In the "
        "weeks he played them, his four opponents went 3 and 41 against the league. Three and forty-one. He "
        "is not on a winning streak, Gil, he is on a guided tour."))
    parts.append(gil(
        "Put his four scores against the whole league every week and his record is 18 and 26. Give him a random "
        "opponent each of those four weeks and he goes 4 and 0 about once in 58 tries."))
    parts.append(boomer(
        "Once in 58, Gil. Geoff did not beat the odds. The odds never showed up."))
    parts.append(gil(
        "This week, though, he earned it. He started 117.26 of the 118.86 he had, and he kept Bryce Young in over "
        "Matthew Stafford and Jordan Love for the third week running. For the first time it was the right call. "
        "Young outscored both of them by more than 11."))
    parts.append(boomer(
        "I told him to start Stafford. He ignored me and was right, and I respect a man who knows which advice to "
        "throw out. Doug Fields, meanwhile, put Joe Burrow back in the lineup, got 27.72 for it, and lost by 24.34 "
        "because his two starting receivers combined for 8.00. Doug fixed the quarterback and the roof fell in "
        "somewhere else."))

    # ---- 2. the big number
    w, l = card_rows("Spencer Lentz", "Scott Reisert")
    parts.append(mcard(
        "m-lentz", "Spencer's 165.18 is the high score of the season", w, l,
        "Bijan Robinson 31.20, Nico Collins 30.30, Chuba Hubbard 28.40 and C.J. Stroud 26.08. Scott Reisert "
        "scored 137.68, left 4.30 behind, and took his first loss.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 165.18 to 137.68. It is the highest score anyone in this league has posted this "
        "season by more than four points. Scott Reisert came in 3 and 0 and still leads their series "
        "5 and 4."))
    parts.append(boomer(
        "A hundred and sixty-five, and he did it with Parker Washington in the lineup for 1.50 while Tee Higgins "
        "scored 24.20 on the bench. He left 29.48 back there, Gil. That is bigger than any margin of victory in this league this week, his own included."))
    parts.append(gil(
        "To be fair to Scott Reisert, 137.68 beats ten of the other eleven teams this week, and it is the sixth-best single week of his 60 in this league. "
        "Javonte Williams gave him 28.80 and Jared Goff 24.48."))
    parts.append(boomer(
        "I picked him to go 4 and 0 and he played well enough to do it against ten teams. He drew the eleventh. "
        "Scott, go ask Geoff Cavender how he keeps avoiding that guy.", "good"))

    # ---- 3. the close one
    w, l = card_rows("dennis couture", "Scott Howard")
    parts.append(mcard(
        "m-da", "DA holds off Howard by 2.54", w, l,
        "Kyren Williams 31.70 for DA, with Kyle Monangai's 30.50 on his bench. Scott Howard got 26.20 from Puka "
        "Nacua and left Brian Robinson Jr.'s 25.20 on his.", SCALE))
    parts.append(gil(
        "DA wins 119.62 to 117.08, the closest game of the week, and is 3 and 1. It ends a four-game Howard run in "
        "this series, which Howard still leads 6 and 4. Scott Howard is 0 and 4, and 117.08 is his best score of "
        "the season by more than 32 points."))
    parts.append(boomer(
        "Scott Howard lost by 2.54 and I counted the exits. Brian Robinson Jr., 25.20 on the bench, behind Bucky "
        "Irving at 6.10. That wins it. Sam LaPorta, 18.40 on the bench, behind Isaiah Likely at 10.10. That wins "
        "it too. And Dak Prescott outscored Lamar Jackson by 2.22, which still loses, by 0.32. Two doors and a window that would not quite open, Scott. You walked into the wall.", "bad"))
    parts.append(gil(
        "Give Scott Howard this much: 117.08 would have beaten five of the other eleven teams this week, and he had 146.70 available, within two points of what DA had. And had it "
        "finished level, this league breaks the tie on bench points. His bench outscored DA's 68.90 to 65.90."))
    parts.append(boomer(
        "DA is not walking out of here clean either. Monangai scored 30.50 sitting down, Mark Andrews scored "
        "11.20 sitting down, and Dalton Kincaid started at tight end for 1.20. Last week I told "
        "you this man does not make mistakes. He saved them all up for one Sunday and still won. That is "
        "what a long marriage teaches you. Be wrong quietly and let the other side be wrong louder."))

    # ---- 4. first win
    w, l = card_rows("Adam Hershberger", "Casey Couture")
    parts.append(mcard(
        "m-hershberger", "Hershberger gets his first win of the season", w, l,
        "Malik Nabers 23.20 and Jameson Williams 16.20 for Adam Hershberger. Casey Couture had T.J. Hockenson at "
        "21.40 and Ollie Gordon II at 20.00 on his bench and lost by 9.36.", SCALE))
    parts.append(gil(
        "Adam Hershberger wins 97.18 to 87.82 and is 1 and 3. He has now beaten Casey Couture twice running, "
        "though Casey still leads the series 7 and 5. Hershberger left 8.50 behind."))
    parts.append(boomer(
        "I called this one and I would like it noted. Adam has had 511.02 points dropped on his head in four weeks. This week the league finally sent him somebody his own size. Ninety-seven was plenty, and Malik Nabers had 23.20 of it.", "good"))
    parts.append(gil(
        "Casey Couture scored the lowest total in the league for the second straight week. He added Ollie Gordon "
        "II off the wire this week, and Gordon scored 20.00 on the bench while D'Andre Swift started for 6.40. "
        "Hockenson for Kyle Pitts Sr. at tight end is worth another 15.20. Either swap wins the game. In fairness to Casey, he is still 2 and 2, and Jonathan Taylor gave him 22.20 and Chris Olave 18.60."))
    parts.append(boomer(
        "Last week he signed a quarterback and left him in the garage. This week he signed a running back and "
        "left him in the garage. Casey, I am starting to think you just like having a full garage. I asked him to start Sam Darnold and he did, for 13.32. He had released his only other quarterback, so I am not taking a bow."))

    # ---- 5. four straight
    w, l = card_rows("Kent Frenger", "Beth Couture")
    parts.append(mcard(
        "m-frenger", "Frenger makes it four straight over Mama Beth", w, l,
        "Kenneth Walker III 33.40 and 16.00 from his kicker for Kent Frenger, who won with Ja'Marr Chase at 4.20. "
        "Zay Flowers led Mama Beth at 24.80.", SCALE))
    parts.append(gil(
        "Kent Frenger wins 107.44 to 89.30 and is 2 and 2. He leads the lifetime series with Mama Beth 14 and 8 "
        "and has won the last four. Alvin Kamara, added off the wire this week, scored 20.30 on his bench."))
    parts.append(boomer(
        "Ja'Marr Chase 4.20, DJ Moore 2.20, Trey McBride 6.60. Three stars, 13 points, and Kent still won by 18. Kenneth Walker had 33.40 by himself and the kicker had 16.00. Kent's two best starters this week were a running back and a foot."))
    parts.append(gil(
        "For the record, Mama Beth left 1.10 on her bench, the least in the league. She had 90.40 available "
        "and started 89.30 of it. Justin Jefferson sat on her bench with a projection of zero, and Saquon "
        "Barkley started for 1.50 against a projection of 14.22."))
    parts.append(boomer(
        "Last week I asked her to turn the dial. She went from 77.92 to 89.30. She turned it, Gil. Eleven points. Saquon Barkley gave her 1.50. Mama Beth did her part. I would like a word with Saquon."))

    # ---- 6. first meeting
    w, l = card_rows("Adam Calvelage", "Ryan Reed")
    parts.append(mcard(
        "m-calvelage", "Calvelage takes the first meeting ever", w, l,
        "Tetairoa McMillan 41.20 and CeeDee Lamb 35.80 for Adam Calvelage. Ryan Reed scored 122.46, got 25.50 "
        "from Emanuel Wilson and 19.00 from his kicker, and lost by 7.46.", SCALE))
    parts.append(gil(
        "Adam Calvelage wins 129.92 to 122.46 and is 3 and 1 after opening the season with 75.46. Two receivers gave him 77.00 of it. His other seven starters combined for "
        "52.92."))
    parts.append(boomer(
        "Tetairoa McMillan, 41.20. CeeDee Lamb, 35.80. Travis Kelce "
        "gave him 2.50, his defense gave him zero, a running back gave him 1.30, and none of it mattered. Adam "
        "did not field a team. He fielded two guys and a carpool.", "good"))
    parts.append(gil(
        "Ryan Reed would have beaten eight of the other eleven teams in each of the last three weeks, and he is 2 and 2 in the standings. Justin Herbert started for 9.56 with Bo Nix at 13.56 behind him, and Jaxon Smith-Njigba, "
        "after 42.00 and 33.36, scored 10.10."))
    parts.append(boomer(
        "Last week I called Smith-Njigba the sunrise. This week it was overcast. Ryan lost a game where his "
        "kicker scored 19, and when the kicker is your second-best player you were not robbed, you were warned."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls. Seven came in, five did not. That is my first winning week, and nobody is more surprised "
        "than the man saying it. Season record, 17 and 19. All twelve are below, the good and the ugly."))
    parts.append(graded_list([
        ("Holy Rollers", "Adam Hershberger beats Casey Couture for his first win.", "RIGHT",
         "By 9.36."),
        ("One Under akaThe Mulligan", "Casey Couture starts Sam Darnold in Week 4.", "RIGHT",
         "He did, for 13.32."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert goes 4 and 0.", "WRONG",
         "Lost by 27.50 while scoring 137.68. Right team, wrong Sunday."),
        ("Balls Deep", "Bijan Robinson clears 20 again for Spencer Lentz.", "RIGHT",
         "31.20."),
        ("Cosby Copperheads", "Doug Fields beats Geoff Cavender.", "WRONG",
         "Lost by 24.34. I said one of these men was due. It was the other one, again."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender clears 100 in Week 4.", "RIGHT",
         "117.26, with the quarterback I told him to sit."),
        ("Momma's Boys", "Mama Beth beats Kent Frenger.", "WRONG",
         "Lost by 18.14 with 1.10 on her bench. That one is on the players."),
        ("Berlin Blitz", "Tyler Shough clears 15 again for Kent Frenger.", "RIGHT",
         "15.94. I will take the 0.94 and I will not be giving it back."),
        ("DA The Badenov's", "DA beats Scott Howard.", "RIGHT",
         "By 2.54, with 30.50 of Kyle Monangai on his bench."),
        ("The Scranton Strangler", "Scott Howard leaves under twenty on his bench in Week 4.", "WRONG",
         "29.62, in a game he lost by 2.54."),
        ("BearDown", "Ryan Reed wins his first ever meeting with Adam Calvelage.", "WRONG",
         "Lost by 7.46 on 122.46."),
        ("An alBum Cover", "Brock Purdy clears 20 again for Adam Calvelage.", "RIGHT",
         "20.62. Sixty-two hundredths to spare."),
    ]))
    parts.append(gil("Seven right, five wrong. Twelve new ones for Week 5, one per team."))
    parts.append(calls_list([
        ("DA The Badenov's", "DA hands Geoff Cavender his first loss.",
         "Cavender is 3 and 0 lifetime against DA, so history says no. But DA has 518.46 points, second in the "
         "league, and he would be the first opponent Cavender has seen all year who can score."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender starts Matthew Stafford in Week 5.",
         "Bryce Young has the week off, so Geoff finally has to start one of the two quarterbacks he has been sitting since Week 2. Stafford scored 23.90 on his bench in Week 3. Jordan Love, you are my second choice."),
        ("Balls Deep", "Spencer Lentz leaves under twenty on his bench in Week 5.",
         "29.48 this week, nothing at all the week before. He knows how. He draws Adam Hershberger, and he leads "
         "that series 6 and 3."),
        ("Holy Rollers", "Malik Nabers clears 15 again for Adam Hershberger.",
         "9.90, 0.60, 5.10, and then 23.20 in Adam's first win. Either that was the breakout or it was a typo. I am calling breakout."),
        ("One Under akaThe Mulligan", "Casey Couture beats Doug Fields.",
         "He leads the series 7 and 5 and won the last one, in 2025. He has had the answer on his bench two weeks "
         "in a row. I am calling the week he starts it."),
        ("Cosby Copperheads", "Doug Fields clears 100 in Week 5.",
         "96.96, 99.58, 105.48 and 92.92. He lives in this neighborhood. Burrow gave him 27.72, and all he needs is two receivers who can beat 8.00 between them."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert beats Mama Beth by twenty or more.",
         "545.46 points, the most in the league, and 19.40 left on his bench all season, the fewest. Mama Beth "
         "leads their series 3 and 2, and I am calling it anyway."),
        ("Momma's Boys", "Mama Beth clears 90 in Week 5.",
         "77.96, 77.92, 89.30. The dial is moving. She left 1.10 behind this week, so the lineup is not the "
         "problem. She can lose by twenty and still make me right on this one."),
        ("BearDown", "Ryan Reed beats Kent Frenger.",
         "Three and three lifetime, and they have not met since 2021. Reed has been top four in the league three "
         "straight weeks. Sooner or later the standings have to notice."),
        ("Berlin Blitz", "Kent Frenger clears 110 in Week 5.",
         "Three of his stars gave him 13 points and he still scored 107.44. If Ja'Marr Chase so much as wakes up, 110 takes care of itself."),
        ("The Scranton Strangler", "Scott Howard wins his first game of the season.",
         "117.08 on Sunday with 146.70 available. He was one right answer from beating DA. Calvelage leads their "
         "series 3 and 2. I am picking the man who is 0 and 4, on purpose."),
        ("An alBum Cover", "CeeDee Lamb clears 20 again for Adam Calvelage.",
         "35.80 on Sunday. Last week he missed 20 by three tenths and we stopped speaking. We are speaking "
         "again."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(award(
        "good", "Owner of the Week", "Spencer Lentz · Balls Deep",
        "165.18, the highest score in the league this season, against a team that came in 3 and 0. He would have "
        "beaten all eleven teams this week.",
        "He gets the trophy and I get to say this while I hand it over. Hold the trophy with both hands, Spencer. The last three good things you held were Tee Higgins, Romeo Doubs and Drake Maye, and you set all three on the bench."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Casey Couture · One Under akaThe Mulligan",
        "87.82, the lowest score in the league for the second straight week, with 118.32 available. He would have "
        "lost to all eleven teams, also for the second straight week.",
        "Oh and eleven, twice. Casey is 2 and 2, which sounds fine until you learn he has gone 0 and 22 against "
        "the league in the last two weeks. Your brother won the award above this one, Casey, and your mother left 1.10 on her bench. Somebody in that house knows how to set a lineup. Ask around."))
    parts.append(award(
        "good", "Start of the Week", "Adam Calvelage · Tetairoa McMillan, 41.20",
        "Projected for 14.31, so 26.89 over, the biggest overperformance by any starter in the league. It is the 65th-highest score by any starter in this league since 2018, out of more than 12,000. Second place this week is also his: "
        "CeeDee Lamb, 21.29 over.",
        "First and second in the same lineup. Adam threw two darts with his eyes shut and hit the bullseye "
        "twice. Do not try to explain it, Adam. Just put the darts down and leave."))
    parts.append(award(
        "bad", "Sit of the Week", "Scott Howard · Brian Robinson Jr., 25.20 on the bench",
        "Bucky Irving started in his place for 6.10, a swing of 19.10 in a game Howard lost by 2.54. Spencer "
        "Lentz's Tee Higgins benching was bigger at 22.70, and he is about to hear about it one award down.",
        "Twenty-five points on the bench in a two-and-a-half point loss. Scott, you have left 141.88 points on "
        "your bench in four weeks. Your best score all year is 117.08. The bench is outscoring your best Sunday."))
    parts.append(award(
        "bad", "Waste of the Week", "Spencer Lentz · 29.48 left behind, and he won anyway",
        "The most points left on a bench by any winner, 0.68 ahead of DA. Tee Higgins scored 24.20 on it and "
        "Romeo Doubs 20.80 while Parker Washington started for 1.50.",
        "Owner of the Week and Waste of the Week, same man, same Sunday. Three weeks of hardware before this one and nobody had taken the top one and a bad one on the same Sunday. Spencer, that is not a double. That is a man who "
        "aced the test and then set fire to the scantron on his way out."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All twelve of you, every week, all season. Scott Howard leads it at 141.88 and second place is Casey Couture at 92.28. The gap between them, 49.60, is more than two and a half times what Scott Reisert has left all season."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 4, season_note=(
        "Season totals come from the season ledger through Week 4. Scott Howard leads at 141.88, Casey Couture "
        "is second at 92.28, Ryan Reed third at 68.84. Scott Reisert has left the fewest, 19.40.")))
    parts.append(gil(
        "Two benches decided a game this week, and they belong to the same two owners as last week. Scott Howard left 29.62 and lost by 2.54. "
        "Casey Couture left 30.50 and lost by 9.36."))
    parts.append(boomer(
        "Same two benches, two weeks running. Fellas, the bench is supposed to be where the bad players go."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Spencer Lentz adding C.J. Stroud, who scored 26.08, for "
        "Fernando Mendoza, who did not score. Stroud started. He was available because Doug Fields released him "
        "this week to add Kirk Cousins."))
    parts.append(gil(
        "<strong>Worst move:</strong> Kent Frenger dropping Keon Coleman, who scored 23.60, to add Adonai "
        "Mitchell, who scored nothing. A 23.60-point swing, the biggest against any owner this week."))
    parts.append(boomer(
        "Follow the quarterback, Gil. Last week Doug Fields cut Bo Nix to sign C.J. Stroud. This week he cut "
        "Stroud to sign Kirk Cousins. Cousins scored 25.60 on Doug's bench. Stroud scored 26.08 in Spencer's "
        "lineup, in the highest score of the year. Doug also let Tucker Kraft go, and Kraft is on "
        "Spencer's roster now too. Doug Fields is not running a team. He is running Spencer's farm system. And Spencer, before you take a bow, Drake Maye was already on your roster and outscored Stroud from your bench, 26.16 to 26.08. Your best move of the week was worth slightly less than doing nothing."))
    parts.append(gil(
        "Twenty moves went through. Scott Reisert made five of them, and in the course of the week he both added "
        "and released RJ Harvey. Adam Calvelage signed Harvey afterward and started him for 14.30."))
    parts.append(boomer(
        "Scott Reisert picked up a running back, looked at him, and put him back on the shelf. Adam Calvelage "
        "took him off the shelf and got 14.30 out of him. For a man who has left 19.40 on his bench all season, that counts as a blunder, and it took two transactions to make it. Kent Frenger needed one. He cut a man who scored 23.60 for a man who scored nothing, and won anyway."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Adam Hershberger at Spencer Lentz, Doug Fields at Casey Couture, Mama Beth at Scott Reisert, DA at "
        "Geoff Cavender, Ryan Reed at Kent Frenger, and Adam Calvelage at Scott Howard."))
    parts.append(boomer(
        "DA at Cavender is the one. Geoff has gone four weeks without meeting a team that scored 93, and here "
        "comes a man averaging just under 130. Either the tour bus keeps rolling or somebody finally checks the "
        "tickets. I picked against Geoff last week and lost. I am doing it again, and this time I brought a man who can score."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 4, HEADLINE, DEK, build(), META, "dlffl-week-4.png",
        published="2026-10-06T11:00:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "dlffl", "week-4.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
