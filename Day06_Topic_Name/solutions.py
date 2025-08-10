# Day 6 - Python Interview Questions Solutions
# Topic: List Comprehension & Lambda

# 1. Odd Number Squares
odd_squares = [x**2 for x in range(1, 16) if x % 2 != 0]
print("1. Odd Number Squares:", odd_squares)

# 2. Filter Strings by Length
words = ["cat", "elephant", "dog", "giraffe"]
long_words = list(filter(lambda w: len(w) > 4, words))
print("2. Filter Strings by Length:", long_words)

# 3. Tuple to Dictionary
tuple_list = [("a", 1), ("b", 2)]
dict_from_tuples = {key: value for key, value in tuple_list}
print("3. Tuple to Dictionary:", dict_from_tuples)

# 4. Common Elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]
common_elements = [x for x in list1 if x in list2]
print("4. Common Elements:", common_elements)

# 5. Sort by Last Character
fruits = ["apple", "banana", "cherry"]
sorted_by_last = sorted(fruits, key=lambda word: word[-1])
print("5. Sort by Last Character:", sorted_by_last)

# 6. Flatten a List of Lists
nested_list = [[1, 2], [3, 4], [5]]
flattened = [item for sublist in nested_list for item in sublist]
print("6. Flatten a List of Lists:", flattened)
