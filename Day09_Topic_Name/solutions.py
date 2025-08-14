"""
Day 9: Math Problems Solutions
30-Day Python Coding Interview Challenge

This file contains optimized solutions to all 10 math problems
with detailed explanations, time/space complexity analysis, and test cases.
"""

import math
from typing import List


# =============================================================================
# PROBLEM 1: Optimized Prime Check
# =============================================================================

def is_prime(n: int) -> bool:
    """
    Check if a number is prime using optimized algorithm.
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    
    Args:
        n: Integer to check for primality
        
    Returns:
        bool: True if n is prime, False otherwise
    """
    # Handle edge cases
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to √n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


# Test cases for Problem 1
def test_is_prime():
    test_cases = [
        (17, True),
        (25, False), 
        (2, True),
        (1, False),
        (29, True),
        (100, False)
    ]
    
    print("Testing Prime Check:")
    for num, expected in test_cases:
        result = is_prime(num)
        status = "✅" if result == expected else "❌"
        print(f"{status} is_prime({num}) = {result} (expected: {expected})")


# =============================================================================
# PROBLEM 2: Fibonacci nth Term
# =============================================================================

def fibonacci(n: int) -> int:
    """
    Calculate nth Fibonacci number efficiently.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: nth Fibonacci number
    """
    if n <= 1:
        return n
    
    # Use two variables to track last two Fibonacci numbers
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


# Alternative: Matrix Exponentiation (O(log n))
def fibonacci_matrix(n: int) -> int:
    """
    Ultra-fast Fibonacci using matrix exponentiation.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion
    """
    if n <= 1:
        return n
    
    def matrix_multiply(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]
    
    def matrix_power(matrix, power):
        if power == 1:
            return matrix
        if power % 2 == 0:
            half = matrix_power(matrix, power // 2)
            return matrix_multiply(half, half)
        else:
            return matrix_multiply(matrix, matrix_power(matrix, power - 1))
    
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n)
    return result_matrix[0][1]


# Test cases for Problem 2
def test_fibonacci():
    test_cases = [
        (10, 55),
        (0, 0),
        (1, 1),
        (7, 13),
        (15, 610)
    ]
    
    print("\nTesting Fibonacci:")
    for n, expected in test_cases:
        result = fibonacci(n)
        status = "✅" if result == expected else "❌"
        print(f"{status} fibonacci({n}) = {result} (expected: {expected})")


# =============================================================================
# PROBLEM 3: Greatest Common Divisor
# =============================================================================

