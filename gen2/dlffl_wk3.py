"""Dewart Lake FFL, Week 3. Editorial.

Outlier engine top items this week: Doug Fields 13-0 lifetime over Scott Howard (headline tier),
Scott Reisert 160.76, second-best game of his career (promote).
"""
import os

import booth
from booth import award, boomer, calls_list, gil, graded_list, jump, ledger, mcard
from compute import ledger_rows, load, by_owner

FACTS = load("dlffl_wk3_facts.json")
SEASON = load("dlffl_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 161.06

HEADLINE = "Scott Howard Has Played Doug Fields 13 Times And Lost All 13"
DEK = (
    "Doug Fields won 105.48 to 84.54 and now leads the series 13 and 0. A fair coin comes up the same way "
    "thirteen straight times about once in 4,096 tries. Elsewhere Scott Reisert hung 160.76 on the board, "
    "Casey Couture benched a quarterback who scored 30.66 in a game he lost by 12.86, and Boomer went 6 and 6."
)
META = (
    "Gil and Boomer call Week 3 of the Dewart Lake FFL: Doug Fields is 13 and 0 lifetime against Scott Howard, "
    "Scott Reisert scored 160.76, and Boomer went 6 and 6 on his calls."
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

    # ---- 1. the streak
    w, l = card_rows("Doug Fields", "Scott Howard")
    parts.append(mcard(
        "m-fields", "Fields makes it 13 for 13 against Howard", w, l,
        "James Cook III 22.40 and Derrick Henry 21.40 for Doug Fields. Scott Howard got 26.90 from Drake London "
        "and left Michael Wilson and 20.40 on his bench. Every meeting these two have ever had has ended the same way.",
        SCALE, key=True))
    parts.append(gil(
        "Doug Fields wins 105.48 to 84.54 and gets his first win of the season. He and Scott Howard have now played "
        "thirteen times since Howard joined this league in 2019. Fields has won all thirteen."))
    parts.append(boomer(
        "Thirteen and oh. That is not a rivalry, Gil, that is a standing appointment. Scott Howard shows up, Doug "
        "Fields signs him in, and Scott goes home. Eight seasons of this. Somebody get the man a punch card."))
    parts.append(gil(
        "In fairness to Scott Howard, he made the right call at quarterback. He started Lamar Jackson for 20.44 over "
        "Dak Prescott at 18.94, and Boomer had said he would do the opposite."))
    parts.append(boomer(
        "He got the hard question right and then started a tight end who scored 2.30. His best possible lineup was "
        "119.74, which beats Doug Fields. Scott, Doug Fields does not need your help. Stop giving it to him."))

    # ---- 2. career night
    w, l = card_rows("Scott Reisert", "Adam Hershberger")
    parts.append(mcard(
        "m-reisert", "Reisert hangs 160.76, second-best of his career", w, l,
        "Jahmyr Gibbs 37.90 and George Kittle 23.20. Only one single week Reisert has ever played in this league beat it: "
        "182.04, in 2023. He left 0.30 on his bench.", SCALE))
    parts.append(gil(
        "Scott Reisert wins 160.76 to 89.88, the widest game of the week at 70.88, and is 3 and 0. He had 161.06 "
        "available and started all but 0.30 of it. It snaps a three-game Hershberger run, and the series is now 4 and 4."))
    parts.append(boomer(
        "Thirty hundredths. He left thirty hundredths of a point on his bench. That is not a bench, Gil, that is "
        "lint. Back in Week 1 I said this man would not reach 120 in Week 2 or Week 3. He cleared it by 22, then by "
        "41, and I would like the record to show I have stopped talking about Scott Reisert.", "good"))
    parts.append(gil(
        "Adam Hershberger is 0 and 3. Matthew Golden gave him 21.50, more than double his projection, and Trevor "
        "Lawrence 19.78. Juwan Johnson scored 19.30 on his bench while Colston Loveland started at tight end for 5.10."))
    parts.append(boomer(
        "89.88 would have beaten four teams in this league this week. He drew the second-best game of Reisert's "
        "life instead. He has had 423.20 scored against him, the most in the league. Adam, the schedule has to even "
        "out sometime. It just has not been told."))

    # ---- 3. the clean sheet
    w, l = card_rows("Spencer Lentz", "Kent Frenger")
    parts.append(mcard(
        "m-lentz", "Spencer's perfect lineup, and his first win", w, l,
        "Bijan Robinson 37.30 and Brock Bowers 25.60. Spencer Lentz started every point he had. "
        "Kent Frenger left 1.00 behind and lost anyway.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 134.26 to 118.70 with a perfect lineup, which happens in about 12% of team-weeks in this "
        "league since 2018. It is his first win of the season and it snaps a four-game Frenger streak. Spencer still leads that "
        "series 16 and 11."))
    parts.append(boomer(
        "Perfect lineup, and I want everybody to see what perfect looked like. Drake Maye at quarterback for 3.76. "
        "The Packers defense for negative six. Perfect "
        "only means nobody on the bench was any better. It does not mean anybody in the lineup was any good."))
    parts.append(gil(
        "Kent Frenger started 118.70 of the 119.70 he had available. Tyler Shough, added off the wire this week, "
        "led him at 23.80, and Kenneth Walker III and Ja'Marr Chase put up 20.30 apiece."))
    parts.append(boomer(
        "One point left behind and he still lost by 15.56. Kent did everything right and ran into a running back "
        "who decided it was his birthday.", "good"))

    # ---- 4. won ugly
    w, l = card_rows("Geoff Cavender", "Casey Couture")
    parts.append(mcard(
        "m-cavender", "Cavender goes 3 and 0 on 89.04", w, l,
        "Bryce Young 13.64 led Geoff Cavender, with Matthew Stafford's 23.90 and Jordan Love's 21.48 on his bench. "
        "Casey Couture's Sam Darnold scored 30.66 on his.", SCALE))
    parts.append(gil(
        "Geoff Cavender wins 89.04 to 76.18 and is 3 and 0. Only 72 winning teams in this league since 2009 have "
        "scored less. He started Bryce Young with two other quarterbacks on his bench "
        "who both scored more than 21."))
    parts.append(boomer(
        "He would have lost to eight of the eleven teams in this league this week, and he drew one of the other three. "
        "Geoff Cavender is not 3 and 0. Geoff Cavender's schedule is 3 and 0.", "good"))
    parts.append(gil(
        "Casey Couture added Sam Darnold off the wire this week, then started Baker Mayfield for 11.28. Darnold "
        "scored 30.66 on the bench. The swing was 19.38 and Casey lost by 12.86."))
    parts.append(boomer(
        "He went to the wire, found the exact thing he needed, and left it in the garage. Casey, that man was the "
        "answer, and you had him in the house."))

    # ---- 5. the streak, other end
    w, l = card_rows("Adam Calvelage", "Beth Couture")
    parts.append(mcard(
        "m-calvelage", "Calvelage makes it three straight over Mama Beth", w, l,
        "Brock Purdy 32.28 and Garrett Wilson 24.70 for Adam Calvelage. The Vikings defense, added off the wire, "
        "led Mama Beth at 19.00.", SCALE))
    parts.append(gil(
        "Adam Calvelage wins 111.68 to 77.92, his third straight win over Mama Beth. De'Von Achane gave him 1.70 "
        "against a projection of 18.35, and Jakobi Meyers put up 15.90 on his bench."))
    parts.append(boomer(
        "He started De'Von Achane for 1.70 and Tetairoa McMillan for 2.70 and still won by 33.76. When Brock Purdy "
        "goes for 32 you can carry passengers. He carried two and never felt the weight."))
    parts.append(gil(
        "Mama Beth scored 77.96 last week and 77.92 this week. Justin Jefferson gave her 4.20 against a projection "
        "of 15.82, with Luther Burden III and 16.30 on her bench."))
    parts.append(boomer(
        "Four hundredths of a point apart, two weeks running. That is not a slump, Gil, that is a setting. She "
        "found the dial and she has not touched it since. Mama Beth, I say this with love: turn the dial.", "bad"))

    # ---- 6. first time
    w, l = card_rows("Ryan Reed", "dennis couture")
    parts.append(mcard(
        "m-reed", "Reed snaps DA's three-game run", w, l,
        "Jaxon Smith-Njigba 33.36 and Harold Fannin Jr. 20.60 for Ryan Reed. DA left just 2.10 on his bench and "
        "lost the closest game of the week by 10.04.", SCALE))
    parts.append(gil(
        "Ryan Reed wins 112.00 to 101.96 and is 2 and 1. Smith-Njigba has now gone for 42.00 and 33.36 in back to "
        "back weeks. It snaps DA's three-game run over him, and DA still leads the "
        "series 5 and 4."))
    parts.append(boomer(
        "Jaxon Smith-Njigba is not a wide receiver on this roster, he is the sunrise. He shows up every Sunday and "
        "the other nine guys just have to not embarrass anybody."))
    parts.append(gil(
        "DA started 101.96 of the 104.06 he had available. Christian McCaffrey gave him 19.60, and Josh Allen "
        "16.96 against a projection of 24.63."))
    parts.append(boomer(
        "Here is the thing about DA. He does not make mistakes. He left 2.10 on his bench this week and he has left "
        "11.50 all season, the fewest in the league. He just needed Josh Allen to "
        "show up. Josh Allen sent a note."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls last week. Six came in, six did not. That is the first week I have broken even, and I would "
        "like a small parade. Season record, 10 and 14. Every one of them is below, winners and losers."))
    parts.append(graded_list([
        ("DA The Badenov's", "DA clears 120 for the third straight week.", "WRONG",
         "101.96. Josh Allen scored 16.96, and the streak stopped at two."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert leaves under ten on his bench again in Week 3.", "RIGHT",
         "0.30. Barely worth the ink."),
        ("Balls Deep", "Spencer Lentz wins his first game of the season.", "RIGHT",
         "By 15.56 over Kent Frenger, with a perfect lineup."),
        ("Momma's Boys", "Mama Beth leaves under ten on her bench in Week 3.", "WRONG",
         "15.42, most of it Luther Burden III."),
        ("Berlin Blitz", "Kenneth Walker III goes for 15 or more again for Kent Frenger.", "RIGHT",
         "20.30."),
        ("One Under akaThe Mulligan", "Casey Couture starts Stefon Diggs in Week 3.", "WRONG",
         "He did not. The quarterback he did not start was the bigger problem."),
        ("An alBum Cover", "CeeDee Lamb clears 20 again for Adam Calvelage.", "WRONG",
         "19.70. Missed by three tenths. Lamb and I are not speaking."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender goes 3 and 0.", "RIGHT",
         "3 and 0, by 12.86, on 89.04. I will take it however it arrives."),
        ("BearDown", "Jaxon Smith-Njigba clears 20 again for Ryan Reed.", "RIGHT",
         "33.36."),
        ("Cosby Copperheads", "Doug Fields beats Scott Howard on Sunday.", "RIGHT",
         "By 20.94. The easiest call I will make all year, and I have eleven more regular-season weeks to find an easier one."),
        ("The Scranton Strangler", "Scott Howard starts Dak Prescott in Week 3.", "WRONG",
         "He started Lamar Jackson, who outscored Prescott by 1.50. He was right and I was not."),
        ("Holy Rollers", "Adam Hershberger clears 100 for the first time this season.", "WRONG",
         "89.88, with Juwan Johnson's 19.30 on the bench. He had 106.08 available."),
    ]))
    parts.append(gil("Six right, six wrong. Twelve new ones for Week 4, one per team."))
    parts.append(calls_list([
        ("Holy Rollers", "Adam Hershberger beats Casey Couture for his first win.",
         "0 and 3, but he has scored more than Casey did this week in two of his three games, and he beat Casey the "
         "last time they met, in 2025. Casey scored 76.18 on Sunday."),
        ("One Under akaThe Mulligan", "Casey Couture starts Sam Darnold in Week 4.",
         "30.66 on the bench on Sunday, against Baker Mayfield's 11.28 in the lineup. I went to the Stefon Diggs "
         "well last week and came up dry. I am going back to the well with a bigger bucket."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert goes 4 and 0.",
         "407.78 points in three weeks, the most in the league, and he has left 15.10 on his bench all season. "
         "He would have beaten all eleven teams this week."),
        ("Balls Deep", "Bijan Robinson clears 20 again for Spencer Lentz.",
         "37.30 on Sunday against a projection of 18.24, the biggest overperformance by any starter in the league. "
         "Spencer draws Reisert, who has left 15.10 on his bench all season to Spencer's 23.00. For "
         "once he is the sloppy one in the matchup."),
        ("Cosby Copperheads", "Doug Fields beats Geoff Cavender.",
         "Fields is 1 and 2 on 302.02 points. Cavender is 3 and 0 on 300.12. Same points, opposite records. One of "
         "these men is due."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender clears 100 in Week 4.",
         "Two quarterbacks scored 21 or more on his bench this week. Start Stafford over Bryce Young and he "
         "scores 99.30. Close is not 100. Do it again next week and this call comes in."),
        ("Momma's Boys", "Mama Beth beats Kent Frenger.",
         "Frenger has won the last three between them. Through last season she had the best lineup "
         "efficiency of any current owner in this league, 90.1% of her available points started, and 77.92 is not a number "
         "that lasts for a woman who scored 149.12 in Week 1."),
        ("Berlin Blitz", "Tyler Shough clears 15 again for Kent Frenger.",
         "Added off the wire, started straight away, 23.80 against a projection of 19.75. Frenger has left 14.00 "
         "on his bench all season. The man knows who to play."),
        ("DA The Badenov's", "DA beats Scott Howard.",
         "Howard has won the last four between them. DA has 398.84 points, second in the league, and he has left 11.50 behind all year."),
        ("The Scranton Strangler", "Scott Howard leaves under twenty on his bench in Week 4.",
         "46.00, 31.06 and 35.20 so far. He got the quarterback right this week. One more right answer at flex "
         "and this call comes in."),
        ("BearDown", "Ryan Reed wins his first ever meeting with Adam Calvelage.",
         "They have never played. Reed's last season before this one was 2021 and Calvelage arrived in 2022. "
         "Reed has Smith-Njigba, 75.36 across the last two weeks."),
        ("An alBum Cover", "Brock Purdy clears 20 again for Adam Calvelage.",
         "32.28 on Sunday, and 28.48 on his bench in Week 2. When Calvelage plays him, Purdy plays back."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(award(
        "good", "Owner of the Week", "Scott Reisert · Simba St. Gibbs Lion Kings",
        "160.76, the highest score in the league, with 0.30 left behind. He is the first owner to win this award "
        "twice.",
        "Two weeks running. At this point I am not giving him a trophy, I am giving him a parking spot. Scott, you "
        "can stop now, the rest of the building would like a turn."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Casey Couture · One Under akaThe Mulligan",
        "76.18, the lowest score in the league, with 106.16 available. He would have lost to all eleven teams.",
        "Casey, your mother scored 77.92 this week, the number I just gave a whole card to making fun of. She "
        "outscored you by 1.74. Think about that at Thanksgiving."))
    parts.append(award(
        "good", "Start of the Week", "Spencer Lentz · Bijan Robinson, 37.30",
        "He was projected for 18.24 and scored more than double it. No starter in the league beat his projection "
        "by more. Ryan Reed's Jaxon Smith-Njigba came closest, 14.87 over.",
        "Bijan went for 37 in a lineup that also started a defense that scored negative six. Bijan was not "
        "playing for Spencer this week, he was covering for him."))
    parts.append(award(
        "bad", "Sit of the Week", "Scott Howard · Michael Wilson, 20.40 on the bench",
        "Isaiah Likely started for 2.30 in his place, a swing of 18.10 in a game Howard lost by 20.94. Casey "
        "Couture's benching was bigger, and he has hardware already.",
        "Michael Wilson scored 20.40 on the bench and Isaiah Likely scored 2.30 in the lineup. Scott, the depth "
        "chart is not alphabetical."))
    parts.append(award(
        "bad", "Waste of the Week", "Doug Fields · 31.30 left behind, and he won anyway",
        "The most points left on a bench by any winner. Joe Burrow scored 22.58 on it and Kalif Raymond 18.00, "
        "while Rhamondre Stevenson started for 5.30.",
        "Joe Burrow scored 22.58 on his bench and Doug won anyway. When your backup quarterback is that good, you "
        "are not managing a lineup, you are managing a waiting list."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All twelve of you, every week, all season. Scott Howard leads it at 112.26 and the gap to second is "
        "47.42. He is lapping the field in the one race nobody signed up for."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 3, season_note=(
        "Season totals come from the season ledger through Week 3. Scott Howard leads at 112.26, Ryan Reed is "
        "second at 64.84, Casey Couture third at 61.78. Spencer Lentz is the only owner with nothing left behind "
        "this week.")))
    parts.append(gil(
        "Two of twelve this week. Casey Couture left 29.98 and lost by 12.86, and Scott Howard left 35.20 and lost "
        "by 20.94. Both of those benches decided a game."))
    parts.append(boomer(
        "This league breaks a tied game on bench points, the one day a full bench saves you. Nobody has been "
        "within ten of a tie yet. Until somebody is, this table is just evidence."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Kent Frenger adding Tyler Shough, who scored 23.80, for Kayshon Boutte, who "
        "scored 3.10. A 20.70-point swing, and he started Shough the same week. He was Frenger's top scorer."))
    parts.append(gil(
        "<strong>Worst move:</strong> Doug Fields dropping Bo Nix, 24.14, to add C.J. Stroud, 11.68. A 12.46-point "
        "swing against him."))
    parts.append(boomer(
        "DA dropped the Packers defense and signed the Panthers, who scored 6.00. His son Spencer went and picked "
        "the Packers up off the curb, started them, and they scored negative six. Some things you do not pull out "
        "of your father's garbage, son. A defense is one of them."))
    parts.append(gil(
        "Twenty-one moves went through. Doug Fields made four of them and also swapped RJ Harvey, 7.70, for Tank "
        "Bigsby, who scored negative one. Mama Beth's Vikings defense, a free-agent pickup, was her top scorer at 19.00."))
    parts.append(boomer(
        "Mama Beth went to the wire and came back with her best player of the week. Doug went four times and came "
        "back 18.96 points lighter, net. The kicker swap made him two. The quarterback swap cost him twelve "
        "and a half."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Casey Couture at Adam Hershberger, Scott Reisert at Spencer Lentz, Geoff Cavender at Doug Fields, Kent "
        "Frenger at Mama Beth, Scott Howard at DA, and Adam Calvelage at Ryan Reed, a pairing this league has never "
        "seen before."))
    parts.append(boomer(
        "Reisert at Spencer is the one. The two cleanest lineups in the building, 0.30 left behind between them "
        "this week, and Reisert leads the series 5 and 3. One of those tidy benches loses Sunday anyway, and the loser has "
        "to go look at his bench and find out it was not his bench's fault."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 3, HEADLINE, DEK, build(), META, "dlffl-week-3.png",
        published="2026-09-29T09:00:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "dlffl", "week-3.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
