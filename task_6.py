try:
    with open("task_6.txt", "r", encoding="utf-8") as f_in:
        sub_dic = {nm: sum(map(int, vl.replace('(лаб)', '').replace('(пр)', '').replace('(л)', '').
                               replace('(лаб)', '').replace('-', '').replace('.', '').split()))
                               for nm, vl in [s.split(':') for s in f_in.readlines()]}

    print(sub_dic)
except IOError:
    print("ОШИБКА при чтении файла!!!")
except ValueError:
    print(f"ОШИБКА в формате задания предмета, количества часов или типа занятий!!!")

