"""Friends of Herb, Week 4. Editorial.

Eleven teams, so one bye every week. The Freiermuth Rule lives on this page only.
No joke on this page may repeat one from the Dewart Lake page. Spencer reads both.

Pays off Week 3's closing call: Eric Olson's OpenAI agent picked Spencer Lentz to beat him
(Olson told the group chat, Weekly Booth Inbox, 2026-09-28) and Boomer took Olson.
Outlier engine top items: Spencer Lentz left 55.46 on the bench, 8th-most since 2018 (promote);
Rahul Pahuja leads Michael Turner 14-5 (promote). No new inbox intel this week.
"""
import os

import booth
from booth import award, boomer, byecard, calls_list, gil, graded_list, jump, ledger, mcard
from compute import by_owner, ledger_rows, load

NAV = (
    '<nav class="nav" aria-label="Sections"><ul>'
    '<li><a href="#board">The Scoreboard</a></li>'
    '<li><a href="#freiermuth">The Freiermuth Rule</a></li>'
    '<li><a href="#calls">On The Record</a></li>'
    '<li><a href="#hardware">The Hardware</a></li>'
    '<li><a href="#ledger">The Bench Ledger</a></li>'
    '<li><a href="#wire">The Waiver Wire</a></li>'
    '<li><a href="#next">Next Sunday</a></li></ul></nav>'
)

