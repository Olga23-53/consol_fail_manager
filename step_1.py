import os # импорт необходимых модулей:
import platform # для управления файлами/папками (os, shutil)
import shutil # для получения информации об ОС


def show_menu():  # Меню программы
    while True:
        print('\nМеню:')
        print("1. Создать папку")
        print("2. Удалить файл/папку")
        print("3. Копировать файл/папку")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счёт")
        print("11. Выход") # цикл работает, пока не вызова 11

        choice = input("Выберите пункт меню (1-11): ").strip()
# программа через if-elif вызывает соответствующую функцию
        try:
            if choice == '1':
                create_folder()
            elif choice == '2':
                delete_item()
            elif choice == '3':
                copy_item()
            elif choice == '4':
                view_directory()
            elif choice == '5':
                view_folders()
            elif choice == '6':
                view_files()
            elif choice == '7':
                os_info()
            elif choice == '8':
                show_creator_info()
            elif choice == '9':
                play_quiz()
            elif choice == '10':
                bank_account()
            elif choice == '11':
                print("Выход из программы.")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")# после выполнения функции программа возвращается в меню


def create_folder():
   # создание папки
    folder_name = input("Введите имя папки: ").strip() # пользователь вводит имя новой папки
    if folder_name:
        if not os.path.exists(folder_name):  # программа проверяет, существует ли уже такая папка
            os.mkdir(folder_name) # если папка отсутствует, она создаётся с помощью os.mkdir()
            print(f"Папка '{folder_name}' создана.")
        else:
            print(f'Папка "{folder_name}" уже существует.')
    else:
        print("Имя папки не может быть пустым.")


def delete_item():
    # удаляет файл/папку
    item_name = input('Введите имя папки или файла для удаления: ').strip()
    if item_name: # Проверяется: существует ли объект? Если да:
        if os.path.exists(item_name):
            if os.path.isfile(item_name): # если это файл (os.path.isfile())
                os.remove(item_name) #  он удаляется через os.remove().
                print(f"Файл '{item_name}' успешно удалён.")
            elif os.path.isdir(item_name): # если это папка (os.path.isdir())
                shutil.rmtree(item_name) # удаляет папку и все её содержимое
                print(f"Папка '{item_name}' успешно удалена.")
        else:
            print(f"Файл или папка с именем '{item_name}' не существует.")
    else:
        print("Имя для удаления не может быть пустым.")


def copy_item():
# копирует файл/папку
    source = input("Введите исходный путь путь файла/папки: ").strip()
    destination = input("Введите имя конечного места назначения: ").strip()

    if source and destination: # программа проверяет, существует ли объект source
        if source == destination: # расположены ли пути назначения и источник одинаково
            print("Ошибка: исходный и целевой путь совпадают.")
            return

        if os.path.exists(source): # если объект существует,
            if os.path.isfile(source):
                shutil.copy2(source, destination)# Для файла используется shutil.copy2(), чтобы скопировать с сохранением метаинформации (например, даты создания)
                print(f"Файл '{source}' скопирован как '{destination}'.")
            elif os.path.isdir(source): # для папки
                shutil.copytree(source, destination)
                print(f"Папка '{source}' скопирована как '{destination}'.")
        else:
            print(f"Ошибка: файл или папка '{source}' не найдена.")
    else:
        print("Пути не могут быть пустыми.")


def view_directory():
     # просмотр содержимого рабочей директории
    print("\nСодержимое текущей рабочей директории:")
    items = os.listdir() # функция выводит список объектов (файлов/папок) в текущей директории через os.listdir()
    if items:
        for item in items:
            print(f" - {item}")
    else:
        print("Рабочая директория пуста.")


def view_folders():
    # собирает и выводит только те элементы, которые являются папками
    print("\nСписок папок:")
    folders = [folder for folder in os.listdir() if os.path.isdir(folder)] # фильтрация через os.path.isdir())
    if folders:
        for folder in folders:
            print(f" - {folder}")
    else:
        print("Папок не найдено.")


