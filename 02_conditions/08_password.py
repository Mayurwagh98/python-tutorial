password = input("Enter a password: ")

length = len(password)

if length < 6:
    strength = "Weak"
elif length < 10:
    strength = "Medium"
elif length > 10:
    strength = "Strong"
else:
    strength = "Invalid password"

print("The password strength is:", strength)