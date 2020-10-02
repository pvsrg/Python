winter = 'Зима'
spring = 'Весна'
summer = 'Лето'
autumn = 'Осень'

month_list = [winter, winter, spring, spring, spring, summer, summer, summer, autumn, autumn, autumn, winter]
month_dict = {1: winter, 2: winter, 12: winter, 3: spring, 4: spring, 5: spring, 6: summer, 7: summer, 8: summer,
              9: autumn, 10: autumn, 11: autumn}

month_number = int(input("Введите номер месяца (число от 1 до 12): "))
if month_number < 1 or month_number > 12:
    print("Ошибка в номере месяца")
else:
    print(f"Время года по списку - {month_list[month_number - 1]}")
    print(f"Время года по списку - {month_dict.get(month_number)}")
