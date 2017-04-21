from unit_class import Unit
from wfb_simulation import *

#cont = cc_round(orc, dwarf)
#print(cont)

orc = Unit(name="Orc", models=20, WS=3, S=4, T=3, I=3, Sv=6, Ld=7)
dwarf = Unit(name="Dwarf", models=20, WS=3, S=3, T=4, I=2, Sv=4, Ld=8)

wfb_simulation(orc, dwarf, 100)
# test