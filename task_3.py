def my_func(arg1, arg2, arg3):
    """Функция сумму двух наибольших аргументов числовых или строкового типа"""
    arg_list = [arg1, arg2, arg3]
    min_arg = min(arg_list)
    arg_list.pop(arg_list.index(min_arg))
    return arg_list[0] + arg_list[1]


print(my_func(3, 1, 5))
print(my_func("aaa", "bbb", "wwww"))
