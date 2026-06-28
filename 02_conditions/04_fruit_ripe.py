fruit = input("Enter a fruit: ")

color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    else:
        print("Unknown color")
elif fruit == "Apple":
    if color == "Red":
        print("Ripe")
    elif color == "Green":
        print("Unripe")
    else:
        print("Unknown color")
else:
    print("Unknown fruit")