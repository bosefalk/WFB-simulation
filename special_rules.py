from unit_class import *
from copy import deepcopy


class Return_special_rules(object):
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

def special_rules(attacker, defender, log, round):

    att_copy = deepcopy(attacker)
    def_copy = deepcopy(defender)

    if att_copy.choppas == True and round == 1:
        log.write(str(att_copy.name) + " has choppas, +1S" + '\n')
        att_copy.S = att_copy.S + 1


    return Return_special_rules(attacker = att_copy, defender=def_copy)