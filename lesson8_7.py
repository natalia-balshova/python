class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = complex(a, b)

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        return f'{self.n}'


n1 = Complex(2, 3)
print(n1)
n2 = Complex(1, 3)
print(n2)
print(n1 + n2)
print(n1 * n2)
