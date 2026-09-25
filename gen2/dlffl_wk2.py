"""Dewart Lake FFL, Week 2. Editorial."""
import json
import os

import booth
from booth import award, boomer, calls_list, esc, gil, graded_list, jump, ledger, mcard
from compute import hardware, ledger_rows, load, by_owner

FACTS = load("dlffl_wk2_facts.json")
SEASON = load("dlffl_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 151.48

HEADLINE = "DA Put 140 On His Wife And Boomer Had Her Winning"
DEK = (
    "Dennis Couture, DA to everybody in this league, went for 140.02 against Mama Beth's 77.96, "
    "the widest game of the week. Boomer called that one for her last week. He was wrong about "
    "that and about seven other things, and he reads every one of them back before he says anything else."
)
META = (
    "Gil and Boomer call Week 2 of the Dewart Lake FFL: DA beat Mama Beth by 62.06, Scott Reisert "
    "started a perfect lineup, and Boomer went 4 and 8 on his Week 1 calls."
)


def m(owner):
    return T[owner]


def card_rows(win_owner, lose_owner):
    w, l = m(win_owner), m(lose_owner)
    return (
        {"team": w["name"], "owner": SEASON["owners"][win_owner]["display"], "score": w["score"], "left": w["left"]},
        {"team": l["name"], "owner": SEASON["owners"][lose_owner]["display"], "score": l["score"], "left": l["left"]},
    )


def build():
    parts = []
    teams = [(t["name"], SEASON["owners"][t["owner"]]["display"]) for t in FACTS["perTeam"]]
    parts.append(jump(teams))
    parts.append('<h2 id="board">The Scoreboard</h2>')

    # ---- 1. the house game
    w, l = card_rows("dennis couture", "Beth Couture")
    parts.append(mcard(
        "m-da", "DA takes the house game by 62.06", w, l,
        "Josh Allen 40.82 and Dalton Kincaid 19.00 for DA. Patrick Mahomes and his 31.98 watched Mama Beth's "
        "loss from her bench.", SCALE, key=True))
    parts.append(gil(
        "DA scores 140.02 and wins the only game in this league played inside one marriage. It is his second "
        "straight week over 140, after 156.86 in Week 1."))
    parts.append(boomer(
        "Last week I told you Mama Beth beats this man on Sunday. She is 17 and 10 against him lifetime and "
        "I liked the number. She started Jalen Hurts for 16.16 and left Patrick Mahomes and 31.98 on the bench, "
        "and I got buried right alongside her."))
    parts.append(gil(
        "Mama Beth scored 77.96, which is 71.16 below the 149.12 she put up in Week 1. Rashod Bateman led her at 18.30 and "
        "Harrison Butker kicked 16.00, which is a sentence nobody wants written about their week."))
    parts.append(boomer(
        "Her kicker outscored Saquon Barkley, Justin Jefferson and David Montgomery put together. Those three "
        "got her 14.20. Butker got her 16.00 by himself and he does not even have to run anywhere.", "bad"))

    # ---- 2. the perfect lineup
    w, l = card_rows("Scott Reisert", "Kent Frenger")
    parts.append(mcard(
        "m-reisert", "Reisert turns in a perfect lineup", w, l,
        "Davante Adams 38.50 and Jared Goff 32.78. Nothing on his bench outscored anything in his lineup, the "
        "first clean sheet of the season in this league.", SCALE))
    parts.append(gil(
        "Scott Reisert scores 142.08, the highest in the league this week, and leaves nothing behind. His best "
        "possible lineup was the one he turned in."))
    parts.append(boomer(
        "I said this man does not reach 120 in Week 2 or Week 3. He hit 142.08 in the first half of that sentence "
        "and did it without a single wrong button. Put it on the board as wrong, and put his name on the trophy.", "good"))
    parts.append(gil(
        "Kent Frenger got 23.80 from Kenneth Walker III and 23.00 from Ja'Marr Chase and still lost by 42.36. "
        "His quarterback, Caleb Williams, scored 7.72 against a projection of 20.30."))
    parts.append(boomer(
        "Two receivers north of 23 and he loses by 42. That is not a lineup problem, that is walking into the one "
        "man in the building who did not make a mistake."))

    # ---- 3. the two man show
    w, l = card_rows("Adam Calvelage", "Spencer Lentz")
    parts.append(mcard(
        "m-calvelage", "Calvelage gets 57.90 out of two men", w, l,
        "CeeDee Lamb 34.30 and Travis Kelce 23.60. Spencer Lentz's Patriots defense scored 20.00, his best starter "
        "and a man he signed off the wire this week.", SCALE))
    parts.append(gil(
        "Adam Calvelage wins 137.74 to 95.82. Lamb and Kelce gave him 57.90 between them, within a point of what "
        "Adam Hershberger's entire team scored on Sunday."))
    parts.append(boomer(
        "And he still left 13.74 on the bench, because Brock Purdy went for 28.48 in street clothes as far as this "
        "lineup was concerned. He won by 41 with 28.48 of quarterback sitting down. Some men are just owed."))
    parts.append(gil(
        "Spencer Lentz is 0 and 2 with the ninth seed and the most points allowed in the league, 294.60 against "
        "him in two weeks. Bijan Robinson scored 9.60 against a projection of 21.66."))
    parts.append(boomer(
        "He started 95.9 percent of the points he owned, the third cleanest lineup in the building, and he is still "
        "0 and 2. Tidy is not a result. Bijan Robinson at 9.60 is a result."))

    # ---- 4. won anyway
    w, l = card_rows("Ryan Reed", "Doug Fields")
    parts.append(mcard(
        "m-reed", "Reed wins with 23.20 still on the bench", w, l,
        "Jaxon Smith-Njigba went for 42.00, the biggest single score in this league this week. Jake Ferguson "
        "added 18.30 from the bench, which is where he stayed.", SCALE))
    parts.append(gil(
        "Ryan Reed wins 118.68 to 99.58 in the closest game of the week. Smith-Njigba's 42.00 was 25.74 above his "
        "projection, the largest overperformance by any starter in the league."))
    parts.append(boomer(
        "I said Reed starts Jaxson Dart this week. He started Justin Herbert, who gave him 7.88, and won anyway "
        "because one receiver did the work of three. Wrong call, right result, and neither of us earned it."))
    parts.append(gil(
        "Doug Fields got 25.70 from DeVonta Smith and 23.40 from James Cook III and is 0 and 2. He has scored "
        "196.54 and had 267.80 scored against him."))
    parts.append(boomer(
        "Two weeks, two of the better rosters he could have drawn, two losses. Doug Fields is playing a schedule "
        "somebody else built for a man they do not like."))

    # ---- 5. the league low
    w, l = card_rows("Geoff Cavender", "Adam Hershberger")
    parts.append(mcard(
        "m-cavender", "Cavender beats the lowest score of the week", w, l,
        "Amon-Ra St. Brown 33.70 and Bryce Young 24.08, a quarterback Cavender added off the wire this week. Adam "
        "Hershberger's 58.86 is the lowest score in this league.", SCALE))
    parts.append(gil(
        "Geoff Cavender wins 114.68 to 58.86 and is 2 and 0. Bryce Young, added off the wire, outscored every "
        "player Adam Hershberger started by at least seven and a half points."))
    parts.append(boomer(
        "I had Hershberger beating this man by twenty or more. He lost by 55.82. I want that on the record early, "
        "because I am about to say some things about his week."))
    parts.append(gil(
        "Adam Hershberger scored 58.86 and would have lost to all eleven other teams in this league. Omarion "
        "Hampton led him at 16.50. In fairness, Malik Nabers scored 0.60 against a projection of 12.96 and "
        "Trevor Lawrence 6.16 against 16.72. Nobody builds a roster expecting that."))
    parts.append(boomer(
        "He is 0 and 2 and he has now lost to the entire league on paper in the same week. Then he went to the wire "
        "and made it worse, which takes some doing from 58.86.", "bad"))

    # ---- 6. the benching
    w, l = card_rows("Casey Couture", "Scott Howard")
    parts.append(mcard(
        "m-casey", "Casey goes 2 and 0 while Howard benches 31.06", w, l,
        "Jonathan Taylor 27.20 for Casey Couture. Stefon Diggs put up 19.20 on his bench, and Scott Howard's Dak "
        "Prescott put up 29.76 on his.", SCALE))
    parts.append(gil(
        "Casey Couture wins 94.28 to 71.10 and is 2 and 0. It is the lowest winning score of the week and it left "
        "15.50 behind, including Stefon Diggs at 19.20."))
    parts.append(boomer(
        "I called him 2 and 0 by Sunday night and I will take it, but let us be honest about how. He started "
        "Emeka Egbuka for 8.80 over Diggs for 19.20 and won by 23 anyway. That is five rings worth of luck "
        "showing up on time.", "good"))
    parts.append(gil(
        "Scott Howard scored 71.10 with 102.16 available, and started Lamar Jackson for 14.80 with Dak Prescott "
        "and 29.76 on his bench. TreVeyon Henderson gave him 13.60."))
    parts.append(boomer(
        "Second week running the bench beat the lineup. But I will say this for the man, he had Puka Nacua in "
        "there on a zero and Rashee Rice at 10.30, so it is not as if the roster was handing him anything. "
        "He is 0 and 2 with the fewest points scored in the league, 151.36."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Twelve calls last week. Four of them came in. Eight of them did not, including the one where I put Mama "
        "Beth over her husband and the one where I said Scott Reisert could not reach 120. Four and eight. Read "
        "it yourself, I am not hiding any of them."))
    parts.append(graded_list([
        ("DA The Badenov's", "DA finishes top three in scoring again in Week 2.", "RIGHT",
         "Second at 140.02, behind Scott Reisert only."),
        ("Momma's Boys", "Mama Beth beats DA on Sunday.", "WRONG",
         "She lost by 62.06, the widest game of the week."),
        ("Berlin Blitz", "Ja'Marr Chase goes for 15 or more for Kent Frenger.", "RIGHT",
         "Chase went for 23.00. Frenger lost anyway."),
        ("One Under akaThe Mulligan", "Casey Couture is 2 and 0 by Sunday night.", "RIGHT",
         "He is 2 and 0, by 23.18 over Scott Howard."),
        ("Balls Deep", "Spencer Lentz beats Adam Calvelage by more than thirty.", "WRONG",
         "He lost by 41.92. Wrong direction, right size."),
        ("BearDown", "Ryan Reed starts Jaxson Dart in Week 2.", "WRONG",
         "He started Justin Herbert for 7.88 and won by 19.10."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert does not reach 120 in Week 2 or Week 3.", "WRONG",
         "142.08 in Week 2. Dead on arrival, with a week to spare."),
        ("Cosby Copperheads", "Doug Fields outscores Ryan Reed on Sunday.", "WRONG",
         "99.58 to 118.68."),
        ("Holy Rollers", "Adam Hershberger beats Geoff Cavender by twenty or more.", "WRONG",
         "He lost by 55.82 with the lowest score of the week."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender does not clear 110 in Week 2.", "WRONG",
         "114.68, and 24.08 of it came from a quarterback he added off the wire this week."),
        ("The Scranton Strangler", "Scott Howard scores 120 or more in Week 2.", "WRONG",
         "71.10. I keep picking this man and he keeps handing me the same answer."),
        ("An alBum Cover", "Adam Calvelage clears 100 in Week 2.", "RIGHT",
         "137.74, with 23.60 of it from a tight end."),
    ]))
    parts.append(gil("Four right, eight wrong. Twelve new ones, one per team."))
    parts.append(calls_list([
        ("DA The Badenov's", "DA clears 120 for the third straight week.",
         "140.02 and 156.86 to open the year, with Josh Allen averaging 39.74 across the two. He has left 9.40 "
         "behind all season, the least of anybody in the league."),
        ("Simba St. Gibbs Lion Kings", "Scott Reisert leaves under ten on his bench again in Week 3.",
         "He left nothing at all this week. Through two weeks he has left 14.80 total, all of it in Week 1, and "
         "he draws the team that just scored 58.86."),
        ("Balls Deep", "Spencer Lentz wins his first game of the season.",
         "0 and 2, and tidy is not a result: he started all but 4.10 of the points he owned and lost by 41.92 anyway. "
         "He draws Kent Frenger, who just lost by 42.36."),
        ("Momma's Boys", "Mama Beth leaves under ten on her bench in Week 3.",
         "She left 29.22 behind on Sunday after leaving 3.90 in Week 1. Across her career she has started more of "
         "her available points than anybody in this league. One bad Sunday is not a pattern."),
        ("Berlin Blitz", "Kenneth Walker III goes for 15 or more again for Kent Frenger.",
         "23.80 this week against a projection of 17.31, and 23.00 from Ja'Marr Chase alongside him. Two men over 23 "
         "and he still lost by 42.36."),
        ("One Under akaThe Mulligan", "Casey Couture starts Stefon Diggs in Week 3.",
         "Diggs scored 19.20 on his bench, more than every starter he had except Jonathan Taylor. "
         "The man is 2 and 0 without needing him. Now he knows."),
        ("An alBum Cover", "CeeDee Lamb clears 20 again for Adam Calvelage.",
         "34.30 on Sunday against a projection of 15.84, the third biggest overperformance in the league. Lamb and "
         "Travis Kelce are 57.90 of his 137.74."),
        ("Hawk Tua Tagovailoa", "Geoff Cavender goes 3 and 0.",
         "2 and 0 with the fewest points allowed in the league, 139.12 in two weeks. Amon-Ra St. Brown at 33.70 "
         "and a wire pickup at 24.08 is a roster that is getting better, not lucky."),
        ("BearDown", "Jaxon Smith-Njigba clears 20 again for Ryan Reed.",
         "42.00 on Sunday, the biggest start in the league, and 20.80 from Jaylen Waddle behind him. Reed has scored "
         "108.26 and 118.68 in his two weeks back."),
        ("Cosby Copperheads", "Doug Fields beats Scott Howard on Sunday.",
         "0 and 2, and his 99.58 on Sunday would have beaten five of the ten teams he did not play. "
         "DeVonta Smith and James Cook III gave him 49.10 between them."),
        ("The Scranton Strangler", "Scott Howard starts Dak Prescott in Week 3.",
         "Prescott has put up 29.76 on his bench while Lamar Jackson has started for 14.80. Both are good "
         "quarterbacks. Only one of them is playing for him."),
        ("Holy Rollers", "Adam Hershberger clears 100 for the first time this season.",
         "96.80 and 58.86 to open the year. Chase Brown gave him 9.70 on Sunday and his defense scored 1.00. The "
         "floor is the defense, and the defense is the one thing on this roster he can fix by Sunday."),
    ]))

    # ---- HARDWARE
    hw = hardware(FACTS, SEASON)
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(award(
        "good", "Owner of the Week", "Scott Reisert · Simba St. Gibbs Lion Kings",
        "142.08 scored, 142.08 available. Nothing on his bench could have improved his lineup.",
        "He owned 142.08 worth of football and started every point of it. Nobody in either league did that, and the "
        "call I made that he could not reach 120 died on the way to the podium."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Adam Hershberger · Holy Rollers",
        "58.86 scored with 75.16 available, the lowest score in this league this week.",
        "He would have lost to all eleven other teams. Then he went to the wire, added Tyler Shough, watched him "
        "score 22.38, and dropped him inside the same week for a tight end who got 8.60."))
    parts.append(award(
        "good", "Start of the Week", "Ryan Reed · Jaxon Smith-Njigba, 42.00",
        "The biggest score by any starter in this league, 25.74 above his projection. Josh Allen is second at 40.82, "
        "Davante Adams third at 38.50.",
        "Forty-two points from one receiver. Reed's quarterback gave him 7.88 and he won by 19 anyway. That is not "
        "a lineup, that is a hostage situation with a happy ending."))
    parts.append(award(
        "bad", "Sit of the Week", "Mama Beth · Patrick Mahomes, 31.98 on the bench",
        "She started Jalen Hurts for 16.16. The swing was 15.82 in a game she lost by 62.06.",
        "It did not cost her the game, nothing was going to save that game. It cost her the argument at dinner, "
        "which in that house is the more expensive one."))
    parts.append(award(
        "bad", "Waste of the Week", "Ryan Reed · 23.20 left behind, and he won anyway",
        "The most points left on a bench by any winner this week. 141.88 available, 118.68 started.",
        "Jake Ferguson sat on 18.30 while Harold Fannin Jr. started for 7.90, and the standings will tell him he "
        "had a fine Sunday. Nine other men looked at their own bench today and left less than he did."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "Every point this league leaves on its bench, all twelve of you, all season. Two weeks in, Scott Howard "
        "leads it at 77.06 and it is not close."))
    rows = ledger_rows(FACTS, SEASON)
    parts.append(ledger(rows, 2, season_note=(
        "Season totals are Week 1 and Week 2 added together. Scott Howard leads the league at 77.06, Ryan Reed is "
        "second at 41.84, Geoff Cavender third at 35.98.")))
    parts.append(gil(
        "One of twelve again. Scott Howard left 31.06 and lost by 23.18, so his bench is the only one that "
        "decided a game this week."))
    parts.append(boomer(
        "Two weeks, two convictions, same man. Everybody else in this table wasted points in a week where it did "
        "not matter, which is the same crime with better timing. The ledger keeps both."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move:</strong> Geoff Cavender adding Bryce Young, who scored 24.08, for Isiah Pacheco, who "
        "scored nothing. A 24.08-point swing, the largest in the league, and he started Young the same week."))
    parts.append(gil(
        "<strong>Worst move:</strong> Adam Hershberger dropping the Patriots defense, which scored 20.00, to add "
        "the Chiefs defense, which scored 1.00. A 19.00-point swing against him. Spencer Lentz signed the Patriots "
        "defense the same week and it was his highest scoring starter."))
    parts.append(boomer(
        "Eighteen moves went through. Hershberger made three of them and they cost him 10.40 on net, which is a "
        "special kind of busy. He added Tyler Shough, who scored 22.38, and dropped him inside the same week. He "
        "found the answer and handed it back before it could do him any good.", "bad"))
    parts.append(gil(
        "Mama Beth dropped Tre Tucker, who scored 23.40, to add Rashod Bateman, who scored 18.30 and led her team."))
    parts.append(boomer(
        "Ten of the eighteen came out positive, so this league is better at the wire than it is at the bench, which "
        "is the lowest bar I have ever had to clear on television. Doug Fields made three moves to gain one point "
        "and he is still 0 and 2."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Adam Hershberger at Scott Reisert, Casey Couture at Geoff Cavender, Spencer Lentz at Kent Frenger, Doug "
        "Fields at Scott Howard, Mama Beth at Adam Calvelage, DA at Ryan Reed."))
    parts.append(boomer(
        "DA at Ryan Reed is the game. Two weeks over 140 against the man who just got 42 points out of one "
        "receiver, and whoever loses it has to explain why they are not the best team in this league."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "dlffl", 2, HEADLINE, DEK, build(), META, "dlffl-week-2.png",
        (f"{booth.SITE}/foh/week-2.html", "Friends of Herb, Week 2"),
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wb", "docs", "dlffl", "week-2.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
