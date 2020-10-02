rating_list = []

while True:
    rating = int(input("Введите элемент рейтинга (-1 выход): "))
    if rating == -1:
        break
    insert = False
    for i, element in enumerate(rating_list):
        if element < rating:
            rating_list.insert(i, rating)
            insert = True
            break
    if not insert:
        rating_list.append(rating)

    print(rating_list)
