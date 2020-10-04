offset = ord('a') - ord('A')


def int_func(word):
    """Функция заменяет в слове из латинских букв в нижнем регистре первую букву на прописную"""
    word_chr = list(word)
    for wchr in word_chr:
        if (wchr < 'a') or (wchr > 'z'):
            raise Exception(f"Ошибка символ '{wchr}'!!! Слова должны содержать только латинские буквы в нижнем регистре")
    word_chr[0] = chr(ord(word_chr[0]) - offset)
    return "".join(word_chr)


try:
    result = ""
    for wrd in input("Введите через провел несколько слов из латинских букв в нижнем регистре\n>").split():
        result = result + " " + int_func(wrd) if len(result) > 0 else int_func(wrd)
    print(result)
except Exception as e:
    print(e)
