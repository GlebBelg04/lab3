color1 = input("enter red, blue or yellow")
color2 = input("enter red, blue or yellow")
if color1 != "red" or color1 != "yellow" or color1 != "blue" or color2 != "red" or color2 != "yellow" or color2 != "blue":
    print("syntax error!")
elif (color1 == "red" and color2 == "blue") or (color1 == "red" and color2 == "blue"):
    print("purple")
elif (color1 == "red" and color2 == "yellow") or (color1 == "red" and color2 == "yellow"):
    print("orange")
elif (color1 == "blue" and color2 == "yellow") or (color2 == "blue" and color1 == "yellow"):
    print("green")
