class DivisionByNull:
    def __init__(self, d_1, d_2):
        self.d_1 = d_1
        self.d_2 = d_2

    @staticmethod
    def divide_by_null(d_1, d_2):
        try:
            return f'Результат: {d_1 / d_2}'
        except:
            return f'Деление на ноль недопустимо'


a = float(input('Ввведите делимое: '))
b = float(input('Ввведите делитель: '))
div = DivisionByNull(a, b)
print(DivisionByNull.divide_by_null(a, b))
