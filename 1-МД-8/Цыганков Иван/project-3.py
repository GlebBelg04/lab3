def calculations(year):
    if (year % 2 == True) and (year % 100 == False) and (year % 400 == True):
        return True
    else:
        return False


check=bool(False)
while check == False:
    year = int(input("type a year: "))
    check = calculations(year)
    print("Year ne visokocniy :)")
print("Year visocosniy :D")