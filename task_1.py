list = ['string', 12, 45.6, True, [1, 2, 3], (1, 2, 3), {1, 2}, {'key_1': 0, 'key_2': 2}, None]

# Хотел узнать как контролировать тип переменной в программе,
# можно через преобразования типа в строковое представление
for elm in list:
    tp = str(type(elm))
    if tp == "<class 'str'>":
        print('String')
    elif tp == "<class 'int'>":
        print('Integer')
    elif tp == "<class 'float'>":
        print('Float')
    elif tp == "<class 'bool'>":
        print('Boolean')
    elif tp == "<class 'list'>":
        print('List')
    elif tp == "<class 'tuple'>":
        print('Tuple')
    elif tp == "<class 'set'>":
        print('Set')
    elif tp == "<class 'dict'>":
        print('Dictionary')
    elif tp == "<class 'NoneType'>":
        print('None')
