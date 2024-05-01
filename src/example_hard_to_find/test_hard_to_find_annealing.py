import hard_to_find
import pytest


def test_0():
	cut = hard_to_find.HardToFind()
	cut.hardmethod(41867,50000,52493)
	cut.easymethod(83600,87713,45359)


def test_1():
	cut = hard_to_find.HardToFind()
