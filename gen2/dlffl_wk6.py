"""Dewart Lake FFL, Week 6. Editorial.

Boomer runs ULTRA SPICY from Week 6 (Spencer, 2026-10-20: "I want spicy Boomer this week. Ultra spicy"):
every Boomer line carries a joke and a blade, Gil plays straight man, nobody is safe including Spencer,
clean language on the page, roast cap and Gil defenses still apply. Never "Mother", "Dad" or "father" for
the parents: Mama Beth and DA, always.

Outlier engine top items: Casey Couture leads DA 18-2 and has won ten straight (headline), Ryan Reed won
with 69.12, the 5th-fewest points in a win since 2009 (headline), Geoff Cavender 5-1 on a 29-37 all-play
(promote). Supporting: Doug Fields benched the win (27.80 left, lost by 8.82), Reisert's 68.68 is the
128th-lowest of 2,851, Kent Frenger left Tyler Shough's 26.96 on his bench, Mama Beth and Scott Howard
both set perfect lineups. Family Sunday: both sons won. DA's best possible lineup (101.30) beats Casey
(100.92) by 0.38. Reisert's Wan'Dale Robinson for Terry McLaurin swap (+0.50) wins his game by 0.06.
Red team round 1 (2026-10-20) fixed: Hershberger "under 100" claim (he beat Casey 97.18 to 87.82 in
Week 4), Cavender "three weeks" (Week 4 left 1.60), Purdy "22 every week", the jewelry line (Spencer has
four titles), the tie-break sentence, "two cleanest benches" (Mama Beth also 0.00), the curb joke (FoH
owns it), duplicated coaster, car and coat lines, "50% progress".
"""
import os

import booth
from booth import award, boomer, calls_list, gil, graded_list, jump, ledger, mcard
from compute import ledger_rows, load, by_owner

