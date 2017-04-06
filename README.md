# WFB-simulation

To simulate one battle, after importing everything from unit_class and cc_round, define the two combatants like this:

orc = Unit(name="Orcs", models=20, WS=3, S=4, T=3, I=3, Sv=6, Ld=7)
dwarf = Unit(name="Dwarf", models=20, WS=3, S=3, T=4, I=2, Sv=4, Ld=8)

Then run

close_combat(orc, dwarf)

and see the results in the log.txt file.

To run several simulations, see the run_simulations.py file.

Currently the simulation incorporates who attacks first based on Initiative, and rolls to hit, to wound, armour save (adjusted by S). However the break test is only modified by number of Wounds caused, no other adjustments (standards, steadfast etc). It also assumes all models in a unit can attack.

