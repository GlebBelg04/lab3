from math import sqrt


def dist(x, y):
    return sqrt((x[1] - y[1]) ** 2 + (x[0] - y[0]) ** 2)


a = []
for i in range(5):
    while True:
        try:
            x = int(input('Введите координату х точки: '))
            y = int(input('Введите координату y точки: '))
            l = int(x), int(y)
            print(l)
            a.append(l)
            break
        except ValueError:
            print('Ошибка ввода')
print(a)

buf = list(a)
print(buf)
mindist = dist(a[0], a[1])


# print(mindist)

for i in a:
    for j in a:
        if i != j:
            print(i)
            print(j)
            dist(i, j)
            if dist(i, j) < mindist:
                mindist = dist(i, j)
                '''g = i
                u = j'''

            print('расстояние между точками ', i, 'и', j, 'равно', dist(i, j))
del i
print('Наименьшее расстояние между точками равно', mindist)

