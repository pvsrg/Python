summ_all = 0.0
print("Введите числа через пробел, символ 'q' - выход")
try:
    while True:
        summ_itr = 0.0
        nmb_list = input(">> ").split()
        for nmb in nmb_list:
            summ_itr += float(nmb)
        summ_all += summ_itr
        print(f"Текущая сумма = {summ_itr:.4f} Общая сумма = {summ_all:.4f}")
except ValueError:
    if nmb == "q":
        summ_all += summ_itr
        print(f"Текущая сумма = {summ_itr:.4f} Общая сумма = {summ_all:.4f}")
    else:
        print(f"Ошибка !!! Некорректно введенное число {nmb}")
