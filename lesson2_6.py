my_list = []
list_name = []
list_price = []
list_amt = []
list_unit = []
what = input('Хотите добавить товар? (да/нет) ')
if what == 'да':
    while True:
        number = int(input('Введите порядковый нормер товара: '))
        name = input('Введите назавание товара: ')
        list_name.append(name)
        price = float(input('Введите цену товара: '))
        list_price.append(price)
        amt = int(input('Введите количество товаров: '))
        list_amt.append(amt)
        unit = input('Введите единицы измерения: ')
        list_unit.append(unit)
        my_dictionary = {'Название': name, 'Цена': price, 'Количество': amt, 'Единицы измерения': unit}
        my_tuple = (number, my_dictionary)
        my_list.append(my_tuple)
        what = input('Хотите добавить еще один товар? (да/нет) ')
        if what == 'нет':
            break
else:
    print('Нет товаров в списке:')
print(my_list)
new_dictionary = {'Название': list(set(list_name)),
                  'Цена': list_price,
                  'Количество': list_amt,
                  'Единицы измерения': list(set(list_unit))}
print(new_dictionary)
