import os
import json
import pytest
from bank_account import load_data, save_data, process_purchase

# Путь к файлам для тестирования
BALANCE_FILE = 'balance_test.json'
PURCHASE_HISTORY_FILE = 'purchase_history_test.json'


# Очистка файлов перед каждым тестом
@pytest.fixture(autouse=True)
def cleanup():
    if os.path.exists(BALANCE_FILE):
        os.remove(BALANCE_FILE)
    if os.path.exists(PURCHASE_HISTORY_FILE):
        os.remove(PURCHASE_HISTORY_FILE)


def test_load_data_existing_file():
    # Создаем файл с данными для теста
    test_data = {'balance': 100, 'history': []}
    save_data(BALANCE_FILE, test_data)

    # Загружаем данные
    loaded_data = load_data(BALANCE_FILE, {'balance': 0, 'history': []})
    assert loaded_data == test_data, "Данные не были загружены корректно."


def test_load_data_non_existing_file():
    # Загружаем данные из несуществующего файла
    default_data = {'balance': 0, 'history': []}
    loaded_data = load_data(BALANCE_FILE, default_data)
    assert loaded_data == default_data, "Должны быть возвращены данные по умолчанию."


def test_save_data():
    test_data = {'balance': 150, 'history': []}
    # Сохраняем данные
    save_data(BALANCE_FILE, test_data)

    # Проверяем, что данные записались
    with open(BALANCE_FILE, 'r', encoding='utf-8') as file:
        saved_data = json.load(file)
    assert saved_data == test_data, "Данные не были сохранены корректно."


def test_process_purchase_success():
    balance = 100
    history = []
    product = 'Товар1'
    price = 50

    new_balance, new_history, message = process_purchase(balance, history, product, price)

    assert new_balance == 50, "Баланс после покупки должен быть 50."
    assert new_history == [(product, price)], "История покупок должна содержать новый товар."
    assert message == f"Покупка {product} за {price} руб. успешно совершена!", "Сообщение должно быть успешным."


def test_process_purchase_insufficient_funds():
    balance = 30
    history = []
    product = 'Товар2'
    price = 50

    new_balance, new_history, message = process_purchase(balance, history, product, price)

    assert new_balance == 30, "Баланс не должен измениться при недостаточности средств."
    assert new_history == [], "История покупок не должна измениться."
    assert message == "Недостаточно средств для покупки.", "Сообщение должно быть о недостаточности средств."


def test_process_purchase_invalid_price():
    balance = 100
    history = []
    product = 'Товар3'
    price = -50

    new_balance, new_history, message = process_purchase(balance, history, product, price)

    assert new_balance == 100, "Баланс не должен измениться при отрицательной цене."
    assert new_history == [], "История покупок не должна измениться."
    assert message == "Цена должна быть положительной.", "Сообщение должно быть о неправильной цене."
