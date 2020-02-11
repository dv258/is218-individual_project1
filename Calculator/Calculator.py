from Calculator.Addition import Addition
from Calculator.Subtraction import Subtraction
from Calculator.Multiplication import Multiplication
from Calculator.Division import Division
from Calculator.Exponentiation import Exponentiation
from Calculator.NthRoot import NthRoot
from Calculator.Logarithm import Logarithm


class Calculator:
    def __init__(self):
        self.result = 0

    def addition(self, augend, addend=None):
        self.result = Addition.addition(augend, addend)
        return self.result

    def subtraction(self, minuend, subtrahend):
        self.result = Subtraction.subtraction(minuend, subtrahend)
        return self.result

    def multiplication(self, multiplier, multiplicand):
        self.result = Multiplication.multiplication(multiplier, multiplicand)
        return self.result

    def division(self, numerator, denominator):
        self.result = Division.division(numerator, denominator)
        return self.result

    def exponentiation(self, base, exponent):
        self.result = Exponentiation.exponentiation(base, exponent)
        return self.result

    def nthRoot(self, radicand, degree):
        self.result = NthRoot.nthRoot(radicand, degree)
        return self.result

    def logarithm(self, antilogarithm, base):
        self.result = Logarithm.logarithm(antilogarithm, base)
        return self.result
