age = int(input("Enter your age: "))
day = ""


price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2


print(f"The price of the ticket is {price}")