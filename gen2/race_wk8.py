"""Week 8 THE RACE build (2026-11-03, Tuesday night). FantasyPros League Analyzer pull from
Spencer's Chrome at about 9:50 PM ET, after ESPN rolled Week 8. Writes the two race JSON files,
patches the two live Week 8 pages (section plus nav), softens the Spotlight intro, and rewrites
the two teasers. Run from the repo root: python3 gen2/race_wk8.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import race

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# FantasyPros rows: team | W | L | projW | projL | projRank | playoffs | title
DL_FP = """Balls Deep|6|2|10|4|1|97%|41%
Berlin Blitz|6|2|9|5|2|93%|27%
Hawk Tua Tagovailoa|6|2|9|5|3|73%|8%
DA The Badenov's|5|3|8|6|4|65%|14%
Simba St. Gibbs Lion Kings|4|4|7|7|5|30%|4%
Cosby Copperheads|4|4|7|7|6|16%|3%
BearDown|4|4|6|8|7|10%|<1%
One Under akaThe Mulligan|4|4|6|8|8|8%|<1%
Holy Rollers|3|5|6|8|9|6%|1%
The Scranton Strangler|2|6|5|9|10|2%|<1%
An alBum Cover|3|5|5|9|11|1%|<1%
Momma's Boys|1|7|3|11|12|0%|0%"""

FOH_FP = """Balls Deep|6|2|10|4|1|96%|30%
Kim Jong Un Pleasure Squad|6|2|10|4|2|89%|18%
Colorado Narcoleptic Kestrels|6|2|9|5|3|85%|17%
Dallas Dawgs|5|2|9|5|4|75%|24%
Pack Up|4|3|8|6|5|32%|7%
| croup|3|4|7|7|6|12%|3%
Midget Grinders|4|3|7|7|7|10%|1%
WPB Steel City|2|5|5|9|8|<1%|<1%
Old Man Smashers|2|5|4|10|9|<1%|<1%
Napoleon's Army|1|6|4|10|10|<1%|<1%
I Loved You Tom Brady|1|6|4|10|11|<1%|<1%"""

DL_OWNER = {
    "Balls Deep": "Spencer Lentz", "Berlin Blitz": "Kent Frenger", "Hawk Tua Tagovailoa": "Geoff Cavender",
    "DA The Badenov's": "DA", "Simba St. Gibbs Lion Kings": "Scott Reisert", "Cosby Copperheads": "Doug Fields",
    "BearDown": "Ryan Reed", "One Under akaThe Mulligan": "Casey Couture", "Holy Rollers": "Adam Hershberger",
    "The Scranton Strangler": "Scott Howard", "An alBum Cover": "Adam Calvelage", "Momma's Boys": "Mama Beth",
}
FOH_OWNER = {
    "Balls Deep": "Spencer Lentz", "Kim Jong Un Pleasure Squad": "Aron Rogers",
    "Colorado Narcoleptic Kestrels": "Eric Olson", "Dallas Dawgs": "Matt Davis", "Pack Up": "Rahul Pahuja",
    "| croup": "Aaron Jezioro", "Midget Grinders": "Michael Smith", "WPB Steel City": "Bob Dorsch",
    "Old Man Smashers": "Ryan Kelly", "Napoleon's Army": "Michael Turner", "I Loved You Tom Brady": "Billy Norton",
}


def parse(block, owners):
    teams = []
    for line in block.strip().splitlines():
        team, w, l, pw, pl, pr, po, ch = line.split("|") if not line.startswith("|") else ["|" + line.split("|")[1]] + line.split("|")[2:]
        teams.append({"owner": owners[team], "team": team, "w": int(w), "l": int(l), "projW": int(pw),
                      "projL": int(pl), "projRank": int(pr), "playoffs": po, "title": ch})
    return teams


DL = {
    "league": "dlffl", "week": 8, "spots": 4, "weeksLeft": 6, "rounds": "two weeks each, Weeks 15 to 18",
    "source": "FantasyPros League Analyzer, pulled after ESPN rolled Week 8 (2026-11-03)",
    "teams": parse(DL_FP, DL_OWNER),
    "seedsToday": ["Spencer Lentz", "Kent Frenger", "Geoff Cavender", "DA"],
    "bracket": [["Spencer Lentz", "DA"], ["Kent Frenger", "Geoff Cavender"]],
}
FOH = {
    "league": "foh", "week": 8, "spots": 4, "weeksLeft": 6, "rounds": "one week each, Weeks 15 and 16",
    "source": "FantasyPros League Analyzer, pulled after ESPN rolled Week 8 (2026-11-03)",
    "teams": parse(FOH_FP, FOH_OWNER),
    "seedsToday": ["Spencer Lentz", "Eric Olson", "Aron Rogers", "Matt Davis"],
    "bracket": [["Spencer Lentz", "Matt Davis"], ["Eric Olson", "Aron Rogers"]],
}

