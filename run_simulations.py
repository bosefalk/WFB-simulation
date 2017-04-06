from collections import Counter

from unit_class import Unit
from cc_round import *

# loser_list makes a note of the loser of the battle, no_rounds notes the number of rounds it took to get the result
loser_list = []
no_rounds = []

# Run simulations - at the top need to initialize the Unit objects
for i in range(0, 300):
    orc = Unit(name="Goblin", models=35, WS=2, S=3, T=3, I=2, Sv=6, Ld=7)
    dwarf = Unit(name="Dwarf", models=20, WS=3, S=3, T=4, I=2, Sv=4, Ld=8)

    c_result = close_combat(orc, dwarf)

    # If both units were wiped out (only possible if they same the same I), record that Both lost
    if c_result.loser == None:
        loser_list.append("Both")
        no_rounds.append(c_result.round)
        continue

    loser_list.append(c_result.loser.name)
    no_rounds.append(c_result.round)

# Prints the number of losses for each unit
print(Counter(loser_list).keys())
print(Counter(loser_list).values())