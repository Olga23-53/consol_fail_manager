import os
import shutil
import platform


def create_folder(folder_name: str) -> str:
    """
создать папку
    :param folder_name: имя папки str
    :return:
    """
    if not folder_name:
        return "Имя папки не может быть пустым."
    if os.path.exists(folder_name):
        return f'Папка "{folder_name}" уже существует.'
    os.mkdir(folder_name)
    return f"Папка '{folder_name}' создана."


def delete_item(item_name: str) -> str:
    if not item_name:
        return "Имя для удаления не может быть пустым."
    if not os.path.exists(item_name):
        return f"Файл или папка с именем '{item_name}' не существует."
    if os.path.isfile(item_name):
        os.remove(item_name)
        return f"Файл '{item_name}' успешно удалён."
    elif os.path.isdir(item_name):
        shutil.rmtree(item_name)
        return f"Папка '{item_name}' успешно удалена."
    return "Неизвестный объект."


def copy_item(source: str, destination: str) -> str:
    if not source or not destination:
        return "Пути не могут быть пустыми."
    if source == destination:
        return "Ошибка: исходный и целевой путь совпадают."
    if not os.path.exists(source):
        return f"Ошибка: файл или папка '{source}' не найдена."
    if os.path.isfile(source):
        shutil.copy2(source, destination)
        return f"Файл '{source}' скопирован как '{destination}'."
    elif os.path.isdir(source):
        shutil.copytree(source, destination)
        return f"Папка '{source}' скопирована как '{destination}'."
    return "Неизвестный объект."


def view_directory() -> list:
    return os.listdir()


def view_folders() -> list:
    return [folder for folder in os.listdir() if os.path.isdir(folder)]


def view_files() -> list:
    return [file for file in os.listdir() if os.path.isfile(file)]


def os_info() -> dict:
    return {
        "Система": platform.system(),
        "Версия": platform.version(),
        "Платформа": platform.platform(),
        "Архитектура": platform.architecture()[0],
        "Процессор": platform.processor(),
        "Имя узла": platform.node(),
    }


def show_creator_info() -> dict:
    return {
        "Имя": "Примерный Автор",
        "Контакты": "пример@почта.com",
        "Описание": "Учебная программа."
    }