def view_files():
    # выводит только файлы
    print("\nСписок файлов:")
    files = [file for file in os.listdir() if os.path.isfile(file)] # фильтрация
    if files:
        for file in files:
            print(f" - {file}")
    else:
        print("Файлов не найдено.")


def os_info(): # информация об ос вывод
    info = {
        "Система": platform.system(),
        "Версия": platform.version(),
        "Платформа": platform.platform(),
        "Архитектура": platform.architecture()[0],
        "Процессор": platform.processor(),
        "Имя узла": platform.node(),
    }

    print("\nИнформация об операционной системе:")
    for key, value in info.items():
        print(f"{key}: {value}")


def show_creator_info():
    # выводит информацию о создателе программы
    creator_info = {
        "Имя": "Примерный Автор",
        "Контакты": "пример@почта.com",
        "Описание": "Учебная программа."
    }

    print("\nИнформация о создателе:")
    for key, value in creator_info.items():
        print(f"{key}: {value}")


def ask_question(question, correct_answer):
    # функция сравнивает ввод пользователя с правильным ответом
    while True:
        answer = input(question).strip()
        if answer == correct_answer:
            print("Верно!\n")
            break
        else:
            print("Неверно! Попробуйте снова.\n")


def play_quiz():
    # функция викторины
    while True:
        print("\nМеню викторины:")
        print("1. Играть: 'Когда родился А.С. Пушкин?'")
        print("2. Выход из викторины")

        choice = input("Выберите пункт (1-2): ").strip()

        if choice == '1':
            print("\nВикторина началась!\n")
            ask_question("Введите год рождения А.С. Пушкина: ", "1799")
            ask_question("Введите день рождения А.С. Пушкина (число июня): ", "6")
            print("Поздравляем! Вы справились с викториной!\n")
        elif choice == '2':
            print("Выход из викторины.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def bank_account():# Важно: баланс и история покупок сохраняются внутри функции bank_account.
    # функция управления банковским счётом
    balance = 0
    purchase_history = []

    def show_balance(): # просмотр баланса
        print(f"\nВаш текущий баланс: {balance} руб.\n")

    def deposit(): # пополнение счета
        nonlocal balance
        try:
            amount = float(input("Введите сумму пополнения: "))
            if amount > 0:
                balance += amount
                print(f"Счёт пополнен. Ваш баланс: {balance} руб.")
            else:
                print("Сумма должна быть больше 0.")
        except ValueError:
            print("Введите корректное число.")

    def make_purchase():# покупки (с ведением списка покупок)
        nonlocal balance, purchase_history
        if balance <= 0:
            print("Недостаточно средств. Сначала пополните счёт.")
            return

        item = input("Что хотите купить? ").strip()
        try:
            price = float(input(f"Сколько стоит {item}? "))
            if price > 0:
                if price <= balance: # при покупке проверяется, достаточно ли средств
                    balance -= price
                    purchase_history.append((item, price))# если их хватает, покупка добавляется в историю
                    print(f"Вы купили {item} за {price} руб. Осталось: {balance} руб.")
                else:
                    print("Недостаточно средств.")
            else:
                print("Цена должна быть больше 0.")
        except ValueError:
            print("Введите корректную цену.")

    def show_history():
        if purchase_history:
            print("\nИстория покупок:")
            for i, (item, price) in enumerate(purchase_history, 1):
                print(f"{i}. {item} — {price} руб.")
        else:
            print("История покупок пуста.")

    while True:
        print("\nМеню счёта:")
        print("1. Пополнить счёт")
        print("2. Совершить покупку")
        print("3. История покупок")
        print("4. Выйти")
        show_balance()

        choice = input("Выберите действие (1-4): ").strip()
        if choice == '1':
            deposit()
        elif choice == '2':
            make_purchase()
        elif choice == '3':
            show_history()
        elif choice == '4':
            print("Выход из системы счёта. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == '__main__':
    show_menu()
