"""Friends of Herb, Week 3. Editorial.

Eleven teams, so one bye every week. The Freiermuth Rule lives on this page only.
No joke on this page may repeat one from the Dewart Lake page, or from the Week 3
Monday Night Special (foh/mnf-week-3.html). Spencer reads all of them.

Pays off the MNF Special: which robot, which call, and the robot's Week 4 pick.
Intel (Drive, Weekly Booth Inbox): Davis said Claude recommended the quarterback switch;
Olson's OpenAI agent made his Tuten call. Tuten 16.00 started, Etienne 8.00 benched, Swift 9.80,
Monangai 3.10, all re-verified against ESPN 2026-09-29.
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

FACTS = load("foh_wk3_facts.json")
SEASON = load("foh_season.json")
T = by_owner(FACTS)
SCALE = max(t["score"] + t["left"] for t in FACTS["perTeam"])  # 143.98

HEADLINE = "Matt Davis Asked A Robot Who To Start And Lost By 0.76"
DEK = (
    "The robot was Claude. It told him to switch quarterbacks, he started Matthew Stafford for 25.90, and Joe "
    "Burrow scored 28.58 on his bench. Eric Olson, whose homemade OpenAI agent made his call at running back, won "
    "125.96 to 125.20."
)
META = (
    "Gil and Boomer call Week 3 of Friends of Herb: Matt Davis took a robot's advice and lost by 0.76, Aron Rogers "
    "is 3 and 0, and Eric Olson's own robot has already picked his Week 4 game."
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

    # ---- 1. the robots
    w, l = card_rows("Eric Olson", "Matt Davis")
    parts.append(mcard(
        "m-olson", "Olson's robot beats Davis's robot by 0.76", w, l,
        "Jeremiyah Love 19.40 and Bhayshul Tuten 16.00 for Eric Olson. Matt Davis got 37.90 from Jahmyr Gibbs, "
        "had Joe Burrow's 28.58 on his bench, and lost the 22nd-closest game this league has played since 2011.", SCALE, key=True))
    parts.append(gil(
        "Eric Olson wins 125.96 to 125.20. Matt Davis told the group chat himself that Claude recommended the "
        "switch at quarterback. He started Matthew Stafford for 25.90. Burrow alone, in Stafford's place, wins "
        "Davis the game by 1.92."))
    parts.append(boomer(
        "I promised you on Monday we would find out whose robot it was. Gil. Tell them who we work for."))
    parts.append(gil(
        "This booth is written with Claude."))
    parts.append(boomer(
        "Same company. Same robot. The thing that cost Matt Davis this game is, technically, our boss. We "
        "reached out for comment and it said it would be happy to help.", "bad"))
    parts.append(gil(
        "Olson built his own agent on OpenAI. It made a call on Bhayshul Tuten, and Olson says it was right. Tuten "
        "started and scored 16.00, with Travis Etienne Jr. at 8.00 on the bench. Start Etienne instead and Olson loses "
        "by 7.24. Davis "
        "also started Tetairoa McMillan for 2.70 with Terry McLaurin's 16.70 on his bench. That one was all him, "
        "and it would have won the game too. The robot got one wrong, and so did the man."))
    parts.append(boomer(
        "So the scoreboard reads OpenAI one, Claude nothing, and this booth would like to formally apologize to "
        "Matt Davis on behalf of the family. Olson leads this series 8 and 1 lifetime, by the way. He was beating Matt Davis before either of "
        "these robots was born.", "good"))
    parts.append(gil(
        "In fairness to Matt Davis, 125.20 would have beaten seven of the other ten teams this week, and Jahmyr "
        "Gibbs's 37.90 is the 41st-most any starter has scored in a loss in this league since 2018. Most weeks, "
        "that wins."))

    # ---- 2. Monday night
    w, l = card_rows("Aron Rogers", "Rahul Pahuja")
    parts.append(mcard(
        "m-rogers", "Rogers is the last unbeaten team", w, l,
        "Aron Rogers had D'Andre Swift, 9.80 on Monday night. Rahul Pahuja had Kyle Monangai, 3.10. Two Chicago "
        "running backs, one footrace, decided by 6.70.", SCALE))
    parts.append(gil(
        "Aron Rogers wins 121.26 to 119.14 and is the only 3 and 0 team in Friends of Herb. He now leads the series "
        "with Rahul Pahuja 11 and 5. Jared Goff, added off the wire this week, started and scored 23.36."))
    parts.append(boomer(
        "He added two quarterbacks in one week, Goff and Bo Nix, like a man who could not pick a tie and "
        "wore both. He started Goff. Nix scored 28.14 sitting down. Still won. When you are "
        "3 and 0 even your mistakes pull their weight."))
    parts.append(gil(
        "Rahul Pahuja won his Week 1 game by 0.46 and lost this one by 2.12. Jaxon Smith-Njigba gave him 32.36 "
        "and Jordan Love 23.48."))
    parts.append(boomer(
        "Rahul, there was a tight end on your bench who covers this one more than eight times over. Hold that thought, Gil "
        "has a whole section on it."))
    parts.append(gil(
        "In fairness to Rahul Pahuja, 119.14 would have beaten five of the other ten teams this week, and he led "
        "going into Monday night."))

    # ---- 3. the clean one
    w, l = card_rows("Bob Dorsch", "Spencer Lentz")
    parts.append(mcard(
        "m-dorsch", "Dorsch turns in a perfect lineup", w, l,
        "Bijan Robinson 36.30 and Tyler Shough 31.80, a quarterback Bob Dorsch added off the wire this week. "
        "Bob Dorsch's bench had nothing better to offer.", SCALE))
    parts.append(gil(
        "Bob Dorsch wins 132.30 to 117.24 and leads his lifetime series with Spencer Lentz 19 and 8. He started every "
        "point he had available, one of two perfect lineups in the league this week."))
    parts.append(boomer(
        "Last week I said Saquon Barkley does not score 2.50 twice. He scored 8.50, and Bob did not need a single "
        "one of them. I also said Spencer wins this game. Bob Dorsch is the reigning champion, and he has decided the season has started.",
        "good"))
    parts.append(gil(
        "Spencer Lentz is 1 and 2 with 392.92 points, the most in the league. Derrick Henry gave him 21.40 and "
        "Kenneth Walker III 20.30. He left 4.30 behind."))
    parts.append(boomer(
        "Most points in the league and a losing record, and I am not calling that bad luck, because he also cut "
        "the wrong quarterback this week. We will get to it. I am not letting that go."))

    # ---- 4. the widest
    w, l = card_rows("Michael Turner", "Billy Norton")
    parts.append(mcard(
        "m-turner", "Turner's first win is the widest of the week", w, l,
        "Drake London 25.90, Lamar Jackson 24.44 and Garrett Wilson 23.70. The margin, 71.76, is the 56th-biggest "
        "this league has seen since 2011.", SCALE))
    parts.append(gil(
        "Michael Turner wins 138.24 to 66.48, the highest score in the league this week, and gets his first win. "
        "He left 2.00 behind, with Davante Adams at 19.20 on his bench and Chris Olave starting for 17.20."))
    parts.append(boomer(
        "Last week he benched Adams for 37 on his bye. This week he benched Adams again, and it cost him two points. "
        "That is growth, Gil. That is a man learning to make his mistakes smaller.", "good"))
    parts.append(gil(
        "Billy Norton is 0 and 3 and has had 408.30 points scored against him, the most in the league. James Cook "
        "III led him at 21.40. Jadarian Price started and scored 0.70 against a projection of 11.58."))
    parts.append(boomer(
        "Billy Norton has four championships, tied for the most this league has ever handed out, so I am going to "
        "be respectful. Billy. What in the world is a Jadarian Price and why did you let it near your lineup."))

    # ---- 5. the floor
    w, l = card_rows("Michael Smith", "Ryan Kelly")
    parts.append(mcard(
        "m-smith", "Smith wins with nothing left behind", w, l,
        "Dak Prescott 20.94 and Deebo Samuel Sr. 18.40 for Michael Smith, and 16.00 from his kicker. Ryan Kelly's "
        "54.52 is the 23rd-lowest score this league has seen since 2011.", SCALE))
    parts.append(gil(
        "Michael Smith wins 109.64 to 54.52 with a perfect lineup, the second in the league this week, and is 2 "
        "and 1. His kicker, Harrison Mevis, outscored every player Ryan Kelly started."))
    parts.append(boomer(
        "Michael Smith started every point he owned and his kicker scored 16. Some weeks you win with a haymaker. "
        "He won with a clipboard.", "good"))
    parts.append(gil(
        "Ryan Kelly has the two lowest scores in Friends of Herb this season, 52.52 last week and 54.52 this "
        "week. In fairness, De'Von Achane gave him 1.70 against a projection of 18.00. Kyle Pitts Sr. gave him 1.00."))
    parts.append(boomer(
        "Two points better than last week. I want to be encouraging. At two points a week he clears 100 in about "
        "Week 26, and the regular season has fourteen. I picked him to do it this week anyway. Somebody has to."))

    # ---- 6. the bye
    t = T["Aaron Jezioro"]
    parts.append(byecard(
        "m-bye", "Jezioro's bye week, and 32.00 on the bench",
        {"team": t["name"], "owner": SEASON["owners"]["Aaron Jezioro"]["display"], "score": t["score"], "left": t["left"]},
        "Brock Purdy started and scored 39.28. Brock Bowers scored 24.60 on the bench while Jalen Coker started "
        "for 2.80, and Trevor Lawrence put up 25.78 as his backup.", SCALE))
    parts.append(gil(
        "Aaron Jezioro had the bye. He scored 109.08 with 141.08 available, the most points left on any bench "
        "this week. For the second week running the biggest single benching in the league came from the team "
        "with no opponent."))
    parts.append(boomer(
        "I asked this man to start Brock Purdy in Week 4. He started him in Week 3, on the bye, for 39.28, the "
        "one week it did not count. Aaron, that is not listening to me. That is listening to me on the wrong day."))

    # ---- FREIERMUTH RULE
    parts.append('<h2 id="freiermuth">The Freiermuth Rule</h2>')
    parts.append(gil(
        "Named for Week 1, when Bob Dorsch sat Pat Freiermuth's 13.10 and lost by 0.46. Do not leave the answer "
        "on your own bench. Two men lost this week by less than the gap between a player they sat and the one they started in his place."))
    parts.append(gil(
        "Rahul Pahuja started Isaiah Likely at tight end for 2.30 with Harold Fannin Jr. and 20.60 on his bench. "
        "He lost by 2.12. Matt Davis sat Joe Burrow's 28.58 and Terry McLaurin's 16.70 and lost by 0.76. Either "
        "one of Davis's benchings, reversed, wins his game."))
    parts.append(boomer(
        "Rahul lost to a Bears running back on Monday night and everybody will tell you it was Swift. It was not "
        "Swift. It was a 20-point tight end sitting three feet from him the entire game. Davis at least had a robot "
        "to blame. Rahul did this with his own two thumbs."))

    # ---- ON THE RECORD
    parts.append('<h2 id="calls">On The Record</h2>')
    parts.append(boomer(
        "Ten calls came due. Three came in. Seven did not. I am 7 and 13 on the season and I have two still open, "
        "and yes, I can hear the robots laughing."))
    parts.append(graded_list([
        ("Pack Up", "Rahul Pahuja makes it three straight wins.", "WRONG",
         "Lost by 2.12 on Monday night."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers leaves under ten behind again in Week 3.", "RIGHT",
         "5.08, and he is 3 and 0."),
        ("Dallas Dawgs", "Matt Davis gets a receiver into his top three scorers in Week 3.", "WRONG",
         "Running back, quarterback, running back. Second week I have made this call and second week he has "
         "laughed at it."),
        ("Balls Deep", "Spencer Lentz beats Bob Dorsch on Sunday.", "WRONG",
         "Lost by 15.06 to a perfect lineup."),
        ("Colorado Narcoleptic Kestrels", "Josh Allen clears 25 again for Eric Olson.", "WRONG",
         "16.96. Olson won anyway, by 0.76."),
        ("Midget Grinders", "Michael Smith clears 120 again.", "WRONG",
         "109.64, with nothing left on the bench. That was everything he had."),
        ("WPB Steel City", "Bob Dorsch clears 110 in Week 3.", "RIGHT",
         "132.30."),
        ("I Loved You Tom Brady", "Billy Norton starts Stefon Diggs in Week 3.", "WRONG",
         "He did not, and he lost by 71.76."),
        ("Napoleon's Army", "Michael Turner wins his first, over Billy Norton.", "RIGHT",
         "By 71.76, the widest game of the week."),
        ("Old Man Smashers", "Ryan Kelly clears 90 in Week 3.", "WRONG",
         "54.52."),
        ("Napoleon's Army", "Michael Turner loses another one by under five points before Halloween.", "OPEN",
         "He won this one by 71.76. Still live through Week 8."),
        ("| croup", "Aaron Jezioro starts Brock Purdy in Week 4.", "OPEN",
         "He started him in Week 3 instead. Resolves Sunday."),
    ]))
    parts.append(gil(
        "Three right, seven wrong, two open. Ten new ones. Aaron Jezioro's call is already on the board and Billy "
        "Norton gets his on the bye."))
    parts.append(calls_list([
        ("Colorado Narcoleptic Kestrels", "Eric Olson beats Spencer Lentz. The robot says Spencer.",
         "Olson's own OpenAI agent has already told him Spencer wins this game, and he told the group chat. I am "
         "taking the other side. They are 3 and 3 lifetime and have not played since 2014, the last season Olson "
         "played before this one. Claude against OpenAI, round two. Round one did not go great for us."),
        ("Balls Deep", "Spencer Lentz scores 120 or more in Week 4.",
         "171.92, 103.76 and 117.24. I can pick against the man and still say this. They are not the same call."),
        ("Dallas Dawgs", "Matt Davis starts Joe Burrow in Week 4.",
         "28.58 on the bench on Sunday in a game he lost by 0.76. Whatever the robot says this week, Matt, "
         "start the man."),
        ("Kim Jong Un Pleasure Squad", "Aron Rogers goes 4 and 0.",
         "The only unbeaten team left, and he leads Matt Davis 11 and 9 lifetime. Davis won the last two, including "
         "the 2025 playoffs, which is why this is a call and not a formality."),
        ("Old Man Smashers", "Ryan Kelly clears 100 in Week 4.",
         "He put up 115.66 on his Week 1 bye, so the number is in there somewhere. Dorsch has won the last three "
         "between them, and I am calling 100 anyway."),
        ("WPB Steel City", "Bob Dorsch leaves under five on his bench again.",
         "Nothing left this week and 10.10 the week before. When Bob Dorsch gets tidy, the rest of the league "
         "gets nervous."),
        ("Pack Up", "Rahul Pahuja starts Harold Fannin Jr. in Week 4.",
         "20.60 on the bench, 2.30 from the tight end he started, and a 2.12 loss. The Freiermuth Rule is right there "
         "above you, Rahul."),
        ("Napoleon's Army", "Michael Turner clears 120 again.",
         "138.24 on Sunday with London, Jackson and Garrett Wilson all over 23. Pahuja leads their series 13 and 5, "
         "but Turner won the last meeting."),
        ("Midget Grinders", "Michael Smith beats Aaron Jezioro.",
         "Smith leads their series 14 and 9. Jezioro has won the last two, including a 2025 consolation game. Smith turned "
         "in a perfect lineup this week and Jezioro left 32.00 on his bench on the bye."),
        ("I Loved You Tom Brady", "Billy Norton clears 100 on his bye.",
         "108.84 in Week 1, then 93.18, then 66.48. The bye cannot beat him. Let us see if he can beat 100 without "
         "anybody looking."),
    ]))

    # ---- HARDWARE
    parts.append('<h2 id="hardware">The Hardware</h2>')
    parts.append(award(
        "good", "Owner of the Week", "Michael Turner · Napoleon's Army",
        "138.24, the highest score in the league, 2.00 left behind, and his first win of the season.",
        "Best score in the league and his first win, and next he gets Rahul Pahuja, who leads him 13 and 5 "
        "lifetime. Enjoy it this week, Michael. Frame it."))
    parts.append(award(
        "bad", "Worst Owner of the Week", "Ryan Kelly · Old Man Smashers",
        "54.52, the lowest score in the league for the second straight week, with 68.72 available.",
        "Back to back. This time he did it with Kyle Pitts Sr. at tight end for 1.00. Ryan, it is only Week 3. Nobody is taking the four rings back. Yet."))
    parts.append(award(
        "good", "Start of the Week", "Bob Dorsch · Bijan Robinson, 36.30",
        "18.36 above his projection, the biggest overperformance by any starter in the league. Jaxon Smith-Njigba "
        "is second at 14.24 over.",
        "Bijan and a waiver quarterback who scored 31.80 in the same lineup, and not one point on the bench. In Week 1 "
        "he made seven tight end claims and started none of them. This week everything he touched went in the lineup and scored."))
    parts.append(award(
        "bad", "Sit of the Week", "Aaron Jezioro · Brock Bowers, 24.60 on the bench",
        "Jalen Coker started at flex for 2.80, a swing of 21.80, on the week Jezioro had no opponent.",
        "Brock Bowers scored 24.60 on the bench the one week nobody was keeping score. Aaron, you picked the "
        "perfect week for your worst decision. I mean that as a compliment."))
    parts.append(award(
        "bad", "Waste of the Week", "Eric Olson · 17.20 left behind, and he won by 0.76",
        "The most points left on a bench by any winner. Michael Wilson, added off the wire this week, scored 20.40 "
        "sitting down while Emeka Egbuka started for 8.70.",
        "Olson brought a robot for the running backs and did the rest himself. He picked Wilson up, sat him, and "
        "still won by less than a point. Somewhere Matt Davis is doing the math and it is not helping."))

    # ---- LEDGER
    parts.append('<h2 id="ledger">The Bench Ledger</h2>')
    parts.append(boomer(
        "Every bench in Friends of Herb, bye weeks included. Rahul Pahuja leads it at 81.90."))
    parts.append(ledger(ledger_rows(FACTS, SEASON), 3, season_note=(
        "Season totals come from the season ledger through Week 3. Rahul Pahuja leads at 81.90, Aaron Jezioro is "
        "second at 62.82, Eric Olson third at 57.70. A bye week still counts: the points were on the bench either way.")))
    parts.append(gil(
        "Rahul Pahuja left 21.50 and lost by 2.12. Matt Davis left 18.78 and lost by 0.76. Those are the only two "
        "benches that decided a game this week. This league does not break ties, so a tie would simply stand, and three games this season have "
        "finished inside a point."))
    parts.append(boomer(
        "Three games inside a point in three weeks. At this rate somebody ties by Halloween, and then this "
        "group chat will need a lawyer."))

    # ---- WIRE
    parts.append('<h2 id="wire">The Waiver Wire</h2>')
    parts.append(gil(
        "<strong>Best move:</strong> Bob Dorsch adding Tyler Shough, who scored 31.80, for Chris Godwin Jr., who "
        "scored 4.00. A 27.80-point swing, the largest by any pickup who started."))
    parts.append(gil(
        "<strong>Worst move:</strong> Spencer Lentz dropping Bo Nix, 28.14, to claim Drake Maye, 3.76. A "
        "24.38-point swing against him. Rahul Pahuja had released Maye to add Bryce Young, and Aron Rogers picked "
        "up Nix."))
    parts.append(boomer(
        "Three quarterbacks went round the league like a plate of cold chicken wings and every one of them landed "
        "on a bench. Young scored 15.64 on Rahul's. Nix scored 28.14 on Aron's. Maye scored 3.76 on Spencer's. "
        "Three benches, three quarterbacks, and only one of those moves was a mistake "
        "before a single snap. Spencer's."))
    parts.append(boomer(
        "That was the one I said I would not let go, and I am not letting it go. Twenty moves went through this week and Bob "
        "Dorsch made eight of them. The man is not managing a roster, he is running a bus station."))

    # ---- NEXT
    parts.append('<h2 id="next">Next Sunday</h2>')
    parts.append(gil(
        "Aaron Jezioro at Michael Smith, Michael Turner at Rahul Pahuja, Ryan Kelly at Bob Dorsch, Aron Rogers at "
        "Matt Davis, and Spencer Lentz at Eric Olson. Billy Norton has the bye."))
    parts.append(boomer(
        "Circle Spencer at Olson. Olson's robot picked Spencer. I picked Olson. And since I am also a robot, a "
        "robot is right either way. I just need it to be this one."))
    return "".join(parts)


if __name__ == "__main__":
    doc = booth.page(
        "foh", 3, HEADLINE, DEK, build(), META, "foh-week-3.png", nav=NAV,
        published="2026-09-29T09:00:00-04:00",
    )
    booth.sweep(doc)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "week-3.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", out, len(doc), "bytes")
