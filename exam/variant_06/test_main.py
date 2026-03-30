# Вариант 6
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import get_string
# main - это main.py
# get_string - это функция из main.py


def test_string_length():
    # len() считает количество символов в строке.
    assert len(get_string()) > 5