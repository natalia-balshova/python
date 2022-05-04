from random import randint

my_list = [randint(1, 100) for n in range(20)]
print(my_list)
new_list = []
for i in range(len(my_list)):
    if my_list.count(my_list[i]) == 1:
        new_list.append(my_list[i])
        i += 1
print(new_list)