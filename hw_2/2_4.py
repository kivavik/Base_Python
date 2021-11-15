a = input('Ввведите текст через пробел: ').split()
for i, word in enumerate(a, 1):
    print(f'{i}) {word[:10]}')