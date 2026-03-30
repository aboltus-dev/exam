# Вариант 13
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import contains_test
# main - это main.py
# contains_test - это функция из main.py


def test_contains_substring():
    assert contains_test("this is a test") == True