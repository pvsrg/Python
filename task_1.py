class MyData:
    def __init__(self, data):
        self.day, self.month, self.year = self.data_split(data)

    @classmethod
    def data_split(cls, data):
        data_list = list(map(int, data.split("-")))
        if len(data_list) < 3:
            raise Exception(f"Ошибка!!! Некорректно задана дата формата(дд-мм-гггг): {data}")
        day, month, year = data_list
        return cls.data_check(day, month, year)

    @staticmethod
    def data_check(day, month, year):
        if day < 1 or day > 31:
            raise Exception("Ошибка!!! День должен быть в пределах 1-31")
        elif month < 1 or month >12:
            raise Exception("Ошибка!!! Месяц должен быть в пределах 1-12")
        elif year < 0 or year > 9999:
            raise Exception("Ошибка!!! Год должен быть в пределах 0-9999")
        return day, month, year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"


dt1 = MyData("23-10-2020")
print(dt1)

try:
    dt2 = MyData("30-12")
except Exception as er:
    print(er)
else:
    print(dt2)

try:
    dt3 = MyData("3o-12-2020")
except ValueError:
    print("Ошибка при вводе числа")
except Exception as er:
    print(er)
else:
    print(dt3)
