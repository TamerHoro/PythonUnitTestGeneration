import calculator
import pytest


def test_0():
	cut = calculator.Calc()
	result = 	cut.divide(2,4)
	result = 	cut.multiply(-3,-1)
	result = 	cut.multiply(6,7)
	result = 	cut.subtract(75,121)
	result = 	cut.subtract(98,140)
	result = 	cut.subtract(113,77)
	result = 	cut.divide(-3,6)
	result = 	cut.add(136,33)


def test_1():
	cut = calculator.Calc()
	result = 	cut.multiply(7,6)
	result = 	cut.add(16,3)
	result = 	cut.add(142,141)
	result = 	cut.multiply(-3,7)
	result = 	cut.add(125,122)
