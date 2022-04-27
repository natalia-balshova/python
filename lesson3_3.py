def my_func(arg_1, arg_2, arg_3):
    my_tuple = arg_1, arg_2, arg_3
    my_list = sorted(my_tuple)
    my_list.pop(0)
    my_sum = sum(my_list)
    print(my_sum)


my_func(3, 1, 4)
