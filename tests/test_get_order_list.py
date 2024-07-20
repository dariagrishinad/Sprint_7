import allure
from constants import ResponseCodes
from order import Order


class TestGetOrderList:
    @allure.step('Тестирование получения списка заказов')
    def test_order_list_get_list(self):
        order = Order()
        response = order.request_for_getting_order_list()

        assert response.status_code == ResponseCodes.CODE_200 and 'orders' in response.json()