def gcd(a: int, b: int) -> int:
    """
    Find GCD using Euclidean algorithm (iterative).
    
    Time Complexity: O(log min(a, b))
    Space Complexity: O(1)
    """
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a: int, b: int) -> int:
    """
    Find GCD using Euclidean algorithm (recursive).
    
    Time Complexity: O(log min(a, b))
    Space Complexity: O(log min(a, b)) due to recursion stack
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


# Test cases for Problem 3
def test_gcd():
    test_cases = [
        (48, 18, 6),
        (17, 13, 1),
        (100, 25, 25),
        (56, 98, 14)
    ]
    
    print("\nTesting GCD:")
    for a, b, expected in test_cases:
        result = gcd(a, b)
        status = "✅" if result == expected else "❌"
        print(f"{status} gcd({a}, {b}) = {result} (expected: {expected})")


# =============================================================================
# PROBLEM 4: Trailing Zeros in Factorial
# =============================================================================

def trailing_zeros_factorial(n: int) -> int:
    """
    Count trailing zeros in n! by counting factors of 5.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Logic: Trailing zeros come from factors of 10 = 2×5.
    Since there are always more factors of 2 than 5, we count factors of 5.
    """
    count = 0
    power_of_5 = 5
    
    # Count factors of 5, 25, 125, etc.
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    
    return count


# Test cases for Problem 4
def test_trailing_zeros():
    test_cases = [
        (5, 1),    # 5! = 120
        (10, 2),   # 10! = 3628800
        (25, 6),
        (100, 24)
    ]
    
    print("\nTesting Trailing Zeros in Factorial:")
    for n, expected in test_cases:
        result = trailing_zeros_factorial(n)
        status = "✅" if result == expected else "❌"
        print(f"{status} trailing_zeros({n}!) = {result} (expected: {expected})")


# =============================================================================
# PROBLEM 5: Fast Exponentiation
# =============================================================================

def power(base: float, exp: int) -> float:
    """
    Calculate base^exp using binary exponentiation.
    
    Time Complexity: O(log exp)
    Space Complexity: O(1)
    """
    if exp == 0:
        return 1.0
    
    if exp < 0:
        return 1.0 / power(base, -exp)
    
    result = 1.0
    current_power = base
    
    while exp > 0:
        if exp % 2 == 1:
            result *= current_power
        current_power *= current_power
        exp //= 2
    
    return result


# Alternative recursive approach
def power_recursive(base: float, exp: int) -> float:
    """Recursive implementation of fast exponentiation."""
    if exp == 0:
        return 1.0
    if exp < 0:
        return 1.0 / power_recursive(base, -exp)
    
    if exp % 2 == 0:
        half = power_recursive(base, exp // 2)
        return half * half
    else:
        return base * power_recursive(base, exp - 1)


# Test cases for Problem 5
def test_power():
    test_cases = [
        (2, 10, 1024),
        (2.1, 3, 9.261),
        (2, -2, 0.25),
        (5, 0, 1),
        (3, 4, 81)
    ]
    
    print("\nTesting Fast Exponentiation:")
    for base, exp, expected in test_cases:
        result = power(base, exp)
        status = "✅" if abs(result - expected) < 1e-6 else "❌"
        print(f"{status} power({base}, {exp}) = {result:.6f} (expected: {expected})")


# =============================================================================
# PROBLEM 6: Perfect Number Check
# =============================================================================

def is_perfect_number(n: int) -> bool:
    """
    Check if number equals sum of its proper divisors.
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    
    A perfect number is a positive integer equal to the sum of its 
    proper positive divisors (divisors excluding the number itself).
    """
    if n <= 1:
        return False
    
    divisor_sum = 1  # 1 is always a proper divisor for n > 1
    
    # Find divisors up to √n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            # Add the corresponding divisor (avoid counting square root twice)
            if i != n // i:
                divisor_sum += n // i
    
    return divisor_sum == n


# Test cases for Problem 6
def test_perfect_number():
    test_cases = [
        (28, True),   # 1+2+4+7+14 = 28
        (6, True),    # 1+2+3 = 6
        (12, False),
        (1, False),
        (496, True)   # 3rd perfect number
    ]
    
    print("\nTesting Perfect Number:")
    for n, expected in test_cases:
        result = is_perfect_number(n)
        status = "✅" if result == expected else "❌"
        print(f"{status} is_perfect_number({n}) = {result} (expected: {expected})")


# =============================================================================
# PROBLEM 7: Reverse Integer
# =============================================================================

def reverse_integer(x: int) -> int:
    """
    Reverse digits of a 32-bit signed integer.
    Return 0 if reversed integer overflows.
    
    Time Complexity: O(log x)
    Space Complexity: O(1)
    """
    # 32-bit integer limits
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    while x != 0:
        digit = x % 10
        x //= 10
        
        # Check for overflow before updating result
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
            return 0
        
        result = result * 10 + digit
    
    result *= sign
    
    # Final overflow check
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result


# Test cases for Problem 7
def test_reverse_integer():
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (1534236469, 0),  # overflow case
        (0, 0)
    ]
    
    print("\nTesting Reverse Integer:")
    for x, expected in test_cases:
        result = reverse_integer(x)
        status = "✅" if result == expected else "❌"
        print(f"{status} reverse_integer({x}) = {result} (expected: {expected})")


# =============================================================================
# PROBLEM 8: Count Primes up to N (Sieve of Eratosthenes)
# =============================================================================

def count_primes(n: int) -> int:
    """
    Count prime numbers less than n using Sieve of Eratosthenes.
    
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    """
    if n < 2:
        return 0
    
    # Initialize boolean array
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples starting from i^2
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    # Count primes
    return sum(is_prime)


def get_primes_up_to_n(n: int) -> List[int]:
    """Return list of all primes less than n."""
    if n < 2:
        return []
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    return [i for i in range(2, n) if is_prime[i]]


# Test cases for Problem 8
def test_count_primes():
    test_cases = [
        (10, 4),   # [2, 3, 5, 7]
        (0, 0),
        (1, 0),
        (20, 8),   # [2, 3, 5, 7, 11, 13, 17, 19]
        (30, 10)
    ]
    
    print("\nTesting Count Primes (Sieve):")
    for n, expected in test_cases:
        result = count_primes(n)
        status = "✅" if result == expected else "❌"
        print(f"{status} count_primes({n}) = {result} (expected: {expected})")
        if n <= 30:  # Show actual primes for small inputs
            primes = get_primes_up_to_n(n)
            print(f"    Primes < {n}: {primes}")


# =============================================================================
# PROBLEM 9: LCM of Multiple Numbers
# =============================================================================

def lcm_two_numbers(a: int, b: int) -> int:
    """Calculate LCM of two numbers using GCD."""
    return abs(a * b) // gcd(a, b)


def lcm_array(numbers: List[int]) -> int:
    """
    Find LCM of multiple numbers.
    
    Time Complexity: O(n * log(max_element))
    Space Complexity: O(1)
    
    Uses the property: LCM(a,b,c) = LCM(LCM(a,b), c)
    """
    if not numbers:
        return 0
    
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm_two_numbers(result, numbers[i])
    
    return result


# Alternative implementation with overflow protection
def lcm_array_safe(numbers: List[int]) -> int:
    """LCM with better overflow protection."""
    if not numbers:
        return 0
    
    result = numbers[0]
    for i in range(1, len(numbers)):
        # Calculate as (result // gcd) * numbers[i] to avoid overflow
        g = gcd(result, numbers[i])
        result = (result // g) * numbers[i]
    
    return result


# Test cases for Problem 9
def test_lcm_array():
    test_cases = [
        ([4, 6, 8], 24),
        ([12, 18], 36),
        ([2, 3, 5], 30),
        ([1], 1),
        ([10, 15, 20], 60)
    ]
    
    print("\nTesting LCM of Array:")
    for numbers, expected in test_cases:
        result = lcm_array(numbers)
        status = "✅" if result == expected else "❌"
        print(f"{status} lcm_array({numbers}) = {result} (expected: {expected})")


# =============================================================================
# PROBLEM 10: Armstrong Numbers in Range
# =============================================================================

def is_armstrong_number(n: int) -> bool:
    """
    Check if number is an Armstrong number.
    Armstrong number: sum of digits^(number of digits) equals the number.
    """
    str_n = str(n)
    num_digits = len(str_n)
    digit_sum = sum(int(digit) ** num_digits for digit in str_n)
    return digit_sum == n


def find_armstrong_numbers_in_range(start: int, end: int) -> List[int]:
    """
    Find all Armstrong numbers in given range [start, end].
    
    Time Complexity: O((end-start) * log end)
    Space Complexity: O(result_size)
    """
    armstrong_numbers = []
    
    # Optimize by grouping numbers by digit count
    current = start
    while current <= end:
        if is_armstrong_number(current):
            armstrong_numbers.append(current)
        current += 1
    
    return armstrong_numbers


# Optimized version using digit count grouping
def find_armstrong_numbers_optimized(start: int, end: int) -> List[int]:
    """
    Optimized Armstrong number finder using pre-computed powers.
    """
    armstrong_numbers = []
    
    # Pre-compute powers for each digit count
    max_digits = len(str(end))
    powers = {}
    for digits in range(1, max_digits + 1):
        powers[digits] = [i ** digits for i in range(10)]
    
    for n in range(start, end + 1):
        str_n = str(n)
        num_digits = len(str_n)
        
        if num_digits in powers:
            digit_sum = sum(powers[num_digits][int(digit)] for digit in str_n)
            if digit_sum == n:
                armstrong_numbers.append(n)
    
    return armstrong_numbers


# Test cases for Problem 10
def test_armstrong_numbers():
    test_cases = [
        (1, 1000, [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 371, 407]),
        (100, 200, [153]),
        (1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (9474, 9475, [9474])  # 4-digit Armstrong number
    ]
    
    print("\nTesting Armstrong Numbers in Range:")
    for start, end, expected in test_cases:
        result = find_armstrong_numbers_in_range(start, end)
        status = "✅" if result == expected else "❌"
        print(f"{status} armstrong_range({start}, {end}) = {result}")
        if result != expected:
            print(f"    Expected: {expected}")


# =============================================================================
# UTILITY FUNCTIONS AND ADDITIONAL HELPERS
# =============================================================================

def is_palindrome_number(n: int) -> bool:
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]


def digit_sum(n: int) -> int:
    """Calculate sum of all digits in a number."""
    return sum(int(digit) for digit in str(abs(n)))


def count_digits(n: int) -> int:
    """Count number of digits in a number."""
    return len(str(abs(n)))


def prime_factors(n: int) -> List[int]:
    """Find all prime factors of a number."""
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


def factorial_iterative(n: int) -> int:
    """Calculate factorial iteratively."""
    if n < 0:
        return None
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def sqrt_newton(n: float, precision: float = 1e-10) -> float:
    """Calculate square root using Newton's method."""
    if n < 0:
        return None
    if n == 0:
        return 0
    
    x = n
    while True:
        root = 0.5 * (x + n / x)
        if abs(root - x) < precision:
            return root
        x = root


