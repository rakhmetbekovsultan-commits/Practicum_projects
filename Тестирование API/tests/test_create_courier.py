import pytest
import allure
from api.courier_api import CourierApi
from helpers import generate_courier_data
from data import ResponseMessage

class TestCreateCourier:
    @allure.title("Успешное создание курьера со всеми обязательными полями")
    def test_create_courier_success(self, courier_api):
        courier_data = generate_courier_data()
        
        response = courier_api.create_courier(courier_data)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        
        # Очистка после теста: удаляем созданного курьера
        login_res = courier_api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_id = login_res.json().get("id")
        courier_api.delete_courier(courier_id)
        

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self, courier_api, created_courier):
        response = courier_api.create_courier(created_courier)
        assert response.status_code == 409
        assert response.json().get("message") == ResponseMessage.CREATE_COURIER_CONFLICT

    @allure.title("Нельзя создать курьера с уже существующим логином")
    def test_create_courier_existing_login_error(self, courier_api, created_courier):
        new_courier = generate_courier_data()
        new_courier["login"] = created_courier["login"]
        
        response = courier_api.create_courier(new_courier)
        assert response.status_code == 409
        assert response.json().get("message") == ResponseMessage.CREATE_COURIER_CONFLICT

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Ошибка при создании курьера без обязательного поля: {missing_field}")
    def test_create_courier_missing_required_field_error(self, courier_api, missing_field):
        courier_data = generate_courier_data()
        courier_data.pop(missing_field)
        
        response = courier_api.create_courier(courier_data)
        assert response.status_code == 400
        assert response.json().get("message") == ResponseMessage.CREATE_COURIER_NO_DATA
