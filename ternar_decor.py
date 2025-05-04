def create_folder(folder_name: str) -> str:
    # проверка, что имя папки не пустое
    if not folder_name:
        return "Имя папки не может быть пустым."
    return (
        f'Папка "{folder_name}" уже существует.'
        if os.path.exists(folder_name)
        else (os.mkdir(folder_name) or f"Папка '{folder_name}' создана.")
    )


import os

def star_decorator(func):
    def wrapper(*args, **kwargs):
        print("***********")
        result = func(*args, **kwargs)
        print(result)
        print("***********")
        return result
    return wrapper

@star_decorator
def create_folder(folder_name: str) -> str:
    # проверка, что имя папки не пустое
    if not folder_name:
        return "Имя папки не может быть пустым."
    return (
        f'Папка "{folder_name}" уже существует.'
        if os.path.exists(folder_name)
        else (os.mkdir(folder_name) or f"Папка '{folder_name}' создана.")
    )

create_folder("new_folder")
