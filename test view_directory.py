import os
from view_directory import view_directory, save_directory_content

# Тест для функции просмотра директории
def test_view_directory_prints(capsys):
    # Вызываем функцию, которая печатает содержимое директории
    view_directory()
    # Сохраняем всё, что напечатала функция
    output = capsys.readouterr().out
    # Проверяем, что в выводе есть слово "Содержимое"
    assert "Содержимое" in output

# Тест для функции сохранения содержимого в файл
def test_save_directory_content_creates_file():
    # Вызываем функцию, которая должна создать файл listdir.txt
    save_directory_content()
    # Проверяем, что файл действительно появился
    assert os.path.exists("listdir.txt")
    # Удаляем файл после теста, чтобы не мешал другим
    os.remove("listdir.txt")

