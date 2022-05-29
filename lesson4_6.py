import itertools

for n in itertools.count(3):
    if n == 10:
        break
    else:
        print(n)
my_list = ['hello', 100, 2.3, [1, 2]]
k = 0
for el in itertools.cycle(my_list):
    if k > 10:
        break
    print(el)
    k += 1

