with open ('text_2.txt', encoding='utf-8') as f:
    line = f.readlines()
    for i, words in enumerate(line, 1):
        num = len(words.split())
        print(f'В строке # {i} {num} слов')