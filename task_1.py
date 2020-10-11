print("Введите данные построчно, пустая строка выход")
with open("task_1.txt", "w", encoding="utf-8") as f_out:
    while len(s := input()) > 0:
        print(s, file=f_out)



