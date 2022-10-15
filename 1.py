# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

str1 = str(input('Введите число :'))
str2 = str1.replace(',', '').replace('.', '')
str3 = int(str2)
index = 0
summ = 0
remainder_ = 0
summ = 0
while (str3 != 0):
    remainder_ = str3 % 10
    summ = summ + remainder_
    str3 = str3//10
print(f'Сумма цифр введенного числа : {summ}')