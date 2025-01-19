import unittest


from zodiac_calculator import calculate_zodiac

class ZoadiacCalculatorTest(unittest.TestCase):

    def test_zodiac_calculator(self):
        self.assertEqual(calculate_zodiac(2, 28), "Pisces")
        self.assertEqual(calculate_zodiac(12, 17), "Sagittarius")
        self.assertEqual(calculate_zodiac(4, 10), "Aries")


if __name__ == '__main__':
    unittest.main()