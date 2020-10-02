# goods - список товаров
goods = []

while True:
    print()
    print('1 Добавить товар')
    print('2 Вывести список товаров')
    print('3 Вывести аналитику')
    print('4 Выход')
    cmd = int(input(' > '))
    if cmd == 4:
        break
    elif cmd == 1:
        name = input('Введите наименование: ')
        price = float(input('Введите цену: '))
        quantity = int(input('Введите количество: '))
        unit = input('Введите единицу измерения: ')
        goods_dict = dict(наименование=name, цена=price, количество=quantity, ед=unit)
        goods_row = (len(goods) + 1, {'наименование': name, 'цена': price, 'количество': quantity, 'ед': unit})
        goods.append(goods_row)
    elif cmd == 2:
        if len(goods) == 0:
            print('В списке нет ни одного товара')
            continue
        for gd in goods:
            print(gd)
    elif cmd == 3:
        if len(goods) == 0:
            print('В списке нет ни одного товара')
            continue
        # разделяем список товара на номера и словари товаров
        numbers_tuple, goods_tuple = zip(*goods)
        # формируем список характеристик
        key_list = list(goods_tuple[0].keys())
        # преобразуем словари товаров в список значений характеристик
        values_list = list(list(e.values()) for e in goods_tuple)
        # транспонируем значение характеристик и переводим их из кортежа в список
        values_zip = list(list(set(e)) for e in zip(*values_list))
        # формируем словарь с аналитикой
        analytics_dict = dict(zip(key_list, values_zip))

        for key, itm in analytics_dict.items():
            print(f"'{key}': {itm}")
