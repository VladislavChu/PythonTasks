from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


password_count = int(input('Сколько паролей необходимо сгенерировать: '))
print('_______________________________________________________________')
password_len = int(input('Укажите кол-во символов для каждого пароля: '))
print('_______________________________________________________________')
need_digit = input('Включать ли в пароль цифры: 0123456789? да/нет: ')
print('_______________________________________________________________')
need_upper_abc = input('Включать ли прописные буквы: ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет: ')
print('_______________________________________________________________')
need_lower_abc = input('Включать ли строчные буквы: abcdefghijklmnopqrstuvwxyz? да/нет: ')
print('_______________________________________________________________')
need_symbols = input('Включать ли символы: !#$%&*+-=?@^_? да/нет: ')
print('_______________________________________________________________')
need_delete_ambiguous = input('Исключать ли неоднозначные символы: "il1Lo0O"? да/нет: ')

if need_digit.lower() == 'да':
    chars += digits
if need_upper_abc.lower() == 'да':
    chars += uppercase_letters
if need_lower_abc.lower() == 'да':
    chars += lowercase_letters
if need_symbols.lower() == 'да':
    chars += punctuation
if need_delete_ambiguous.lower() == 'да':
    for char in chars:
        if char in 'il1Lo0O':
            chars = chars.replace(char, '')


def generate_password(length, chars):
    for i in range(password_count):
        print(*sample(chars, length), sep='')


generate_password(password_len, chars)