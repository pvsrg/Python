from abc import ABC, abstractmethod


class MyStock:
    def __init__(self, name):
        self.name = name
        self.stock = {}
        self.count = 0

    def append(self, obj):
        if obj is not None:
            self.count += 1
            self.stock.update({self.count: obj})
            return True
        else:
            return False

    def pop(self, count):
        if (pos := self.stock.get(count)) is not None:
            self.stock.pop(count)
        return pos

    def move(self, count, other):
        other.append(self.pop(count))

    def report(self):
        print()
        print(self.name)
        print("| Скл. номер |    Наименование   ")
        print("-" * 40)
        for nmb in self.stock:
            print(f"|{nmb:12}|{self.stock[nmb]}")

    def analitics(self):
        lst = [el.type() for el in self.stock.values()]
        print()
        print(self.name)
        print("|   Тип    | Кол-во ")
        print("-" * 20)
        for tp in set(lst):
            print(f"|{tp:10}|{lst.count(tp):>8}")


class MyDigital:
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def type(self):
        pass

    def __str__(self):
        return f"{self.type():10}{self.model:40}"

    @classmethod
    def factory(cls):
        tp = input("Введите номер типа устройства (1-Printer, 2-Scaner, 3-Copier):")
        if tp.isnumeric():
            model = input("Введите модель устройства: ")
            tp = int(tp)
            if tp == 1:
                return MyPrinter(model)
            if tp == 2:
                return MyScaner(model)
            if tp == 3:
                return MyCopier(model)
        print("Ошибка при вводе номера типа")
        return None


class MyCopier(MyDigital):
    def type(self):
        return "Copier"


class MyPrinter(MyDigital):
    def type(self):
        return "Printer"


class MyScaner(MyDigital):
    def type(self):
        return "Scaner"


def select_function():
    print()
    print()
    print("Выберите действие")
    print("1 - Прием техники на склад")
    print("2 - Передача техники в магазин")
    print("3 - Наличие техники")
    print("4 - Количество техники по типам")
    print("5 - Выход")
    while True:
        fn = input(">")
        if fn.isnumeric():
            fn = int(fn)
            if (fn >= 1) and (fn <= 5):
                return fn
        print("Ошибка при вводе номера!")


def select_shop():
    print()
    print()
    print("Выберите магазин")
    print("1 - Магазин №1")
    print("2 - Магазин №2")
    while True:
        sh = input(">")
        if sh.isnumeric():
            sh = int(sh)
            if (sh >= 1) and (sh <= 2):
                return sh
        print("Ошибка при вводе номера!")


def select_number():
    print("Введите складской номер")
    while True:
        nmb = input(">")
        if nmb.isnumeric():
            return int(nmb)
        print("Ошибка при вводе номера!")


def select_stock():
    print()
    print()
    print("Выберите место хранения")
    print("1 - Склад")
    print("2 - Магазин №1")
    print("3 - Магазин №2")
    while True:
        sh = input(">")
        if sh.isnumeric():
            sh = int(sh)
            if (sh >= 1) and (sh <= 3):
                return sh
        print("Ошибка при вводе номера!")


my_stock = MyStock("Склад")
my_shop1 = MyStock("Магазин 1")
my_shop2 = MyStock("Магазин 1")

while True:
    fn = select_function()
    if fn == 5:
        break
    elif fn == 1:
        my_stock.append(MyDigital.factory())
    elif fn == 2:
        shp = select_shop()
        if shp == 1:
            my_stock.move(select_number(), my_shop1)
        elif shp == 2:
            my_stock.move(select_number(), my_shop2)
    elif fn == 3:
        stk = select_stock()
        if stk == 1:
            my_stock.report()
        elif stk == 2:
            my_shop1.report()
        elif stk == 3:
            my_shop2.report()
    elif fn == 4:
        stk = select_stock()
        if stk == 1:
            my_stock.analitics()
        elif stk == 2:
            my_shop1.analitics()
        elif stk == 3:
            my_shop2.analitics()
