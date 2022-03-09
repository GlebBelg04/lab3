def first():
    print('Введите число: ')
    a = int(input('a= '))
    b = int(input('b= '))
    c = int(input('c= '))
    n = ((a * b) * (a + b + c) * (a + b - c)) ** 1 / 2
    print(n)


def second():
    for i in range(N):
        for j in range(M):
            print(A[i, j])