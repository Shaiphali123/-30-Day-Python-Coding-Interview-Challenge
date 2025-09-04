# Solution.py
# This script contains all the Python code examples from the dictionary use cases notes.

from collections import Counter

# --- Use Case 1: Representing Structured Data ---
print("--- 1. Representing Structured Data ---")
# A dictionary representing a user's profile
user_profile = {
    "user_id": 101,
    "username": "alex_coder",
    "email": "alex@example.com",
    "is_active": True,
    "permissions": ["read", "write"]
}

# Accessing data is intuitive
print(f"Username: {user_profile['username']}")
print(f"Permissions: {user_profile['permissions'][0]}")
print("-" * 20 + "\n")


# --- Use Case 2: Frequency Counting ---
print("--- 2. Frequency Counting ---")
# Example: Counting Characters in a String (Manual)
text = "hello world"
char_counts = {}
for char in text:
    # Use .get() to handle the first time a character is seen
    char_counts[char] = char_counts.get(char, 0) + 1
print(f"Manual Count: {char_counts}")

# Pro Tip: Using collections.Counter
char_counts_pro = Counter(text)
print(f"Using Counter: {char_counts_pro}")
print("-" * 20 + "\n")


# --- Use Case 3: Caching / Memoization ---
print("--- 3. Caching / Memoization ---")
# A cache to store previously computed Fibonacci numbers
fib_cache = {}

def fibonacci(n):
    # If the value is in the cache, return it
    if n in fib_cache:
        return fib_cache[n]
    
    # Base cases
    if n <= 1:
        return n
        
    # Compute it, store it in the cache, and then return it
    result = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = result
    return result

# The calculation for 35 would be very slow without memoization
fib_num = fibonacci(35)
print(f"Fibonacci(35) = {fib_num}")
print(f"Cache now contains {len(fib_cache)} memoized results.")
print("-" * 20 + "\n")


# --- Use Case 4: Grouping Data ---
print("--- 4. Grouping Data ---")
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "C"},
    {"name": "Eve", "grade": "B"},
]

grades = {}
for student in students:
    grade = student["grade"]
    # .setdefault() initializes the key with an empty list if it's not present
    grades.setdefault(grade, []).append(student["name"])

print(f"Students grouped by grade: {grades}")
print("-" * 20 + "\n")


# --- Interview Questions Solutions ---
print("--- Interview Questions Solutions ---\n")

# Q1: Merging two dictionaries
print("--- Q1: Merging Dictionaries ---")
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Method 1: Using update()
merged_dict1 = dict1.copy() # Use copy to avoid modifying the original
merged_dict1.update(dict2)
print(f"Using update(): {merged_dict1}")

# Method 2: Using dictionary unpacking (Python 3.5+)
merged_dict2 = {**dict1, **dict2}
print(f"Using unpacking: {merged_dict2}")
print("-" * 20 + "\n")


# Q2: d[key] vs d.get(key)
print("--- Q2: d[key] vs d.get(key) ---")
d = {'a': 100}

# Using bracket notation (safe)
print(f"d['a']: {d['a']}") 
# The following line would raise a KeyError if uncommented:
# print(d['b']) 

# Using .get() for safe access
print(f"d.get('a'): {d.get('a')}")       # Prints 100
print(f"d.get('b'): {d.get('b')}")       # Prints None (default value)
print(f"d.get('b', 0): {d.get('b', 0)}") # Prints 0 (specified default)
print("-" * 20 + "\n")


# Q3: Find key with the maximum value
print("--- Q3: Find Key with Maximum Value ---")
scores = {'math': 95, 'science': 98, 'history': 88}

# The key=scores.get tells max() to look at the values, not the keys
top_subject = max(scores, key=scores.get)

print(f"The subject with the highest score is: {top_subject}")
print("-" * 20 + "\n")
