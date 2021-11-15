original_list = input('Ввведите числа через пробел: ').split()

print(f'Оригинальный список {original_list}')
i = 0

while i + 1 < len(original_list):
    if i % 2 == 0:
        original_list.insert(i+1,original_list.pop(i))
    i += 1

print(f'Измененный список {original_list}')