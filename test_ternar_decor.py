import os
import shutil
from ternar_decor import create_folder

import os
import shutil
from ternar_decor import create_folder

def test_create_folder_with_empty_name():
    assert create_folder("") == "Имя папки не может быть пустым."

def test_create_folder_success():
    folder_name = "my_test_folder"

    # Удаляем папку, если уже есть
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)

    result = create_folder(folder_name)
    assert result == f"Папка '{folder_name}' создана."
    assert os.path.exists(folder_name)

    # Убираем папку после теста
    shutil.rmtree(folder_name)

def test_create_folder_already_exists():
    folder_name = "my_test_folder"

    # Создаём папку, если её ещё нет
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    result = create_folder(folder_name)
    assert result == f'Папка "{folder_name}" уже существует.'
    shutil.rmtree(folder_name)
