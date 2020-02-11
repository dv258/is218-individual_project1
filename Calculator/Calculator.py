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

    def sum(self, augend, addend=None):
        self.result = Addition.sum(augend, addend)
        return self.result

    def difference(self, minuend, subtrahend):
        self.result = Subtraction.difference(minuend, subtrahend)
        return self.result

    def product(self, multiplier, multiplicand):
        self.result = Multiplication.product(multiplier, multiplicand)
        return self.result

    def quotient(self, numerator, denominator):
        self.result = Division.quotient(numerator, denominator)
        return self.result

    def power(self, base, exponent):
        self.result = Exponentiation.power(base, exponent)
        return self.result

    def root(self, radicand, degree):
        self.result = NthRoot.root(radicand, degree)
        return self.result

    def logarithm(self, antilogarithm, base):
        self.result = Logarithm.logarithm(antilogarithm, base)
        return self.result
