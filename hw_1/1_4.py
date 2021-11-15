n = int(input('Введите число'))

a = -1
b = -1
while n > 10:
    a = n % 10
    n //= 10
    if a > b:
        b = a

print(b)