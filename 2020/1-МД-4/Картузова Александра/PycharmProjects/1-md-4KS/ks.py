print(" 0. Добро пожаловать"
      
      " 1. Привет"
      
      " 2. Хочу спать"
      
      " 3. Хочу есть"
      
      " 4. Хочу домой")

a = int(input("a="))
if a == 0:
    print("Привет")
elif a == 1:
    print("Иди спать")
elif a == 2:
    print("еда в холодильнике")
elif a == 3:
    print("сладких снов")
elif a == 4:
    print("ну и вали домой")
else:
    print("ББ")

12
#l = list(1,2,3,4,7,8,9,9)
l = [1,2,3,3,3,3,3]

l.append(8)
l.pop(3)

#print(dir(l))

#help(l)

s = set(l)

s.add(6)
s.add(5)

s.pop()

print(s)

d = {1:"1", 2:"444",3:"kyky"}
d["4"] = "fff"
#d.pop(5)
#print(dir(d))
