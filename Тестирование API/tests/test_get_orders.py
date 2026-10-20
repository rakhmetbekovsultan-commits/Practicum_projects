import allure
from api.order_api import OrderApi


class TestGetOrders:

    @allure.title("Успешное получение списка заказов")
    def test_get_orders_list_success(self):
        order_api = OrderApi()

        response = order_api.get_orders_list()

        # Проверки: код 200 и присутствие массива "orders" в ответе
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)