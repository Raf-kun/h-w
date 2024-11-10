num = int(input("Введите число: "))
num2 = int(input("Введите второе число: "))

user_list = [i for i in range(num, num2 + 1)]
print(*user_list)
odd = [i for i in user_list if i % 2 != 0]
print(*odd)
even = [i for i in user_list if i % 2 == 0 and i != 0]
print(*even)
for_nine = [i for i in user_list if i % 9 == 0]
print(*for_nine)

print("Среднее арифмитическое нечетных: " + sum(odd) / len(odd))
print("Среднее арифмитическое четных: " + sum(even) / len(even))
print("Среднее арифмитическое четных: " + sum(for_nine) / len(for_nine))
