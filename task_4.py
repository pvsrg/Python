number = int(input('Введите число: '))

max_digit = 0
while number > 0:
    digit = number % 10
    number //= 10
    if digit > max_digit:
        max_digit = digit
print(f'Максимальная цифра числа: {max_digit}')
