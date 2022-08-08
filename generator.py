import random 
import time

def dec(f):
    def f1(*args,**kwargs):
        start = time.monotonic()
        password = f(*args,**kwargs)
        end = time.monotonic()
        finish = end - start
        print(f'Время работы функции = {finish}')
        return password
    return f1


@dec
def foonction3(symbol): #Функция для генерации пароля из символов по умолчанию
    password = []
    length = int(input('Введите длину пароля \n'))
    for i in range(length):
        password.append(random.choice(symbol))
    return password


@dec
def foonction2(): # функция для открытия файла и взятия символов для генерации паролей
    adress = str(input('Введите адресс файла \n'))
    with open(adress,'r') as f:
        symbol = f.read()
        print(symbol)
        password = foonction3(symbol)
    return password
    

def main():
    symbol = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    print('*' * 10,'Функционал', '*'*10)
    print('1 - Сгенерировать пароль из своих символов ')
    print('2 - Сгенерировать пароль из своих символов(с файла)')
    print(f'3 - Сгенерировать пароль из символов по умолчанию: {symbol}')
    
    buf = int(input('Ввыберите действие \n'))
    if buf == 3:
        password = foonction3(symbol)
        password = ''.join(password)
        print(password)
    elif buf == 2:
        password = foonction2()
        password = ''.join(password)
        print(password)
    elif buf == 1:
        symbol = input('Введите символы из которых вы хотите создать пароль \n')
        password = foonction3(symbol)
        password = ''.join(password)
        print(password)
    else:
        print(f'{buf} - неверный символ ')
   
    


if __name__ == '__main__':
    main()