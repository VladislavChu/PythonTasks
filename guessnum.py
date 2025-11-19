from random import *
from math import *

while True:

    print('Добро пожаловать в числовую угадайку!')

    mx = int(input('Задайте максимальное число для игры: '))

    num  = randint(1, mx)

    #объявление функции "проверка на дурака"
    def is_valid(number):
        if number.isdigit() and 0 < int(number) < mx:
            return True
        else:
            return False

    total = 1

    while True:
        n = input(f'Введите число от 1 до {mx} включительно: ')

        if is_valid(n) == True:

            n = int(n)
            if num < n:
                print('Ваше число больше загаданного, попробуйте еще разок')
            if num > n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            if num == n:
                print('Вы угадали, поздравляем!')
                print(f'Количество ваших попыток: {total}')
                print('Спасибо, что играли в числовую угадайку. Давайте сыграем еще раз!')
                print('_________________________________________________________________')
                print()
                break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {mx}?')
    
        total += 1
