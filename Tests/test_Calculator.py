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

    def test_static_Addition(self):
        self.assertEqual(6, Addition.addition(4, 2))

    def test_static_AdditionList(self):
        self.assertEqual(14, Addition.addition([4, 2, 8]))

    def test_static_Subtraction(self):
        self.assertEqual(-2, Subtraction.subtraction(2, 4))

    def test_static_Multiplication(self):
        self.assertEqual(20, Multiplication.multiplication(4, 5))

    def test_static_Division(self):
        self.assertEqual(6, Division.division(12, 2))

    def test_static_Exponentiation(self):
        self.assertEqual(36, Exponentiation.exponentiation(6, 2))

    def test_static_NthRoot(self):
        self.assertEqual(2, NthRoot.nthRoot(4, 2))

    def test_static_Logarithm(self):
        self.assertEqual(3, Logarithm.logarithm(8, 2))

    def test_instantiate(self):
        self.assertIsInstance(self.calc, Calculator)

    def test_addition(self):
        result = self.calc.addition(2, 2)
        self.assertEqual(4, result)

    def test_addition_list(self):
        result = self.calc.addition([5, 2, 7, 1])
        self.assertEqual(15, result)

    def test_subtraction(self):
        result = self.calc.subtraction(7, 4)
        self.assertEqual(3, result)

    def test_multiplication(self):
        result = self.calc.multiplication(-2, 6)
        self.assertEqual(-12, result)

    def test_division(self):
        result = self.calc.division(8, 4)
        self.assertEqual(2, result)

    def test_exponentiation(self):
        result = self.calc.exponentiation(4, 2)
        self.assertEqual(16, result)

    def test_nthRoot(self):
        result = self.calc.nthRoot(8, 3)
        self.assertEqual(2, result)

    def test_logarithm(self):
        result = self.calc.logarithm(8, 2)
        self.assertEqual(3, result)


if __name__ == "__main__":
    unittest.main()
