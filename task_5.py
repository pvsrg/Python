vyruchka = float(input('Введите выручку: '))
izdergki = float(input('Введите издержки: '))

if vyruchka == izdergki:
    print('Вы сработали в ноль')
elif vyruchka < izdergki:
    print('Вы сработали в убыток')
    print(f'Убыток составил: {izdergki - vyruchka:.2f} рублей')
else:
    print('Вы сработали с прибылью')
    print(f'Прибыль составила: {vyruchka - izdergki:.2f} рублей')
    print(f'Рентабельность составила: {(vyruchka - izdergki) / vyruchka * 100:.2f} %')
    number_employes = int(input('Введите количество сотрудников: '))
    print(f'Удельная прибыль на сотрудника составила: {(vyruchka - izdergki) / number_employes:.2f} рублей')
