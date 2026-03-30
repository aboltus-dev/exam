# Вариант 2
# По заданию нужно проверить, что деление на ноль вызывает ZeroDivisionError.
# Этот файл содержит саму функцию.
# main.py можно было бы назвать и иначе: division.py, calc.py и т.д.

def divide(a, b):
    return a / b  # Если b = 0, Python сам вызовет ZeroDivisionError.