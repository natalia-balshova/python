from functools import reduce


def my_func(a, b):
    return a * b


print(reduce(my_func, [n for n in range(100, 1001) if n % 2 == 0]))
