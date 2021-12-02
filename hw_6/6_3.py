class Worker:
    def __init__(self, name, surname, position, wage, bonus):
       self.name =name
       self.surname = surname
       self.position = position
       self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_full_income(self):
        return f'{sum(self._income.values())}'

manager = Position('Иван', 'Иванов', "Менеджер", 1000, 100)

print(manager.position)
print(manager.get_full_name())
print(manager.get_full_income())