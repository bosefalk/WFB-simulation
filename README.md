# WFB-simulation

Simulates a Warhammer Fantasy close combat battle between two user-defined units. Currently quite basic simulation:

* Determines who attacks first based on Initiative, and rolls to hit, to wound, armour save (adjusted by S), followed by counterattack by any surviving models
* Break test for loser adjusted by combat score (currently combat score is based only on numer of Wounds caused, no other adjustments)
* If no unit failed the break test and is not wiped out, continues for another round of combat
* Currently assumes all models can attack once, and has one W each
* Currently no special rules, weapons, champions etc are incorporated

To run several simulations of a battle between two units, in python console first import wfb_simulation, then define the the Units and run the simulation function:

```python
from wfb_simulation import *
orc = Unit(name="Orc", models=20, WS=3, S=4, T=3, I=3, Sv=6, Ld=7)
dwarf = Unit(name="Dwarf", models=20, WS=3, S=3, T=4, I=2, Sv=4, Ld=8)
wfb_simulation(orc, dwarf, runs = 20, filename = "dwarf_vs_orc")
```

The results of each simulated battle is a row printed in the dwarf_vs_orc.csv file (default name is results.csv if filename is blank), with details on who won, how many rounds it took, and the final units sizes at the battle end.

