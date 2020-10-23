class MyError(Exception):
    def __str__(self):
        return "Ошибка!!! Деление на ноль"


div = float(input("Введите делимое: "))
rt = float(input("Введите делитель: "))
try:
    if rt == 0:
        raise MyError()
except MyError as er:
    print(er)
else:
    print(f"{div} / {rt} = {div / rt:<10.3f}")







