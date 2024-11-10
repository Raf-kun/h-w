num = int(input("Введите число: "))
num2 = int(input("Введите второе число: "))
for i in range(num, num2 + 1):
    if i % 7 == 0:
        print(i)
    else:
        print("Сори, но не то)")