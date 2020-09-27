a = float(input('Введите результат первого дня (км): '))
b = float(input('Введите общий результат не менее (км): '))

if a >= 0:
    day_number = 1
    result = a
    while True:
        if result >= b:
            break
        day_number += 1
        a *= 1.1
        result += a
    print(f'Общий результат составит не менее {b:.2f} км. на {day_number} день')
else:
    print('Ошибка! Результат первого дня должен быть больше 0')
