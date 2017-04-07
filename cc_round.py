from roll_dice import *
from compare_characteristics import *

# Calculate number of wounds taken by the defender
def cc_attack(attacker, defender, log = None):
    # attacker and defender are Unit class objects
    # log is optional logging text file

    # Rolls for success is calculated by the compare_characteristics functions
    # Attacker rolls to hit per number of models, then to wound
    # Defender rolls how many wounds are saved
    # Final return is total number of wounds taken by the defender

    to_hit_value = to_hit(attacker.WS, defender.WS)
    hits = roll_dice(attacker.models, to_hit_value)

    to_wound_value = to_wound(attacker.S, defender.T)
    wounds = roll_dice(hits, to_wound_value)

    save_value = armour_save(attacker.S, defender.Sv)
    saves = roll_dice(wounds, save_value)

    wounds_final = wounds - saves

    # If the log file isn't specified don't do any logging
    if log != None:

        log.write("Attacks: " + str(attacker.models) + '\n')
        log.write("Hits: " + str(hits) + " (" + str(to_hit_value) + "+)" + '\n')
        log.write("Wounds: " + str(wounds) + " (" + str(to_wound_value) + "+)" + '\n')
        log.write("Saves: " + str(saves) + " (" + str(save_value) + "+)" + '\n')
        log.write("Final Wounds: " + str(wounds_final) + '\n')


    return wounds_final;


# Temp class for returning both roll and pass / fail result of leadership tests
class Return_cc_round(object):
  def __init__(self, winner, combat_continues):
     self.winner = winner
     self.combat_continues = combat_continues

