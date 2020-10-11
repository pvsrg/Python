try:
    with open("task_3.txt", "r", encoding="utf-8") as f_in:
        salary_list = [{'Фамилия': name, 'Зарплата': float(sal)} for name, sal in
                       [sl.split() for sl in f_in.readlines()]]
    if len(salary_list) == 0:
        raise Exception("Ошибка!!! Пустой список")

    empl_list = [empl for empl in salary_list if empl['Зарплата'] < 20000.0]
    average = sum([empl['Зарплата'] for empl in salary_list]) / len(salary_list)
    print(f'Сотрудники с окладом меньше 20 тыс.рублей ({len(empl_list)} чел.):')
    for i, empl in enumerate(empl_list, 1):
        print(f"{i:>3}.{empl['Фамилия'][:30]:<30} {empl['Зарплата']:>10.2f}")
    print(f"Средний оклад по списку: {average:>10.2f}")
except IOError:
    print("ОШИБКА при чтении файла!!!")
except ValueError:
    print(f"ОШИБКА в значении оклада!!!")
except Exception as er:
    print(er)
