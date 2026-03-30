# Вариант 9
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import add
# main - это main.py
# add - это функция из main.py


def test_sum():
    assert add(3, 5) == 8