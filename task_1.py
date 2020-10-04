def div_numbers(number_1, number_2):
    """Функция возвращает частное двух чисел"""
    return number_1 / number_2


try:
    n_1 = int(input("Введите делимое: "))
    n_2 = int(input("Введите делитель: "))
    print(f"Частное двух чисел: {div_numbers(n_1, n_2):<8.3f}")
except ValueError:
    print("Ошибка !!! Некорректно введенное число")
except ZeroDivisionError:
    print("Ошибка !!! Деление на ноль")
