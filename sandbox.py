from collections import Counter

from unit_class import Unit
from cc_round import *



#cont = cc_round(orc, dwarf)
#print(cont)

loser_list = []
no_rounds = []


for i in range(0, 1000):
    orc = Unit(name="Orc", models=20, WS=3, S=4, T=3, I=3, Sv=6, Ld=7)
    dwarf = Unit(name="Dwarf", models=20, WS=3, S=3, T=4, I=2, Sv=4, Ld=8)

    c_result = close_combat(orc, dwarf)

    if c_result.loser == None:
        loser_list.append("Both")
        no_rounds.append(c_result.round)
        continue

    loser_list.append(c_result.loser.name)
    no_rounds.append(c_result.round)

print(Counter(loser_list).keys())
print(Counter(loser_list).values())