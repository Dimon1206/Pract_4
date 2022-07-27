import random

a = int(input('Введите количество проверяемых чисел: '))
b = [random.randint(0, 100) for i in range(a)]

c = int(input('Ведите искомую цифру: '))
d = 0
print(b)

for i in b:
    for e in str(i):
        if int(e) == c:
            d += 1
            if d == 1 or d == 2 or d == 3 or d == 4:
                print('Искомая цифра встречается', d, 'раз')
            else:
                print('Искомая цифра не встречается')