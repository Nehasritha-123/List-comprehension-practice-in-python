num = int(input("Enter number: "))
print([x for x in range(num) if x % 2 != 0])

fruits = ["apple", "banana", "cherry"]
print([f.capitalize() for f in fruits])