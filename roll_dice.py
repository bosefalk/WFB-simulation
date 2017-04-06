# Library import
import random

def roll_dice(n_rolls, success_plus):

    # Create empty list
    roll_results = []

    # Roll n_roll dice
    for i in range(1, n_rolls):
        # Add roll result to list
        roll_results.append(random.randint(1,6))

    # Count number of rolls equal to or greater than success_plus
    tmp = [i for i in roll_results if i >= success_plus]
    n_success = len(tmp)
    return n_success


