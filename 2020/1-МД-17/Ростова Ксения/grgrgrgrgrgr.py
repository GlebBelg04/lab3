print('Введите 3 числа')
a = int(input())
b = int(input())
c = int(input())

if a+b > c and b+c > a and a+c > b:
    print('значения являются сторонами тряугольника')
    h = int(input())
    if h == 90:
        print('треугольник прямоугольный')
    elif a == b == c:
        print('равностороний')
    elif a != b and a != c and b != c:
        print('разносторонний')
    else:
        print('равнобедренный')
else:
    print('треугольник не существует')


import random
array = [[random.randint(0,100) for i in range(4)] for j in range(4)]
print(array)
s = 1
for i in range(4):
    s *= array[i][i]
    h = s ** (1/4)
print(h)
if  arrai [i][-j]