def fact(n):
    """Итератор выдает последовательно факториалы чисел"""
    res = 1
    for f in range(1, n):
        res = res * f
        yield res


for i, el in enumerate(fact(6), 1):
    print(f"{i}! = {el}")
