# Вариант 14
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import is_divisible_by_3
# main - это main.py
# is_divisible_by_3 - это функция из main.py


def test_divisible_by_3():
    assert is_divisible_by_3(9) == True