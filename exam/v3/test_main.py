# Вариант 3
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import get_list
# main - это main.py
# get_list - это функция из main.py


def test_list_length():
    # len() считает количество элементов.
    assert len(get_list()) == 3