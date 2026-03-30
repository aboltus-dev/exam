# Вариант 2
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

import pytest
from main import divide
# from main import divide:
# main - это main.py
# divide - это функция из main.py


def test_zero_division():
    # pytest.raises проверяет, что внутри блока возникнет нужная ошибка.
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)