# Вариант 12
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import is_greater_than_10
# main - это main.py
# is_greater_than_10 - это функция из main.py


def test_greater_than_10():
    assert is_greater_than_10(15) == True