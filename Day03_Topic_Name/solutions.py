# ✅ Solution 1: Odd or Even
def odd_even(n):
    return "Even" if n % 2 == 0 else "Odd"

# ✅ Solution 2: Largest of 3
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# ✅ Solution 3: Print Prime Numbers
def print_primes_upto_100():
    for num in range(2, 101):
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

# ✅ Solution 4: Sum of Digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# ✅ Solution 5: FizzBuzz
def fizz_buzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example Usage
if __name__ == "__main__":
    print("Odd or Even:", odd_even(7))
    print("Largest:", largest_of_three(10, 25, 5))
    print("Prime numbers from 1 to 100:")
    print_primes_upto_100()
    print("\nSum of digits:", sum_of_digits(1234))
    print("FizzBuzz from 1 to 50:")
    fizz_buzz()
