num = int(input("Введите число: "))
num2 = int(input("Введите второе число: "))

user_list = [i for i in range(num, num2 + 1)]
print(*user_list)

print(*user_list[::-1])
print(*[i for i in user_list if i % 7 == 0])
print(len([i for i in user_list if i % 5 == 0]))