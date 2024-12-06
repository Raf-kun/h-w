def tablica():

    num = int(input("Введите начальное число диапозона 1-10: "))
    num2 = int(input("Введите конечное число диапозона 1-10: "))

    first = num
    second = 1
    while first in range (num, num2 + 1):
        for second in range(1, 12):
            if second <= 10:
                print(f'{first} * {second} = {first * second}')
            else:
                print('-'*22)
        first += 1

tablica()
