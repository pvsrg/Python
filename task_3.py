n_str = input('Введите число n: ')

# Вариант 1 с помощью операции слияния строк
result = int(n_str) + int(n_str + n_str) + int(n_str + n_str + n_str)
print(f'1. Результат: n + nn + nnn = {result:<}')

# Вариант 2 узнаем размерность числа
n_int = int(n_str)
razm = 1
while n_int // razm > 0:
    razm *= 10
result = n_int + (n_int * razm + n_int) + ((n_int * razm + n_int) * razm + n_int)
print(f'2. Результат: n + nn + nnn = {result:<}')
