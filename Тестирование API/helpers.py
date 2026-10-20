import random
import string


def generate_random_string(length=10):
    """Генерирует случайную строку из букв нижнего регистра."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_data():
    """
    Генерирует словарь с данными нового курьера.
    Возвращает dict с login, password, firstName.
    """
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }