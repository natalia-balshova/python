my_list = [1, 4, 7, 4, 9, 12, 32]
add_to_list = int(input('Введите натуральное число для рейтинга: '))
if add_to_list in my_list:
    my_list.sort()
    my_list.reverse()
    i = my_list.index(add_to_list) + my_list.count(add_to_list)
    my_list.insert(i, add_to_list)
else:
    my_list.append(add_to_list)
    my_list.sort()
    my_list.reverse()
print(my_list)
