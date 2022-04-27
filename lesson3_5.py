#решение без функций
new_list = []
my_str = input('Введите числа через пробел')
my_list = my_str.split()
print(my_list)
for i in my_list:
    i = int(i)
    new_list.append(i)
print(new_list)
print('Сумма: ', sum(new_list))
what = input('Хотите продолжить введение чисел?(да/нет)')
if what == 'да':
    while True:
        add_to_str = input('Введите числа через пробел')
        add_to_list = add_to_str.split()
        for el in add_to_list:
            el = int(el)
            new_list.append(el)
        print(new_list)
        print('Новая сумма: ', sum(new_list))
        what = input('Хотите продолжить введение чисел?(да/нет)')
        if what == 'нет':
            break
else:
    print('Программа завершена')
