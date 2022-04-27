# Способ 1
def my_func(x, y):
    print(x ** y)


my_func(2, -2)


# Способ 2
def my_func2(x, y):
    result = 1
    for i in range(abs(y)):
        result = result * x
    print(1 / result)


my_func2(2, -2)
