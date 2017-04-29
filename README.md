# WFB-simulation

Simulates a Warhammer Fantasy close combat battle (8th ed) between two user-defined units. Currently quite basic simulation:

* Determines who attacks first based on Initiative, and rolls to hit, to wound, armour save (adjusted by S), followed by counterattack by any surviving models
* Break test for loser adjusted by combat score (currently combat score is based only on number of Wounds caused, no other adjustments)
* If no unit failed the break test and is not wiped out, continues for another round of combat
* Currently assumes all models can attack once, and has one W each
* Currently no special rules, weapons, champions etc

Running [here](http://172.104.131.71) 

