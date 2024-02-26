from random import randint as rnd

result = rnd(1, 100)

x = int(input('Введите число: '))

while x != result:
    if x > result:
        print('Ваше число больше того, что загадано')
    else:
        print('Ваше число меньше того, что загадано')
    x = int(input('Попробуй еще: '))

print('Отличная интуиция! Вы угадали число :)')