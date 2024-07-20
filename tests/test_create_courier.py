import allure
from constants import ResponseCodes, ResponseMessages
from courier import Courier
from data import CourierData
import pytest


class TestCreateCourier:
    @allure.step('Тестирование успешного создания курьера')
    def test_create_courier_successfully(self):
        courier = Courier()
        response = courier.request_for_create_courier(CourierData.registration)

        assert response.status_code == ResponseCodes.CODE_201 and response.json() == ResponseMessages.MESSAGE_SUCCESSFUL_REGISTRATION

    @allure.step('Тестирование создания курьера с существующим логином')
    def test_create_courier_with_exists_login(self):
        courier = Courier()
        response = courier.request_for_create_courier(CourierData.registration_with_exists_data)

        assert response.status_code == ResponseCodes.CODE_409

    @allure.step('Тестирование создания курьера с недостающими обязательными полями')
    @pytest.mark.parametrize('payload', [CourierData.registration_without_login, CourierData.registration_without_password])
    def test_create_courier_without_required_data(self, payload):
        courier = Courier()
        response = courier.request_for_create_courier(payload)

        assert response.status_code == ResponseCodes.CODE_400 and response.json()['message'] == ResponseMessages.MESSAGE_REGISTRATION_WITHOUT_DATA
