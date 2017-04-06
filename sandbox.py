from roll_dice import roll_dice
from compare_characteristics import *

#roll1 = roll_dice(10, 4)
#roll2 = roll_dice(roll1, 5)
#print(roll2)

# Attacker WS4, S4, defender WS 3, T3, Save 4+
hits = roll_dice(10, to_hit(4, 3))
wounds = roll_dice(hits, to_wound(4, 3))
saves = roll_dice(wounds, armour_save(4, 4))
wounds_final = wounds - saves

print("Hits: " + str(hits))
print("Wounds: " + str(wounds))
print("Saves: " + str(saves))
print("Final Wounds: " + str(wounds_final))






