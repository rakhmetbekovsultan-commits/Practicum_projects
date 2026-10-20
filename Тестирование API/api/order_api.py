import requests
import allure
import json
from data import URL


class OrderApi:

    @allure.step("Отправить POST-запрос на создание заказа")
    def create_order(self, payload):
        """
        Создание заказа /api/v1/orders
        Используем json=payload или headers, так как тело содержит массив/структуру
        """
        headers = {"Content-Type": "application/json"}
        return requests.post(URL.CREATE_ORDER, data=json.dumps(payload), headers=headers)

    @allure.step("Отправить GET-запрос на получение списка заказов")
    def get_orders_list(self, params=None):
        """Получение списка заказов /api/v1/orders"""
        return requests.get(URL.GET_ORDERS, params=params)