# =============================================================================
# COMPREHENSIVE TEST SUITE
# =============================================================================

def run_all_tests():
    """Run all test cases for math problems."""
    print("=" * 60)
    print("🧮 DAY 9: MATH PROBLEMS - COMPREHENSIVE TEST SUITE")
    print("=" * 60)
    
    test_is_prime()
    test_fibonacci()
    test_gcd()
    test_trailing_zeros()
    test_power()
    test_perfect_number()
    test_reverse_integer()
    test_count_primes()
    test_lcm_array()
    test_armstrong_numbers()
    
    print("\n" + "=" * 60)
    print("🎉 ALL TESTS COMPLETED!")
    print("=" * 60)


# =============================================================================
# PERFORMANCE BENCHMARKS
# =============================================================================

def benchmark_algorithms():
    """Benchmark different algorithm implementations."""
    import time
    
    print("\n" + "=" * 50)
    print("⚡ PERFORMANCE BENCHMARKS")
    print("=" * 50)
    
    # Fibonacci benchmarks
    print("\n📊 Fibonacci Performance (n=35):")
    
    # Iterative Fibonacci
    start = time.time()
    result1 = fibonacci(35)
    time1 = time.time() - start
    print(f"Iterative: {result1} in {time1:.6f}s")
    
    # Matrix Fibonacci
    start = time.time()
    result2 = fibonacci_matrix(35)
    time2 = time.time() - start
    print(f"Matrix:    {result2} in {time2:.6f}s")
    
    # Prime counting benchmark
    print("\n📊 Prime Counting Performance (n=100000):")
    start = time.time()
    prime_count = count_primes(100000)
    elapsed = time.time() - start
    print(f"Sieve of Eratosthenes: {prime_count} primes in {elapsed:.4f}s")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run all tests
    run_all_tests()
    
    # Run benchmarks
    benchmark_algorithms()
    
    # Additional examples and edge cases
    print("\n" + "=" * 50)
    print("🔍 ADDITIONAL EXAMPLES & EDGE CASES")
    print("=" * 50)
    
    # Edge cases demonstration
    print("\n🚨 Edge Cases:")
    print(f"is_prime(0) = {is_prime(0)}")
    print(f"is_prime(1) = {is_prime(1)}")
    print(f"fibonacci(0) = {fibonacci(0)}")
    print(f"gcd(0, 5) = {gcd(0, 5)}")
    print(f"power(0, 0) = {power(0, 0)}")
    print(f"reverse_integer(2147483647) = {reverse_integer(2147483647)}")
    
    # Mathematical properties demonstration
    print("\n📐 Mathematical Properties:")
    a, b = 12, 8
    print(f"gcd({a}, {b}) × lcm({a}, {b}) = {gcd(a, b)} × {lcm_two_numbers(a, b)} = {gcd(a, b) * lcm_two_numbers(a, b)}")
    print(f"{a} × {b} = {a * b}")
    print(f"Property verified: {gcd(a, b) * lcm_two_numbers(a, b) == a * b}")
    
    print("\n🎯 Challenge completed successfully!")
    print("Next: Practice these problems on coding platforms!")
