import json

try:
    with open("task_7.txt", "r", encoding="utf-8") as f_in:
        firm_dic = {name: float(income) - float(costs) for name, form, income, costs in
                    [s.split() for s in f_in.readlines()]}
    pozitive_list = [prof for prof in firm_dic.values() if prof > 0]
    json_list = [firm_dic, {'average_profit': sum(pozitive_list) / len(pozitive_list)} if len(pozitive_list) > 0 else {
        'average_profit': 0.0}]
    with open("task_7.json", "w") as json_file:
        json.dump(json_list, json_file, indent=4)
except IOError:
    print("ОШИБКА при чтении/записи в файл!!!")
except ValueError:
    print(f"ОШИБКА в значениях расходов/доходов!!!")