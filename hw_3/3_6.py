def int_func(word):
    latin_letters = 'qwertyuiopasdfghjklzxcvbnm'
    if not set(word).difference(latin_letters):
        return word.title()
    #else:
        #print(f'Cлово {word} не соответствует критериям обработки')

word = input('Ввведите слова через пробел: ').split()
for w in word:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')