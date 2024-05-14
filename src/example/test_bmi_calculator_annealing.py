import bmi_calculator
import pytest


def test_0():
	cut = bmi_calculator.BMICalc(368,699,7)
	cut.classify_bmi_teens_and_children()
	cut.weight = 260
	cut.weight = 836
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.weight = 557
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.age = 22
	cut.age = -1
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.weight = 73


def test_1():
	cut = bmi_calculator.BMICalc(417,213,121)
	cut.height = 330
	cut.height = 277
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.weight = 601
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.height = 398


def test_2():
	cut = bmi_calculator.BMICalc(884,454,65)
	cut.classify_bmi_adults()
	cut.weight = 333
	cut.height = 725
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.height = 231
	cut.bmi_value()
	cut.weight = 80
	cut.bmi_value()
	cut.weight = 710
	cut.age = 82
	cut.weight = 940
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.height = 427
	cut.classify_bmi_adults()
	cut.height = 838
	cut.bmi_value()


def test_3():
	cut = bmi_calculator.BMICalc(515,765,102)
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.age = 43
	cut.bmi_value()
	cut.bmi_value()
	cut.weight = 170
	cut.bmi_value()


def test_4():
	cut = bmi_calculator.BMICalc(962,961,117)
	cut.classify_bmi_adults()
	cut.age = 147
	cut.weight = 130
	cut.bmi_value()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.age = 150
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.height = 146
	cut.weight = 165


def test_5():
	cut = bmi_calculator.BMICalc(321,450,135)
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.height = 745
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.age = 64
	cut.classify_bmi_teens_and_children()
	cut.age = 114
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.age = 96
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.age = 128
	cut.age = 42
	cut.weight = 620
	cut.height = 967
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.height = 62


def test_6():
	cut = bmi_calculator.BMICalc(727,891,35)
	cut.weight = 295
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.weight = 502
	cut.weight = 323
	cut.age = 48
	cut.age = 11
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.height = 887
	cut.weight = 882
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.bmi_value()


def test_7():
	cut = bmi_calculator.BMICalc(541,936,84)
	cut.weight = 534
	cut.height = 438
	cut.height = 726
	cut.weight = 805
	cut.weight = 960
	cut.age = 30
	cut.height = 741
	cut.classify_bmi_adults()
	cut.height = 509
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.weight = 352
	cut.height = 818
	cut.height = 884


def test_8():
	cut = bmi_calculator.BMICalc(537,738,59)
	cut.classify_bmi_adults()
	cut.age = 93
	cut.classify_bmi_adults()
	cut.weight = 462
	cut.weight = 983
	cut.weight = 942
	cut.height = 329
	cut.height = 576
	cut.weight = 468
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.age = 40
	cut.weight = 210
	cut.height = 99
	cut.height = 616
	cut.classify_bmi_adults()
	cut.age = 49
	cut.weight = 592
	cut.bmi_value()


def test_9():
	cut = bmi_calculator.BMICalc(80,622,31)
	cut.weight = 765
	cut.height = 686
	cut.weight = 40
	cut.age = 62
	cut.weight = 2
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.height = 82
	cut.age = 135
	cut.weight = 438
	cut.height = 792
	cut.weight = 772
	cut.height = 72
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.bmi_value()
	cut.weight = 646


def test_10():
	cut = bmi_calculator.BMICalc(946,44,110)
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.weight = 544
	cut.height = 902
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.weight = 214
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.weight = 17
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.weight = 12
	cut.bmi_value()


def test_11():
	cut = bmi_calculator.BMICalc(346,630,46)
	cut.age = 112


def test_12():
	cut = bmi_calculator.BMICalc(388,836,149)
	cut.bmi_value()
	cut.age = 17
	cut.age = 56
	cut.age = 133
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.weight = 501
	cut.bmi_value()


def test_13():
	cut = bmi_calculator.BMICalc(885,812,49)
	cut.age = 58
	cut.age = 117
	cut.bmi_value()
	cut.classify_bmi_teens_and_children()
	cut.age = 120
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.age = 123
	cut.classify_bmi_adults()
	cut.height = 810
	cut.classify_bmi_teens_and_children()
	cut.age = 72
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.bmi_value()
	cut.weight = 741
	cut.weight = 886
	cut.weight = 989


def test_14():
	cut = bmi_calculator.BMICalc(991,902,56)
	cut.age = 32
	cut.age = 24
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.height = 688
	cut.age = 117
	cut.classify_bmi_adults()
	cut.age = 120
	cut.age = 20
	cut.weight = 338
	cut.classify_bmi_teens_and_children()
	cut.height = 401
	cut.classify_bmi_adults()
	cut.weight = 690
	cut.classify_bmi_adults()
	cut.weight = 360
	cut.bmi_value()
	cut.weight = 948
	cut.classify_bmi_adults()
	cut.bmi_value()


def test_15():
	cut = bmi_calculator.BMICalc(493,314,124)
	cut.classify_bmi_adults()
	cut.age = 99
	cut.bmi_value()
	cut.bmi_value()
	cut.weight = 671
	cut.age = 113
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.weight = 628
	cut.weight = 5
	cut.bmi_value()
	cut.bmi_value()
	cut.weight = 457


def test_16():
	cut = bmi_calculator.BMICalc(602,20,140)
	cut.classify_bmi_adults()
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.weight = 96
	cut.classify_bmi_teens_and_children()
	cut.age = 76
	cut.bmi_value()
	cut.classify_bmi_adults()
	cut.classify_bmi_adults()
	cut.age = 59
	cut.classify_bmi_teens_and_children()
	cut.weight = 343
	cut.weight = 821
	cut.weight = 272
	cut.age = 138
	cut.weight = 52
	cut.bmi_value()
	cut.height = 611
	cut.height = 290
	cut.height = 928


def test_17():
	cut = bmi_calculator.BMICalc(697,220,55)
	cut.bmi_value()
	cut.weight = 154
	cut.classify_bmi_teens_and_children()
	cut.age = 147
	cut.classify_bmi_adults()
	cut.classify_bmi_teens_and_children()
	cut.classify_bmi_adults()
	cut.age = 118
	cut.classify_bmi_adults()
	cut.height = 690
	cut.height = 157
	cut.height = 358
	cut.weight = 658


def test_18():
	cut = bmi_calculator.BMICalc(708,893,35)
	cut.classify_bmi_adults()
