num = int(input("Enter the number: "))
copy_num = num
factorial = 1

while copy_num > 0:
    factorial *= copy_num
    copy_num -= 1

print(f"Factorial of {num} is: {factorial}")