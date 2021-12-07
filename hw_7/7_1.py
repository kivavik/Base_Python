from itertools import zip_longest

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*p, fillvalue=0)) for p in zip_longest(self.matrix, other.matrix, fillvalue=[])])



matrix_1 = [[31, 22], [37, 43], [51, 86]]
matrix_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]

m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)

print(f'{m_1}\n')
print(f'{m_2}\n')
print(m_1+m_2)

