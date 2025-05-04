import os
import shutil
import pytest
from pure_functions import os_info, create_folder, delete_item, copy_item, view_directory, view_folders, view_files, \
    show_creator_info


def test_os_info():
    # Проверяем, что возвращается словарь
    result = os_info()
    assert isinstance(result, dict), "os_info должен возвращать словарь"

    # Проверяем наличие ожидаемых ключей
    expected_keys = {"Система", "Версия", "Платформа", "Архитектура", "Процессор", "Имя узла"}
    assert expected_keys.issubset(result.keys()), "В словаре os_info нет всех ключей"




def test_create_folder():
    # Проверяем пустое имя
    assert create_folder("") == "Имя папки не может быть пустым."

    # Имя тестовой папки
    folder_name = "test_folder"

    # Удаляем папку, если она уже существует (подготовка к тесту)
    if os.path.exists(folder_name):
        os.rmdir(folder_name)

    # Проверяем создание новой папки
    assert create_folder(folder_name) == f"Папка '{folder_name}' создана."
    assert os.path.exists(folder_name)

    # Проверяем обработку случая, когда папка уже существует
    assert create_folder(folder_name) == f'Папка "{folder_name}" уже существует.'

    # Удаляем папку после теста (уборка после теста)
    if os.path.exists(folder_name):
        os.rmdir(folder_name)


def test_delete_item():
    # Проверка пустого имени
    assert delete_item("") == "Имя для удаления не может быть пустым."

    # Проверка удаления несуществующего объекта
    assert delete_item("non_existing_item") == "Файл или папка с именем 'non_existing_item' не существует."

    # Проверка удаления файла
    file_name = "test_file.txt"
    with open(file_name, "w"):  # Создаём тестовый файл
        pass
    assert delete_item(file_name) == f"Файл '{file_name}' успешно удалён."
    assert not os.path.exists(file_name), "Тестовый файл не был удалён."

    # Проверка удаления папки
    folder_name = "test_folder"
    os.mkdir(folder_name)  # Создаём тестовую папку
    assert delete_item(folder_name) == f"Папка '{folder_name}' успешно удалена."
    assert not os.path.exists(folder_name), "Тестовая папка не была удалена."


def test_copy_item():
    # Проверка пустых путей
    assert copy_item("", "") == "Пути не могут быть пустыми."

    # Проверка совпадения путей
    with open("file.txt", "w"):
        pass
    assert copy_item("file.txt", "file.txt") == "Ошибка: исходный и целевой путь совпадают."
    os.remove("file.txt")

    # Копирование файла
    with open("source.txt", "w") as file:
        file.write("File content")
    assert copy_item("source.txt", "copy.txt") == "Файл 'source.txt' скопирован как 'copy.txt'."
    assert os.path.exists("copy.txt")
    os.remove("source.txt")
    os.remove("copy.txt")

    # Копирование папки
    os.mkdir("source_folder")
    with open("source_folder/file.txt", "w"):
        pass
    assert copy_item("source_folder", "target_folder") == "Папка 'source_folder' скопирована как 'target_folder'."
    assert os.path.exists("target_folder")
    shutil.rmtree("source_folder")
    shutil.rmtree("target_folder")

def test_view_directory():
    # Создаём тестовый файл
    with open("test.txt", "w"):
        pass

    # Проверяем, что файл отображается в содержимом директории
    result = view_directory()
    assert "test.txt" in result

    # Удаляем тестовый файл
    os.remove("test.txt")


def test_view_folders():
    # Создаём папку и файл
    os.mkdir("folder")
    with open("file.txt", "w"):
        pass

    # Проверяем, что отображаются только папки
    result = view_folders()
    assert "folder" in result
    assert "file.txt" not in result

    # Удаляем тестовые данные
    os.rmdir("folder")
    os.remove("file.txt")


def test_view_files():
    # Создаём папку и файл
    os.mkdir("folder")
    with open("file.txt", "w"):
        pass

    # Проверяем, что отображаются только файлы
    result = view_files()
    assert "file.txt" in result
    assert "folder" not in result

    # Удаляем тестовые данные
    os.rmdir("folder")
    os.remove("file.txt")

def test_show_creator_info():
    # Ожидаемый результат
    expected = {
        "Имя": "Примерный Автор",
        "Контакты": "пример@почта.com",
        "Описание": "Учебная программа."
    }

    # Проверить результат функции
    output = show_creator_info()
    assert isinstance(output, dict), "Функция должна возвращать словарь"
    assert output == expected, "Данные, возвращённые функцией, не совпадают с ожидаемыми"


    # Проверяем результат работы функции
    output = show_creator_info()
    assert output == expected







