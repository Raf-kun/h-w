my_list = [int(i) for i in input("Введите число").split(",")]
summa = 0
composition = 1
for i in my_list:
    summa += i
    composition *= i
print(summa, composition)
