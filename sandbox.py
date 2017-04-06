from unit_class import Unit
from cc_round import *

orc = Unit(name = "Orc", models = 20, WS = 3, S = 4, T = 3, I = 3, Sv = 6, Ld = 7)
dwarf = Unit(name = "Dwarf", models = 15, WS = 3, S = 3, T = 3, I = 3, Sv = 4, Ld = 8)


cc_round(orc, dwarf)


print("Orc models:" + str(orc.models))
print("Dwarf models:" + str(dwarf.models))