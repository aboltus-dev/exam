# Вариант 10
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import is_even
# main - это main.py
# is_even - это функция из main.py


def test_odd_is_false():
    assert is_even(3) == False