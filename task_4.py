my_str = input('Введите несколько слов через пробел: ')

for i, my_word in enumerate(my_str.split(), 1):
    print(f"{i:>2} {my_word[:10]:10}")
