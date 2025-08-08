
# Problem 1: Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Problem 2: Fibonacci Series using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Problem 3: Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# Problem 4: Sum of Digits using Recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

# Problem 5: GCD using Recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
