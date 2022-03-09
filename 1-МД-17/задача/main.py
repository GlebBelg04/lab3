a = "Vasya"
print(a)

b = "20"
print(b)

a1 = a*5
print(a1)

print("Как тебя зовут и сколько тебе лет?")
user_name = input()
user_age = input()
print("Привет", user_name, "тебе не", user_age, "хахахах я пошутил")

print("Напиши свой возраст")

user_age = int(input())
if user_age >= 20:
    print("Ну ты старик")
else:
    print("Везет... ты еще молодой")


print(user_name[1:-1])
print(user_name[::-1])
print(user_name[-3])
print(user_name[5])
