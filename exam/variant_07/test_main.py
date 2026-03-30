# Вариант 7
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import get_none
# main - это main.py
# get_none - это функция из main.py


def test_returns_none():
    assert get_none() is None