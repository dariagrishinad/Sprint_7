from faker import Faker
from constants import Constants

faker = Faker()


class CourierData:
    registration = {
        "login": faker.email(),
        "password": Constants.PASSWORD,
        "firstName": Constants.FIRST_NAME
    }
    registration_with_exists_data = {
        "login": Constants.LOGIN,
        "password": Constants.PASSWORD,
        "firstName": Constants.FIRST_NAME
    }
    registration_without_login = {
        "password": Constants.PASSWORD,
        "firstName": Constants.FIRST_NAME
    }
    registration_without_password = {
        "login": Constants.LOGIN,
        "firstName": Constants.FIRST_NAME
    }
    login = {
        "login": Constants.LOGIN,
        "password": Constants.PASSWORD
    }
    login_without_login = {
        "password": Constants.PASSWORD
    }
    login_without_password = {
        "password": Constants.LOGIN
    }
    login_with_invalid_login = {
        "login": Constants.INVALID_LOGIN,
        "password": Constants.PASSWORD
    }
    login_with_invalid_password = {
        "login": Constants.LOGIN,
        "password": Constants.INVALID_PASSWORD
    }


class OrderData:
    create_order_with_black_color = {
        "firstName": "Daria",
        "lastName": "Grishina",
        "address": "Moscow",
        "metroStation": 2,
        "phone": "+7 999 999 99 99",
        "rentTime": 5,
        "deliveryDate": "2024-07-20",
        "comment": "Test",
        "color": [
            "BLACK"
        ]
    }
    create_order_with_grey_color = {
        "firstName": "Daria",
        "lastName": "Grishina",
        "address": "Moscow",
        "metroStation": 2,
        "phone": "+7 999 999 99 99",
        "rentTime": 5,
        "deliveryDate": "2024-07-20",
        "comment": "Test",
        "color": [
            "GREY"
        ]
    }
    create_order_without_color = {
        "firstName": "Daria",
        "lastName": "Grishina",
        "address": "Moscow",
        "metroStation": 2,
        "phone": "+7 999 999 99 99",
        "rentTime": 5,
        "deliveryDate": "2024-07-20",
        "comment": "Test",
        "color": []
    }

