# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bmi_calculator as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    module_0.BMICalc(bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.BMICalc(bool_0, bool_0, bool_0)


def test_case_2():
    float_0 = 207.37
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_adults()
    assert var_0 == "Severely Obese"
    with pytest.raises(ValueError):
        b_m_i_calc_0.classify_bmi_teens_and_children()


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.BMICalc(none_type_0, none_type_0, none_type_0)


def test_case_4():
    float_0 = 18.806202878120434
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"


def test_case_5():
    float_0 = 205.8423769273918
    bool_0 = True
    b_m_i_calc_0 = module_0.BMICalc(bool_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    b_m_i_calc_1 = module_0.BMICalc(float_0, bool_0, float_0)
    assert (
        f"{type(b_m_i_calc_1).__module__}.{type(b_m_i_calc_1).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    var_0 = b_m_i_calc_1.classify_bmi_adults()
    assert var_0 == "Underweight"
    var_1 = b_m_i_calc_0.classify_bmi_adults()
    assert var_1 == "Severely Obese"
    object_0 = module_1.object()
    var_2 = b_m_i_calc_1.bmi_value()
    assert var_2 == pytest.approx(0.2360100102033419, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_6():
    float_0 = 14.730486882357233
    bool_0 = True
    b_m_i_calc_0 = module_0.BMICalc(float_0, bool_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"
    bool_1 = False
    module_0.BMICalc(float_0, bool_0, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_7():
    int_0 = 10
    b_m_i_calc_0 = module_0.BMICalc(int_0, int_0, int_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    float_0 = -1830.421032
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"
    module_0.BMICalc(int_0, float_0, b_m_i_calc_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    int_0 = 496
    b_m_i_calc_0 = module_0.BMICalc(int_0, int_0, int_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_adults()
    assert var_0 == "Normal weight"
    var_0.bmi_value()


def test_case_9():
    float_0 = 150.77331908375913
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.bmi_value()
    assert var_0 == pytest.approx(66.32473212614428, abs=0.01, rel=0.01)
    b_m_i_calc_1 = module_0.BMICalc(var_0, float_0, float_0)
    b_m_i_calc_2 = module_0.BMICalc(float_0, var_0, float_0)
    var_1 = b_m_i_calc_2.classify_bmi_adults()
    assert var_1 == "Overweight"
    var_2 = b_m_i_calc_1.classify_bmi_adults()
    assert var_2 == "Severely Obese"
    with pytest.raises(ValueError):
        b_m_i_calc_1.classify_bmi_teens_and_children()


@pytest.mark.xfail(strict=True)
def test_case_10():
    float_0 = 15.990475062087734
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"
    var_0.bmi_value()


def test_case_11():
    float_0 = 15.990475062087734
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"
    with pytest.raises(ValueError):
        b_m_i_calc_0.classify_bmi_adults()


@pytest.mark.xfail(strict=True)
def test_case_12():
    float_0 = 12.766813231092454
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"
    module_0.BMICalc(var_0, var_0, float_0)


def test_case_13():
    float_0 = 5.672301768053821
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"


def test_case_14():
    float_0 = 10.0
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"


def test_case_15():
    float_0 = 2.318570295982509
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"


def test_case_16():
    float_0 = 19.0
    float_1 = 19.13404871982066
    b_m_i_calc_0 = module_0.BMICalc(float_1, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.bmi_value()
    assert var_0 == pytest.approx(518.9671280920164, abs=0.01, rel=0.01)
    b_m_i_calc_1 = module_0.BMICalc(var_0, var_0, float_0)
    var_1 = b_m_i_calc_1.classify_bmi_teens_and_children()
    assert var_1 == "Normal weight"
    with pytest.raises(ValueError):
        b_m_i_calc_0.classify_bmi_adults()


@pytest.mark.xfail(strict=True)
def test_case_17():
    float_0 = 15.759969696823225
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Obese"
    var_1 = b_m_i_calc_0.bmi_value()
    assert var_1 == pytest.approx(634.5189865444806, abs=0.01, rel=0.01)
    b_m_i_calc_1 = module_0.BMICalc(float_0, float_0, var_1)
    assert (
        f"{type(b_m_i_calc_1).__module__}.{type(b_m_i_calc_1).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    b_m_i_calc_2 = module_0.BMICalc(var_1, var_1, float_0)
    var_2 = b_m_i_calc_1.classify_bmi_adults()
    assert var_2 == "Severely Obese"
    var_3 = b_m_i_calc_2.classify_bmi_teens_and_children()
    assert var_3 == "Underweight"
    module_1.object(**var_3)


@pytest.mark.xfail(strict=True)
def test_case_18():
    float_0 = 2364.731587
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.bmi_value()
    assert var_0 == pytest.approx(4.228809753705041, abs=0.01, rel=0.01)
    b_m_i_calc_1 = module_0.BMICalc(float_0, float_0, var_0)
    assert (
        f"{type(b_m_i_calc_1).__module__}.{type(b_m_i_calc_1).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    int_0 = 659
    b_m_i_calc_2 = module_0.BMICalc(float_0, int_0, int_0)
    var_1 = b_m_i_calc_2.classify_bmi_adults()
    assert var_1 == "Underweight"
    var_2 = b_m_i_calc_1.classify_bmi_teens_and_children()
    assert var_2 == "Underweight"
    var_2.classify_bmi_adults()


def test_case_19():
    float_0 = 19.0
    float_1 = 409.03
    b_m_i_calc_0 = module_0.BMICalc(float_1, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Underweight"


def test_case_20():
    float_0 = 18.757886242823496
    bool_0 = True
    b_m_i_calc_0 = module_0.BMICalc(float_0, bool_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Overweight"
    with pytest.raises(ValueError):
        b_m_i_calc_0.classify_bmi_adults()


@pytest.mark.xfail(strict=True)
def test_case_21():
    float_0 = 13.0
    float_1 = 2136.279835
    b_m_i_calc_0 = module_0.BMICalc(float_1, float_1, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Underweight"
    var_1 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_1 == "Underweight"
    module_0.BMICalc(float_0, b_m_i_calc_0, var_0)


def test_case_22():
    float_0 = 8.759815713162812
    float_1 = 52.18311771148527
    b_m_i_calc_0 = module_0.BMICalc(float_1, float_0, float_1)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    b_m_i_calc_1 = module_0.BMICalc(float_1, float_0, float_0)
    var_0 = b_m_i_calc_1.bmi_value()
    assert var_0 == pytest.approx(32.168804712483215, abs=0.01, rel=0.01)
    b_m_i_calc_2 = module_0.BMICalc(float_1, var_0, float_0)
    var_1 = b_m_i_calc_1.classify_bmi_teens_and_children()
    assert var_1 == "Obese"
    var_2 = b_m_i_calc_0.classify_bmi_adults()
    assert var_2 == "Obese"


def test_case_23():
    float_0 = 2.0
    float_1 = 46.527528242587906
    b_m_i_calc_0 = module_0.BMICalc(float_1, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Underweight"
    object_0 = module_1.object()


@pytest.mark.xfail(strict=True)
def test_case_24():
    float_0 = 9.327979124400965
    float_1 = 2051.779
    b_m_i_calc_0 = module_0.BMICalc(float_1, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    b_m_i_calc_1 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert b_m_i_calc_1 == "Underweight"
    b_m_i_calc_1.bmi_value()


def test_case_25():
    float_0 = 8.759815713162812
    float_1 = 69.08234679867148
    b_m_i_calc_0 = module_0.BMICalc(float_1, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Normal weight"
    object_0 = module_1.object()
    object_1 = module_1.object()
    with pytest.raises(ValueError):
        b_m_i_calc_0.classify_bmi_adults()


@pytest.mark.xfail(strict=True)
def test_case_26():
    float_0 = 11.795736219212351
    bool_0 = True
    b_m_i_calc_0 = module_0.BMICalc(float_0, bool_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.bmi_value()
    assert var_0 == pytest.approx(71.87037249300631, abs=0.01, rel=0.01)
    b_m_i_calc_1 = module_0.BMICalc(var_0, float_0, float_0)
    var_1 = b_m_i_calc_1.classify_bmi_teens_and_children()
    assert var_1 == "Overweight"
    var_0.classify_bmi_adults()


@pytest.mark.xfail(strict=True)
def test_case_27():
    float_0 = 11.582173364411888
    b_m_i_calc_0 = module_0.BMICalc(float_0, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    bool_0 = True
    b_m_i_calc_1 = module_0.BMICalc(float_0, bool_0, float_0)
    assert (
        f"{type(b_m_i_calc_1).__module__}.{type(b_m_i_calc_1).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    var_0 = b_m_i_calc_1.bmi_value()
    assert var_0 == pytest.approx(74.54523316542631, abs=0.01, rel=0.01)
    b_m_i_calc_2 = module_0.BMICalc(var_0, float_0, float_0)
    var_1 = b_m_i_calc_2.classify_bmi_teens_and_children()
    assert var_1 == "Normal weight"
    var_0.classify_bmi_adults()


@pytest.mark.xfail(strict=True)
def test_case_28():
    float_0 = 13.02
    bool_0 = True
    float_1 = 19.0
    b_m_i_calc_0 = module_0.BMICalc(float_1, bool_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Overweight"
    var_0.classify_bmi_teens_and_children()


def test_case_29():
    float_0 = 8.51172050026517
    float_1 = 62.63042858295091
    b_m_i_calc_0 = module_0.BMICalc(float_1, float_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Overweight"
    with pytest.raises(ValueError):
        b_m_i_calc_0.classify_bmi_adults()


def test_case_30():
    float_0 = 13.02
    bool_0 = True
    float_1 = 20.653423817368694
    b_m_i_calc_0 = module_0.BMICalc(float_1, bool_0, float_0)
    assert (
        f"{type(b_m_i_calc_0).__module__}.{type(b_m_i_calc_0).__qualname__}"
        == "bmi_calculator.BMICalc"
    )
    assert (
        f"{type(module_0.BMICalc.height).__module__}.{type(module_0.BMICalc.height).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.age).__module__}.{type(module_0.BMICalc.age).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.BMICalc.weight).__module__}.{type(module_0.BMICalc.weight).__qualname__}"
        == "builtins.property"
    )
    var_0 = b_m_i_calc_0.classify_bmi_teens_and_children()
    assert var_0 == "Normal weight"
    b_m_i_calc_1 = module_0.BMICalc(float_0, bool_0, float_1)
    with pytest.raises(ValueError):
        b_m_i_calc_1.classify_bmi_teens_and_children()