from functools import reduce


def mul(prev_el, el):
    """Перемножает все элементы списка"""
    return prev_el * el


my_list = [nmb for nmb in range(100, 1001) if nmb % 2 == 0]
print(my_list)
print(reduce(mul, my_list))
