# Library import
import random

# Given the number of rolls and the value to roll equal to or above (i.e. 4+), returns number of successes
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




# Temp class for returning both roll and pass / fail result of leadership tests
class Return_ld_test(object):
  def __init__(self, result, roll):
     self.result = result
     self.roll = roll

# Given a (possibly modified) Ld value, rolls 2d6 and records "Pass" if equal or below
def ld_test(ld_value):
    # ld_value is the number to be rolled equal to or below
    # Create empty list
    roll_results = []

    # Roll 2d6
    roll_results.append(random.randint(1,6) + random.randint(1,6))

    roll = roll_results[0]

    if roll <= ld_value:
        result = "Pass"
    else:
        result = "Fail"

    return Return_ld_test(roll = roll, result = result)



