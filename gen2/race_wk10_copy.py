"""Week 10 THE RACE: data and copy. FantasyPros League Analyzer pulled from Spencer's Chrome after ESPN
rolled Week 10 (2026-11-17, evening); both leagues confirmed at a four-team playoff field and synced to
the Week 10 records. Run from the repo root to write docs/data/<league>_race_wk10.json.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DL_ROWS = [  # owner, team, w, l, projW, projL, rank, playoffs, title
    ("Spencer Lentz", "Balls Deep", 8, 2, 11, 3, 1, ">99%", "43%"),
    ("Kent Frenger", "Berlin Blitz", 7, 3, 9, 5, 2, "96%", "29%"),
    ("Geoff Cavender", "Hawk Tua Tagovailoa", 7, 3, 9, 5, 3, "77%", "8%"),
    ("DA", "DA The Badenov's", 6, 4, 8, 6, 4, "74%", "14%"),
    ("Scott Reisert", "Simba St. Gibbs Lion Kings", 5, 5, 7, 7, 5, "22%", "3%"),
    ("Doug Fields", "Cosby Copperheads", 5, 5, 7, 7, 6, "10%", "1%"),
    ("Adam Calvelage", "An alBum Cover", 5, 5, 7, 7, 7, "10%", "<1%"),
    ("Scott Howard", "The Scranton Strangler", 4, 6, 6, 8, 8, "7%", "<1%"),
    ("Adam Hershberger", "Holy Rollers", 4, 6, 6, 8, 9, "2%", "<1%"),
    ("Ryan Reed", "BearDown", 4, 6, 6, 8, 10, "2%", "<1%"),
    ("Casey Couture", "One Under akaThe Mulligan", 4, 6, 6, 8, 11, "<1%", "<1%"),
    ("Mama Beth", "Momma's Boys", 1, 9, 3, 11, 12, "0%", "0%"),
]
FOH_ROWS = [
    ("Spencer Lentz", "Balls Deep", 7, 2, 10, 4, 1, "95%", "28%"),
    ("Aron Rogers", "Kim Jong Un Pleasure Squad", 7, 3, 10, 4, 2, "95%", "21%"),
    ("Matt Davis", "Dallas Dawgs", 6, 3, 9, 5, 3, "76%", "22%"),
    ("Rahul Pahuja", "Pack Up", 6, 3, 8, 6, 4, "67%", "18%"),
    ("Eric Olson", "Colorado Narcoleptic Kestrels", 6, 3, 8, 6, 5, "48%", "9%"),
    ("Michael Smith", "Midget Grinders", 6, 3, 7, 7, 6, "13%", "1%"),
    ("Aaron Jezioro", "| croup", 4, 5, 6, 8, 7, "4%", "<1%"),
    ("Bob Dorsch", "WPB Steel City", 4, 5, 5, 9, 8, "1%", "<1%"),
    ("Ryan Kelly", "Old Man Smashers", 2, 7, 4, 10, 9, "0%", "0%"),
    ("Billy Norton", "I Loved You Tom Brady", 1, 8, 3, 11, 10, "0%", "0%"),
    ("Michael Turner", "Napoleon's Army", 1, 8, 3, 11, 11, "0%", "0%"),
]
K = ("owner", "team", "w", "l", "projW", "projL", "projRank", "playoffs", "title")
SRC = "FantasyPros League Analyzer, pulled after ESPN rolled Week 10 (2026-11-17)"
DL = {"league": "dlffl", "week": 10, "spots": 4, "weeksLeft": 4, "rounds": "two weeks each, Weeks 15 to 18",
      "source": SRC, "teams": [dict(zip(K, r)) for r in DL_ROWS],
      "seedsToday": ["Spencer Lentz", "Kent Frenger", "Geoff Cavender", "DA"],
      "bracket": [["Spencer Lentz", "DA"], ["Kent Frenger", "Geoff Cavender"]]}
FOH = {"league": "foh", "week": 10, "spots": 4, "weeksLeft": 4, "rounds": "one week each, Weeks 15 and 16",
       "source": SRC, "teams": [dict(zip(K, r)) for r in FOH_ROWS],
       "seedsToday": ["Spencer Lentz", "Aron Rogers", "Matt Davis", "Rahul Pahuja"],
       "bracket": [["Spencer Lentz", "Rahul Pahuja"], ["Aron Rogers", "Matt Davis"]]}

INTRO = ("THE RACE, through the playoff cut. Four weeks left in the regular season and four playoff spots. "
         "FantasyPros simulated the rest of the season from every roster as it stands after Week 10. Below is every "
         "team's chance to make the playoffs and its chance to win the title, then the bracket if the season ended today.")
CAP = "After Week 10: chance to make the playoffs and chance to win the title, by FantasyPros, ranked by its projected finish"

DL_COPY = {
    "gilIntro": INTRO,
    "tiles": [
        ["4", "playoff spots. Two-week rounds, Weeks 15 to 18. Seeding ties go to total points."],
        ["4", "weeks left in the regular season, Weeks 11 to 14."],
        ["3", "teams at 5 and 5, one game behind DA for the fourth spot: Scott Reisert, Doug Fields and Adam Calvelage."],
    ],
    "caption": CAP,
    "gilAfter": "Spencer Lentz is better than 99% to make the playoffs and 43% to win the title, projected 11 and 3. Kent Frenger is 96% and 29%. DA rose from 56% to 74% to make the playoffs by beating Frenger, and Geoff Cavender from 67% to 77%. Scott Reisert fell from 42% to 22%. Doug Fields and Adam Calvelage are each at 10%, and Scott Howard is at 7% at 4 and 6. Adam Hershberger fell from 11% to 2%. If the season ended today: Spencer Lentz against DA, Kent Frenger against Geoff Cavender, two weeks a round.",
    "boomer1": "DA went up eighteen points on the chance to make the playoffs in one afternoon, and Scott Reisert went down twenty. That is the same door swinging. Reisert plays DA on Sunday, so he can swing it right back. And look at Cavender. 77% to make the playoffs and 8% to win the title. FantasyPros thinks Geoff is very likely to get into the building and not likely to find the stage. Same as last week.",
    "gilFair": "For the teams at 5 and 5, one game back with four to play is still one Sunday. Doug Fields went from 6% to 10% to make the playoffs with his best score of the season. Scott Howard is at 7% with the fifth-most points in the league, 1,135.22. Mama Beth is at 0% by FantasyPros at 1 and 9, and she has won this league three times.",
    "boomer2": "Scott Howard is 7% to make the playoffs, per FantasyPros, at 4 and 6, and he is the one team down there nobody wants to see, because he has the points of a playoff team and just left 4.20 on his bench. Doug Fields and Adam Calvelage are 10% each, one game back. Four weeks. Three teams at 5 and 5 chasing the elder.",
}
FOH_COPY = {
    "gilIntro": INTRO,
    "tiles": [
        ["4", "playoff spots. One-week rounds, Weeks 15 and 16. Seeding ties go to total points."],
        ["4", "weeks left in the regular season, Weeks 11 to 14."],
        ["4", "teams at 6 and 3 for the third and fourth spots: Matt Davis, Rahul Pahuja, Eric Olson and Michael Smith."],
    ],
    "caption": CAP,
    "gilAfter": "Spencer Lentz and Aron Rogers are each 95% to make the playoffs. Lentz is 28% to win the title, down from 31% after his bye, and Rogers is 21%, up from 15%. Four teams are 6 and 3. Matt Davis is 76% to make the playoffs and 22% to win the title, Rahul Pahuja 67% and 18%, Eric Olson 48% and 9%, and Michael Smith 13% and 1%. Olson was 70% a week ago. Aaron Jezioro fell from 23% to 4%. If the season ended today: Spencer Lentz against Rahul Pahuja, Aron Rogers against Matt Davis, one week a round.",
    "boomer1": "Four teams at 6 and 3, and FantasyPros has their chances to make the playoffs at 76%, 67%, 48% and 13%. Same record, four different futures. Rahul's chance went from 50% to 67% by scoring 173 again. Olson's went from 70% to 48% by scoring 102 again. Consistency is a virtue, Eric, but you have to pick the right number to be consistent at. And the first-place team's chance to win the title fell from 31% to 28% without a game that counted. The league got better while he was benching Mahomes.",
    "gilFair": "Eric Olson is still 6 and 3 and one tiebreaker from a playoff spot, and he has the third-most points of the four teams tied at that record. Michael Smith has the same record and won again. Bob Dorsch is at 1% to make the playoffs at 4 and 5. Ryan Kelly, Billy Norton and Michael Turner are at 0% by FantasyPros.",
    "boomer2": "Jezioro was 23% to make the playoffs last week, scored 129 with a perfect lineup, and is 4% now. That is the cruelest line on the board. Bob Dorsch is 1% to make the playoffs for the second straight week, per FantasyPros, so Bob has now won a game and gained nothing, which pairs nicely with scoring 75 and losing nothing.",
}

if __name__ == "__main__":
    for lg, data in (("dlffl", DL), ("foh", FOH)):
        with open(os.path.join(ROOT, "docs", "data", "%s_race_wk10.json" % lg), "w") as f:
            json.dump(data, f, indent=1)
        print("wrote", lg)
