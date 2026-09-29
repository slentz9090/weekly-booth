"""Friends of Herb, Week 3 Monday Night Special. One-off bulletin page."""
import os, booth
from booth import gil, boomer, mcard

RED = "#ff6b6b"
HEAD = "Aron Rogers Needs A Bear To Outrun His Own Teammate"
DEK = ("Rahul Pahuja and Aron Rogers came into Monday night both unbeaten, fifteen meetings deep, with Aron up 10 and 5 "
       "lifetime. Rahul leads by 4.58 and the only two players left are both Chicago Bears running backs. A Monday "
       "Night Special, because last week's Booth was late.")
META = ("A Monday Night Special from Gil and Boomer: Rahul Pahuja leads Aron Rogers by 4.58 and it comes down to two "
        "Bears running backs in the same backfield.")

win = {"team": "Pack Up", "owner": "Rahul Pahuja", "score": 116.04, "left": 0}
lose = {"team": "Kim Jong Un Pleasure Squad", "owner": "Aron Rogers", "score": 111.46, "left": 0}
card = mcard("m-mnf", "Special Bulletin · Monday Night", win, lose,
             "Still to play, Eagles at Bears: <b>Kyle Monangai</b> for Rahul, projected 7.8. "
             "<b>D'Andre Swift</b> for Aron, projected 12.1. Swift has to beat his own teammate by more than 4.58. "
             "Beat him by exactly 4.58 and it is a tie, because this league does not break them.",
             130.0, ribbon_color=RED)
card = card.replace("nothing left behind", "leads by 4.58", 1).replace("nothing left behind", "trails by 4.58", 1).replace('class="mc-row win"', 'class="mc-row win bye"')

body = "".join([
    card,
    '<h2 id="booth">From The Booth</h2>',
    gil("We owe you one. Last week's Booth showed up after Week 3 had already kicked off. Consider this the makeup call."),
    boomer("Late is late, Gil. I've been late to two weddings and one of 'em was mine."),
    gil("Here's the table. Rahul Pahuja and Aron Rogers both came into Monday night 2 and 0. Rahul leads 116.04 to "
        "111.46. Whoever wins walks out the only unbeaten team in Friends of Herb."),
    boomer("Two undefeated teams, Gil, and it comes down to two running backs who share a locker room."),
    gil("Two players left, both Chicago Bears running backs. Swift for Aron. Monangai for Rahul."),
    boomer("Same huddle. Same helmet. Same damn position coach. One of those boys is gonna shit all over somebody's "
           "week, then slap his buddy's ass on the sideline like nothing happened. Aron is rooting for a man to outrun "
           "his own teammate. That's not a matchup, that's a sibling fight at Thanksgiving."),
    '<h2 id="rivalry">The Rivalry</h2>',
    gil("And these two have history. Fifteen meetings since 2012. Aron leads the series 10 and 5."),
    boomer("Ten and five! Aron's got Rahul's number, his address, and a key to the side door."),
    gil("Aron won six straight from 2020 into 2023, including a playoff game in 2022."),
    boomer("Six in a row. Rahul spent three years losing to this man like a gym membership he forgot to cancel."),
    gil("One of those six was Week 7 of 2023. Aron won it by 0.90."),
    boomer("Hold on. Rahul won Week 1 this year by 0.46. Man doesn't win games, he wins rounding errors. And he lost "
           "one by 0.90? To Aron? The decimals switched sides, Gil. Even the math has quit on him."),
    gil("Rahul got it back in the 2023 playoffs. 125.88 to 86.90. He snapped the streak by 38.98."),
    boomer("Thirty-nine points in a playoff game. That's not snapping a streak. That's backing the truck over it, "
           "then putting it in reverse."),
    gil("Rahul won again in 2024. Aron took last year's. Each man has exactly one title. Rahul in 2013, Aron in 2019."),
    boomer("One ring apiece and fourteen years of this shit. It's Ali and Frazier, if Ali and Frazier sat on their "
           "asses and yelled at their phones."),
    gil("If Swift beats Monangai by exactly 4.58, it's a tie. This league doesn't break them."),
    boomer("Fourteen years of blood and it ends 2, 0 and 1. Like kissing your sister, if your sister played running "
           "back for the Bears."),
    '<h2 id="league">Around The League</h2>',
    gil("Olson beat Davis by 0.76. I'm told computers were involved."),
    boomer("Oh, computers were involved. Friends of Herb has an AI arms race now, Gil. Grown men asking chatbots who "
           "to start. One robot got it right. One robot got a man beat by less than a point."),
    gil("We know which robot. We are not telling you tonight."),
    boomer("Tomorrow we find out whose robot is a dumbass, and which dumbass listened to it. And one of those robots "
           "already made a pick for next week. We'll be grading that too."),
    gil("And Spencer is down 2 with his own quarterback playing tonight. From his bench. Throwing to Dorsch's guys."),
    boomer("Seven podiums, zero titles, and now his own damn quarterback is working for the other side. Hurts is on "
           "Spencer's bench feeding Barkley and Smith. That's not a benching, that's treason with extra steps. Dorsch "
           "already owns him 18 and 8 lifetime. He did not need the help."),
    gil("Full Week 3 Booth coming. Boomer's extra frisky tonight, folks."),
    boomer("Hell of a Monday, Gil."),
    boomer("...Wait. It is Monday, right?"),
])
NAV = '<nav class="nav" aria-label="Sections"><ul><li><a href="#m-mnf">The Game</a></li><li><a href="#booth">From The Booth</a></li><li><a href="#rivalry">The Rivalry</a></li><li><a href="#league">Around The League</a></li></ul></nav>'
doc = booth.page("foh", 3, HEAD, DEK, body, META, "foh-mnf-week-3.png", nav=NAV)
doc = (doc.replace("/foh/week-3.html", "/foh/mnf-week-3.html")
          .replace("Friends of Herb, Week 3 | The Weekly Booth", "Friends of Herb, Monday Night Special | The Weekly Booth")
          .replace('<span aria-current="page">Week 3</span>', '<span aria-current="page">Monday Night Special</span>')
          .replace("Week 3 · 2026<br>", "Monday Night Special · Week 3<br>")
          .replace("2026-09-24T09:00:00-04:00", "2026-09-28T20:00:00-04:00")
          .replace("Friends of Herb, Week 3, 2026.", "Friends of Herb, Week 3 Monday Night Special, 2026."))
booth.sweep(doc)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "foh", "mnf-week-3.html")
open(out, "w").write(doc)
print("wrote", out, len(doc))
