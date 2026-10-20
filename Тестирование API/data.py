class URL:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    # Courier endpoints
    CREATE_COURIER = f"{BASE_URL}/api/v1/courier"
    LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login"
    DELETE_COURIER = f"{BASE_URL}/api/v1/courier/"  # + id
    
    # Order endpoints
    CREATE_ORDER = f"{BASE_URL}/api/v1/orders"
    GET_ORDERS = f"{BASE_URL}/api/v1/orders"


class ResponseMessage:
    # Ошибки создания курьера
    CREATE_COURIER_NO_DATA = "Недостаточно данных для создания учетной записи"
    CREATE_COURIER_CONFLICT = "Этот логин уже используется. Попробуйте другой."

    # Ошибки логина курьера
    LOGIN_COURIER_NO_DATA = "Недостаточно данных для входа"
    LOGIN_COURIER_NOT_FOUND = "Учетная запись не найдена"