FACTS = load("foh_wk4_facts.json")
SEASON = load("foh_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 199.96

HEADLINE = "Eric Olson's Robot Told Him He Would Lose. He Lost By 57."
DEK = (
    "Olson's homemade OpenAI agent picked Spencer Lentz to beat him in Week 4, and Olson told the group chat. "
    "Spencer won 144.50 to 87.02. The five players on Spencer's bench outscored Olson's nine starters, 110.38 to "
    "87.02. Boomer had picked Olson."
)
META = (
    "Gil and Boomer call Week 4 of Friends of Herb: Eric Olson's robot correctly predicted his 57-point loss, "
    "Matt Davis handed Aron Rogers his first defeat, and Michael Turner lost by 5.08 with a perfect lineup."
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

    # ---- 1. the robot was right
    w, l = card_rows("Spencer Lentz", "Eric Olson")
    parts.append(mcard(
        "m-lentz", "Spencer by 57.48, as Olson's robot predicted", w, l,
        "Kenneth Walker III 32.40, Nico Collins 29.30 and Chuba Hubbard 27.40 for Spencer Lentz, with 55.46 left "
        "behind. Josh Allen led Eric Olson at 20.52.", SCALE, key=True))
    parts.append(gil(
        "Spencer Lentz wins 144.50 to 87.02. A week ago Eric Olson told the group chat that the agent he built "
        "on OpenAI was already picking Spencer to beat him. It was their first meeting since 2014, and Spencer "
        "now leads the series 4 and 3."))
    parts.append(boomer(
        "The robot said Spencer. I said Olson. Final margin, 57.48. I did not lose a call, Gil, I got run over by one. This booth is written with Claude. Last week Claude talked Matt Davis out of Joe Burrow and he lost by 0.76. This week Olson's OpenAI robot out-picked me by 57. That is OpenAI two, us nothing. Eric's robot beat me and it beat Eric, in the same game."))
    parts.append(gil(
        "Spencer left 55.46 on his bench, which is how much better his best possible lineup was than the one he set. Only seven benches in this league since 2018 have left more. Drake Maye scored 32.16 there, Javonte Williams 28.80 and Tee Higgins 23.20. Add up everyone he sat and it comes to 110.38. Olson's entire starting lineup scored 87.02."))
    parts.append(boomer(
        "Read that again slowly. Five men who were told to sit down beat nine men who were told to play, by 23. "
        "Spencer could have started his bench, gone to lunch, and still won. Eric built a machine smart enough to "
        "see this coming and it still could not find him a tight end. Trey McBride, 6.60.", "bad"))
    parts.append(gil(
        "In fairness to Eric Olson, there was no lineup that saved him. He had 100.02 available, which loses by 44, and his agent told him so in advance. As "
        "forecasting goes, that is a very good robot."))

    # ---- 2. the last unbeaten
    w, l = card_rows("Matt Davis", "Aron Rogers")
    parts.append(mcard(
        "m-davis", "Davis hands Rogers his first loss", w, l,
        "Tetairoa McMillan 40.20, Kyren Williams 31.70 and Joe Burrow 26.72 for Matt Davis, the high score of the "
        "week. Aron Rogers got 34.80 from CeeDee Lamb and nobody in Friends of Herb is unbeaten anymore.", SCALE))
    parts.append(gil(
        "Matt Davis wins 145.02 to 117.68 and is 3 and 1. He has beaten Aron Rogers three straight, and Rogers "
        "still leads that series 11 and 10. Last week Davis sat Joe Burrow and lost by 0.76. This week Burrow "
        "started and outscored Matthew Stafford, on the bench, by 16.04."))
    parts.append(boomer(
        "I asked for Joe Burrow and Matt gave me Joe Burrow, 26.72. Terry McLaurin was projected for zero and delivered every bit of it. Matt scored 145 playing eight on nine.", "good"))
    parts.append(gil(
        "Aron Rogers left 7.00 behind and had the fifth-best score in the league. He has left 17.78 on his bench all season, the fewest in Friends of Herb."))
    parts.append(boomer(
        "Aron did nothing wrong. Clean lineup, 34.80 from his best player, and he ran into a receiver who went for 40. I had him at 4 and 0. He left 7.00 on his bench and lost by 27.34. There is no lineup fix for that."))

    # ---- 3. the five-point game
    w, l = card_rows("Rahul Pahuja", "Michael Turner")
    parts.append(mcard(
        "m-pahuja", "Pahuja by 5.08, now 14 and 5 over Turner", w, l,
        "Bryce Young 26.46 for Rahul Pahuja, who won with Kyle Monangai's 29.50 on his bench. Michael Turner turned in his best possible lineup and lost.", SCALE))
    parts.append(gil(
        "Rahul Pahuja wins 99.06 to 93.98 and is 3 and 1. He has won 14 of his 19 meetings with Michael Turner. A fair coin does something that lopsided about once in 16 tries. Turner turned in a "
        "perfect lineup, which happens in about 11% of team-weeks in this league since 2018, and lost anyway."))
    parts.append(boomer(
        "Michael Turner's bench was Jayden Daniels, Breece Hall, Dallas Goedert and Alec Pierce, and they scored "
        "zero, combined. Garrett Wilson added 4.20. There was nothing back there to find. He set the best lineup he had, and the best lineup he had was 93.98. And Michael, about that margin. I will see you in On The Record. Bring something to bite down on."))
    parts.append(gil(
        "Pahuja has now played three games decided by about five points or less and won two of them. He started David "
        "Montgomery for 4.30. With Monangai in that spot he wins by 30.28."))
    parts.append(boomer(
        "Two weeks running, Rahul and Kyle Monangai have been in the wrong room. Last week he started him on "
        "Monday night for 3.10 and lost. So he sat him. Twenty-nine and a half. Rahul, the man is not bad. He is "
        "just allergic to your lineup."))

    # ---- 4. the wide one
    w, l = card_rows("Bob Dorsch", "Ryan Kelly")
    parts.append(mcard(
        "m-dorsch", "Dorsch by 60.86, his fourth straight over Kelly", w, l,
        "Bijan Robinson 29.20 and Zay Flowers 23.80 for Bob Dorsch. Emanuel Wilson, added off the wire this "
        "week, led Ryan Kelly at 25.50.", SCALE))
    parts.append(gil(
        "Bob Dorsch wins 128.64 to 67.78, the widest game of the week. He leads the series 15 and 11. Saquon Barkley started for 1.50 with Rhamondre "
        "Stevenson at 16.90 behind him."))
    parts.append(boomer(
        "Two weeks ago I said Saquon Barkley does not score 2.50 twice. I was right. He scored 1.50. Bob left "
        "20.30 on his bench after I called under five, and he won by 60 anyway. Bob is the reigning champion, and that is the privilege. You get to be sloppy when the other fella scores 67."))
    parts.append(gil(
        "In fairness to Ryan Kelly, 67.78 is his best score in a game that counted this season, up 13.26 from "
        "last week. He added Emanuel Wilson, started him, and got 25.50. Rashee Rice started and did not "
        "score against a projection of 12.55, and three of his bench players, Justin Jefferson, Josh Jacobs and Caleb Williams, carried no projection at all."))
    parts.append(boomer(
        "Last week he was improving two points a week and I had him clearing 100 around Week 26. He just "
        "improved thirteen. New math says Week 7. Ryan, that is the single biggest upgrade to a forecast I have "
        "ever issued, and I issued it to a man who lost by 60."))

    # ---- 5. the clean one
    w, l = card_rows("Michael Smith", "Aaron Jezioro")
    parts.append(mcard(
        "m-smith", "Smith's third straight, with a tenth of a point wasted", w, l,
        "Puka Nacua 25.20, Jonathan Taylor 22.20 and Dak Prescott 21.10 for Michael Smith. Aaron Jezioro got "
        "23.62 from Brock Purdy and started a flex who scored nothing.", SCALE))
    parts.append(gil(
        "Michael Smith wins 129.30 to 115.12 and is 3 and 1. He leads the series with Aaron Jezioro 15 and 9. "
        "After a perfect lineup last week he left 0.10 behind this week: Jake Ferguson scored 2.60 on his "
        "bench and Travis Kelce 2.50 in the lineup."))
    parts.append(boomer(
        "A tenth of a point. In two weeks Michael Smith has misplaced one tenth of one point, and it was the "
        "difference between two tight ends who were both having a terrible afternoon. That is not a mistake. "
        "That is a rounding error with a helmet on.", "good"))
    parts.append(gil(
        "Aaron Jezioro started Brock Purdy, as called, for 23.62. He also started Jalen Coker at flex. Coker was "
        "projected for zero and scored zero, with Tucker Kraft at 13.50, Rome Odunze at 12.40, Denzel Boston at "
        "10.90 and Khalil Shakir at 9.70 all on the bench. He lost by 14.18. In fairness to Aaron Jezioro, 115.12 was the sixth-best score in an eleven-team league, and Brock Purdy was the right call."))
    parts.append(boomer(
        "Four men on that bench with a pulse and a projection, and Aaron went with the one guy the computer "
        "said would score nothing. The computer was right. It has been a very good week for computers and a "
        "very bad one for the people ignoring them."))

    # ---- 6. the bye
    t = T["Billy Norton"]
    parts.append(byecard(
        "m-bye", "Norton's bye week: 66.00, and none of it counted",
        {"team": t["name"], "owner": SEASON["owners"]["Billy Norton"]["display"], "score": t["score"], "left": t["left"]},
        "Malik Nabers 22.20, James Cook III 15.30 and 14.00 from his kicker. RJ Harvey scored 14.30 on the bench.", SCALE))
    parts.append(gil(
        "Billy Norton had the bye and scored 66.00 with 86.30 available. His quarterback, Baker Mayfield, carried a projection of zero, and there was no other quarterback on the roster. Nothing was at stake this week."))
    parts.append(boomer(
        "I called 100 for Billy on the bye. He scored 66.00. Nobody was looking, Billy, and that includes me. It did not count. Sunday does."))

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "Named for Week 1, when Bob Dorsch sat Pat Freiermuth's 13.10 and lost by 0.46. Do not leave the answer "
        "on your own bench. The test is one swap: a player you sat, for the player you started in his place, "
        "worth more than you lost by. This week nobody failed it."))
    parts.append(gil(
        "Aaron Jezioro came closest. Tucker Kraft for Jalen Coker is worth 13.50, and he lost by 14.18. He "
        "passed by 0.68. Four winners sat bigger answers than that and got away with it: Rahul Pahuja with Monangai, Spencer Lentz with Tee Higgins, Matt Davis with Jameson Williams, and Bob Dorsch with Stevenson."))
    parts.append(boomer(
        "Nobody broke the rule, and that is not the same as everybody following it. Four of you sat the answer and won anyway. Aaron sat his, lost, and stayed legal by 0.68. One swap does not get him there. Two do, and that is a different section."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Eleven calls came due. Four came in. Seven did not. I am 11 and 20 on the season, and the one call I "
        "still have open just missed by eight hundredths of a point. Read on. I had to."))
    parts.append(graded_list([
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Spencer Lentz. The robot says Spencer.", "WRONG",
         "Lost by 57.48. The robot says hello."),
        ("Balls Deep", "Spencer Lentz scores 120 or more in Week 4.", "RIGHT",
         "144.50."),
        ("Dallas Dawgs", "Matt Davis starts Joe Burrow in Week 4.", "RIGHT",
         "26.72, and the high score of the week."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers goes 4 and 0.", "WRONG",
         "Lost by 27.34 to that same Matt Davis. I talked one man into his quarterback and it beat my other pick."),
        ("Old Man Smashers", "Ryan Kelly clears 100 in Week 4.", "WRONG",
         "67.78. Closer than last time."),
        ("WPB Steel City", "Bob Dorsch leaves under five on his bench again.", "WRONG",
         "20.30, most of it Rhamondre Stevenson."),
        ("Pack Up", "Rahul Pahuja starts Harold Fannin Jr. in Week 4.", "WRONG",
         "He started Isaiah Likely again. Likely scored 10.10 and Fannin 10.20. He ignored me and it cost him a tenth."),
        ("Napoleon's Army", "Michael Turner clears 120 again.", "WRONG",
         "93.98, and there was no better lineup on the roster."),
        ("Midget Grinders", "Michael Smith beats Aaron Jezioro.", "RIGHT",
         "By 14.18."),
        ("| croup", "Aaron Jezioro starts Brock Purdy in Week 4.", "RIGHT",
         "23.62. Right quarterback."),
        ("I Loved You Tom Brady", "Billy Norton clears 100 on his bye.", "WRONG",
         "66.00. It did not count for him. It counts against me."),
        ("Napoleon's Army", "Michael Turner loses another one by under five points before Halloween.", "OPEN",
         "He lost by 5.08. Eight hundredths over the line. The call is still open, and I am not well."),
    ]))
    parts.append(gil(
        "Four right, seven wrong, one open. Eleven new ones, with Michael Smith's on the bye. Michael Turner's "
        "standing call stays on the board."))
    parts.append(calls_list([
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Ryan Kelly.",
         "I picked Olson against his own robot and lost by 57. I am picking him again. They are 3 and 3 lifetime "
         "and last met in 2014. Eric, ask the machine. If it says Kelly, do not tell me."),
        ("Old Man Smashers", "Ryan Kelly clears 80 in Week 5.",
         "52.52, 54.52, 67.78. Emanuel Wilson gave him 25.50 and that is a "
         "real player now."),
        ("Balls Deep", "Spencer Lentz starts Drake Maye in Week 5.",
         "Mahomes is on his bye, which leaves two quarterbacks and one chair. Maye scored 32.16 on the bench and Jalen Hurts 17.52. Last week I gave him the business for adding Maye at all. He was right about the "
         "player and wrong about the chair."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers leaves under ten on his bench for the fifth straight week.",
         "2.00, 3.70, 5.08, 7.00. Nobody in this league wastes less. He leads Spencer 10 and 7 lifetime."),
        ("Dallas Dawgs", "Matt Davis clears 120 for the fourth straight week.",
         "122.18, 125.20, 145.02. Up every week, with one receiver slot he fills without looking."),
        ("Napoleon's Army", "Michael Turner clears 110 in Week 5.",
         "131.16, 85.60, 138.24, 93.98. He goes up, he goes down. This is an up week. He and Davis are 11 and 11 "
         "lifetime."),
        ("I Loved You Tom Brady", "Billy Norton clears 90 in Week 5.",
         "66.48 and 66.00 the last two weeks, but 108.84 and 93.18 before that. Malik Nabers just gave him 22.20. The number is in there."),
        ("Pack Up", "Rahul Pahuja starts Kyle Monangai in Week 5.",
         "Sat him for 21.40, started him for 6.80 and 3.10, sat him for 29.50. Four weeks, wrong room every time. Put him in, Rahul, and find out which one he is."),
        ("| croup", "Aaron Jezioro leaves under fifteen on his bench in Week 5.",
         "26.82, 32.00 and 21.70 the last three weeks. He scored 115.12 anyway. The points are there."),
        ("WPB Steel City", "Bob Dorsch beats Aaron Jezioro.",
         "He leads the series 15 and 5 and has won the last thirteen. I am not going to overthink it."),
        ("Midget Grinders", "Michael Smith clears 110 on his bye.",
         "122.66, 109.64, 129.30. He left a tenth of a point behind in two weeks. If anyone sets a lineup with "
         "nobody watching, it is this man."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(award(
        "good", "Owner of the Week", "Michael Smith · Midget Grinders",
        "129.30 with 0.10 left behind, a week after a perfect lineup, and his third straight win. Two teams outscored him this week and left 87.76 on their benches between them.",
        "He started 0 and 1 with a 94 and nobody noticed him. Since then he is 3 and 0, and in the last two weeks he has left a tenth of a point behind. Michael Smith is the quiet fella at the end of the bar who turns out to own the bar."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Aaron Jezioro · | croup",
        "Started a flex projected for zero, who scored zero, with four usable receivers and tight ends behind "
        "him. He left 21.70 on the bench and lost by 14.18.",
        "Kraft plus Odunze covers that loss with room to spare. Aaron scored 115.12, which is a good team. It "
        "is a good team being driven with the parking brake on."))
    parts.append(award(
        "good", "Start of the Week", "Matt Davis · Tetairoa McMillan, 40.20",
        "26.11 over a projection of 14.09. No starter in Friends of Herb beat his number by more.",
        "Last week Gil pointed out that Matt started this same man for 2.70. Matt started him again. That is either faith or stubbornness, and at 40.20 nobody is going to ask which."))
    parts.append(award(
        "bad", "Sit of the Week", "Rahul Pahuja · Kyle Monangai, 29.50 on the bench",
        "David Montgomery started in his place for 4.30, a swing of 25.20, the biggest single benching in the "
        "league. Pahuja won by 5.08.",
        "He benched 29.50 and won by 5.08. Rahul leads this league in points left behind and is 3 and 1. Four weeks, four different men on his bench with 20 or more: Likely, Tucker, Fannin, Monangai. He keeps hiding them and he keeps winning."))
    parts.append(award(
        "bad", "Waste of the Week", "Spencer Lentz · 55.46 left behind in a 57.48 win",
        "The most points left on a bench by any winner, and the eighth-most by anyone in this league since "
        "2018. He started Kenyon Sadiq at tight end, a pickup this week who did not score, with Colston Loveland at 8.70 behind him.",
        "Three quarterbacks on the roster. He started the one who scored 21.00 and sat the one who scored 32.16. The third one scored 17.52 and at least had the manners to be the wrong answer. He had 199.96 available, Gil. Two hundred points. "
        "Spencer looked at 200 and said no thank you, 144 is plenty."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "Every bench in Friends of Herb, bye weeks included. Rahul Pahuja still leads it at 107.90. Spencer Lentz left more on his bench this Sunday than in the first three weeks combined, and he is second."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 4, season_note=(
        "Season totals come from the season ledger through Week 4. Rahul Pahuja leads at 107.90, Spencer Lentz "
        "is second at 92.38, Aaron Jezioro third at 84.52. Aron Rogers has left the fewest, 17.78. A bye week "
        "still counts: the points were on the bench either way.")))
    parts.append(gil(
        "One bench decided a game this week. Aaron Jezioro left 21.70 and lost by 14.18. Michael Turner is the "
        "only owner who left nothing, and Michael Smith left a tenth of a point."))
    parts.append(boomer(
        "Four winners left 20 or more on the bench this week. Spencer, Davis, Rahul, Dorsch. A hundred and thirty-four points on the floor between them and not one loss. I have been preaching clean lineups for a month and the congregation just skipped church and won anyway. Do not learn from this."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move:</strong> Ryan Kelly adding Emanuel Wilson, who scored 25.50, for De'Von Achane, who "
        "did not score. A 25.50-point swing, he started him, and Wilson was his top scorer by 14."))
    parts.append(gil(
        "<strong>Worst move:</strong> Bob Dorsch dropping Devaughn Vele, who scored 14.40, to add Tyreek Hill, "
        "who did not score. A 14.40-point swing against him."))
    parts.append(boomer(
        "Ryan Kelly made the best move in the league and lost by 60.86. Emanuel Wilson scored 25.50 and the other eight starters managed 42.28 between them. Ryan, you found one man who showed up. Now find eight more."))
    parts.append(gil(
        "Fourteen moves went through. Bob Dorsch made three of them, down from eight last week. Eric Olson "
        "added Ollie Gordon II, who scored 19.00 on his bench."))
    parts.append(boomer(
        "Olson went and got a running back who scored 19 and then sat him behind one who scored 6. The robot "
        "can predict the loss, Eric. Somebody still has to read it the lineup."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Rahul Pahuja at Billy Norton, Bob Dorsch at Aaron Jezioro, Matt Davis at Michael Turner, Eric Olson at "
        "Ryan Kelly, and Spencer Lentz at Aron Rogers. Michael Smith has the bye."))
    parts.append(boomer(
        "Spencer at Rogers is the game. Rogers leads it 10 and 7, and they have traded wins for six straight "
        "meetings. Rogers took the last one, so the pattern says Spencer. The cleanest bench in the league "
        "against a man who just left 55 on his. If Spencer starts the right quarterback this time, look out. If "
        "he does not, I will see you in the Waste of the Week."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 4, HEADLINE, DEK, build(), META, "foh-week-4.png", nav=NAV,
        published="2026-10-06T09:00:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "week-4.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
