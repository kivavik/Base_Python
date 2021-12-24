class MyStores:
    def __init__(self, department, shelf, place):
        self.department = department
        self.shelf = shelf
        self.place = place

    def __str__(self):
        return f'Department: {self.department} // shelf: {self.shelf} // place: {self.place}'

    @classmethod
    def depatment(cls):
        try:
            cls.name = input('Enter department: ')
            cls.shelf = int(input('Enter shelf number: '))
            cls.place = int(input('Enter place number: '))
            cls.department = {'Deparment': cls.name, 'shelf': cls.shelf, 'place': cls.place}
            print(f'{cls.department}')
            return MyAssets.choose()
        except:
            print(f'Data type error!')
            pass

class MyAssets:

    def __init__(self, model, price, quantity, *args):
        self.model = model
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return str({'Model': self.model, 'Price': self.price, 'Quantity': self.quantity})

    def choose():
        choose = input(f'Choose:\nP - printer\nS - scanner\nC - copier\nAny other key - quit\n---> ').capitalize()
        if choose == 'P':
            return Printer()
        elif choose == 'S':
            return Scanner()
        elif choose == 'C':
            return Copier()
        else:
            print(f'No asset was chosen!')


    @classmethod
    def assets(cls):
        cls.assets = []
        while True:
            try:
                cls.model = input(f'Enter model: ')
                cls.price = int(input(f'Enter price per item: '))
                cls.quantity = int(input(f'Enter quantity: '))
                cls.unit = {'Model': cls.model, 'Price': cls.price, 'Quantity': cls.quantity}
                cls.unit.update(cls.unit)
                cls.assets.append(cls.unit)
                print(f'Current list:')
                for i in cls.assets:
                    print(f'{i}')
            except:
                print(f'Data type error!')
                pass

            print(f'Press "Q" to quite, Press any "Enter" to continuous')
            q = (input(f'---> ')).capitalize()
            if q == 'Q':
                # return print(f'Next step')
                break


class Printer(MyAssets):

    def __init__(self, *copies):
        print(f'Enter printer to print')
        super().assets()
        self.copies = copies
        copies = int(input(f'Enter number of copies to print: '))
        return print(f'Printed {copies} copies')


class Scanner(MyAssets):

    def __init__(self, *copies):
        print(f'Enter scanner to scan')
        super().assets()
        self.copies = copies
        copies = int(input(f'Enter number of copies to scan: '))
        return print(f'Scanned {copies} copies')


class Copier(MyAssets):

    def __init__(self, *copies):
        print(f'Enter copier to copy')
        super().assets()
        self.copies = copies
        copies = int(input(f'Enter number of copies to copy: '))
        return print(f'Copied {copies} copies')


dep = MyStores.depatment()

# assets = MyAssets.choose()
# assets = MyAssets.assets()

# printer = Printer()
# scaner = Scanner()
# copier = Copier()