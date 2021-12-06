class Cell:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 else 'Cell (n) < Cell (n+1)'

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell(self.nums / other.nums)

    def make_order(self, other):
        return '\n'.join([other for _ in range(self.nums // other)]) + '\n' + (self.nums % other)


c_1 = Cell(13)
c_2 = Cell(5)

print(Cell.__add__(c_1, c_2))
print(Cell.__sub__(c_1, c_2))
print(Cell.__mul__(c_1, c_2))
print(Cell.__truediv__(c_1, c_2))
print(Cell.make_order(13, 5))
