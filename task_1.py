from sys import argv

try:
    my_par = dict(zip(('выработка', 'ставка', 'премия'), list(map(float, argv[1:]))))
    print(f"Заработная плата = {(my_par['выработка'] * my_par['ставка']) + my_par['премия']:10.2f}")
except ValueError:
    print("ОШИБКА!!! Не корректно указаны парметры")
except KeyError:
    print("ОШИБКА!!! Не все парметры указаны")
