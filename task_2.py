try:
    with open("task_1.txt", "r", encoding="utf-8") as f_in:
        list_line = f_in.readlines()
    print(f"Количество строк в файле: {len(list_line)}")
    for i, line in enumerate(list_line, 1):
        print(f"Слов в {i} строке = {len(line.split())}")
except IOError:
    print("ОШИБКА при чтении файла!!!")



