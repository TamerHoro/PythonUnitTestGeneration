import bmi_calculator
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(717,491,45)
	cut.classify_bmi_adults()
	cut.height = 108
	cut.height = 550
	cut.bmi_value()
	cut.bmi_value()
	cut.age = 101
	cut.weight = 647
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.height = 853
	cut.classify_bmi_adults()


def test_1():
	cut = bmi_calculator.BMICalc(634,622,60)
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.height = 437
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.weight = 890
	cut.weight = 33
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_adults()


def test_2():
	cut = bmi_calculator.BMICalc(466,662,18)
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()


def test_3():
	cut = bmi_calculator.BMICalc(118,447,22)
	cut.age = 5
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.height = 127
	cut.height = 420
	cut.weight = 864
	cut.bmi_value()
	cut.weight = 775
	cut.weight = 974
	cut.height = 869
	cut.bmi_value()
	cut.height = 690


def test_4():
	cut = bmi_calculator.BMICalc(995,866,5)
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.age = 27
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.height = 288
	cut.weight = 492
	cut.height = 361
	cut.height = 7
	cut.weight = 554
	cut.classify_bmi_adults()
	cut.bmi_value()


def test_5():
	cut = bmi_calculator.BMICalc(743,226,137)
	cut.weight = 931
	cut.bmi_value()
	cut.weight = 521
	cut.bmi_value()
	cut.height = 817
	cut.age = 140
	cut.age = 15
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.height = 775
	cut.height = 461
	cut.weight = 991
	cut.classify_bmi_teens_and_children()
	cut.height = 821
	cut.height = 965
	cut.age = 127
	cut.classify_bmi_adults()
	cut.bmi_value()


def test_6():
	cut = bmi_calculator.BMICalc(295,822,0)
	cut.weight = 937
	cut.height = 39
	cut.weight = 384
	cut.classify_bmi_adults()


def test_7():
	cut = bmi_calculator.BMICalc(550,279,95)
	cut.bmi_value()


def test_8():
	cut = bmi_calculator.BMICalc(195,804,17)
	cut.age = 15
	cut.classify_bmi_teens_and_children()
	cut.weight = 902
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.age = 108
	cut.bmi_value()
	cut.age = 76


def test_9():
	cut = bmi_calculator.BMICalc(9,447,4)
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.age = 16
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()


def test_10():
	cut = bmi_calculator.BMICalc(254,845,150)
	cut.classify_bmi_adults()


def test_11():
	cut = bmi_calculator.BMICalc(497,819,25)
	cut.age = 12
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.height = 192
	cut.classify_bmi_adults()
	cut.weight = 66
	cut.height = 506
	cut.age = 39
	cut.classify_bmi_teens_and_children()
	cut.age = 60
	cut.height = 493
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
