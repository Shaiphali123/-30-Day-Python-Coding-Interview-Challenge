# Problem 1: Swap two variables
a = 5
b = 10
a, b = b, a
print("Swapped values:", a, b)

# Problem 2: Sum of digits
num = 1234
sum_digits = sum(int(digit) for digit in str(num))
print("Sum of digits:", sum_digits)

# Problem 3: Data type of user input
user_input = input("Enter something: ")
print("Data type:", type(user_input))

# Problem 4: Celsius to Fahrenheit
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Problem 5: Convert seconds to HH:MM:SS
total_seconds = 3665
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
