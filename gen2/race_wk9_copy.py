"""Week 9 THE RACE: data and copy. FantasyPros League Analyzer pulled from Spencer's Chrome after ESPN
rolled Week 9 (2026-11-10, about 3:20 AM ET); both leagues confirmed at a four-team playoff field and
synced to the Week 9 records. Run from the repo root to write docs/data/<league>_race_wk9.json.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DL_ROWS = [  # owner, team, w, l, projW, projL, rank, playoffs, title
    ("Spencer Lentz", "Balls Deep", 7, 2, 10, 4, 1, ">99%", "42%"),
    ("Kent Frenger", "Berlin Blitz", 7, 2, 10, 4, 2, "98%", "28%"),
    ("Geoff Cavender", "Hawk Tua Tagovailoa", 6, 3, 8, 6, 3, "67%", "8%"),
    ("DA", "DA The Badenov's", 5, 4, 8, 6, 4, "56%", "12%"),
    ("Scott Reisert", "Simba St. Gibbs Lion Kings", 5, 4, 7, 7, 5, "42%", "6%"),
    ("Adam Hershberger", "Holy Rollers", 4, 5, 7, 7, 6, "11%", "2%"),
    ("Adam Calvelage", "An alBum Cover", 4, 5, 6, 8, 7, "7%", "<1%"),
    ("Ryan Reed", "BearDown", 4, 5, 6, 8, 8, "6%", "<1%"),
    ("Doug Fields", "Cosby Copperheads", 4, 5, 6, 8, 9, "6%", "<1%"),
    ("Scott Howard", "The Scranton Strangler", 3, 6, 6, 8, 10, "4%", "<1%"),
    ("Casey Couture", "One Under akaThe Mulligan", 4, 5, 6, 8, 11, "4%", "<1%"),
    ("Mama Beth", "Momma's Boys", 1, 8, 3, 11, 12, "0%", "0%"),
]
FOH_ROWS = [
    ("Spencer Lentz", "Balls Deep", 7, 2, 11, 3, 1, "99%", "31%"),
    ("Aron Rogers", "Kim Jong Un Pleasure Squad", 6, 3, 9, 5, 2, "83%", "15%"),
    ("Eric Olson", "Colorado Narcoleptic Kestrels", 6, 2, 9, 5, 3, "70%", "14%"),
    ("Matt Davis", "Dallas Dawgs", 5, 3, 8, 6, 4, "66%", "20%"),
    ("Rahul Pahuja", "Pack Up", 5, 3, 8, 6, 5, "50%", "13%"),
    ("Aaron Jezioro", "| croup", 4, 4, 7, 7, 6, "23%", "6%"),
    ("Michael Smith", "Midget Grinders", 5, 3, 7, 7, 7, "8%", "<1%"),
    ("Bob Dorsch", "WPB Steel City", 3, 5, 5, 9, 8, "1%", "<1%"),
    ("Ryan Kelly", "Old Man Smashers", 2, 6, 4, 10, 9, "<1%", "<1%"),
    ("Billy Norton", "I Loved You Tom Brady", 1, 7, 3, 11, 10, "<1%", "<1%"),
    ("Michael Turner", "Napoleon's Army", 1, 7, 3, 11, 11, "0%", "0%"),
]
K = ("owner", "team", "w", "l", "projW", "projL", "projRank", "playoffs", "title")
SRC = "FantasyPros League Analyzer, pulled after ESPN rolled Week 9 (2026-11-10)"
DL = {"league": "dlffl", "week": 9, "spots": 4, "weeksLeft": 5, "rounds": "two weeks each, Weeks 15 to 18",
      "source": SRC, "teams": [dict(zip(K, r)) for r in DL_ROWS],
      "seedsToday": ["Spencer Lentz", "Kent Frenger", "Geoff Cavender", "DA"],
      "bracket": [["Spencer Lentz", "DA"], ["Kent Frenger", "Geoff Cavender"]]}
FOH = {"league": "foh", "week": 9, "spots": 4, "weeksLeft": 5, "rounds": "one week each, Weeks 15 and 16",
       "source": SRC, "teams": [dict(zip(K, r)) for r in FOH_ROWS],
       "seedsToday": ["Spencer Lentz", "Eric Olson", "Aron Rogers", "Matt Davis"],
       "bracket": [["Spencer Lentz", "Matt Davis"], ["Eric Olson", "Aron Rogers"]]}

INTRO = ("THE RACE, through the playoff cut. Five weeks left in the regular season and four playoff spots. "
         "FantasyPros simulated the rest of the season from every roster as it stands after Week 9. Below is every "
         "team's chance to make the playoffs and its chance to win the title, then the bracket if the season ended today.")
CAP = "After Week 9: chance to make the playoffs and chance to win the title, by FantasyPros, ranked by its projected finish"

DL_COPY = {
    "gilIntro": INTRO,
    "tiles": [
        ["4", "playoff spots. Two-week rounds, Weeks 15 to 18. Seeding ties go to total points."],
        ["5", "weeks left in the regular season, Weeks 10 to 14."],
        ["34.42", "points between DA and Scott Reisert, both 5 and 4, for the fourth spot."],
    ],
    "caption": CAP,
    "gilAfter": "Spencer Lentz is better than 99% to make the playoffs and 42% to win the title, and Kent Frenger is 98% and 28%. Both are 7 and 2 and projected 10 and 4. A week ago they were 41% and 27% to win it. Geoff Cavender fell from 73% to 67% to make the playoffs, and DA from 65% to 56%. Scott Reisert, level with DA at 5 and 4, rose from 30% to 42%. Adam Hershberger is the best of the five teams at 4 and 5, at 11%. If the season ended today: Spencer Lentz against DA, Kent Frenger against Geoff Cavender, two weeks a round.",
    "boomer1": "Two teams are in, and three teams are fighting over two spots: Cavender at 67% to make the playoffs, DA at 56%, Reisert at 42%. Geoff is 67% to get in and 8% to win the title. DA is 56% to get in and 12% to win it. FantasyPros thinks Geoff gets through the door more often and DA does more damage once he is inside. And the top line is 42% to win the title for a man who benched forty points on Sunday. The computer does not watch the games. It just counts the roster.",
    "gilFair": "For the five teams at 4 and 5, one game back of the fourth spot with five to play is still one Sunday. Adam Calvelage went from 1% to 7% to make the playoffs with one win. Scott Howard is at 4% with the fifth-most points in the league, 1,009.10. Mama Beth is at 0% by FantasyPros at 1 and 8, and she has won this league three times.",
    "boomer2": "Doug Fields was 16% to make the playoffs a week ago and is 6% now. He dropped ten points on that number by scoring 91, which is how Doug does everything, quietly. Casey is at 4%. Five rings and 4%, and I would still rather not see him in a bracket. Howard is 4% with a team that just scored 148, and Calvelage is 7% and climbing. Five weeks. Somebody at 4 and 5 is going to make Reisert and DA sweat, and nobody on this table can tell you which one.",
}
FOH_COPY = {
    "gilIntro": INTRO,
    "tiles": [
        ["4", "playoff spots. One-week rounds, Weeks 15 and 16. Seeding ties go to total points."],
        ["5", "weeks left in the regular season, Weeks 10 to 14."],
        ["3", "teams at 5 and 3 for the fourth spot: Matt Davis, Rahul Pahuja and Michael Smith."],
    ],
    "caption": CAP,
    "gilAfter": "Spencer Lentz is 99% to make the playoffs and 31% to win the title, projected 11 and 3 as the one seed. Aron Rogers is 83% to make the playoffs and Eric Olson 70%, down from 89% and 85% a week ago. Matt Davis holds the fourth spot at 66% to get in and is second to win the title at 20%. Rahul Pahuja went from 32% to 50% to make the playoffs and from 7% to 13% to win the title. Aaron Jezioro went from 12% to 23% to get in. Michael Smith, also 5 and 3, is at 8%. If the season ended today: Spencer Lentz against Matt Davis, Eric Olson against Aron Rogers, one week a round.",
    "boomer1": "Rahul went from 32% to 50% to make the playoffs in one afternoon, which is what winning by 112 does. Davis, Rahul and Smith are all 5 and 3, and FantasyPros has them at 66%, 50% and 8% to get in. Same record, Michael. The computer looked at three identical records and handed you the short straw, because it has also seen the 32 and 40. And Eric Olson went from 85% to 70% to make the playoffs on his bye, without playing a game. He sat still and the league moved around him.",
    "gilFair": "Michael Smith has the same record as Davis and Pahuja and has won five of the eight games on his schedule. Bob Dorsch is at 1% to make the playoffs at 3 and 5, two games back with five weeks to play. Ryan Kelly and Billy Norton are under 1%, and Michael Turner is at 0% by FantasyPros at 1 and 7.",
    "boomer2": "Jezioro is 23% to make the playoffs at 4 and 4, nearly three times Smith's number with a worse record, because the computer likes his roster and has not seen his bench. I have. He left zero on it this week, so maybe the computer knows something. Bob Dorsch is 1%, up from under 1%, and with four titles Bob will tell you that is a trend. And the one seed is 31% to win the title with a bye week to think about his lineups, which is the most dangerous thing you can give him.",
}

if __name__ == "__main__":
    for lg, data in (("dlffl", DL), ("foh", FOH)):
        with open(os.path.join(ROOT, "docs", "data", "%s_race_wk9.json" % lg), "w") as f:
            json.dump(data, f, indent=1)
        print("wrote", lg)
