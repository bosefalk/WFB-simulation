from unit_class import Unit
from copy import deepcopy
import csv
from cc_round import *


class Return_wfb_simulation:
    def __init__(self, winner, round, unit1_size, unit2_size):
         self.winner = winner
         self.round = round
         self.unit1_size = unit1_size
         self.unit2_size = unit2_size

def wfb_simulation(unit1, unit2, runs, filename = 'results'):
    # Runs simulations given two Unit objects and prints results to filename.csv

    with open(filename + ".csv", "w") as output:
        outputwriter = csv.writer(output)
        outputwriter.writerow(["Winner", "Rounds", "Final_size_" + str(unit1.name), "Final_size_" + str(unit2.name)])

        for i in range(0, runs):

            # Create a fresh copy of the Unit before each new combat to modify as the unit takes losses
            unit1_copy = deepcopy(unit1)
            unit2_copy = deepcopy(unit2)

            c_result = close_combat(unit1_copy, unit2_copy)

            # If both units were wiped out (only possible if they same the same I), record that Both lost
            if c_result.winner == None:
                outcome = Return_wfb_simulation(winner = "Both", round = c_result.round,
                                                unit1_size = unit1_copy.models,
                                                unit2_size = unit2_copy.models)
            else:
                outcome = Return_wfb_simulation(winner=c_result.winner, round=c_result.round,
                                                unit1_size=unit1_copy.models,
                                                unit2_size=unit2_copy.models)

            outputwriter.writerow([outcome.winner.name, outcome.round,
                                  outcome.unit1_size, outcome.unit2_size])


    print("Finished, results printed in " + filename + ".csv")