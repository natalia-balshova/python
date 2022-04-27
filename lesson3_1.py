def dev_f(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ArithmeticError:
        return


a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))
if b != 0:
    print(f"При делении {a} на {b} получается {round(dev_f(a, b), 2)}")
else:
    print('На 0 делить нельзя')