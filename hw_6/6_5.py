class Stationery:
    def __init__(self, title = 'Office supplies'):
        self.title = title

    def draw(self):
        print(f'Draw! {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Draw with {self.title} pen')

class Pencil(Stationery):
    def draw(self):
        print(f'Draw with {self.title} pencil')

class Handle(Stationery):
    def draw(self):
        print(f'Draw with {self.title} handle')

stat = Stationery()
pen = Pen('Green')
pencil = Pencil('Black')
handle = Handle("Red")

office_supplies = [stat, pen, pencil, handle]

for i in office_supplies:
    i.draw()