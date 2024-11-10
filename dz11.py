num = 0

while num != 7:
    num = int(input("Введите число: "))
    if num == 7:
        print("Все норм)")
    elif num > 0:
        print("Число больше нуля!")
    elif num < 0:
        print("Число меньше нуля!")
    else:
        print("Число равно нулю!")