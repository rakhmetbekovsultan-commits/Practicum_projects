import pytest
import allure
from api.order_api import OrderApi


class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Создание заказа с разным набором цветов: {color}")
    def test_create_order_success(self, color):
        order_api = OrderApi()
        
        # Базовое тело заказа с подстановкой списка цветов
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2026-09-10",
            "comment": "Saske, come back to Konoha",
            "color": color
        }

        response = order_api.create_order(payload)

        # Проверки: код 201 и наличие ключа "track" в теле ответа
        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)