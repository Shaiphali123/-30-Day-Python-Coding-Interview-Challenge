# Day 26 — Decorators & Generators Solutions

import time
from functools import wraps


# 1. Basic Decorator
def basic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function is being executed")
        return func(*args, **kwargs)
    return wrapper

@basic_decorator
def greet():
    print("Hello, World!")

print("1:")
greet()


# 2. Timing Decorator
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.2f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    print("Done")

print("\n2:")
slow_function()


# 3. Authentication Decorator
def auth_decorator(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            print("Access denied")
            return
        return func(user, *args, **kwargs)
    return wrapper

@auth_decorator
def view_dashboard(user):
    print(f"Welcome {user}!")

print("\n3:")
view_dashboard("admin")
view_dashboard("guest")


# 4. Countdown Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("\n4:")
for num in countdown(5):
    print(num, end=" ")
print()


# 5. Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\n5:")
for num in fibonacci(10):
    print(num, end=" ")
print()


# 6. Infinite Even Numbers Generator
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

print("\n6:")
gen = even_numbers()
for _ in range(5):
    print(next(gen), end=" ")
print()


# 7. Generator Expression
print("\n7:")
sum_squares = sum(x**2 for x in range(1, 6))
print(sum_squares)  # 55


# 8. Chained Decorators
def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet_html():
    return "Hello"

print("\n8:")
print(greet_html())  # <b><i>Hello</i></b>
