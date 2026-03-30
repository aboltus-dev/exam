# Вариант 8
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import is_palindrome
# main - это main.py
# is_palindrome - это функция из main.py


def test_palindrome():
    assert is_palindrome("racecar") == True