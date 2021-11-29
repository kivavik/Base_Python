with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите новую строку или пустую строку для выхода: ')
        if not line:
            break
        print(line, file=f)