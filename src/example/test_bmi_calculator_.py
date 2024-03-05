import bmi_calculator
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(733,662,14)
	cut.height = 520
	cut.bmi_value()
	cut.bmi_value()
	cut.bmi_value()
	cut.height = 960
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.bmi_value()
	cut.weight = 663
	cut.weight = 663
	cut.height = 666
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.age = 138


def test_1():
	cut = bmi_calculator.BMICalc(608,287,131)
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.age = 69
	cut.height = 791
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.height = 799
	cut.weight = 104
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.weight = 438
	cut.weight = 593
	cut.bmi_value()


def test_2():
	cut = bmi_calculator.BMICalc(150,311,147)
	cut.bmi_value()
	cut.height = 443
	cut.height = 199
	cut.weight = 651
	cut.bmi_value()
	cut.age = 46
	cut.bmi_value()
	cut.age = 64
	cut.weight = 128
	cut.classify_bmi_teens_and_children()
	cut.height = 917
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()


def test_3():
	cut = bmi_calculator.BMICalc(76,280,68)
	cut.classify_bmi_adults()


def test_4():
	cut = bmi_calculator.BMICalc(369,225,26)
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.weight = 628
	cut.classify_bmi_adults()


def test_5():
	cut = bmi_calculator.BMICalc(267,547,100)
	cut.classify_bmi_adults()
	cut.age = -1
	cut.weight = 9
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.weight = 39
	cut.weight = 782
	cut.height = 233
	cut.bmi_value()
	cut.bmi_value()
	cut.weight = 181
	cut.classify_bmi_teens_and_children()
	cut.age = 133
