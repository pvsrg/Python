number = int(input('Введите размер списка: '))

my_list = []
for i in range(number):
    my_list.append(input(f'Введите {i + 1}-й элемент: '))

print('Исходный список')
print(my_list)

for i in range(number // 2):
    my_list[2 * i], my_list[2 * i + 1] = my_list[2 * i + 1], my_list[2 * i]

print('Результирующий список')
print(my_list)
