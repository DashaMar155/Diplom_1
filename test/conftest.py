import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()

def test_burger_price_with_mock_bun(burger):
    bun = Mock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 50

    burger.set_bun(bun)
    # Например, если бургер состоит только из булки, цена равна цене булки * 2
    expected_price = bun.get_price.return_value * 2
    assert burger.get_price() == expected_price

def test_bun_name_is_correct(burger):
    bun = Mock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 50

    burger.set_bun(bun)
    assert burger.get_bun().get_name() == "Test Bun"

