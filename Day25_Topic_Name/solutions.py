# Day 25 - Python Tricks Solutions

# 1. Swap Without Temp
a, b = 15, 25
a, b = b, a
print("1:", a, b)  # 25 15

# 2. Squares with List Comprehension
squares = [x**2 for x in range(1, 11)]
print("2:", squares)  # [1, 4, 9, ..., 100]

# 3. Dictionary Comprehension (cubes)
cubes = {x: x**3 for x in range(1, 6)}
print("3:", cubes)  # {1:1, 2:8, 3:27, 4:64, 5:125}

# 4. Zip Two Lists
names = ["Alice", "Bob", "Charlie"]
scores = [90, 80, 85]
print("4:")
for name, score in zip(names, scores):
    print(name, score)

# 5. Enumerate with Index
fruits = ["Apple", "Banana", "Cherry"]
print("5:")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# 6. Reverse a String
s = "interview"
print("6:", s[::-1])  # weivretni

# 7. Merge Two Dictionaries
dict1 = {"x": 1, "y": 2}
dict2 = {"z": 3}
merged = {**dict1, **dict2}
print("7:", merged)  # {"x": 1, "y": 2, "z": 3}

# 8. Check Even Numbers with all()
nums = [2, 4, 6, 8]
print("8:", all(x % 2 == 0 for x in nums))  # True

# 9. Ternary Operator
num = 11
result = "Even" if num % 2 == 0 else "Odd"
print("9:", result)  # Odd

# 10. File Writing with Context Manager
with open("output.txt", "w") as f:
    f.write("Python is powerful")
print("10: File written successfully")

# 11. F-String Formatting
name = "Alice"
score = 95
print("11:", f"{name} scored {score} marks")  # Alice scored 95 marks
