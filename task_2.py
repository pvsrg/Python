def print_profile(first_name, last_name="", year_of_birth=0, city="", email="", phone=""):
    """Печатает данные прользователя

        Параметры:
        first_name - обязательный параметр
        last_name, year_of_birth, city, email, phone - именнованные необязательные параметры
    """
    print(f"Имя: {first_name[:20]} ", end="")
    if len(last_name) > 0:
        print(f"Фамилия: {last_name[:20]} ", end="")
    if year_of_birth > 0:
        print(f"Год рождения: {year_of_birth:<4} ", end="")
    if len(city) > 0:
        print(f"Город: {city[:20]} ", end="")
    if len(email) > 0:
        print(f"Почта: {email[:20]} ", end="")
    if len(phone) > 0:
        print(f"Телефон: {phone[:20]}", end="")
    return


atr_dict = {'last_name': ('s', 'Фамилия'), 'year_of_birth': ('i', 'Год рождения'), 'city': ('s', 'Город'),
            'email': ('s', 'Почта'), 'phone': ('s', 'Телефон')}
name = input("Введите Ваше имя (обязательный параметра): ")
if len(name) == 0:
    print("Ошибка! Не введено имя")
else:
    profile_atr = dict()
    for atr in atr_dict:
        atr_val = input(f"{atr_dict[atr][1]}: ")
        if atr_dict[atr][0] == "i":
            try:
                atr_val = int(atr_val) if len(atr_val) > 0 else 0
            except ValueError:
                print("Ошибка !!! Некорректно введенное число")
                atr_val = 0
        if (atr_dict[atr][0] == "i" and atr_val > 0) or (atr_dict[atr][0] == "s" and len(atr_val) > 0):
            profile_atr.update({atr: atr_val})
    print_profile(first_name=name, **profile_atr)
