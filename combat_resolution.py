from unit_class import *

# Calculates combat resultion results
class Return_combat_resolution(object):
    def __init__(self, unit1_score, unit2_score, winner, loser, loser_diff):
        self.unit1_score = unit1_score
        self.unit2_score = unit2_score
        self.winner = winner
        self.loser = loser
        self.loser_diff = loser_diff

def combat_resolution(unit1, unit2, to_remove_unit1, to_remove_unit2, log, round = 1):
    unit1_score = to_remove_unit2
    if unit1.standard == True:
        log.write(str(unit1.name) + " has Standard" + '\n')
        unit1_score = unit1_score + 1

    unit2_score = to_remove_unit1
    if unit2.standard == True:
        log.write(str(unit2.name) + " has Standard" + '\n')
        unit2_score = unit2_score + 1

    if unit1.charge == True and round == 1:
        log.write(str(unit1.name) + " charged" + '\n')
        unit1_score = unit1_score + 1

    if unit2.charge == True and round == 1:
        log.write(str(unit2.name) + " charged" + '\n')
        unit2_score = unit2_score + 1

    log.write("Combat Score: " + str(unit1.name) + " " + str(unit1_score) + " vs " + str(unit2.name) + " " + str(
        unit2_score) + '\n')

    if unit1_score > unit2_score:
        loser = unit2
        winner = unit1
        loser_diff = unit1_score - unit2_score
        log.write(str(unit2.name) + " lost the round by " + str(loser_diff) + '\n')

    if unit1_score < unit2_score:
        loser = unit1
        winner = unit2
        loser_diff = unit2_score - unit1_score
        log.write(str(unit1.name) + " lost the round by " + str(loser_diff) + '\n')

    if unit1_score == unit2_score:
        if unit1.musician == True:
            log.write(str(unit1.name) + " has musician" + '\n')
        if unit2.musician == True:
            log.write(str(unit2.name) + " has musician" + '\n')

        if unit1.musician == False and unit2.musician == False:

            log.write("Round was a draw" + '\n')
            return Return_combat_resolution(unit1_score = unit1_score,
                                       unit2_score = unit1_score,
                                       loser = None, winner=None, loser_diff = 0)

        if unit1.musician == True and unit2.musician == True:
            log.write("Round was a draw" + '\n')
            return Return_combat_resolution(unit1_score=unit1_score,
                                            unit2_score=unit1_score,
                                            loser=None, winner=None, loser_diff=0)

        if unit1.musician == True and unit2.musician == False:
            loser = unit2
            winner = unit1
            loser_diff = 0

        if unit1.musician == False and unit2.musician == True:
            loser = unit1
            winner = unit2
            loser_diff = 0



    return Return_combat_resolution(unit1_score = unit1_score, unit2_score = unit2_score,
                                   loser = loser, winner = winner, loser_diff = loser_diff)