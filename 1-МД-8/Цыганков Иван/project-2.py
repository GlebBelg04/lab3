seat = int(input("Your seat number, please: "))
if seat % 5 == 0:
    print("your seat is on side")
elif seat % 2 == 1:
    print("your seat is down one")
elif seat % 2 == 0:
    print("your seat is upper one")