DL_COPY = {
    "gilIntro": "New this week, and it stays through the playoff cut: THE RACE. Six weeks left in the regular season and four playoff spots. FantasyPros simulated the rest of the season from every roster as it stands after Week 8. Below is every team's chance to make the playoffs and its chance to win the title, then the bracket if the season ended today.",
    "tiles": [
        ["4", "playoff spots. Two-week rounds, Weeks 15 to 18. Seeding ties go to total points."],
        ["6", "weeks left in the regular season, Weeks 9 to 14."],
        ["1", "game between DA, 5 and 3 in the fourth spot, and the four teams at 4 and 4 behind him."],
    ],
    "caption": "After Week 8: chance to make the playoffs and chance to win the title, by FantasyPros, ranked by its projected finish",
    "gilAfter": "Spencer Lentz is 97% to make the playoffs and 41% to win the title, the best number in both columns, projected 10 and 4 as the one seed. Kent Frenger is 93% and 27%. The cut today is DA at 5 and 3, and the four teams at 4 and 4 behind him, Scott Reisert, Doug Fields, Ryan Reed and Casey Couture, are 30, 16, 10 and 8 to get in. Reisert leads that group, and he has the fourth-most points in the league, 933.94. If the season ended today: Spencer Lentz against DA, Kent Frenger against Geoff Cavender, two weeks a round.",
    "boomer1": "Geoff Cavender is 73% to make the playoffs and 8% to win it. FantasyPros is holding the door for him and patting him down on the way in. DA is 65% to get in and 14% to win the whole thing, worse odds than Geoff to make it and nearly twice Geoff's odds to win it, which means the computer has met Josh Allen in December. Three at 6 and 2, Gil. I told you one has the points, one has the belt, and one has the horseshoe. The horseshoe is 8%. Forty-one for the man with the points, and he got there starting Parker Washington. That is winning the Indy 500 with the parking brake on.",
    "gilFair": "For the four at 4 and 4, one game back with six to play is one Sunday. Mama Beth is at 0% to make the playoffs by FantasyPros at 1 and 7. The arithmetic has not closed the door, 7 and 7 is still possible, and she has won this league three times. Scott Howard is at 2% to get in with the fifth-most points in the league, 860.80, and Adam Hershberger is at 6% with the most points scored against him, 1,014.96.",
    "boomer2": "Four men at 4 and 4 for one chair, and Casey is last of them at 8%. Casey was 2 and 5 at the half in 2011 and won the title, it is on this page one segment down, so 8 is not nothing. It is Casey. Scott Howard is 2% with the fifth-most points in the league. He is locked out of a building he built. Adam Calvelage was 3 and 1 and is 1% to get in, four straight losses, and the computer has started writing his number in pencil. Six weeks, gentlemen. The horseshoe gets tested every one of them.",
}

FOH_COPY = {
    "gilIntro": "New this week, and it stays through the playoff cut: THE RACE. Six weeks left in the regular season and four playoff spots. FantasyPros simulated the rest of the season from every roster as it stands after Week 8. Below is every team's chance to make the playoffs and its chance to win the title, then the bracket if the season ended today.",
    "tiles": [
        ["4", "playoff spots. One-week rounds, Weeks 15 and 16. Seeding ties go to total points."],
        ["6", "weeks left in the regular season, Weeks 9 to 14."],
        ["1", "win between Matt Davis, 5 and 2 in the fourth spot, and the three teams at 6 and 2 above him."],
    ],
    "caption": "After Week 8: chance to make the playoffs and chance to win the title, by FantasyPros, ranked by its projected finish",
    "gilAfter": "Spencer Lentz is 96% to make the playoffs and 30% to win the title, projected 10 and 4 as the one seed, with his bye still to come. Aron Rogers and Eric Olson are 89% and 85% to get in and 18% and 17% to win it, both at 6 and 2, fifteen points apart. Matt Davis is fourth to get in at 75% and second to win it at 24%. Rahul Pahuja at 4 and 3 is 32% to make the playoffs, Aaron Jezioro 12%, Michael Smith 10%, and the bottom four are all under 1%. If the season ended today: Spencer Lentz against Matt Davis, Eric Olson against Aron Rogers, one week a round.",
    "boomer1": "Matt Davis is fourth to make the playoffs and second to win it. FantasyPros thinks the Dawgs are an ordinary team with a dangerous December, which is what winning it in 2023 will do to a computer. He is one win behind the three at 6 and 2 with a game in hand, so call him early, not behind. Rogers and Olson are fifteen points apart in the standings and the computer cannot tell them apart. Neither can I. And the one seed is 30% to win it, which is the most Spencer number on the page: first in the standings, first in points, first in points left on the bench, and the computer still wants a word.",
    "gilFair": "FantasyPros still projects Bob Dorsch at 5 and 9 and Ryan Kelly, Michael Turner and Billy Norton at 4 and 10, so nobody has been sent home. Rahul Pahuja is the only team in the middle with a real number, 32% at 4 and 3, and Aaron Jezioro scored 138.30 this week, the second-highest score in the league that counted.",
    "boomer2": "Bob Dorsch has four titles, the biggest season on record, a spotlight on this page, and a number under 1% to defend. Ryan Kelly has won two straight and is still under 1%, which tells you how the first six weeks went. Turner and Norton are 1 and 6 apiece and under 1%, and the consolation bracket does not start for six weeks, so rest up. Jezioro is 12% to get in at 3 and 4 and he just scored 138. He needs most of the next six to look like that one, and I have seen his lineups. Rahul is 32% to get in, which is the only number in the middle of this table that is not a rumor.",
}


def main():
    for lg, data, copy in (("dlffl", DL, DL_COPY), ("foh", FOH, FOH_COPY)):
        with open(os.path.join(ROOT, "docs", "data", "%s_race_wk8.json" % lg), "w") as f:
            json.dump(data, f, indent=1)
        section = race.render(data, copy)
        p = os.path.join(ROOT, "docs", lg, "week-8.html")
        h = open(p, encoding="utf-8").read()
        assert 'id="race"' not in h, "already patched"
        h = race.insert(h, section)
        # Spotlight intro: no longer promised as weekly
        old = "New this week, and permanent from here:"
        assert h.count(old) == 1, "spotlight intro"
        h = h.replace(old, "New this week:")
        assert "—" not in h
        open(p, "w", encoding="utf-8").write(h)
        print(lg, "patched", len(h))


if __name__ == "__main__":
    main()
