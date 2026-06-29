str = input("Enter string: ")

for char in str:
    if str.count(char) == 1:
        print(f"Character is: {char}")
        break
