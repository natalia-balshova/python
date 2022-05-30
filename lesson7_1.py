from random import randint


class Matrix:

    def __init__(self, matrix=[]):
        for i in range(3):
            matrix.append([randint(1, 100) for n in range(3)])
        self.matrix = matrix

    def __str__(self):
        return f'{self.matrix[0][0]} {self.matrix[0][1]} {self.matrix[0][2]}\n' \
               f'{self.matrix[1][0]} {self.matrix[1][1]} {self.matrix[1][2]}\n' \
               f'{self.matrix[2][0]} {self.matrix[2][1]} {self.matrix[2][2]}'

    def __add__(self, other):
        return Matrix([[a+b for a, b in zip(*couples)] for couples in zip(self.matrix, other.matrix)])

m1 = Matrix()
print(m1.matrix)
print(m1)
print()
m2 = Matrix(matrix=[])
print(m2.matrix)
print(m2)
print()
print(m1+m2)
