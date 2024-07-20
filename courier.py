import allure
import requests
from faker import Faker
from constants import Urls

faker = Faker()


class Courier:
    @allure.step('Отправка post запроса на эндпоинт создания курьера')
    def request_for_create_courier(self, payload):
        response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
        return response

    @allure.step('Отправка post запроса на эндпоинт авторизации курьера')
    def request_for_login_courier(self, payload):
        response = requests.post(Urls.LOGIN_COURIER_URL, data=payload)
        return response
