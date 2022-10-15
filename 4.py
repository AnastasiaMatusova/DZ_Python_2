# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

from math import prod
with open('file.txt', 'r') as my_file:
    data = my_file.read()
lst = data.split()
lst2 = []
print('Элементы из файла: ', lst)
for element in lst:
    lst2.append(int(element))
print('Отредактированный список :', lst2)
print('Произведение элементов на указанных позициях равно:', prod(lst2))