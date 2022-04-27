#решение с функцией my_func
new_list = []


def my_func():
    """
    преобразовывет строку в список
    преобразовывет элементы этого списка в формат int
    добавляет эти элементы в другой список
    """
    my_str = input('Введите числа через пробел')
    my_list = my_str.split()
    for i in my_list:
        i = int(i)
        new_list.append(i)


my_func()
print('Сумма: ', sum(new_list))
what = input('Хотите продолжить введение чисел?(да/нет)')
while what == 'да':
    my_func()
    print('Новая сумма: ', sum(new_list))
    what = input('Хотите продолжить введение чисел?(да/нет)')
    if what == 'нет':
        break
print('Сумма всех элементов окончательного списка: ', sum(new_list))
