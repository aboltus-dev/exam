# Вариант 5
# Этот файл содержит тест.
# Запуск в терминале:
# python -m pytest test_main.py --junitxml=report.xml
# Эта команда запускает тест и создаёт XML-отчёт report.xml.
# Если вы переименовали test_main.py, в команде укажите своё имя файла.

from main import get_dict
# main - это main.py
# get_dict - это функция из main.py


def test_has_name_key():
    # Проверяем, что в словаре есть ключ 'name'.
    assert "name" in get_dict()