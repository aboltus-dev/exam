# Вариант 15
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import is_length_4
# main - это main.py
# is_length_4 - это функция из main.py


def test_length_4():
    assert is_length_4("test") == True