# Calculate a round of close combat, and update the input Unit objects with remaining number of models
def cc_round(unit1, unit2, log):

    # Write output to log.txt (and pass this open connection to cc_attack)

    log.write("Combat Round Starts" + '\n')
    log.write("Number of " + str(unit1.name) + ": " + str(unit1.models) + '\n')
    log.write("Number of " + str(unit2.name) + ": " + str(unit2.models) + '\n')

    # Determine who goes first, or if simultaneous
    # The unit with lower I first removes casualties before attacking back
    if unit1.I > unit2.I:
        log.write(str(unit1.name) + " attacks first" + '\n')
        log.write(str(unit1.name) + " I: " + str(unit1.I) + " vs " + str(unit2.name) + " I: " + str(unit2.I) + '\n')

        log.write(str(unit1.name) + " attacks " + '\n')
        to_remove_unit2 = cc_attack(attacker = unit1, defender = unit2, log = log)
        unit2.models = unit2.models - to_remove_unit2
        log.write("Remaining " + str(unit2.name) + ": " + str(unit2.models) + '\n')
        if unit2.models <= 0:
            return Return_cc_round(winner = unit1, combat_continues = False)

        log.write(str(unit2.name) + " attacks " + '\n')
        to_remove_unit1 = cc_attack(attacker = unit2, defender = unit1, log = log)
        unit1.models = unit1.models - to_remove_unit1
        log.write("Remaining " + str(unit1.name) + ": " + str(unit1.models) + '\n')
        if unit1.models <= 0:
            return Return_cc_round(winner = unit2, combat_continues = False)


    if unit1.I < unit2.I:
        log.write(str(unit2.name) + " attacks first" + '\n')
        log.write(str(unit1.name) + " I: " + str(unit1.I) + " vs " + str(unit2.name) + " I: " + str(unit2.I) + '\n')

        log.write(str(unit2.name) + " attacks " + '\n')
        to_remove_unit1 = cc_attack(attacker = unit2, defender = unit1, log = log)
        unit1.models = unit1.models - to_remove_unit1
        log.write("Remaining " + str(unit1.name) + ": " + str(unit1.models) + '\n')
        if unit1.models <= 0:
            return Return_cc_round(winner = unit2, combat_continues = False)

        log.write(str(unit1.name) + "attacks" + '\n')
        to_remove_unit2 = cc_attack(attacker = unit1, defender = unit2, log = log)
        unit2.models = unit2.models - to_remove_unit2
        log.write("Remaining " + str(unit2.name) + ": " + str(unit2.models) + '\n')
        if unit2.models <= 0:
            return Return_cc_round(winner = unit1, combat_continues = False)


    if unit1.I == unit2.I:
        log.write("Simultaneous attacks" + '\n')
        log.write(str(unit1.name) + " I: " + str(unit1.I) + " vs " + str(unit2.name) + " I: " + str(unit2.I) + '\n')

        log.write(str(unit2.name) + " attacks " + '\n')
        to_remove_unit1 = cc_attack(attacker = unit2, defender = unit1, log = log)

        log.write(str(unit1.name) + " attacks " + '\n')
        to_remove_unit2 = cc_attack(attacker = unit1, defender = unit2, log = log)


        unit1.models = unit1.models - to_remove_unit1
        log.write("Remaining " + str(unit1.name) + ": " + str(unit1.models) + '\n')

        unit2.models = unit2.models - to_remove_unit2
        log.write("Remaining " + str(unit2.name) + ": " + str(unit2.models) + '\n')

        if unit2.models <= 0 and unit1.models > 0:
            return Return_cc_round(winner = unit1, combat_continues=False)
        if unit1.models <= 0 and unit2.models > 0:
            return Return_cc_round(winner=unit2, combat_continues=False)
        if unit2.models <= 0 and unit1.models <= 0:
            return Return_cc_round(winner=None, combat_continues=False)

    # Break test
    adj_w_unit1 = to_remove_unit2
    adj_w_unit2 = to_remove_unit1

    log.write("Combat Score: " + str(unit1.name) + " " + str(adj_w_unit1) + " vs " + str(unit2.name) + " " + str(adj_w_unit2) + '\n')

    if adj_w_unit1 > adj_w_unit2:
        loser = unit2
        winner = unit1
        loser_diff = adj_w_unit1 - adj_w_unit2
        log.write(str(unit2.name) + " lost the round by " + str(loser_diff) + '\n')

    if adj_w_unit1 < adj_w_unit2:
        loser = unit1
        winner = unit2
        loser_diff = adj_w_unit2 - adj_w_unit1
        log.write(str(unit1.name) + " lost the round by " + str(loser_diff) + '\n')

    if adj_w_unit1 == adj_w_unit2:
        log.write("Round was a draw" + '\n')
        combat_continues = True
        return Return_cc_round(winner = None, combat_continues = True)

    break_value = loser.Ld - loser_diff
    break_result = ld_test(break_value)

    log.write(str(loser.name) + " break test against modified Ld " + str(break_value) + '\n')
    log.write("Roll: " + str(break_result.roll) + '\n')
    log.write("Break test result: " + break_result.result + '\n')

    if break_result.result == "Fail":
        combat_continues = False
    else:
        combat_continues = True

    log.write("Combat Round ends" + '\n')


    return Return_cc_round(winner = winner, combat_continues = combat_continues)



# Temp class for returning overall loser and number of rounds of fighting
class Return_close_combat(object):
  def __init__(self, winner, round):
     self.winner = winner
     self.round = round

# Continues the combat by iterating cc_round until one units fails a break test or is wiped out
def close_combat(unit1, unit2):

    log = open("log.txt", "w+")
    cont = True
    round = 0

    # Update cont by result of combat_continues, if this is False the loop breaks
    while cont == True:
        round = round + 1
        log.write("Combat Round " + str(round) + '\n')

        cc_result = cc_round(unit1, unit2, log = log)

        cont = cc_result.combat_continues


    winner = cc_result.winner

    if winner == None:
        log.write("Both units were wiped out")
        log.close
        return Return_close_combat(winner = None, round = round)

    log.write(str(winner.name) + " won the battle")
    log.close

    return Return_close_combat(winner = winner, round = round)







