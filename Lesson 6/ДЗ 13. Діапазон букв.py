import string
user_input_liters = input('Введите две буквы через дефис: ')
lst = [] # Пустой спискок в который добовляются символы без "-"
index_find = [] # Список для найденых индексов
if len(user_input_liters) > 3:
    print('Вы ввели больше символов')
else:
    lst = user_input_liters.split('-')
    for x in lst:
        fd = string.ascii_letters.find(x)
        index_find.append(fd)
print(string.ascii_letters[min(index_find):max(index_find) + 1])

# import string
#
# user_input_liters = input('Введите две буквы через дефис: ')
# if len(user_input_liters) > 3:
#     print('Вы ввели больше символов')
# a = string.ascii_letters.find(user_input_liters[0])
# b = string.ascii_letters.find(user_input_liters[2])
# if a < b:
#     print(string.ascii_letters[a:b + 1])
# else:
#     print(string.ascii_letters[b:a + 1])
