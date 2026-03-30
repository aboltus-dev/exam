# Вариант 11
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import is_empty
# main - это main.py
# is_empty - это функция из main.py


def test_empty_list():
    assert is_empty([]) == True