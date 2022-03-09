x = 0
while x == 0:
    try:
        space = " "
        dgts = '1234567890+-/.+'
        name = input("Как тебя зовут? \n")
        if space in name:
            x = 0
            space = 1
        else:
            space = 0
            x = 1
        if space == 1:
            print("Убери пробел")
        for i in name:
            if i in dgts:
                x = 0
                dg = 1
            else:
                dg = 0
                x = 1
        if dg == 1:
            print("Убери символы")
        x2 = 0
        while x2 == 0:
            if x == 1:
                x3 = 0
                while x3 == 0:
                    try:
                        age = input("Сколько тебе лет, " + name + "? \n")
                        if int(age) < 1 or int(age) > 150:
                            print("Ты либо еще не родился, либо уже мертв")
                            x2 = 0
                        else:
                            x2 = 1
                            if int(age[len(age) - 1:len(age):]) < 5:
                                print(name + ", тебе " + age + " лет", sep=" ")
                            else:
                                print(name + ", тебе " + age + " лет", sep=" ")
                        x3 = 1
                    except:
                        x3 = 0
                        print("Ввозраст должен быть корректным...")
    except:
        x = 0
