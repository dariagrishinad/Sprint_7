import json
import allure
import requests
from constants import Urls


class Order:
    @allure.step('Отправка post запроса на эндпоинт создания заказа')
    def request_for_create_order(self, payload):
        response = requests.post(Urls.CREATE_ORDER_URL, data=json.dumps(payload))
        return response

    @allure.step('Отправка get запроса на получение списка заказов')
    def request_for_getting_order_list(self):
        response = requests.get(Urls.CREATE_ORDER_URL)
        return response
