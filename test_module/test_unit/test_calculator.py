import unittest
from calculator import Calculator


class TestCalculatorPositive(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.sum(5, 4), 9)

    def test_sub(self):
        self.assertEqual(self.calc.subtraction(10, 7), 3)

    def test_multiple(self):
        self.assertEqual(self.calc.multiplication(3, 5), 15)

    def test_div(self):
        self.assertEqual(self.calc.division(10, 2), 5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.division(12, 0)


class TestCalculatorNegative(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_failed_sum(self):
        self.assertNotEqual(self.calc.sum(4, 2), 7)

    def test_failed_sub(self):
        self.assertNotEqual(self.calc.subtraction(12, 2), 9)

    def test_failed_multiple(self):
        self.assertNotEqual(self.calc.multiplication(5, 4), 3)

    def test_failed_div(self):
        self.assertNotEqual(self.calc.division(12, 6), 3)


if __name__ == '__main__':
    unittest.main()
