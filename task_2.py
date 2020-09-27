seconds = int(input('Введите время в секундах: '))
hours = seconds // (60 * 60)
seconds %= 60 * 60
minuts = seconds // 60
seconds %= 60

print(f'Время {hours:02d}:{minuts:02}:{seconds:02}')
