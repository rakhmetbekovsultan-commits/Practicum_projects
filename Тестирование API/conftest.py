import pytest
import allure
from api.courier_api import CourierApi
from helpers import generate_courier_data

@pytest.fixture
def courier_api():
    """Фикстура для инициализации API-клиента курьера."""
    return CourierApi()

@pytest.fixture
def created_courier(courier_api):
    """
    Фикстура создает курьера перед тестом,
    передает данные (login, password, firstName) в тест,
    а после выполнения теста автоматически удаляет курьера.
    """
    courier_data = generate_courier_data()
    
    # Регистрируем курьера (без assert)
    courier_api.create_courier(courier_data)
    
    # Передаем данные в тест
    yield courier_data
    
    # --- Teardown (очистка после теста) ---
    with allure.step("Очистка: удаление созданного курьера"):
        login_payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        login_response = courier_api.login_courier(login_payload)
        
        # Если удалось залогиниться — берем id и удаляем
        courier_id = login_response.json().get("id")
        if courier_id:
            courier_api.delete_courier(courier_id)
