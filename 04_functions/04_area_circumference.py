import math

def measurements(radius):
    area = round(math.pi * radius ** 2,2)
    circumference = round(2 * math.pi * radius,2)

    return area, circumference

a, c = measurements(int(input("Enter radius: ")))

print(f"Area: {a}, Circumference: {c}")
