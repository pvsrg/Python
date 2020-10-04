def my_func(osn, stpn):
    """Функция возводит действительное положительное число в отрицательную цлую степень"""
    if stpn >= 0:
        raise Exception("Ошибка!!! Степень должна быть отрицательая")
    if osn <= 0:
        raise Exception("Ошибка!!! Основание должно быть положительным числом")
    result = 1
    for i in range(-stpn):
        result /= osn
    return result


try:
    number_1 = float(input("Введите действительное положительное число (основание): "))
    number_2 = int(input("Введите целое отрицательное число (степень): "))
    print(f'Результат: {my_func(number_1, number_2):.6f}')
except ValueError:
    print("Ошибка !!! Некорректно введенное число")
except Exception as e:
    print(e)
