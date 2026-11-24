"""Week 11 THE RACE: data and copy. FantasyPros League Analyzer pulled from Spencer's Chrome after ESPN
rolled Week 11 (2026-11-24, early morning); both leagues confirmed at a four-team playoff field and
synced to the Week 11 records (Friends of Herb needed a manual Refresh League Data, Dewart Lake had
already synced). Run from the repo root to write docs/data/<league>_race_wk11.json.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DL_ROWS = [  # owner, team, w, l, projW, projL, rank, playoffs, title
    ("Spencer Lentz", "Balls Deep", 9, 2, 11, 3, 1, "100%", "43%"),
    ("Geoff Cavender", "Hawk Tua Tagovailoa", 8, 3, 9, 5, 2, "92%", "11%"),
    ("Kent Frenger", "Berlin Blitz", 7, 4, 8, 6, 3, "88%", "25%"),
    ("DA", "DA The Badenov's", 6, 5, 8, 6, 4, "49%", "10%"),
    ("Scott Reisert", "Simba St. Gibbs Lion Kings", 6, 5, 7, 7, 5, "35%", "6%"),
    ("Adam Calvelage", "An alBum Cover", 6, 5, 7, 7, 6, "23%", "3%"),
    ("Scott Howard", "The Scranton Strangler", 5, 6, 7, 7, 7, "10%", "1%"),
    ("Doug Fields", "Cosby Copperheads", 5, 6, 7, 7, 8, "2%", "<1%"),
    ("Casey Couture", "One Under akaThe Mulligan", 5, 6, 6, 8, 9, "1%", "<1%"),
    ("Ryan Reed", "BearDown", 4, 7, 5, 9, 10, "<1%", "<1%"),
    ("Adam Hershberger", "Holy Rollers", 4, 7, 5, 9, 11, "0%", "0%"),
    ("Mama Beth", "Momma's Boys", 1, 10, 2, 12, 12, "0%", "0%"),
]
FOH_ROWS = [
    ("Spencer Lentz", "Balls Deep", 8, 2, 10, 4, 1, "97%", "28%"),
    ("Matt Davis", "Dallas Dawgs", 7, 3, 9, 5, 2, "84%", "24%"),
    ("Aron Rogers", "Kim Jong Un Pleasure Squad", 7, 3, 9, 5, 3, "78%", "18%"),
    ("Eric Olson", "Colorado Narcoleptic Kestrels", 7, 3, 8, 6, 4, "60%", "13%"),
    ("Rahul Pahuja", "Pack Up", 6, 4, 8, 6, 5, "51%", "15%"),
    ("Michael Smith", "Midget Grinders", 7, 3, 8, 6, 6, "29%", "2%"),
    ("Aaron Jezioro", "| croup", 4, 6, 6, 8, 7, "<1%", "<1%"),
    ("Bob Dorsch", "WPB Steel City", 4, 6, 5, 9, 8, "<1%", "<1%"),
    ("Ryan Kelly", "Old Man Smashers", 2, 8, 4, 10, 9, "0%", "0%"),
    ("Billy Norton", "I Loved You Tom Brady", 2, 8, 3, 11, 10, "0%", "0%"),
    ("Michael Turner", "Napoleon's Army", 1, 9, 2, 12, 11, "0%", "0%"),
]
K = ("owner", "team", "w", "l", "projW", "projL", "projRank", "playoffs", "title")
SRC = "FantasyPros League Analyzer, pulled after ESPN rolled Week 11 (2026-11-24)"
DL = {"league": "dlffl", "week": 11, "spots": 4, "weeksLeft": 3, "rounds": "two weeks each, Weeks 15 to 18",
      "source": SRC, "teams": [dict(zip(K, r)) for r in DL_ROWS],
      "seedsToday": ["Spencer Lentz", "Geoff Cavender", "Kent Frenger", "DA"],
      "bracket": [["Spencer Lentz", "DA"], ["Geoff Cavender", "Kent Frenger"]]}
FOH = {"league": "foh", "week": 11, "spots": 4, "weeksLeft": 3, "rounds": "one week each, Weeks 15 and 16",
       "source": SRC, "teams": [dict(zip(K, r)) for r in FOH_ROWS],
       "seedsToday": ["Spencer Lentz", "Matt Davis", "Aron Rogers", "Eric Olson"],
       "bracket": [["Spencer Lentz", "Eric Olson"], ["Matt Davis", "Aron Rogers"]]}

INTRO = ("THE RACE, through the playoff cut. Three weeks left in the regular season and four playoff spots. "
         "FantasyPros simulated the rest of the season from every roster as it stands after Week 11. Below is every "
         "team's chance to make the playoffs and its chance to win the title, then the bracket if the season ended today.")
CAP = "After Week 11: chance to make the playoffs and chance to win the title, by FantasyPros, ranked by its projected finish"

DL_COPY = {
    "gilIntro": INTRO,
    "tiles": [
        ["4", "playoff spots. Two-week rounds, Weeks 15 to 18. Seeding ties go to total points."],
        ["3", "teams at 6 and 5 for the fourth spot: DA, Scott Reisert and Adam Calvelage."],
        ["1.88", "points between DA and Scott Reisert on the season, 1,264.06 to 1,262.18. That is the tiebreaker."],
    ],
    "caption": CAP,
    "gilAfter": "Spencer Lentz is 100% to make the playoffs and 43% to win the title, by FantasyPros, projected 11 and 3. Geoff Cavender rose from 77% to 92% to make the playoffs. Kent Frenger fell from 96% to 88%, and his chance to win the title from 29% to 25%. DA fell from 74% to 49% to make the playoffs. Scott Reisert rose from 22% to 35% and Adam Calvelage from 10% to 23%. Scott Howard is at 10% at 5 and 6. Doug Fields fell from 10% to 2%. If the season ended today: Spencer Lentz against DA, Geoff Cavender against Kent Frenger, two weeks a round.",
    "boomer1": "Last week DA's chance to make the playoffs went up to 74%. This week FantasyPros has him at 49%, which is a coin flip with a slightly bad attitude. Three teams at 6 and 5 and their chances to make the playoffs add up to 107%, mostly for one spot. And Calvelage plays Reisert on Sunday, so by Monday night one of those two numbers is going to look very silly.",
    "gilFair": "In fairness to the teams at 5 and 6, they are one game back with three to play. Scott Howard has won three straight and has the fifth-most points in the league, 1,245.22. Casey Couture is 1% to make the playoffs, by FantasyPros, and one game out. Mama Beth is at 0% at 1 and 10, and she has won this league three times.",
    "boomer2": "Geoff Cavender is 92% to make the playoffs and 11% to win the title. Kent Frenger is 88% and 25%. So FantasyPros thinks Geoff is more likely to get in and Kent is more than twice as likely to win the whole thing. They would play each other in the first round if it ended today. Two weeks, Geoff. Your luck has to hold for two weeks in a row, and it has to do it against a man who is tired of losing.",
}
FOH_COPY = {
    "gilIntro": INTRO,
    "tiles": [
        ["4", "playoff spots. One-week rounds, Weeks 15 and 16. Seeding ties go to total points."],
        ["4", "teams at 7 and 3 behind the leader: Matt Davis, Aron Rogers, Eric Olson and Michael Smith. Three of them fit."],
        ["2.68", "points between Spencer Lentz and Matt Davis on the season, 1,320.50 to 1,317.82."],
    ],
    "caption": CAP,
    "gilAfter": "Spencer Lentz is 97% to make the playoffs and 28% to win the title, by FantasyPros. Matt Davis rose from 76% to 84% to make the playoffs and is 24% to win the title. Aron Rogers fell from 95% to 78% on his bye. Eric Olson rose from 48% to 60%. Rahul Pahuja fell from 67% to 51% and is the one team at 6 and 4. Michael Smith rose from 13% to 29%. Aaron Jezioro and Bob Dorsch are each under 1%. If the season ended today: Spencer Lentz against Eric Olson, Matt Davis against Aron Rogers, one week a round.",
    "boomer1": "Aron Rogers took the week off, scored 136.86 that did not count, and his chance to make the playoffs fell from 95% to 78%, by FantasyPros. He lost ground on a week off. That is what happens when three other teams have your record and all three won. And look at Rahul. Sixth place, 51% to make the playoffs, 15% to win the title. FantasyPros gives the man in sixth a better chance to win the whole thing than the man in fourth.",
    "gilFair": "In fairness to Michael Smith, he is 7 and 3 with three straight wins, and the 29% is up from 13% a week ago. FantasyPros still projects him sixth, behind Rahul Pahuja at 6 and 4, because he has the fewest points of the four teams at 7 and 3, 1,117.02, and points break the ties. Ryan Kelly, Billy Norton and Michael Turner are at 0%.",
    "boomer2": "Smith plays Davis on Sunday. Davis has beaten him seven straight times. If Smith wins that one he is 8 and 3 and FantasyPros has to come up with a new reason. If he loses, he is in a knot at 7 and 4 with the fewest points in it. No game on the board matters more to Michael Smith.",
}

if __name__ == "__main__":
    for lg, data in (("dlffl", DL), ("foh", FOH)):
        with open(os.path.join(ROOT, "docs", "data", "%s_race_wk11.json" % lg), "w") as f:
            json.dump(data, f, indent=1)
        print("wrote", lg)