FACTS = load("dlffl_wk6_facts.json")
SEASON = load("dlffl_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 151.66

HEADLINE = "DA Has Lost To Casey Couture Ten Straight Times. Two Bench Swaps Would Have Won This One By 0.38."
DEK = (
    "Family Sunday went to the sons. Casey beat DA 100.92 to 92.00 and leads the series 18 and 2, and Spencer "
    "Lentz beat Mama Beth 100.30 to 93.48 to end her four-game regular-season run against him. Ryan Reed won "
    "with 69.12, the fifth-lowest winning score in this league since 2009, over a Scott Reisert who left the "
    "winning swap on his bench."
)
META = (
    "Gil and Boomer call Week 6 of the Dewart Lake FFL: Casey Couture beats DA for the tenth straight time, "
    "Spencer Lentz ends Mama Beth's run, Ryan Reed wins with 69.12, Kent Frenger scores 136.90, and Boomer "
    "goes 4 and 8 on his calls."
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

    # ---- 1. ten straight
    w, l = card_rows("Casey Couture", "dennis couture")
    parts.append(mcard(
        "m-casey", "Casey's tenth straight over DA, by 8.92", w, l,
        "D'Andre Swift 21.00, Jonathan Taylor 20.10 and Emeka Egbuka 14.30 for Casey Couture, who left 1.30 "
        "behind. Christian McCaffrey gave DA 26.20. Mark Andrews gave him 0.90, with Dalton Kincaid's 7.30 on "
        "the bench.", SCALE, key=True))
    parts.append(gil(
        "Casey Couture wins 100.92 to 92.00 and is 3 and 3. He has beaten DA ten straight times and leads the "
        "series 18 and 2. DA's best possible lineup this week was 101.30. Casey scored 100.92."))
    parts.append(boomer(
        "Ten straight, Gil. DA has been in this league since 2009 and he has beaten Casey twice. I have beaten "
        "my own kid at cards twice in that time, and I cheat. And the man had this one. Kincaid for Andrews is "
        "six and a half. Worthy for Watson is three. DA wins by 0.38. Casey did not beat DA this week. DA's "
        "bench did. The man had the answer twice and sat it both times, and twice in one afternoon stops "
        "being a mistake, Gil. It becomes a policy."))
    parts.append(gil(
        "In fairness to DA, Christian McCaffrey gave him 26.20, the best start on either side, and he is 4 and 2 "
        "with 761.56 points, second in the league. Josh Allen was projected for 26.36 and scored 18.30. And "
        "Casey has five titles here, the most of anyone."))
    parts.append(boomer(
        "Second in the league in points, and he cannot beat the kid who got his last name. Eighteen and two. "
        "Casey, I bet against you last week and I would like to formally withdraw from the family business. "
        "DA, I am not withdrawing from you. I am just going to stop watching, the way you stop watching a man "
        "parallel park."))

    # ---- 2. the photo finish at the bottom
    w, l = card_rows("Ryan Reed", "Scott Reisert")
    parts.append(mcard(
        "m-reed", "Reed's 69.12, the fifth-lowest winning score since 2009", w, l,
        "Jaxon Smith-Njigba 22.40 and DK Metcalf 14.80 for Ryan Reed, whose quarterback, Jacoby Brissett, "
        "scored 6.92. Scott Reisert's quarterback, Jameis Winston, scored 6.48, and his kicker, Nick Folk, "
        "scored 1.00.", SCALE))
    parts.append(gil(
        "Ryan Reed wins 69.12 to 68.68 and is 3 and 3. It is the fifth-lowest winning score in 1,424 games in "
        "this league since 2009, and the two lowest scores of the week played each other. Reisert had Wan'Dale "
        "Robinson on his bench for 3.70 and started Terry McLaurin for 3.20. That one swap wins him the game by "
        "0.06."))
    parts.append(boomer(
        "Sixty-nine to sixty-eight. Two grown men, eighteen starters, 137.80 points between them, and Kent "
        "Frenger scored 136.90 by himself. Scott Reisert has the cleanest bench in the league, 28.70 all season, "
        "and he lost by 0.44 with 0.50 of it sitting right there. Half a point, Scott. You count every slot like "
        "a man counting the silverware, and this week you got robbed by a teaspoon."))
    parts.append(gil(
        "In fairness to Scott Reisert, Jahmyr Gibbs, Jared Goff and his kicker all had the week off, and he is "
        "still 4 and 2 with 739.38 points, third in the league. He signed Jameis Winston and Nick Folk this week "
        "to cover the byes. They gave him 7.48 between them. For Ryan Reed, Jaxon Smith-Njigba gave him 22.40 "
        "and DK Metcalf 14.80, and the series with Reisert is now 1 and 1."))
    parts.append(boomer(
        "A one-week quarterback and a one-week kicker, and the pair of them scored seven and a half. Scott, you "
        "did not sign replacements. You hired two guys off a flyer stapled to a pole. And Ryan: you won with "
        "Cam Skattebo at running back for zero and a quarterback under seven, and you are 3 and 3. Somewhere "
        "Scott Howard, who scored 99 with a perfect lineup and lost, is staring at this card like it owes him "
        "something."))

    # ---- 3. the other son
    w, l = card_rows("Spencer Lentz", "Beth Couture")
    parts.append(mcard(
        "m-lentz", "Spencer ends Mama Beth's four-game run against him", w, l,
        "Drake Maye 23.80 and Chuba Hubbard 21.60 for Spencer Lentz, with C.J. Stroud's 25.98 on his bench. "
        "Mama Beth set a perfect lineup, led by the Chiefs defense at 14.00 and Rachaad White at 13.70.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 100.30 to 93.48 and is 4 and 2. Mama Beth had won their last four regular-season "
        "meetings. Spencer leads the series 16 and 10. She set a perfect lineup, and every player on her bench "
        "scored zero. Rachaad White was Spencer's running back until he released him this week. Mama Beth "
        "claimed him, and he gave her 13.70, her second-best player."))
    parts.append(boomer(
        "Spencer cut a running back, Mama Beth signed him, and he scored 13.70 against Spencer. That is the "
        "most Family Sunday thing that has ever happened. The man cleaned out his garage and his own family "
        "ran the yard sale. And Spencer still won, with C.J. Stroud scoring 25.98 on his bench. Spencer, the "
        "four-game streak against you is over, and so is your two-week streak of clearing 150. You went from "
        "192 to 100 in one week. Pick one to celebrate."))
    parts.append(gil(
        "Mama Beth has three titles in this league. Patrick Mahomes was projected for 19.62 and scored 10.48, "
        "and her best player was a defense."))
    parts.append(boomer(
        "Three rings and 1 and 5. Mama Beth can lose five of six and still own more rings than nine of the "
        "eleven people across from her. She set every slot right, her bench scored a perfect zero, six men "
        "without a point between them, and she lost by seven. Mama Beth, the lineup was perfect. The roster is "
        "the crime scene."))

    # ---- 4. the high score, and the quarterback on the bench
    w, l = card_rows("Kent Frenger", "Scott Howard")
    parts.append(mcard(
        "m-frenger", "Frenger scores 136.90 and benches a 26.96", w, l,
        "Kenneth Walker III 29.90, Bhayshul Tuten 22.70 and Germie Bernard 20.20 for Kent Frenger, with Tyler "
        "Shough's 26.96 on his bench. Scott Howard set a perfect lineup, led by Isaiah Likely at 20.90.", SCALE))
    parts.append(gil(
        "Kent Frenger wins 136.90 to 99.12 and is 4 and 2. It is the high score of the week by 32.76, and he "
        "would have beaten all eleven teams. Germie Bernard, signed this week, started and scored 20.20 on a "
        "projection of 8.02. Frenger leads Scott Howard 6 and 3."))
    parts.append(boomer(
        "Kent signed a receiver off the wire this week, started him, and got twenty. Then he left Tyler Shough "
        "on the bench for 26.96 behind Caleb Williams and 19.50. Kent, I bet on Shough this week. He scored 27 "
        "and I lost, because you sat him. You beat Scott by 38 and still found a way to beat me too. I am "
        "starting to think you did it on purpose."))
    parts.append(gil(
        "Scott Howard set a perfect lineup for the first time this season. Nothing on his bench. He scored "
        "99.12 and lost by 37.78. He is 1 and 5, and against the whole league he is 26 and 40, so his record "
        "is about a win and a half worse than his scores."))
    parts.append(boomer(
        "Scott Howard has left 163.50 on his bench this season, the most in the league by 52 points. This week "
        "he left nothing. Zero. The man finally did everything right, and the man across from him scored 137. "
        "Scott, the universe heard you fix the lineup and sent Kent Frenger. There is no lesson here. I "
        "checked. There is not even a moral.", "bad"))

    # ---- 5. the coaster
    w, l = card_rows("Adam Hershberger", "Doug Fields")
    parts.append(mcard(
        "m-hershberger", "Hershberger by 8.82, and Fields left 27.80 behind", w, l,
        "Trevor Lawrence 30.34, Malik Nabers 25.50 and Matthew Golden 22.40 for Adam Hershberger, who left "
        "26.50 behind. Doug Fields started Rhamondre Stevenson for 3.60 with Tre Tucker's 24.20 on his bench.",
        SCALE))
    parts.append(gil(
        "Adam Hershberger wins 104.14 to 95.32 and is 2 and 4. The series is now 6 and 6. Fields left 27.80 on "
        "his bench and lost by 8.82. Tucker for Stevenson alone is a 20.60 swing, and with it Fields wins by "
        "11.78. It is the biggest benching in the league this week that flipped a game by itself."))
    parts.append(boomer(
        "Doug started Rhamondre Stevenson at flex. Stevenson was projected for 12.34 and scored 3.60. Tre "
        "Tucker sat behind him and scored 24.20. Doug, you had the answer key and you used it as a coaster. "
        "And Adam: 26.50 on the bench, Colston Loveland for 15.50 behind Juwan Johnson for zero, and he won "
        "anyway. Two men brought the wrong lineup to the same game, and the man with the better wrong lineup "
        "won."))
    parts.append(gil(
        "In fairness to Doug Fields, James Cook III gave him 22.80 and Kirk Cousins 21.52, and he has scored "
        "between 92 and 106 every week this season. Adam Hershberger has had 799.00 points scored against him "
        "this year, still the most in the league."))
    parts.append(boomer(
        "Six weeks, six scores between 92 and 106. Doug is the most consistent man in the league and it has "
        "gotten him to 2 and 4. He is a metronome, Gil. Nobody has ever won a game with a metronome, and "
        "nobody has ever lost one by nine with 24 points on the bench and called it bad luck. Doug is about to "
        "be the first."))

    # ---- 6. the top seed
    w, l = card_rows("Geoff Cavender", "Adam Calvelage")
    parts.append(mcard(
        "m-cavender", "Cavender takes the top seed with 88.98", w, l,
        "Matthew Stafford 16.88 and Carnell Tate 16.00 for Geoff Cavender, with Jordan Love's 20.24 on his "
        "bench. Adam Calvelage started Brock Purdy for 17.36 with Jayden Daniels's 24.00 on his bench, and his "
        "kicker scored 1.00.", SCALE))
    parts.append(gil(
        "Geoff Cavender wins 88.98 to 72.26 and is 5 and 1, the top seed. It is the 71st-lowest winning score in "
        "this league since 2009. He has beaten Adam Calvelage three straight times, every meeting. Against the "
        "whole league Cavender is 29 and 37 this season, so his record is about two and a half wins better "
        "than his scores."))
    parts.append(boomer(
        "Geoff Cavender is the top seed and the league has outscored him more often than not. Five and one on "
        "a 29 and 37 all-play. That is not a record, Gil. That is a magic trick, and the league keeps lining up "
        "to see it."))
    parts.append(gil(
        "Two weeks ago Boomer called for Cavender to start Stafford, and in Week 5 Stafford outscored Jordan "
        "Love by 1.04. This week Love outscored Stafford by 3.36 from the bench, Cavender's first imperfect "
        "lineup since Week 4. In fairness to Adam Calvelage, RJ Harvey gave him 13.10 on a projection of 7.70, "
        "and he is 3 and 3 with 628.92 points, sixth in the league. His 72.26 is the seventh-worst of his 62 "
        "games here."))
    parts.append(boomer(
        "That one is mine. I told the man to start Stafford and he did it twice. Geoff, the first one was "
        "advice. The second one was you not reading the fine print. And Adam Calvelage: Jayden Daniels scored "
        "35.26 for you last week, and this week you sat him, and he scored 24.00 on the bench. Brandon Aubrey "
        "scored 1.00. MarShawn Lloyd, signed this week, scored 1.00. Adam, you had two men score exactly one "
        "point and you picked both of them on purpose. Sixth in points and 3 and 3. The man is average at "
        "everything except quarterback decisions, where he is a pioneer."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls came due. Four right, eight wrong. Season record, 27 and 33. Last week I took both "
        "parents on Family Sunday. Both parents lost. I am no longer welcome at the house. Every call is below."))
    parts.append(graded_list([
        ("DA The Badenov's", "DA beats Casey Couture.", "WRONG",
         "Lost by 8.92. Ten straight. Two swaps and he wins by 0.38. I picked a man who had the answer on his "
         "bench, and I should have known he would sit on it."),
        ("One Under akaThe Mulligan", "Casey Couture leaves under ten on his bench in Week 6.", "RIGHT",
         "1.30. I bet on his lineup and against his record in the same breath. The lineup carried me. The "
         "record carried him."),
        ("Balls Deep", "Spencer Lentz clears 150 for the third straight week.", "WRONG",
         "100.30. The streak is over and so is my parade."),
        ("Momma's Boys", "Mama Beth beats Spencer Lentz.", "WRONG",
         "Lost by 6.82 with a perfect lineup. Four straight against him, and I picked the week it ended. I have "
         "a gift."),
        ("Holy Rollers", "Adam Hershberger beats Doug Fields.", "RIGHT",
         "By 8.82, with 26.50 on his bench. He won carrying a bag of rocks."),
        ("Cosby Copperheads", "Doug Fields clears 100 in Week 6.", "WRONG",
         "95.32. Tre Tucker scored 24.20 on his bench. Start him and it is 115.92 and a win. Doug, I am 0 and 2 "
         "on this call and you are the reason both times."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert leaves under ten on his bench in Week 6.", "RIGHT",
         "3.20, and half a point of it was the whole game. I won the call. Scott lost the week."),
        ("BearDown", "Ryan Reed beats Scott Reisert.", "RIGHT",
         "By 0.44, with 69.12, the fifth-lowest winning score here since 2009. A win is a win, and this one I "
         "will take with both hands and a glove."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender sets a perfect lineup again.", "WRONG",
         "Left 3.36. Jordan Love outscored Stafford from the bench, and I am the one who told him to start "
         "Stafford two weeks ago. That one goes on my record, not his."),
        ("An alBum Cover", "Adam Calvelage beats Geoff Cavender for the first time.", "WRONG",
         "Lost by 16.72 with Jayden Daniels on the bench for 24.00. Now 0 and 3, and the man who could have "
         "fixed it watched from the bench."),
        ("The Scranton Strangler", "Scott Howard clears 150 again.", "WRONG",
         "99.12, a perfect lineup, his first all year. He did the one thing I asked and lost by 38. I need a "
         "new thing to yell about."),
        ("Berlin Blitz", "Tyler Shough gets back into double figures for Kent Frenger.", "WRONG",
         "Shough scored 26.96. On the bench. The call needs him in the lineup, and Kent sat him for Caleb "
         "Williams and 19.50. Right about the quarterback, wrong about the man holding the clipboard."),
    ]))
    parts.append(gil(
        "Four right, eight wrong. Twelve new ones for Week 7, one per team. The Bills, Chargers, Commanders "
        "and Jaguars have the week off."))
    parts.append(calls_list([
        ("Momma's Boys", "Mama Beth beats Adam Hershberger.",
         "She leads the series 6 and 2, Justin Jefferson is back from his bye, and Adam's only quarterback, "
         "Trevor Lawrence, has the week off, along with his defense. I took her against her son and lost. I am "
         "taking her against a man with no quarterback. If this one misses, I am done picking the parents."),
        ("Holy Rollers", "Malik Nabers clears 20 again for Adam Hershberger.",
         "25.50 this week, 26.60 the week before. Lawrence is on bye, so somebody has to carry Adam, and "
         "Nabers is the only man on that roster who keeps showing up."),
        ("Cosby Copperheads", "Doug Fields starts Tre Tucker in Week 7.",
         "Tucker scored 24.20 on the bench while Rhamondre Stevenson started for 3.60. James Cook III and Keon "
         "Coleman have the week off. There is a slot open, Doug, and the man is standing right next to it."),
        ("DA The Badenov's", "DA beats Doug Fields with Aaron Rodgers at quarterback.",
         "Josh Allen, Khalil Shakir and Dalton Kincaid all have the week off with the Bills. DA signed Aaron "
         "Rodgers this week, before he needed him, and he leads Fields 8 and 3. For once the elder planned "
         "ahead, and I am rewarding it."),
        ("Balls Deep", "Spencer Lentz beats Ryan Reed by twenty or more.",
         "Spencer leads the series 4 and 2 and has the most points in the league. Reed's last two scores are "
         "91.88 and 69.12. Spencer's worst score all season is 95.82. Spencer's floor is higher than Ryan's "
         "ceiling, Gil."),
        ("BearDown", "Jaxon Smith-Njigba clears 20 again for Ryan Reed.",
         "22.40 this week, and he is the one thing on that roster you can set a watch by. Ryan, the rest of "
         "your lineup scored 46.72. Smith-Njigba can only carry so much."),
        ("One Under akaThe Mulligan", "Casey Couture beats Adam Calvelage for the sixth straight time.",
         "5 and 0 lifetime, and Casey just beat DA with 1.30 on his bench. Adam Calvelage has Jayden Daniels "
         "on bye, so for once he cannot sit him. I bet against Casey last week and he made me look like a man "
         "who bet against Casey."),
        ("An alBum Cover", "Brock Purdy clears 20 for Adam Calvelage.",
         "17.36 this week with Daniels on the bench. Daniels is on bye, so Purdy starts, and Purdy has cleared "
         "20 in four of six weeks. Adam, this is the week the quarterback decision makes itself. Try not to "
         "interfere."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert clears 120 in Week 7.",
         "Jahmyr Gibbs and Jared Goff are back from the bye. With them he scored 105, 142, 161, 138 and 125. "
         "Without them, 68.68. The Lions are back, Scott. Put the flyer guys back in the drawer."),
        ("The Scranton Strangler", "Scott Howard beats Scott Reisert.",
         "Howard is 1 and 5, and the league has outscored him 40 times in 66, so he is about a win and a half "
         "short of his scores. Sam LaPorta is back from the bye. Reisert leads the series 3 and 2. I am betting "
         "on the law of averages, which has clearly never met Scott Howard."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender beats Kent Frenger for the first time.",
         "0 and 2 lifetime, by 35 and by 7. Kent has Bhayshul Tuten on bye and Ja'Marr Chase back from his. "
         "Geoff is 5 and 1 and nobody believes it, including me, so I am betting he proves one of us wrong."),
        ("Berlin Blitz", "Kent Frenger starts Tyler Shough in Week 7.",
         "I bet on Shough's points this week and he scored 26.96 on the bench, so the loss went on my record. "
         "This time I am betting on Kent's finger. Caleb Williams scored 19.50. Start the man, Kent, and we "
         "both win."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "One piece of hardware per owner per week. When an owner already has one, the next name in line takes "
        "it."))
    parts.append(award(
        "good", "Owner of the Week", "Kent Frenger · Berlin Blitz",
        "136.90, the high score of the week by 32.76. He would have beaten all eleven teams. Kenneth Walker III "
        "29.90, Bhayshul Tuten 22.70, and Germie Bernard, signed this week, 20.20. The reigning champion's first "
        "trophy of the season.",
        "He won it with a receiver he signed this week and a quarterback he benched. Kent, first thing on the "
        "shelf this year. Put it up before the quarterback you benched asks to hold it."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Scott Reisert · Simba St. Gibbs Lion Kings",
        "68.68, the lowest score in the league and the 128th-lowest of 2,851 team-weeks here since 2009. It "
        "loses to all eleven teams. He lost by 0.44 with a half-point swap on his bench that would have won it.",
        "Three byes, two one-week stand-ins, 7.48 points from the pair, and a loss by 0.44 to the second-lowest "
        "score of the week. Scott, the man across from you scored 69 and you still came up short. You lost a "
        "limbo contest to a man who was already lying down."))
    parts.append(award(
        "good", "Start of the Week", "Adam Hershberger · Trevor Lawrence, 30.34",
        "Projected for 18.57, so 11.77 over. Germie Bernard's 20.20 for Kent Frenger was 0.41 bigger, and "
        "Frenger already has a trophy.",
        "Enjoy it, Adam. It comes with a note: Lawrence has the week off next week and there is not a single "
        "quarterback on your bench. The trophy is the good news. The note is the news."))
    parts.append(award(
        "bad", "Sit of the Week", "Doug Fields · Tre Tucker, 24.20 on the bench",
        "Rhamondre Stevenson started at flex in his place for 3.60, a swing of 20.60 in a game Fields lost by "
        "8.82. The biggest benching in the league that flipped its game by itself.",
        "Twenty-four on the bench, three and a half in the lineup, and a loss by nine. Doug, the answer was in "
        "the building. It was just not in the room."))
    parts.append(award(
        "bad", "Waste of the Week", "Spencer Lentz · 10.58 left behind, and he won",
        "C.J. Stroud scored 25.98 on his bench behind Drake Maye's 23.80, and the Browns defense scored 10.00 "
        "behind the Panthers' 6.00. Adam Hershberger left 26.50 and Kent Frenger 14.76, but both already hold a "
        "trophy.",
        "Spencer made two moves this week and lost points on both. He signed Jonathon Brooks, who is on injured "
        "reserve and scored zero, and he signed the Panthers defense and released Rachaad White, who scored "
        "13.70 for Mama Beth. Then he started the Panthers and sat the Browns. Spencer, you did not waste ten "
        "points. You exported them."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "All twelve of you, every week, all season. Scott Howard still leads at 163.50, and for the first time "
        "this year he added nothing to it. Casey Couture is second at 111.48 and added 1.30. The two names at "
        "the top of this table left 1.30 between them this week, and one of them won. Six weeks, Gil, and the "
        "first clean week at the top came with a loss attached."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 6, season_note=(
        "Season totals come from the season ledger through Week 6. Scott Howard leads at 163.50, Casey Couture "
        "is second at 111.48, Adam Hershberger third at 107.20. Scott Reisert has left the fewest, 28.70.")))
    parts.append(gil(
        "Three benches cost a game this week: Doug Fields left 27.80 and lost by 8.82, DA left 9.30 and lost by "
        "8.92, and Scott Reisert left 3.20 and lost by 0.44. Mama Beth and Scott Howard left nothing, and both "
        "lost."))
    parts.append(boomer(
        "Three losses, three benches, and the smallest one hurts the most. 3.20 on the bench, a loss by 0.44, "
        "and the half point he needed was sitting in the one slot he did not check. You cannot see a splinter "
        "either, Gil. You just feel it all week."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Kent Frenger adding Germie Bernard, who started and "
        "scored 20.20, for Will Shipley, who scored zero. The biggest swing of any move in the league this week."))
    parts.append(gil(
        "<strong>Worst move:</strong> Spencer Lentz releasing Rachaad White, who scored 13.70 for Mama Beth, to "
        "add the Panthers defense, who started and scored 6.00. A 7.70-point swing against him, and the player "
        "went to the other side of his own matchup."))
    parts.append(boomer(
        "Spencer handed his opponent a running back the week he played her. Thirteen points. That is not a "
        "waiver move, Gil. That is a hostess gift."))
    parts.append(gil(
        "Thirty-two moves went through. Mama Beth, Doug Fields and Scott Reisert made five each. Mama Beth's "
        "five included Kimani Vidal twice and James Conner once at the same running back slot, before she "
        "landed on Rachaad White. DA signed Aaron Rodgers, who scored 16.02 on his bench, ahead of the Bills' "
        "bye."))
    parts.append(boomer(
        "Four moves for one running back slot. Vidal, then Conner, then Vidal again, then White. Mama Beth did "
        "not fill a running back slot this week, Gil. She held auditions, and the part went to Spencer's old "
        "running back."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Adam Hershberger at Mama Beth, DA at Doug Fields, Ryan Reed at Spencer Lentz, Adam Calvelage at Casey "
        "Couture, Scott Howard at Scott Reisert, and Kent Frenger at Geoff Cavender. The Bills, Chargers, "
        "Commanders and Jaguars have the week off."))
    parts.append(boomer(
        "No family games next week, so the Coutures can go back to pretending they are not keeping score, which "
        "they are, in pen. DA signed Aaron Rodgers for the Bills' bye and I am calling it. Mama Beth gets a man "
        "with no quarterback and I am calling that too. I went 0 for 2 on the parents last week, Gil. I set the "
        "plate, nobody came, and I ate alone in the car. This week I am back at the table, and if both parents "
        "lose again I am moving in with Casey."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 6, HEADLINE, DEK, build(), META, "dlffl-week-6.png",
        published="2026-10-20T11:30:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "dlffl", "week-6.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
