# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def sum_digit(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    return sum


def multi_digit(num):
    res = 1
    while num != 0:
        res *= num % 10
        num //= 10
    return res


name = 'Alisa'
print(name)

age = 19
print('Hi, my name is', name, 'and I am', age)

name5 = name * 5
print(name5)

guestName = input('What is your name?')
if guestName.isalpha() == False or guestName.isspace() == True:
    print('')

guestAge = input('How old are you?')
guestAge = int(guestAge)

if guestAge < 0 or guestAge > 150:
    print('')
print('Hi,', guestName, '!', 'I have', guestAge, 'cats)')

if guestAge < 18:
    print("You're so little cutie pie")
else:
    print("How is your health? Are knees and back ok?")

print(guestName[1:-1])
print(guestName[::-1])
print(guestName[-3:])
print(guestName[:6])

print('Name len:', len(guestName))
print(sum_digit(guestAge))
print(multi_digit(guestAge))

print(guestName.upper())
print(guestName.lower())
print(guestName.capitalize())
print(guestName.capitalize().swapcase())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
