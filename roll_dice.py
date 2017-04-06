# Library import
import random

def roll_dice(n_rolls, success_plus):

    # Create empty list
    roll_results = []

    # Roll n_roll dice
    for i in range(0, n_rolls):
        # Add roll result to list
        roll_results.append(random.randint(1,6))

    # Count number of rolls equal to or greater than success_plus

    tmp = [i for i in roll_results if i >= success_plus]
    n_success = len(tmp)
    return n_success;


def ld_test(ld_value):
    # ld_value is the number to be rolled equal to or below
    # Two possible output values (as strings), "Pass" or "Fail"
    # Create empty list
    roll_results = []

    # Roll 2d6
    roll_results.append(random.randint(1,6) + random.randint(1,6))

    # See if result is equal to or below ld_value
    if roll_results[0] <= ld_value:
        return "Pass";
    else:
        return "Fail";



