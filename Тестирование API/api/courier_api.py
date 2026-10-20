import requests
import allure
from data import URL


class CourierApi:

    @allure.step("Отправить POST-запрос на создание курьера")
    def create_courier(self, payload):
        """Создание курьера /api/v1/courier"""
        return requests.post(URL.CREATE_COURIER, data=payload)

    @allure.step("Отправить POST-запрос на логин курьера")
    def login_courier(self, payload):
        """Авторизация курьера /api/v1/courier/login"""
        return requests.post(URL.LOGIN_COURIER, data=payload)

    @allure.step("Отправить DELETE-запрос на удаление курьера")
    def delete_courier(self, courier_id):
        """Удаление курьера /api/v1/courier/:id"""
        return requests.delete(f"{URL.DELETE_COURIER}{courier_id}")