import os

def view_directory():
    """Просмотр содержимого текущей рабочей директории"""
    print("\nСодержимое текущей рабочей директории:")
    items = os.listdir()
    if items:
        for item in items:
            print(f" - {item}")
    else:
        print("Рабочая директория пуста.")

def save_directory_content():
    """Сохранить содержимое директории в файл listdir.txt"""
    file_list = []
    dir_list = []

    for item in os.listdir():
        if os.path.isfile(item):
            file_list.append(item)
        elif os.path.isdir(item):
            # Исключаем скрытые и системные папки
            if not item.startswith('.') and item != '__pycache__':
                dir_list.append(item)

    with open('listdir.txt', 'w', encoding='utf-8') as f:
        f.write(f"files: {', '.join(file_list)}\n")
        f.write(f"dirs: {', '.join(dir_list)}\n")

    print("Содержимое директории сохранено в файл listdir.txt")

def main():
    while True:
        print("\nМеню:")
        print("1. Просмотр содержимого директории")
        print("2. Сохранить содержимое директории в файл")
        print("3. Выход")

        user_choice = input("Выберите пункт меню: ")

        if user_choice == '1':
            view_directory()
        elif user_choice == '2':
            save_directory_content()
        elif user_choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

