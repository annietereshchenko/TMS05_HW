import unittest
from calculator import Calculator


class TestCalculatorPositive(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCalculatorPositive, self).__init__(*args, **kwargs)
        self.calc = Calculator()

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

    def __init__(self, *args, **kwargs):
        super(TestCalculatorNegative, self).__init__(*args, **kwargs)
        self.calc = Calculator()

    @unittest.expectedFailure
    def test_failed_sum(self):
        self.assertEqual(self.calc.sum(4, 2), 7)

    @unittest.expectedFailure
    def test_failed_sub(self):
        self.assertEqual(self.calc.subtraction(12, 2), 9)

    @unittest.expectedFailure
    def test_failed_multiple(self):
        self.assertEqual(self.calc.multiplication(5, 4), 3)

    @unittest.expectedFailure
    def test_failed_div(self):
        self.assertEqual(self.calc.division(12, 6), 3)


if __name__ == '__main__':
    unittest.main()
