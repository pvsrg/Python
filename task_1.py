product_name = 'Смартфон Samsung Galaxy Note 20 Ultra 5G 12/512GB'
product_number = 1
product_summa = 119990.0

print('Ваш заказ')
print(f'{product_name:<30}  {product_number:>4} шт.  {product_summa:>12.2f} руб.')

print('Для оплаты введите:')
kart_number = input('Номер банковской карточки: ')
kart_owner = input('Владельца: ')
kart_kod = int(input('Секретный код: '))

print(f'Ваша карта номер: {kart_number:<20} владелец: {kart_owner:<20} код: {kart_kod:3}')
