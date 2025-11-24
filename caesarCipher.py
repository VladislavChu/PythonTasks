from math import *

while True:

    print('Добро пожаловать! Данная программа предназначена для шифрования и дешифрования по методу "Шифр Цезаря"')
    print('______________________________________________________________________________________')
    code_decode = input('Вы планируете зашифровать или дешифровать текст? код/декод: ')
    print('______________________________________________________________________________________')
    alpha_language = input('Вы планируете использовать английский или русский алфавит? рус/англ: ')
    print('______________________________________________________________________________________')
    move_point = int(input('Какой будет шаг сдвига вправо? Введите число: '))
    print('______________________________________________________________________________________')
    user_text = input('Введите изначальный текст: ')
    print('______________________________________________________________________________________')
    print('Ваш результат: ', end='')
    print()

    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


    def caesar_cipher(method, language, step, text):
        if language == 'рус':
            moch = 32
        if language == 'англ':
            moch = 26
        if method == 'декод':
            step = -step
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i] == text[i].upper():
                    for j in range(moch):
                        if moch == 32:
                            if text[i] == rus_upper_alphabet[j]:
                                print(rus_upper_alphabet[(j + step) % moch], end='')
                                break
                        if moch == 26:
                            if text[i] == eng_upper_alphabet[j]:
                                print(eng_upper_alphabet[(j + step) % moch], end='')
                                break
                elif text[i] == text[i].lower():
                    for j in range(moch):
                        if moch == 32:
                            if text[i] == rus_lower_alphabet[j]:
                                print(rus_lower_alphabet[(j + step) % moch], end='')
                                break
                        if moch == 26:
                            if text[i] == eng_lower_alphabet[j]:
                                print(eng_lower_alphabet[(j + step) % moch], end='')
                                break
            else:
                print(text[i], end='')



    caesar_cipher(code_decode, alpha_language, move_point, user_text)
