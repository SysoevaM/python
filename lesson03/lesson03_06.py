# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую
# его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной
# строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную
# ранее функцию int_func().

import re


# функция преобразования слова: первая заглавная, остальные строчные
def int_func(word):
    result = word.capitalize()
    return result


user_string = input('Введите строку из латинских букв в нижнем регистре >>>')

# проверяем введенную строку на запрещенные символы
if None is re.search(r"[а-яА-Я0-9,.?!/`~'@#$%^&*()_+=]", user_string):

    # преобразуем в список
    user_string = user_string.split()

    string_new = ""

    # в цикле преобразуем строку
    for i in range(len(user_string)):
        string_new = string_new + " " + int_func(user_string[i])

    print(string_new)
else:
    print('Строка содержит не только латинские буквы!')
