class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка или булево")
                decision = (input(f'Продолжить? Введите "Y" or "N" ')).upper()

                if decision == 'Y':
                    print(try_except.my_input())
                elif decision == 'N':
                    print(f'Операция завершена')
                    quit()
                else:
                    print(f"Недопустимое значение - строка или булево")
                    print(try_except.my_input())


try_except = Error(1)
print(try_except.my_input())
