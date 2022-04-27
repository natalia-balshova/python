def int_func(word):
    return word.capitalize()


my_str = input('Введите строку из слов через пробел: ')
my_list = my_str.split()
new_list = []
for el in my_list:
    el = int_func(el)
    new_list.append(el)
print(' '.join(new_list))

