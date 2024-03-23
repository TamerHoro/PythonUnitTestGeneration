import bmi_calculator
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(243,210,43)
	cut.classify_bmi_adults()
	cut.weight = 36
	cut.classify_bmi_adults()
	cut.weight = 409
	cut.height = 891
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.height = 176
	cut.age = 40
	cut.weight = 803
	cut.height = 935
	cut.height = 684


def test_1():
	cut = bmi_calculator.BMICalc(168,350,19)
	cut.classify_bmi_teens_and_children()


def test_2():
	cut = bmi_calculator.BMICalc(240,300,135)
	cut.height = 223
	cut.classify_bmi_adults()
	cut.age = 69
	cut.bmi_value()


def test_3():
	cut = bmi_calculator.BMICalc(187,273,53)
	cut.age = 16
	cut.classify_bmi_teens_and_children()
	cut.age = 139
	cut.weight = 247
	cut.age = 140
	cut.classify_bmi_teens_and_children()
	cut.height = 121
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.weight = 365


def test_4():
	cut = bmi_calculator.BMICalc(255,156,112)
	cut.classify_bmi_adults()


def test_5():
	cut = bmi_calculator.BMICalc(401,892,18)
	cut.weight = 202
	cut.classify_bmi_teens_and_children()


def test_6():
	cut = bmi_calculator.BMICalc(988,899,1)


def test_7():
	cut = bmi_calculator.BMICalc(766,256,-1)
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()


def test_8():
	cut = bmi_calculator.BMICalc(947,759,13)
	cut.classify_bmi_teens_and_children()
	cut.weight = 165
	cut.weight = 59


def test_9():
	cut = bmi_calculator.BMICalc(290,79,117)
	cut.weight = -1
	cut.age = 29


def test_10():
	cut = bmi_calculator.BMICalc(634,787,55)
	cut.bmi_value()
	cut.age = 9
	cut.weight = 336
	cut.classify_bmi_teens_and_children()


def test_11():
	cut = bmi_calculator.BMICalc(331,864,2)
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.height = 515
	cut.bmi_value()
	cut.bmi_value()


def test_12():
	cut = bmi_calculator.BMICalc(827,873,15)
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
