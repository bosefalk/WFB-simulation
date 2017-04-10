import unittest
from roll_dice import *
import random
from statistics import mean
from compare_characteristics import *


# Tests for roll_dice

class roll_dice_test(unittest.TestCase):
    def test_return_int(self):
        # Should return an integer
        out = roll_dice(random.randint(0, 100), random.randint(0, 10))
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
        out = ld_test(random.randint(0, 20))
        self.assertTrue(type(out.result) == str)
        self.assertTrue(type(out.roll) == int)

    def test_seed1(self):
        # Expects pass result with set seed
        random.seed(578)
        out = ld_test(7)
        self.assertEqual(out.result, "Pass")
        self.assertEqual(out.roll, 5)

    def test_result_is_2(self):
        # With random.seed(2), the rolls should be 2, check it passes even with lower Ld
        random.seed(2)
        out = ld_test(-2)
        self.assertTrue(out.result == "Pass")
        self.assertTrue(out.roll == 2)


# Unit tests for compare characteristics


class to_hit_test(unittest.TestCase):

    def test_return_int(self):
        # Should return an integer between 3 and 5, given any inputs between 1 and 9
        out = to_hit(random.randint(1, 9), random.randint(1,9))
        self.assertTrue(type(out) == int)
        self.assertTrue(3 <= out <= 5)

    # A couple of spotchecks making sure the to-hit calculations are correct
    def test_spot_checks(self):
        self.assertEqual(to_hit(3, 3), 4)
        self.assertEqual(to_hit(4, 3), 3)
        self.assertEqual(to_hit(3, 4), 4)
        self.assertEqual(to_hit(3, 5), 4)
        self.assertEqual(to_hit(3, 6), 4)
        self.assertEqual(to_hit(3, 7), 5)
        self.assertEqual(to_hit(2, 4), 4)
        self.assertEqual(to_hit(2, 5), 5)
        self.assertEqual(to_hit(5, 2), 3)
        self.assertEqual(to_hit(3, 2), 3)
        self.assertEqual(to_hit(4, 2), 3)


class to_wound_test(unittest.TestCase):

    def test_return_int(self):
        # Should return integer between 2 and 6 given random inputs (between 1 and 9)
        out = to_wound(random.randint(1,9), random.randint(1, 9))
        self.assertTrue(type(out) == int)
        self.assertTrue(2 <= out <= 6)

    # Spotchecks for a few common combinations
    def test_spot_checks(self):
        self.assertEqual(to_wound(3, 3), 4)
        self.assertEqual(to_wound(4, 3), 3)
        self.assertEqual(to_wound(3, 4), 5)
        self.assertEqual(to_wound(5, 3), 2)
        self.assertEqual(to_wound(3, 5), 6)
        self.assertEqual(to_wound(6, 3), 2)
        self.assertEqual(to_wound(3, 6), 6)
        self.assertEqual(to_wound(7, 3), 2)
        self.assertEqual(to_wound(3, 7), 6)
        self.assertEqual(to_wound(8, 3), 2)
        self.assertEqual(to_wound(3, 8), 6)
        self.assertEqual(to_wound(2, 3), 5)
        self.assertEqual(to_wound(4, 2), 2)

class armour_save_test(unittest.TestCase):

    def test_return_int(self):
        # Should return integer for any input value
        out = armour_save(random.randint(0, 10), random.randint(0, 10))
        self.assertTrue(type(out) == int)

    def test_less_than_2(self):
        # Check that if save is less than 2, a 2+ roll is still returned
        out = armour_save(3, 1)
        self.assertTrue(out >= 2)

    def test_spot_checks(self):
        # A couple of spot checks on common combinations
        self.assertEqual(armour_save(3, 5), 5)
        self.assertEqual(armour_save(4, 5), 6)
        self.assertEqual(armour_save(5, 5), 7)
        self.assertEqual(armour_save(2, 4), 4)
        self.assertEqual(armour_save(4, 2), 3)
        self.assertEqual(armour_save(5, 2), 4)
        self.assertEqual(armour_save(4, 1), 2)
        self.assertEqual(armour_save(4, -1), 2)
        self.assertEqual(armour_save(7, -1), 3)
        

if __name__ == '__main__':
    unittest.main()
