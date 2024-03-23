import bmi_calculator
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(243,486,68)
	cut.age = 8
	cut.classify_bmi_teens_and_children()
	cut.age = 107
	cut.height = 395
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.height = 92
	cut.classify_bmi_adults()
	cut.weight = 985
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()


def test_1():
	cut = bmi_calculator.BMICalc(193,471,36)
	cut.age = 98
	cut.bmi_value()
	cut.bmi_value()
	cut.age = 110
	cut.age = 40
	cut.classify_bmi_adults()
	cut.height = 326
	cut.age = 83


def test_2():
	cut = bmi_calculator.BMICalc(753,705,0)


def test_3():
	cut = bmi_calculator.BMICalc(832,284,84)
	cut.age = 2
	cut.classify_bmi_teens_and_children()


def test_4():
	cut = bmi_calculator.BMICalc(340,94,69)
	cut.height = 303
	cut.height = 304
	cut.weight = 185
	cut.classify_bmi_adults()


def test_5():
	cut = bmi_calculator.BMICalc(773,528,11)
	cut.classify_bmi_teens_and_children()
	cut.weight = 522
	cut.age = 144
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.age = 81
	cut.bmi_value()


def test_6():
	cut = bmi_calculator.BMICalc(117,382,3)
	cut.classify_bmi_teens_and_children()
	cut.height = 900
	cut.age = 96
	cut.age = 94
	cut.classify_bmi_adults()


def test_7():
	cut = bmi_calculator.BMICalc(821,597,19)
	cut.classify_bmi_teens_and_children()


def test_8():
	cut = bmi_calculator.BMICalc(173,459,150)
	cut.age = 5
	cut.classify_bmi_teens_and_children()


def test_9():
	cut = bmi_calculator.BMICalc(892,307,15)
	cut.classify_bmi_teens_and_children()
	cut.weight = 696
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.age = 70
	cut.classify_bmi_teens_and_children()
	cut.weight = 216
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()


def test_10():
	cut = bmi_calculator.BMICalc(99,371,133)
	cut.age = 5
	cut.height = 862
	cut.classify_bmi_teens_and_children()
