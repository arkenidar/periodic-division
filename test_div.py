import unittest
from div import divide_with_period

class TestDivision(unittest.TestCase):
    def test_basic_division(self):
        """Test simple division with remainder"""
        self.assertEqual(divide_with_period(10, 3), "3.(3)")

    def test_repeating_decimal(self):
        """Test division with repeating decimal"""
        self.assertEqual(divide_with_period(22, 7), "3.(142857)")

    def test_non_repeating_decimal(self):
        """Test division that terminates"""
        self.assertEqual(divide_with_period(1, 2), "0.5")

    def test_division_by_zero(self):
        """Test division by zero raises exception"""
        with self.assertRaises(ValueError):
            divide_with_period(22, 0)

    def test_negative_numbers(self):
        """Test division with negative numbers"""
        self.assertEqual(divide_with_period(-22, 7), "-3.(142857)")

    def test_known_fractions(self):
        """Test known fraction results"""
        test_cases = [
            (1, 3, "0.(3)"),
            (1, 6, "0.1(6)"),
            (1, 7, "0.(142857)"),
            (2, 5, "0.4"),
        ]
        for numerator, denominator, expected in test_cases:
            self.assertEqual(divide_with_period(numerator, denominator), expected)


if __name__ == "__main__":
    unittest.main()
