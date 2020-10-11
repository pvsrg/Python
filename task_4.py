tran = {'ONE': 'Один', 'TWO': 'Два', 'THREE': 'Три', 'FOUR': 'Четыре'}
try:
    f_inp = open("task_4.txt", "r", encoding="utf-8")
    f_out = open("task_4out.txt", "w", encoding="utf-8")
    f_out.writelines([f"{tran[n.upper()]} - {v}" for n, v in [s.split(' - ') for s in f_inp.readlines()]])
    f_inp.close()
    f_out.close()
except IOError:
    print("ОШИБКА при чтении/записи файла!!!")
except KeyError:
    print("ОШИБКА английского названия числа нет в справочнике!!!")
except ValueError:
    print("ОШИБКА строка не соответсвует формату 'NAMBER - VALUE'!!!")