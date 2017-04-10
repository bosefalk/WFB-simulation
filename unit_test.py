import unittest
from roll_dice import *
import random
from statistics import mean


# Tests for roll_dice

class roll_dice_test(unittest.TestCase):
    def test_return_int(self):
        # Should return an integer
        out = roll_dice(10, 4)
        self.assertTrue(type(out) == int)

    def test_seed1(self):
        # Should return 7 passed rolls with this seed
        random.seed(100)
        out = roll_dice(10, 4)
        self.assertEqual(out, 7)

    def test_seed2(self):
        # Should return 85 successful rolls
        random.seed(7124)
        out = roll_dice(100, 2)
        self.assertEqual(out, 85)

    def test_greater(self):
        # Tests that if running 1000 rolls, the average passes where the number needed for success is 4
        # is higher than 1000 rolls where it is 5
        out_list_4 = []
        for i in range(0, 1000):
            out_list_4.append(roll_dice(10, 4))

        out_list_5 = []
        for i in range(0, 1000):
            out_list_5.append(roll_dice(10, 5))

        self.assertTrue(mean(out_list_4) > mean(out_list_5))


class ld_roll_test(unittest.TestCase):
    def test_return_int(self):
        # Roll return should be integer, result should be string
        out = ld_test(7)
        self.assertTrue(type(out.result) == str)
        self.assertTrue(type(out.roll) == int)

    def test_seed1(self):
        # Expects pass result with a roll of
        random.seed(578)
        out = ld_test(7)
        self.assertEqual(out.result, "Pass")
        self.assertEqual(out.roll, 5)




if __name__ == '__main__':
    unittest.main()
