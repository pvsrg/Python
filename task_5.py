print("Введите несколько чисел через пробел")
try:
    with open("task_5.txt", "w", encoding="utf-8") as f_out:
        f_out.write(' '.join([f"{float(nmb)}" for nmb in input().split()]))
    with open("task_5.txt", "r", encoding="utf-8") as f_inp:
        print(f"Сумма чисел в файле: {sum([float(nmb) for nmb in f_inp.readline().split()])}")
except IOError:
    print("ОШИБКА при чтении/записи в файл!!!")
except ValueError:
    print(f"ОШИБКА в значении числа!!!")

