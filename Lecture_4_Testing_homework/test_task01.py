import pytest, allure
from hw1 import cont_fraction

@allure.feature("f1")
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.parametrize("number, divider, result", [(239, 30, [7, 1, 29]), (100, 30, [3, 3]), (0, 30, [0])])
def test_cont_fraction(number, divider, result):
    assert list(cont_fraction(number, divider)) == result

@allure.feature("f2")
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.parametrize("number, divider, result", [(239, 30, [7, 1, 30])])
def test_cont_fraction_failed(number, divider, result):
    assert list(cont_fraction(number, divider)) == result
