import calculator
import pytest


def test_0():
	cut = calculator.Calc()
	result = 	cut.multiply(-5,3)
	result = 	cut.subtract(128,10)
	result = 	cut.add(63,147)


def test_1():
	cut = calculator.Calc()
	result = 	cut.divide(-1,-7)
