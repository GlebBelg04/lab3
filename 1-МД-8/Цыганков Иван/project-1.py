verification_name = input("Your name: ")
verification_password = input("Your password: ")
verification_password_correct = input("Repeat password: ")
if verification_password == verification_password_correct:
    print("Success verification. Welcome,", verification_name)
else:
    print("Error!")

    