import os
import json

# Вспомогательная функция для загрузки данных из файла
def load_data(filename, default_value):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return default_value

# Вспомогательная функция для сохранения данных в файл
def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

# Чистая функция для обработки покупки
def process_purchase(balance, history, product, price):
    if price <= 0:
        return balance, history, "Цена должна быть положительной."
    if price > balance:
        return balance, history, "Недостаточно средств для покупки."
    balance -= price
    new_history = history + [(product, price)]  # создаём новую историю
    return balance, new_history, f"Покупка {product} за {price} руб. успешно совершена!"



# Основная функция программы
def bank_account():
    balance = load_data('balance.json', 0)
    purchase_history = load_data('purchase_history.json', [])

    def show_balance():
        print(f"\nВаш текущий баланс: {balance} руб.\n")

    def deposit_money():
        nonlocal balance
        try:
            amount = float(input("Введите сумму пополнения: "))
            if amount > 0:
                balance += amount
                print(f"Счет пополнен. Ваш баланс: {balance} руб.")
            else:
                print("Сумма должна быть больше 0.")
        except ValueError:
            print("Ошибка ввода. Введите число.")

    def make_purchase():
        nonlocal balance, purchase_history
        if balance <= 0:
            print("Недостаточно средств на счете.")
            return

        product = input("Что хотите купить? ").strip()
        try:
            price = float(input(f"Сколько стоит {product}? "))
            if price > 0:
                if price <= balance:
                    balance -= price
                    purchase_history.append([product, price])  # список вместо кортежа
                    print(f"Покупка {product} за {price} руб. успешно совершена!")
                else:
                    print("Недостаточно средств для покупки.")
            else:
                print("Цена должна быть положительной.")
        except ValueError:
            print("Ошибка ввода. Введите цену числом.")

    def show_purchase_history():
        if purchase_history:
            print("\nИстория покупок:")
            for number, item in enumerate(purchase_history, 1):
                product, price = item
                print(f"{number}. {product} - {price} руб.")
        else:
            print("История покупок пуста.")

    while True:
        print("\nМеню:")
        print("1. Пополнить счет.")
        print("2. Совершить покупку.")
        print("3. Показать историю покупок.")
        print("4. Выход.")

        show_balance()

        user_choice = input("Выберите действие (1-4): ").strip()
        if user_choice == '1':
            deposit_money()
        elif user_choice == '2':
            make_purchase()
        elif user_choice == '3':
            show_purchase_history()
        elif user_choice == '4':
            save_data('balance.json', balance)
            save_data('purchase_history.json', purchase_history)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    bank_account()

