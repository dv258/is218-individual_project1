import unittest

from Calculator.Addition import Addition
from Calculator.Subtraction import Subtraction
from Calculator.Multiplication import Multiplication
from Calculator.Division import Division
from Calculator.Exponentiation import Exponentiation
from Calculator.NthRoot import NthRoot
from Calculator.Logarithm import Logarithm

from Calculator.Calculator import Calculator


class TestCases(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_static_sum(self):
        self.assertEqual(6, Addition.sum(4, 2))

    def test_static_sum_list(self):
        self.assertEqual(14, Addition.sum([4, 2, 8]))

    def test_static_difference(self):
        self.assertEqual(-2, Subtraction.difference(2, 4))

    def test_static_product(self):
        self.assertEqual(20, Multiplication.product(4, 5))

    def test_static_quotient(self):
        self.assertEqual(6, Division.quotient(12, 2))

    def test_static_power(self):
        self.assertEqual(36, Exponentiation.power(6, 2))

    def test_static_root(self):
        self.assertEqual(2, NthRoot.root(4, 2))

    def test_static_logarithm(self):
        self.assertEqual(3, Logarithm.logarithm(8, 2))

    def test_instantiate(self):
        self.assertIsInstance(self.calc, Calculator)

    def test_sum(self):
        result = self.calc.sum(2, 2)
        self.assertEqual(4, result)

    def test_sum_list(self):
        result = self.calc.sum([5, 2, 7, 1])
        self.assertEqual(15, result)

    def test_difference(self):
        result = self.calc.difference(7, 4)
        self.assertEqual(3, result)

    def test_product(self):
        result = self.calc.product(-2, 6)
        self.assertEqual(-12, result)

    def test_quotient(self):
        result = self.calc.quotient(8, 4)
        self.assertEqual(2, result)

    def test_power(self):
        result = self.calc.power(4, 2)
        self.assertEqual(16, result)

    def test_root(self):
        result = self.calc.root(8, 3)
        self.assertEqual(2, result)

    def test_logarithm(self):
        result = self.calc.logarithm(8, 2)
        self.assertEqual(3, result)


if __name__ == "__main__":
    unittest.main()
