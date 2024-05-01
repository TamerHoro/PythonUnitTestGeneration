import bmi_calculator
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(86,531,97)
	cut.age = 1


def test_1():
	cut = bmi_calculator.BMICalc(242,298,74)
	cut.age = 57
	cut.classify_bmi_adults()
	cut.height = 522
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.weight = 72
	cut.height = 551
	cut.weight = 914


def test_2():
	cut = bmi_calculator.BMICalc(970,935,15)
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()


def test_3():
	cut = bmi_calculator.BMICalc(943,801,2)
	cut.classify_bmi_teens_and_children()


def test_4():
	cut = bmi_calculator.BMICalc(661,784,5)
	cut.classify_bmi_teens_and_children()
	cut.height = 75
	cut.classify_bmi_teens_and_children()


def test_5():
	cut = bmi_calculator.BMICalc(394,555,127)
	cut.classify_bmi_adults()


def test_6():
	cut = bmi_calculator.BMICalc(77,480,103)
	cut.age = -1


def test_7():
	cut = bmi_calculator.BMICalc(964,110,12)
	cut.classify_bmi_teens_and_children()
	cut.weight = 806
	cut.classify_bmi_adults()
	cut.weight = 315
	cut.classify_bmi_adults()
	cut.weight = 969
	cut.height = 70
	cut.bmi_value()
	cut.weight = 560
	cut.bmi_value()


def test_8():
	cut = bmi_calculator.BMICalc(44,506,28)
	cut.height = 504
	cut.classify_bmi_adults()


def test_9():
	cut = bmi_calculator.BMICalc(358,367,3)
	cut.classify_bmi_teens_and_children()


def test_10():
	cut = bmi_calculator.BMICalc(881,569,9)
	cut.weight = 652
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.height = 631
	cut.height = 777
	cut.classify_bmi_adults()
