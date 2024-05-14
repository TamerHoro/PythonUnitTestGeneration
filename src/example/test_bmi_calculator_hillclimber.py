import bmi_calculator
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(443,872,73)
	cut.classify_bmi_adults()
	cut.height = 776
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.height = 908
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.weight = 200
	cut.classify_bmi_adults()
	cut.weight = 265
	cut.age = 109
	cut.bmi_value()


def test_1():
	cut = bmi_calculator.BMICalc(996,858,54)
	cut.weight = 411
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.age = 124
	cut.weight = 372
	cut.classify_bmi_teens_and_children()
	cut.height = 986
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.bmi_value()


def test_2():
	cut = bmi_calculator.BMICalc(389,273,4)
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.height = 4
	cut.weight = 117
	cut.weight = 964
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.height = 287
	cut.bmi_value()
	cut.age = 123
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.age = 66
	cut.bmi_value()


def test_3():
	cut = bmi_calculator.BMICalc(290,722,8)
	cut.classify_bmi_adults()
