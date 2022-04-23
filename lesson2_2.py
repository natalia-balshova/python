my_list = input('Введите этементы, которые вы хотите внести в список, через пробел')
my_list = my_list.split()
print(my_list)
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)
