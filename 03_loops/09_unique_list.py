items = ["apple", "banana", "orange", "mango"]

unique_list = set()

for item in items:
    if item in unique_list:
        print("Duplicate")
        break
    unique_list.add(item)
