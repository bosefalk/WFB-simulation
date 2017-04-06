from roll_dice import *
from compare_characteristics import *
from unit_class import Unit

#roll1 = roll_dice(10, 4)
#roll2 = roll_dice(roll1, 5)
#print(roll2)

# Attacker WS4, S4, defender WS 3, T3, Save 4+
#hits = roll_dice(10, to_hit(4, 3))
#wounds = roll_dice(hits, to_wound(4, 3))
#saves = roll_dice(wounds, armour_save(4, 4))
#wounds_final = wounds - saves

#print("Hits: " + str(hits))
#print("Wounds: " + str(wounds))
#print("Saves: " + str(saves))
#print("Final Wounds: " + str(wounds_final))


orc = Unit(models = 20, WS = 3, S = 4, T = 3, Sv = 6, Ld = 7)
dwarf = Unit(models = 15, WS = 3, S = 3, T = 4, Sv = 4, Ld = 8)

print("Number of dwarfs: " + str(dwarf.models))

# Orcs attacking dwarfs
hits = roll_dice(orc.models, to_hit(orc.WS, dwarf.WS))
wounds = roll_dice(hits, to_wound(orc.S, dwarf.T))
saves = roll_dice(wounds, armour_save(orc.S, dwarf.Sv))
wounds_final = wounds - saves

print("Hits: " + str(hits))
print("Wounds: " + str(wounds))
print("Saves: " + str(saves))
print("Final Wounds: " + str(wounds_final))

break_test = ld_test(dwarf.Ld - wounds_final)
print("Break test:" + break_test)
