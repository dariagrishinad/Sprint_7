import allure
import pytest
from constants import ResponseCodes
from data import OrderData
from order import Order


class TestCreateOrder:
    @allure.step('Тестирование создания заказа с разными вариантами расцветки самоката')
    @pytest.mark.parametrize('payload', [OrderData.create_order_with_grey_color, OrderData.create_order_with_black_color, OrderData.create_order_without_color])
    def test_create_order(self, payload):
        order = Order()
        response = order.request_for_create_order(payload)

        assert response.status_code == ResponseCodes.CODE_201 and 'track' in response.json()
