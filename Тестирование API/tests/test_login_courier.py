import pytest
import allure
from api.courier_api import CourierApi
from helpers import generate_courier_data, generate_random_string
from data import ResponseMessage

class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier_api, created_courier):
        payload = {
            "login": created_courier["login"],
            "password": created_courier["password"]
        }
        response = courier_api.login_courier(payload)
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Ошибка при авторизации без поля: {missing_field}")
    def test_login_courier_missing_field_error(self, courier_api, created_courier, missing_field):
        payload = {
            "login": created_courier["login"],
            "password": created_courier["password"]
        }
        payload.pop(missing_field)
        
        response = courier_api.login_courier(payload)
        
        # Проверка по документации API
        assert response.status_code == 400
        assert response.json().get("message") == ResponseMessage.LOGIN_COURIER_NO_DATA

    @allure.title("Ошибка авторизации при неправильном логине или пароле")
    def test_login_courier_wrong_credentials_error(self, courier_api, created_courier):
        payload = {
            "login": created_courier["login"],
            "password": generate_random_string(10)
        }
        response = courier_api.login_courier(payload)
        assert response.status_code == 404
        assert response.json().get("message") == ResponseMessage.LOGIN_COURIER_NOT_FOUND

    @allure.title("Ошибка авторизации несуществующим пользователем")
    def test_login_non_existent_courier_error(self, courier_api):
        non_existent_data = generate_courier_data()
        payload = {
            "login": non_existent_data["login"],
            "password": non_existent_data["password"]
        }
        response = courier_api.login_courier(payload)
        assert response.status_code == 404
        assert response.json().get("message") == ResponseMessage.LOGIN_COURIER_NOT_FOUND
