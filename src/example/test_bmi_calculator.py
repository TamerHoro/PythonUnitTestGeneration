import bmi_calculator
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(767,200,20)
	cut.height = 735
	cut.age = 74
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.age = 94
	cut.classify_bmi_adults()
	cut.height = 872


def test_1():
	cut = bmi_calculator.BMICalc(122,317,44)
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.age = 3
	cut.height = 701
	cut.weight = 510
	cut.age = 145
	cut.age = 27
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()


def test_2():
	cut = bmi_calculator.BMICalc(193,80,51)
	cut.age = 1
	cut.age = 63
	cut.height = 880
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.age = 44
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()


def test_3():
	cut = bmi_calculator.BMICalc(352,797,33)
	cut.weight = 393
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.age = 125
	cut.weight = 778
	cut.weight = 892
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.height = 386
	cut.height = 944
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.weight = 941
	cut.age = 11


def test_4():
	cut = bmi_calculator.BMICalc(289,54,141)
	cut.height = 936
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.weight = 781
	cut.weight = 373
	cut.height = 462
	cut.bmi_value()
	cut.height = 392
	cut.weight = 624
	cut.height = 648
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()


def test_5():
	cut = bmi_calculator.BMICalc(82,203,67)
	cut.bmi_value()
	cut.height = 628
	cut.age = 14
	cut.height = 492
	cut.bmi_value()
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.weight = 872
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.age = 137
	cut.height = 596
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.weight = 770


def test_6():
	cut = bmi_calculator.BMICalc(140,124,2)
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.height = 335
	cut.weight = 780
