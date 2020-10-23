class MyError(Exception):
    def __init__(self, er_number):
        self.er_number = er_number

    def __str__(self):
        return f"Ошибка!!! Некорректно введенное число {self.er_number}"


list_nmb = []
while True:
    inp = input("Введите число (stop -завершение): ")
    if inp == "stop":
        break
    try:
        if not inp.isnumeric():
            raise MyError(inp)
    except MyError as er:
        print(er)
    else:
        list_nmb.append(int(inp))

print(list_nmb)
