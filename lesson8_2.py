class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = input('Введите делимое: ')
    b = input('Введите делитель: ')
    a = int(a)
    b = int(b)
    if b == 0:
        raise MyZeroDivisionError('Деление на ноль невозможно!')
except ValueError:
    print('Вы ввели не число. Будьте внимательнее!')
except MyZeroDivisionError as err:
    print(err)
else:
    print(f"При делении {a} на {b} получается {a / b}")
