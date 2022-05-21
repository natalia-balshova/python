class Cell:
    def __init__(self, n):
        self.number = n

    def __add__(self, other):
        result = self.number + other.number
        return result

    def __sub__(self, other):
        result = self.number - other.number
        return result if result > 0 else 'Ошибка: результат вычитания должен быть больше 0!'

    def __mul__(self, other):
        result = self.number * other.number
        return result

    def __truediv__(self, other):
        result = self.number // other.number
        return result

    # целочисленное деление через __floordiv__(self, other)
    def __floordiv__(self, other):
        result = self.number // other.number
        return result

    def make_order(self, n):
        self.n = n
        return '\n'.join([f'{"🦝" * self.n}' for el in range(self.number)])


a = Cell(11)
b = Cell(5)
print(f'Увеличение ячеек: {a + b}')
print(f'Уменьшение ячеек: {a - b}')
print(f'Умножение ячеек: {a * b}')
print(f'Деление ячеек: {a / b}')
print(f'Деление ячеек (второй способ): {a / b}')
print(b.make_order(5))
