"""Friends of Herb, Week 5. Editorial.

Eleven teams, so one bye every week. The Freiermuth Rule lives on this page only.
No joke on this page may repeat one from the Dewart Lake page. Spencer reads both.
Boomer runs at SCORCHING from Week 5 on (Spencer, 2026-10-13).

Outlier engine top items: Aaron Jezioro snapped Bob Dorsch's 13-game streak in the series (headline,
once in 50 seasons), Tyler Shough -0.16 on a 19.70 projection for Dorsch (headline), Pahuja six straight
over Norton (promote), Matt Davis 170.70 is 5th-best of his 240 (promote), Drake Maye 48.46 is the
21st-best start since 2018 (promote). Kelly, Norton and Dorsch (four titles each) are a combined 2 and 11.
No new inbox intel this week.
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

FACTS = load("foh_wk5_facts.json")
SEASON = load("foh_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 172.42

HEADLINE = "Bob Dorsch Had Beaten Aaron Jezioro 13 Straight Times. Then His Quarterback Scored Less Than Zero."
DEK = (
    "Jezioro won 132.36 to 92.44, his first win over Dorsch since 2016, while Tyler Shough scored minus 0.16. "
    "The three owners with four titles apiece are now a combined 2 and 11. Matt Davis scored 170.70 and still "
    "started the wrong quarterback."
)
META = (
    "Gil and Boomer call Week 5 of Friends of Herb: Aaron Jezioro ends Bob Dorsch's 13-game run, Matt Davis "
    "scores 170.70, Ryan Kelly starts a receiver on a bye, and Boomer goes 5 and 6 on his calls."
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

    # ---- 1. the streak ends
    w, l = card_rows("Aaron Jezioro", "Bob Dorsch")
    parts.append(mcard(
        "m-jezioro", "Jezioro ends a 13-game losing run to Dorsch", w, l,
        "Jaylen Warren 38.80, Brock Bowers 21.00 and Brock Purdy 20.16 for Aaron Jezioro, with Trevor Lawrence's "
        "26.74 on his bench. Bob Dorsch's quarterback, Tyler Shough, scored minus 0.16 on a projection of 19.70.",
        SCALE, key=True))
    parts.append(gil(
        "Aaron Jezioro wins 132.36 to 92.44 and is 2 and 2. Bob Dorsch had won their last 13 meetings, every one "
        "since 2017. Jezioro's last win in the series came in 2016. Dorsch still leads it 15 and 6."))
    parts.append(boomer(
        "Thirteen straight, and I picked Bob. I said I was not going to overthink it. Then Bob sent out Tyler "
        "Shough, projected for 19.70, and Shough came back with minus 0.16. Gil, that is not a bad game. That is "
        "an anti-game. Bob would have scored more starting the Gatorade cooler."))
    parts.append(gil(
        "Shough's miss is the 20th-worst by any starter projected for 10 or more in this league since 2018, out "
        "of 6,712. Dorsch had no other quarterback on the roster. In fairness to Bob Dorsch, his best possible "
        "lineup, 111.84, still loses by 20.52."))
    parts.append(boomer(
        "The reigning champion drove into Sunday with one quarterback, like a man who crosses the desert with no "
        "spare tire. And Aaron, nine full seasons without beating this man, and you finally do it by 40 with "
        "your best quarterback on the bench. That is revenge served with one hand in your pocket.", "good"))

    # ---- 2. the high score
    w, l = card_rows("Matt Davis", "Michael Turner")
    parts.append(mcard(
        "m-davis", "Davis 170.70, the high score of the week", w, l,
        "Jahmyr Gibbs 37.20, Joe Burrow 32.60 and Bucky Irving 32.50 for Matt Davis, with Matthew Stafford's "
        "34.32 on his bench. Jayden Daniels gave Michael Turner 34.26.", SCALE))
    parts.append(gil(
        "Matt Davis wins 170.70 to 119.86 and is 4 and 1. It is the fifth-best of his 240 games in this league. "
        "He leads Michael Turner 12 and 11 lifetime."))
    parts.append(boomer(
        "Four straight weeks Matt has had to pick Burrow or Stafford. Week 2 he took Burrow and Stafford scored "
        "35.98 on the bench. Week 3 he took Stafford, Burrow scored more, and he lost by 0.76. Week 4 he took "
        "Burrow, right call. This week Burrow again, and Stafford beat him from the bench by 1.72. One for his last "
        "four, Gil. Matt scored 170 and is still losing a coin toss to himself."))
    parts.append(gil(
        "Michael Turner's 119.86 beats five of the other ten teams, and against the whole league he is 25 and 15 "
        "this season. In the standings he is 1 and 3."))
    parts.append(boomer(
        "Michael Turner is not bad at fantasy football. He is bad at the schedule. He also sat Garrett Wilson's "
        "21.90 for Chris Olave's 6.60, so he is a little bit bad at fantasy football. But mostly the schedule."))

    # ---- 3. the alternating series
    w, l = card_rows("Spencer Lentz", "Aron Rogers")
    parts.append(mcard(
        "m-lentz", "Spencer by 24.02, and the series flips again", w, l,
        "Drake Maye 48.46 and Parker Washington 32.40 for Spencer Lentz, who left 1.10 behind. Jared Goff gave "
        "Aron Rogers 34.94, and CeeDee Lamb gave him 1.90.", SCALE))
    parts.append(gil(
        "Spencer Lentz wins 137.66 to 113.64 and is 3 and 2. Aron Rogers leads the series 10 and 8, and they have "
        "now traded wins for seven straight meetings. Maye's 48.46 is the 21st-best start by any player in this "
        "league since 2018, out of 10,676."))
    parts.append(boomer(
        "Last week Spencer left 55 points on his bench and I took him apart in public. This week he left 1.10. "
        "Spencer, I do not know if you learned something or if somebody hid your phone until kickoff, but keep "
        "the phone hidden."))
    parts.append(gil(
        "Aron Rogers has scored 131.50, 125.20, 121.26, 117.68 and 113.64. Four straight drops. In fairness "
        "to him, Goff's 34.94 is one of the 75 biggest games by a starter in a loss here since 2018."))
    parts.append(boomer(
        "Aron is not having a bad season. He is having a slow leak. About four points a week, every week, like a "
        "tire with a nail in it. And he still has the cleanest bench in the league. Best-kept flat tire you ever "
        "saw."))

    # ---- 4. the bye-week receiver
    w, l = card_rows("Eric Olson", "Ryan Kelly")
    parts.append(mcard(
        "m-olson", "Olson by 73.32 over Kelly, who started a man on bye", w, l,
        "Christian Watson 35.30, Josh Allen 34.50 and 23.00 from his kicker for Eric Olson, who left 21.52 "
        "behind. Ryan Kelly started Rashee Rice, whose Chiefs had the week off.", SCALE))
    parts.append(gil(
        "Eric Olson wins 150.18 to 76.86 and is 3 and 2. He leads Ryan Kelly 4 and 3 lifetime. Kelly is 0 and 4. "
        "Rashee Rice started at receiver and scored nothing because the Chiefs did not play, with Justin "
        "Jefferson's 15.80 on the bench."))
    parts.append(boomer(
        "Ryan started a wide receiver whose team had the day off. Rashee Rice spent Sunday at home and Ryan "
        "put him in the lineup anyway. Ryan, the Chiefs bye was on the schedule. It has been on the schedule "
        "since May. It was printed. People have it on their refrigerators.", "bad"))
    parts.append(gil(
        "Ryan Kelly, Billy Norton and Bob Dorsch have four titles apiece, tied for the most in this league. "
        "Between them they are 2 and 11 this season. In fairness to Kelly, 76.86 is his best score in a game "
        "that counted this year."))
    parts.append(boomer(
        "That is a Hall of Fame wing, Gil, and every one of them is out in the parking lot looking for his car "
        "keys. And Eric, you have told this league you built an AI system on OpenAI to help with your lineup. "
        "You left 21.52 on the bench. I do not know if the robot set that lineup or you did, and I think we both "
        "know which answer you are going to give me."))

    # ---- 5. six straight
    w, l = card_rows("Rahul Pahuja", "Billy Norton")
    parts.append(mcard(
        "m-pahuja", "Pahuja's sixth straight over Norton", w, l,
        "Isaiah Likely 26.90, C.J. Stroud 22.94 and Jaxon Smith-Njigba 22.30 for Rahul Pahuja, who left 0.50 "
        "behind. Billy Norton started three players projected for zero.", SCALE))
    parts.append(gil(
        "Rahul Pahuja wins 130.24 to 67.50 and is 4 and 1. He has beaten Billy Norton six straight times and leads "
        "their series 12 and 10. Norton started Baker Mayfield, Ladd McConkey and DJ Moore, all projected for "
        "zero, and all three scored zero. MarShawn Lloyd scored 16.20 on his bench."))
    parts.append(boomer(
        "Billy named his team after Tom Brady and could not find one quarterback. Last week, on his bye, we "
        "noted he had no quarterback but Mayfield. This week it counted, and he still did not have one. Billy, "
        "the free agent pool is open all week. It is not a museum. You are allowed to touch things."))
    parts.append(gil(
        "In fairness to Billy Norton, Malik Nabers gave him 25.60 and James Cook III 24.30. Rahul Pahuja, for "
        "his part, left half a point on his bench."))
    parts.append(boomer(
        "Half a point left on the bench. Rahul measures twice and cuts once, and he has now cut Billy six "
        "straight times.", "good"))

    # ---- 6. the bye
    t = T["Michael Smith"]
    parts.append(byecard(
        "m-bye", "Smith's bye week: 89.04, and none of it counted",
        {"team": t["name"], "owner": SEASON["owners"]["Michael Smith"]["display"], "score": t["score"], "left": t["left"]},
        "Puka Nacua 31.20, Aaron Jones Sr. 19.20 and Dak Prescott 15.64 for Michael Smith, who had the week "
        "off.", SCALE))
    parts.append(gil(
        "Michael Smith had the bye and scored 89.04. Nothing was at stake. He is 3 and 1 and third in the "
        "standings."))
    parts.append(boomer(
        "I called 110 for Michael on his bye and he scored 89.04. That is two straight weeks I have lost a bet "
        "on a man who was on vacation. The vacationers are "
        "beating me and they are not even trying."))

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "Named for Week 1, when Bob Dorsch sat Pat Freiermuth's 13.10 and lost by 0.46. Do not leave the answer "
        "on your own bench. The test is one swap: a player you sat, for the player you started in his place, "
        "worth more than you lost by. This week nobody failed it."))
    parts.append(gil(
        "Aron Rogers came closest. Jacory Croskey-Merritt for Tony Pollard is worth 9.00, and he lost by 24.02, "
        "15.02 short. Bob Dorsch could not take the test at quarterback at all. There was nobody on his bench to "
        "swap in."))
    parts.append(boomer(
        "Nobody broke the rule because nobody got close enough to break it. The nearest loser came up fifteen "
        "points short of even having an excuse. The bench is innocent, Gil. Arrest the starters."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Eleven calls came due. Five right, six wrong, and one older call still riding. Season record, 16 and 26. I would like "
        "to say I am improving. I am improving the way Aron Rogers is improving. Read them all."))
    parts.append(graded_list([
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Ryan Kelly.", "RIGHT",
         "By 73.32."),
        ("Old Man Smashers", "Ryan Kelly clears 80 in Week 5.", "WRONG",
         "76.86. Jefferson for the man on bye gets him to 92.66 and gets me a win. Ryan, I was rooting for you."),
        ("Balls Deep", "Spencer Lentz starts Drake Maye in Week 5.", "RIGHT",
         "48.46."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers leaves under ten on his bench for the fifth straight week.",
         "WRONG", "13.30, the first time all season he went over ten. The week I bet on it."),
        ("Dallas Dawgs", "Matt Davis clears 120 for the fourth straight week.", "RIGHT",
         "170.70."),
        ("Napoleon's Army", "Michael Turner clears 110 in Week 5.", "RIGHT",
         "119.86, in a loss."),
        ("I Loved You Tom Brady", "Billy Norton clears 90 in Week 5.", "WRONG",
         "67.50, without a quarterback."),
        ("Pack Up", "Rahul Pahuja starts Kyle Monangai in Week 5.", "WRONG",
         "Monangai was projected for zero and scored zero. Rahul was right to sit him and I was wrong to ask."),
        ("| croup", "Aaron Jezioro leaves under fifteen on his bench in Week 5.", "RIGHT",
         "14.98. Two hundredths to spare."),
        ("WPB Steel City", "Bob Dorsch beats Aaron Jezioro.", "WRONG",
         "Lost by 39.92. Thirteen straight, and I picked the Sunday it ended."),
        ("Midget Grinders", "Michael Smith clears 110 on his bye.", "WRONG",
         "89.04. It did not count for him. It counts against me."),
        ("Napoleon's Army", "Michael Turner loses another one by under five points before Halloween.", "OPEN",
         "Lost by 50.84. Not close to close. Still open."),
    ]))
    parts.append(gil(
        "Five right, six wrong, one open. Eleven new ones, with Rahul Pahuja's on the bye. The Bengals, Lions, "
        "Dolphins and Vikings have the week off."))
    parts.append(calls_list([
        ("Midget Grinders", "Michael Smith beats Bob Dorsch.",
         "Dorsch leads 13 and 9 and has won the last five. But Bob just lost a 13-game streak to a quarterback "
         "who scored minus 0.16. Streaks are dropping like flies, Michael. Swat one."),
        ("WPB Steel City", "Bob Dorsch clears 110 in Week 6.",
         "He scored 132.30 and 128.64 the two weeks before Tyler Shough happened. Get a second quarterback, Bob. "
         "They are not rationed."),
        ("I Loved You Tom Brady", "Billy Norton wins his first game, over Matt Davis.",
         "Norton leads that series 11 and 5. Davis is the hottest team in the league and Norton has no "
         "quarterback. I am betting on history and on Billy finding a quarterback before Sunday."),
        ("Dallas Dawgs", "Matt Davis clears 120 for the fifth straight week.",
         "Joe Burrow and Jahmyr Gibbs both have the week off, so Stafford starts by default. Matt cannot pick the "
         "wrong quarterback if there is only one."),
        ("| croup", "Aaron Jezioro beats Eric Olson.",
         "Olson leads 5 and 2, and they have not met since 2014. Aaron just ended a nine-season drought. Olson "
         "has not seen you in twelve years, Aaron. He will not recognize you. Use it."),
        ("Colorado Narcoleptic Kestrels", "Eric Olson leaves under fifteen on his bench in Week 6.",
         "21.52 this week, the most by any winner. Tell the robot, or tell yourself. One of you is listening."),
        ("Napoleon's Army", "Michael Turner beats Spencer Lentz.",
         "Spencer leads 15 and 8. Turner has outscored the league 25 times in 40 tries and has one win to show "
         "for it. The schedule owes this man one."),
        ("Balls Deep", "Spencer Lentz leaves under five on his bench again.",
         "1.10 this week, 55.46 the week before. One clean week is a fluke. Two is a pattern. Three and we stop "
         "hiding his phone."),
        ("Old Man Smashers", "Ryan Kelly wins his first game, over Aron Rogers.",
         "Kelly has won the last six meetings and leads 7 and 6. One thing, Ryan: Justin Jefferson, the man you "
         "benched for a receiver on bye, is on bye this week. Check the list."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers leaves under ten on his bench in Week 6.",
         "Under ten in four of his five weeks, and 31.08 all season, the fewest in the league. Amon-Ra St. "
         "Brown and Jared Goff have the week off, so the bench is going to get a workout."),
        ("Pack Up", "Rahul Pahuja clears 110 on his bye.",
         "I have lost two straight bye-week calls and I swore them off. Then I looked at a man who left half a "
         "point on his bench. Last time, I promise."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(gil(
        "Five trophies, five different owners. Nobody takes two in the same week."))
    parts.append(award(
        "good", "Owner of the Week", "Matt Davis · Dallas Dawgs",
        "170.70, the high score of the week and the fifth-best of his 240 games here. He would have beaten all "
        "ten teams, and he left 1.72 behind.",
        "117, 122, 125, 145, 170. Matt has gone up every single week, like an elevator nobody has shown the stop "
        "button. Matt, do not look for it."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Billy Norton · I Loved You Tom Brady",
        "67.50, the lowest score in the league. Three starters projected for zero, including his only "
        "quarterback. A loss to all ten teams.",
        "Billy started three men who were never going to show up, including his quarterback. That is not a "
        "lineup, Gil. That is a group project. And the one team with the week off scored 89.04. A man on "
        "vacation outscored Billy by 21 and he was not even home."))
    parts.append(award(
        "good", "Start of the Week", "Spencer Lentz · Drake Maye, 48.46",
        "Projected for 22.07, so 26.39 over, the biggest beat by any starter this week, and the 21st-best start by "
        "anyone in this league since 2018.",
        "Last week Maye scored 32 on Spencer's bench. This week Spencer started him and he scored 48. Spencer, "
        "the lesson is not that you are a genius. The lesson is that the man spent a whole week trying to get "
        "your attention."))
    parts.append(award(
        "bad", "Sit of the Week", "Ryan Kelly · Justin Jefferson, 15.80 on the bench",
        "Rashee Rice started in his place and scored nothing, because the Chiefs did not play. No benching cost a "
        "game this week, so, bye weeks aside, it goes by size: Billy Norton's MarShawn Lloyd benching was 0.40 bigger, and Billy "
        "already has a trophy.",
        "Ryan benched the guy who played to start the guy who stayed home. Jefferson scored 15.80 from the "
        "bench, which is the best attendance record on that team."))
    parts.append(award(
        "bad", "Waste of the Week", "Eric Olson · 21.52 left behind, and he won",
        "The most left on a bench by any winner. Ollie Gordon II scored 14.80 and Emeka Egbuka 14.20 there, while "
        "Ashton Jeanty started for 9.20 and Jeremiyah Love for 2.20.",
        "Two men on his bench outscored the two running backs he started by 17.60. Eric won by 73, so it cost him "
        "nothing but this trophy. Hand it to the robot. If it set the lineup, it can carry the hardware."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "Every bench in Friends of Herb, bye weeks included. Rahul Pahuja still leads at 108.40 after leaving half "
        "a point this week. That is dieting by skipping one Tic Tac. Aron Rogers has left the fewest, 31.08, and "
        "13.30 of it came this Sunday."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 5, season_note=(
        "Season totals come from the season ledger through Week 5. Rahul Pahuja leads at 108.40, Aaron Jezioro "
        "is second at 99.50, Spencer Lentz third at 93.48. Aron Rogers has left the fewest, 31.08. A bye week "
        "still counts: the points were on the bench either way.")))
    parts.append(gil(
        "No bench decided a game this week. Spencer Lentz left 1.10, a week after leaving 55.46."))
    parts.append(boomer(
        "Rahul leads the season ledger and left the least of any winner this week. He is a reformed man. He is a "
        "reformed man with 108 points of priors."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move that made a lineup:</strong> Rahul Pahuja adding C.J. Stroud, who started and scored "
        "22.94, for Tre Tucker, who scored 5.50."))
    parts.append(gil(
        "<strong>Worst move:</strong> Rahul Pahuja dropping Jordan Love, who scored 30.28, to add Brian Robinson "
        "Jr., who scored 1.60 on his bench. A 28.68-point swing, the biggest against anyone this week."))
    parts.append(boomer(
        "Best move and worst move, same man, same week. Rahul hired a quarterback and fired a better one in the "
        "same interview, and the one he fired scored 30."))
    parts.append(gil(
        "Ten moves went through. Bob Dorsch made three of them, including Roman Wilson, who started and scored "
        "zero, in for Tyreek Hill, who scored zero."))
    parts.append(boomer(
        "Bob swapped a zero for a zero and started the new zero. Honest work. Nobody can say the man does not "
        "know what he wants."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Michael Smith at Bob Dorsch, Billy Norton at Matt Davis, Aaron Jezioro at Eric Olson, Michael Turner at "
        "Spencer Lentz, and Ryan Kelly at Aron Rogers. Rahul Pahuja has the bye."))
    parts.append(boomer(
        "Norton at Davis is the one. The hottest team in the league against a man with no quarterback, and Billy "
        "leads the series 11 and 5. History says Billy. I took Billy. I have a type, Gil, and the type is lost "
        "causes."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 5, HEADLINE, DEK, build(), META, "foh-week-5.png", nav=NAV,
        published="2026-10-13T11:15:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "week-5.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
