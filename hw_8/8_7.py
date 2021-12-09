class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * j'

    def __add__(self, other):
        print(f'Сумма c_1 и c_2 равна: ')
        return f'c = {self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        print(f'Произведение c_1 и c_2 равно: ')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * j'

    def __str__(self):
        return f'c = {self.a} + {self.b} * j'


c_1 = ComplexNumber(3, 4)
c_2 = ComplexNumber(5, 6)
print(c_1)
print(c_2)
print(ComplexNumber.__add__(c_1, c_2))
print(ComplexNumber.__mul__(c_1, c_2))