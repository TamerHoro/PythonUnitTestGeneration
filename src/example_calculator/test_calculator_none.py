import calculator
import pytest



def test_0():
	cut = calculator.Calc()	
	result = cut.add(-247,-318)
	assert result == -565
	assert cut.multiply(132,916) == 120912
	assert cut.subtract(-887,-397)	== -490
	assert cut.divide(-627,-43)  == 14.581395348837209

