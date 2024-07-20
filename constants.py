class Urls:
    CREATE_COURIER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    LOGIN_COURIER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    CREATE_ORDER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'


class Constants:
    LOGIN = 'dariagrishina10@ya.ru'
    PASSWORD = '123456'
    FIRST_NAME = 'Daria'
    INVALID_LOGIN = 'dariagrishina10@ya.r'
    INVALID_PASSWORD = '12345'


class ResponseCodes:
    CODE_200 = 200
    CODE_201 = 201
    CODE_409 = 409
    CODE_400 = 400
    CODE_404 = 404


class ResponseMessages:
    MESSAGE_SUCCESSFUL_REGISTRATION = {"ok": True}
    MESSAGE_REGISTRATION_WITHOUT_DATA = 'Недостаточно данных для создания учетной записи'
    MESSAGE_LOGIN_WITHOUT_DATA = 'Недостаточно данных для входа'
    MESSAGE_LOGIN_WITH_INVALID_DATA = 'Учетная запись не найдена'
    MESSAGE_SUCCESSFUL_LOGIN = {"id": 351733}

