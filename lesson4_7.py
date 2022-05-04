def fact(n):
    f = 1
    for k in range(1, n + 1):
        f = f * k
        yield f


n = int(input('Введите число: '))
for el in fact(n):
    print(el, end=' ')

