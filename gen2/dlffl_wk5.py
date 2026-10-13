"""Dewart Lake FFL, Week 5. Editorial.

Boomer runs at SCORCHING from Week 5 on (Spencer, 2026-10-13): every Boomer line carries a joke, Gil plays
straight man, nobody is safe including Spencer, clean language, roast cap and Gil defenses still apply.

Outlier engine top items: Scott Howard's 173.32 is the best of his 101 games here (headline), Spencer
Lentz's 192.66 is the 9th-highest of 2,839 team-weeks since 2009 (headline), the 84.12 margin (promote),
Tyler Shough -0.16 on a 17.37 projection (promote). Supporting: DA and Cavender both perfect lineups,
Mama Beth 66.70 is 5th-worst of her 219, Casey's best possible lineup lost by 0.20.
"""
import os

import booth
from booth import award, boomer, calls_list, gil, graded_list, jump, ledger, mcard
from compute import ledger_rows, load, by_owner

FACTS = load("dlffl_wk5_facts.json")
SEASON = load("dlffl_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 199.66

HEADLINE = "Scott Howard Played The Best Game Of His Life. It Was The Second-Best Score Of The Week."
DEK = (
    "Howard's 173.32 beat his own record from 2020 by four tenths of a point and got him his first win of the "
    "season. Spencer Lentz scored 192.66, the ninth-highest score in this league since 2009. DA ended Geoff "
    "Cavender's unbeaten run with a perfect lineup, and on the same Sunday his wife, Mama Beth, scored 66.70."
)
META = (
    "Gil and Boomer call Week 5 of the Dewart Lake FFL: Scott Howard's career night, Spencer Lentz's 192.66, "
    "DA ends Geoff Cavender's unbeaten start, and Boomer goes 6 and 6 on his calls."
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

    # ---- 1. the career night
    w, l = card_rows("Scott Howard", "Adam Calvelage")
    parts.append(mcard(
        "m-howard", "Howard's best game ever, and his first win", w, l,
        "Bucky Irving 33.50, Puka Nacua 32.20 and Braelon Allen 21.10 for Scott Howard. Jayden Daniels gave "
        "Adam Calvelage 35.26 and CeeDee Lamb gave him 1.90.", SCALE, key=True))
    parts.append(gil(
        "Scott Howard wins 173.32 to 101.86 and is 1 and 4. It is the best score of his 101 games in this league, "
        "four tenths of a point past the 172.92 he put up in 2020. The series with Adam Calvelage is now 3 and 3."))
    parts.append(boomer(
        "Eighty, seventy-one, eighty-four, one-seventeen, and then one hundred seventy-three. Gil, that is not a "
        "turnaround. That is a hostage video where the hostage suddenly starts juggling. Scott, blink twice if "
        "somebody else set this lineup."))
    parts.append(gil(
        "In fairness to Adam Calvelage, Jayden Daniels gave him 35.26, one of the 45 biggest games by any starter "
        "in a loss in this league since 2018. CeeDee Lamb was projected for 16.46."))
    parts.append(boomer(
        "And CeeDee gave him 1.90. I co-signed for CeeDee Lamb in this booth last week. Projected 16.46, "
        "delivered 1.90. Gil, I am now personally on the hook for the other 14.56.", "bad"))

    # ---- 2. the big number
    w, l = card_rows("Spencer Lentz", "Adam Hershberger")
    parts.append(mcard(
        "m-lentz", "Spencer's 192.66, ninth-best on record", w, l,
        "Drake Maye 42.46, Jaylen Warren 38.80 and Parker Washington 31.40 for Spencer Lentz, who left 7.00 "
        "behind. Malik Nabers gave Adam Hershberger 26.60.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 192.66 to 108.54. It is the ninth-highest score in 2,839 team-weeks in this league "
        "since 2009 and the fourth-best of his own career. The 84.12 margin is the 32nd-biggest in 1,420 games. "
        "He has beaten Adam Hershberger three straight times and leads the series 7 and 3."))
    parts.append(boomer(
        "Adam named his team the Holy Rollers, and on Sunday he got baptized. Full dunk. Spencer held him under "
        "for 84 points and only let him up because the pastor started asking questions. And Spencer, before "
        "you take a lap: your kicker scored 23.00 and Bijan Robinson scored 13.80. Your kicker outscored Bijan by "
        "nine. Put that in the acceptance speech."))
    parts.append(gil(
        "For Adam Hershberger, 108.54 is his best score of the season. He has had 703.68 points scored against "
        "him in five weeks, the most in the league, an average of 140.74 a game."))
    parts.append(boomer(
        "Adam finally brings a casserole to the potluck and somebody parks a catering truck on the lawn. He "
        "started Omarion Hampton for 4.40 and Chase Brown for 5.50 with Jameson Williams, Blake Corum and "
        "Jacory Croskey-Merritt on the bench for 46.60 between them. Even his perfect lineup loses by 58.82. "
        "Adam did not lose this game, Gil. He attended it."))

    # ---- 3. the unbeaten falls
    w, l = card_rows("dennis couture", "Geoff Cavender")
    parts.append(mcard(
        "m-da", "DA ends Cavender's unbeaten start", w, l,
        "Josh Allen 33.50 and Christian Watson 33.30 for DA, with nothing left on his bench. Geoff Cavender also "
        "left nothing behind, got 30.32 from Matthew Stafford, and took his first loss.", SCALE))
    parts.append(gil(
        "DA wins 151.10 to 131.12 and is 4 and 1. It is his first win over Geoff Cavender in four tries. Both men set perfect lineups. Since 2018 that happens in "
        "about 12% of team-weeks here. Two in the same game, and one of them had to lose."))
    parts.append(boomer(
        "For four weeks nobody Geoff played could find 93. Last week I said somebody had to check the tickets. "
        "DA checked the tickets, checked the ID, scored 151 and had the bouncer take Geoff's lanyard. Every slot "
        "right. The man set his lineup like he was defusing a bomb.", "good"))
    parts.append(gil(
        "Give Geoff Cavender his due. 131.12 is the fourth-best of his 33 games here, and it beats eight of the "
        "other eleven teams this week. He started Matthew Stafford, as called, for 30.32, with Jordan Love at "
        "29.28 on the bench."))
    parts.append(boomer(
        "Geoff did everything right and lost by 20. Welcome to the Dewart Lake FFL, Geoff. The rest of us have "
        "been living in that apartment for years. The hot water never works and the landlord is DA."))

    # ---- 4. the negative quarterback
    w, l = card_rows("Kent Frenger", "Ryan Reed")
    parts.append(mcard(
        "m-frenger", "Frenger wins with a quarterback below zero", w, l,
        "Trey McBride 17.10, Ka'imi Fairbairn 17.00 and Ja'Marr Chase 16.70 for Kent Frenger, whose quarterback "
        "scored minus 0.16. Ryan Reed got 24.78 from Jacoby Brissett and left the Texans defense's 15.00 on his "
        "bench.", SCALE))
    parts.append(gil(
        "Kent Frenger wins 97.34 to 91.88 and is 3 and 2. He leads the series with Ryan Reed 4 and 3. His "
        "quarterback, Tyler Shough, was projected for 17.37 and scored minus 0.16."))
    parts.append(boomer(
        "Last week I bet Tyler Shough would clear 15 and he gave me 15.94. This week he went out there and made "
        "the scoreboard go backwards. Gil, Kent won a football game with a quarterback in reverse. He is a "
        "getaway driver who backed out of the bank and still beat the cops."))
    parts.append(gil(
        "Ryan Reed lost by 5.46 with the answer on his bench. He started the Steelers defense for 1.00 and sat "
        "the Texans defense, who scored 15.00. It is the only bench in the league this week that cost its owner "
        "the game. Doug Fields released the Texans defense this week, and Reed claimed them."))
    parts.append(boomer(
        "Ryan rescued that defense off the curb, brought it home, and left it in the car. Fifteen points in the "
        "car with the windows up, Ryan. Lost by five. Somebody call somebody.", "bad"))

    # ---- 5. the two tenths
    w, l = card_rows("Doug Fields", "Casey Couture")
    parts.append(mcard(
        "m-fields", "Fields by 18.10, and Casey could not have caught him", w, l,
        "James Cook III 25.30, Joe Burrow 24.60 and Derrick Henry 23.50 for Doug Fields, who won with a defense "
        "at minus 6.00. Casey Couture's best possible lineup was 91.80.", SCALE))
    parts.append(gil(
        "Doug Fields wins 92.00 to 73.90 and is 2 and 3. Casey Couture still leads their series 7 and 6. "
        "Casey's best possible lineup this week was 91.80. Fields scored 92.00."))
    parts.append(boomer(
        "Casey, if you had set every slot perfectly, you lose by two tenths of a point. Two tenths. A time "
        "machine does not save you. You go back, fix everything, and come home to the same loss with better "
        "posture."))
    parts.append(gil(
        "Emeka Egbuka scored 14.20 on Casey's bench while KC Concepcion, added this week, started for 1.00. To "
        "make room for Concepcion he released Kyle Pitts Sr., who scored 12.70. To be fair to Casey Couture, he "
        "has five titles, the most in this league, and D'Andre Swift gave him 15.30. And for Doug Fields, James "
        "Cook III, Joe Burrow and Derrick Henry gave him 73.40 between them. A win is a win."))
    parts.append(boomer(
        "Doug, meanwhile, started a defense that scored minus 6 and a receiver he signed this week, Roman Wilson, "
        "who scored zero. Two holes in the boat and he still beat Casey to shore, bailing with his "
        "hat the whole way."))

    # ---- 6. the wide one
    w, l = card_rows("Scott Reisert", "Beth Couture")
    parts.append(mcard(
        "m-reisert", "Reisert by 58.54, and the top seed", w, l,
        "Jahmyr Gibbs 38.20 and Jared Goff 28.94 for Scott Reisert, who left 6.10 behind. Justin Jefferson led "
        "Mama Beth at 15.80, and David Montgomery gave her 1.10.", SCALE))
    parts.append(gil(
        "Scott Reisert wins 125.24 to 66.70 and is 4 and 1, holding the top seed. The series with Mama Beth is "
        "now 3 and 3. He has left 25.50 on his bench all season, the fewest in the league."))
    parts.append(boomer(
        "I called Reisert by twenty. He won by twenty, came back and won by twenty again, and then stuck around "
        "and helped with the dishes. Scott Reisert does not manage a fantasy team, Gil. He audits one.", "good"))
    parts.append(gil(
        "Mama Beth made five moves this week. In fairness to her, David Montgomery was projected for 11.41 and "
        "gave her 1.10, and three of her bench players were projected for zero."))
    parts.append(boomer(
        "Five moves, and two of them were Michael Mayer. She went to the wire five times and came home with the "
        "same tight end twice. Mayer started and scored 0.70 with Dallas Goedert's 6.80 on the bench. Mama Beth, "
        "when a tight end keeps coming back like that, he is not a free agent. He is a stray cat, and you fed him."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls came due. Six right, six wrong, the most average week a man can have. Season record, 23 and "
        "25. Two more and I am a .500 man, and in this booth that gets a parade. Every one is below."))
    parts.append(graded_list([
        ("DA The Badenov's", "DA hands Geoff Cavender his first loss.", "RIGHT",
         "By 19.98, with a perfect lineup."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender starts Matthew Stafford in Week 5.", "RIGHT",
         "30.32. Jordan Love scored 29.28 on the bench. Right by 1.04 and I will take every hundredth."),
        ("Balls Deep", "Spencer Lentz leaves under twenty on his bench in Week 5.", "RIGHT",
         "7.00."),
        ("Holy Rollers", "Malik Nabers clears 15 again for Adam Hershberger.", "RIGHT",
         "26.60. Breakout confirmed. Adam still lost by 84."),
        ("One Under akaThe Mulligan", "Casey Couture beats Doug Fields.", "WRONG",
         "Lost by 18.10. His perfect lineup loses by 0.20, so I am blaming the schedule."),
        ("Cosby Copperheads", "Doug Fields clears 100 in Week 5.", "WRONG",
         "92.00. He won, so he does not care what I think."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert beats Mama Beth by twenty or more.", "RIGHT",
         "By 58.54."),
        ("Momma's Boys", "Mama Beth clears 90 in Week 5.", "WRONG",
         "66.70. The dial went the other way."),
        ("BearDown", "Ryan Reed beats Kent Frenger.", "WRONG",
         "Lost by 5.46 with 15.00 on his bench. That one was sitting right there."),
        ("Berlin Blitz", "Kent Frenger clears 110 in Week 5.", "WRONG",
         "97.34. His quarterback scored minus 0.16. I do not know what I expected."),
        ("The Scranton Strangler", "Scott Howard wins his first game of the season.", "RIGHT",
         "173.32, the best game of his life. I picked a man who was 0 and 4. You are welcome, Scott."),
        ("An alBum Cover", "CeeDee Lamb clears 20 again for Adam Calvelage.", "WRONG",
         "1.90."),
    ]))
    parts.append(gil(
        "Six right, six wrong. Twelve new ones for Week 6, one per team. The Bengals, Lions, Dolphins and "
        "Vikings have the week off."))
    parts.append(calls_list([
        ("DA The Badenov's", "DA beats Casey Couture.",
         "Casey leads their lifetime series 17 and 2. DA has beaten his own son twice in nineteen tries. But DA is "
         "4 and 1 with a perfect lineup in his pocket, and Casey has been under 90 three weeks running. If it is "
         "ever going to be Dad's Sunday, it is this one."),
        ("One Under akaThe Mulligan", "Casey Couture leaves under ten on his bench in Week 6.",
         "110.18 left behind this season, second-most in the league. Casey, I am betting on your father and on "
         "your lineup in the same week. Make one of us right."),
        ("Balls Deep", "Spencer Lentz clears 150 for the third straight week.",
         "165.18, then 192.66. Somebody in this league has to be the favorite, and I am betting he does not "
         "forget how between now and Sunday. Mother is waiting for him."),
        ("Momma's Boys", "Mama Beth beats Spencer Lentz.",
         "Spencer leads the series 15 and 10, but she has won their last four regular-season meetings. She is 1 "
         "and 4 and just scored 66.70. I am betting on Mother. Every son in this league should."),
        ("Holy Rollers", "Adam Hershberger beats Doug Fields.",
         "Fields leads 6 and 5, and Adam won the last one, in 2025. Doug won with 92.00 this week. Adam scored "
         "108.54 and lost by 84. Same scores this week and Adam finally gets the casserole to the table."),
        ("Cosby Copperheads", "Doug Fields clears 100 in Week 6.",
         "96.96, 99.58, 105.48, 92.92, 92.00. Under 100 since Week 3, and Joe Burrow has the week off. At this "
         "point it is not a call, Doug. It is a hobby."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert leaves under ten on his bench in Week 6.",
         "25.50 all season, the fewest in the league. Jahmyr Gibbs, Jared Goff and his kicker play for teams "
         "with the week off, so the bench has to come off the bench. If anybody gets that right, it is the "
         "auditor."),
        ("BearDown", "Ryan Reed beats Scott Reisert.",
         "Reisert won the only meeting, in 2021, 84.68 to 74.26. Ryan lost by 5.46 this week with a defense in "
         "the car. Crack a window this time, Ryan, and take down the top seed."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender sets a perfect lineup again.",
         "He set one on Sunday and lost by 20. He is 2 and 0 against Adam Calvelage. Do it again, Geoff, and "
         "see if perfect travels."),
        ("An alBum Cover", "Adam Calvelage beats Geoff Cavender for the first time.",
         "0 and 2 lifetime. Jayden Daniels just gave him 35.26 in a loss, and CeeDee Lamb came in 14.56 under "
         "his projection. Collect, Adam."),
        ("The Scranton Strangler", "Scott Howard clears 150 again.",
         "Before Sunday he had not cleared 120 all season. Then 173.32. Sam LaPorta has the week off. Either the "
         "ceiling moved or it fell on him. I say it moved."),
        ("Berlin Blitz", "Tyler Shough gets back into double figures for Kent Frenger.",
         "Minus 0.16 on Sunday, 15.94 the week before. Nobody stays below zero forever. I would know. I am 23 and "
         "25 and I am still on the air."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. When an owner already has one, the next name in line takes "
        "it."))
    parts.append(award(
        "good", "Owner of the Week", "Spencer Lentz · Balls Deep",
        "192.66, the high score of the week and the ninth-highest in this league since 2009. He would have beaten "
        "all eleven teams, and he left 7.00 behind.",
        "Three straight weeks his score went up by about 30. Keep that pace and he scores 300 before Thanksgiving "
        "and the league opens an investigation. Enjoy it, Spencer. Next week you visit your mother, and she has won "
        "the last four."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Mama Beth · Momma's Boys",
        "66.70, the lowest score in the league and the fifth-lowest of her 219 games here. It loses to all eleven "
        "teams. On the same Sunday her husband, DA, set a perfect lineup and scored 151.10.",
        "Now, Mama Beth has three titles in this league and DA has none, so for exactly one week the man gets "
        "to talk. Let him, Mama Beth. You have three rings and he has one good Sunday. He will be unbearable "
        "until Thursday and then he will lose the remote."))
    parts.append(award(
        "good", "Start of the Week", "DA · Christian Watson, 33.30",
        "Projected for 12.15, so 21.15 over. Spencer Lentz had the two biggest beats in the league, and he "
        "already has a trophy.",
        "Christian Watson was projected for a nice quiet afternoon and instead he showed up like the brother-in-law "
        "at a cookout and ate everything on the grill. DA started him in a perfect lineup, nine for nine. The man "
        "has been in this league since 2009 and he picked this week to stop guessing."))
    parts.append(award(
        "bad", "Sit of the Week", "Ryan Reed · Texans D/ST, 15.00 on the bench",
        "The Steelers defense started in their place for 1.00, a swing of 14.00 in a game Reed lost by 5.46. A "
        "benching that cost a game goes ahead of one that did not, and this was the only one.",
        "Fourteen points of defense sitting on the bench in a five-point loss. Ryan, they were dressed. They had "
        "the helmets on. They were standing right next to you making eye contact."))
    parts.append(award(
        "bad", "Waste of the Week", "Scott Howard · 21.62 left behind, and he won",
        "The most left on a bench by any winner. Isaiah Likely scored 26.90 there while Michael Wilson started at "
        "flex for 5.28. With Likely in, Howard scores 194.94, the high score of the week by "
        "2.28.",
        "Scott played the best game of his life and his bench played a better one. He threw a career night and "
        "forgot to invite his tight end. Twenty-one points, Scott. You were one click from the top of the board."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All twelve of you, every week, all season. Scott Howard leads it at 163.50. Scott Reisert has left 25.50 "
        "all year. Howard left more than a whole Reisert season on his bench in four of five weeks. This week, "
        "in the best game of his life, he only left most of one. Growth, Gil."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 5, season_note=(
        "Season totals come from the season ledger through Week 5. Scott Howard leads at 163.50, Casey Couture "
        "is second at 110.18, Ryan Reed third at 85.34. Scott Reisert has left the fewest, 25.50.")))
    parts.append(gil(
        "One bench decided a game this week: Ryan Reed left 16.50 and lost by 5.46. DA and Geoff Cavender left "
        "nothing at all, in the same game."))
    parts.append(boomer(
        "Two spotless benches in the same game, and one of them still lost. That is the whole sport, Gil. You "
        "can do everything right, and so can the other guy."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Ryan Reed adding Jacoby Brissett, who started and scored "
        "24.78, for Justin Herbert, who scored 10.24."))
    parts.append(gil(
        "<strong>Worst move:</strong> Doug Fields dropping the Texans defense, who scored 15.00, to add the Raiders "
        "defense, who started and scored minus 6.00. A 21.00-point swing, the biggest against any owner this "
        "week."))
    parts.append(boomer(
        "Doug cut a defense that scored 15 and started one that scored minus 6. Ryan Reed claimed the 15 and "
        "benched them. Fifteen points of Texans defense this week, and they did not count for anybody."))
    parts.append(gil(
        "Twenty-five moves went through. Scott Reisert released the Browns defense to add the Cowboys defense, who "
        "started and scored minus 2.00. Spencer Lentz claimed the Browns, started them for 11.00, and released "
        "the Packers defense, who scored 19.00."))
    parts.append(boomer(
        "Reisert gave away a defense and Spencer gave away a better one. Spencer won by 84 and still found a way "
        "to lose a waiver move by eight. That is like winning the pie contest and tripping on the way to the "
        "ribbon."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Doug Fields at Adam Hershberger, Spencer Lentz at Mama Beth, Casey Couture at DA, Scott Reisert at Ryan "
        "Reed, Geoff Cavender at Adam Calvelage, and Kent Frenger at Scott Howard."))
    parts.append(boomer(
        "Family Sunday. Both sons go home on the same weekend. Casey visits DA, and DA is 2 and 17 lifetime "
        "against him. Spencer visits Mama Beth, and she has won their last four regular-season meetings. I took "
        "both parents. Somebody set an extra plate, because I am coming to dinner and I am bringing the scores."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 5, HEADLINE, DEK, build(), META, "dlffl-week-5.png",
        published="2026-10-13T11:30:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "dlffl", "week-5.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
