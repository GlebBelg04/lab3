name = 'Дарья'
print(name)

age = '18'
print("Меня зовут", name, ",", "мне" , age)

print(name+name+name+name+name)
print(name * 5)

user_name = input("Как вас зовут? :")
user_age = input("Сколько вам лет? :")
print(f"Привет, {user_name}!")
user_age_str = int(user_age)
if user_age_str < 18:
    print("Давно родился?")
if user_age_str >= 18:
    print("Скоро на пенсию?")





