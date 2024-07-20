import allure
import pytest
from constants import ResponseCodes, ResponseMessages
from courier import Courier
from data import CourierData


class TestLoginCourier:
    @allure.step('Тестирование успешной авторизации курьера')
    def test_login_courier_successfully(self):
        courier = Courier()
        response = courier.request_for_login_courier(CourierData.login)

        assert response.status_code == ResponseCodes.CODE_200 and response.json() == ResponseMessages.MESSAGE_SUCCESSFUL_LOGIN

    @allure.step('Тестирование авторизации курьера с недостающим обязательным полем')
    @pytest.mark.parametrize('payload', [CourierData.login_without_login, CourierData.login_without_password])
    def test_login_courier_without_data(self, payload):
        courier = Courier()
        response = courier.request_for_login_courier(payload)

        assert response.status_code == ResponseCodes.CODE_400 and response.json()['message'] == ResponseMessages.MESSAGE_LOGIN_WITHOUT_DATA

    @allure.step('Тестирование авторизации курьера с некорректными данными')
    @pytest.mark.parametrize('payload', [CourierData.login_with_invalid_login, CourierData.login_with_invalid_password])
    def test_login_courier_with_invalid_data(self, payload):
        courier = Courier()
        response = courier.request_for_login_courier(payload)

        assert response.status_code == ResponseCodes.CODE_404 and response.json()['message'] == ResponseMessages.MESSAGE_LOGIN_WITH_INVALID_DATA
