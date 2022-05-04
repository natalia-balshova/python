import random

my_list = [random.randint(1, 100) for n in range(20)]
print(my_list)
new_list = []
for i in range(len(my_list) - 1):
    if my_list[i] < my_list[i+1]:
        new_list.append(my_list[i+1])
        i += 1
print(new_list)
