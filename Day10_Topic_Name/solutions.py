"""
Complete Number Theory Interview Questions - Python Solutions
===========================================================
All solutions with optimal time and space complexity
From Basic to Expert Level (Problems 1-13 from the document)
"""

import math
from typing import List, Set
from collections import defaultdict

# =============================================================================
# BASIC LEVEL PROBLEMS (1-13)
# =============================================================================

class NumberTheorySolutions:
    
    def __init__(self):
        """Initialize the solution class"""
        pass
    
    # Problem 1: Check if Number is Prime
    def is_prime(self, n: int) -> bool:
        """
        Time: O(√n) | Space: O(1)
        Check if a number is prime by testing divisors up to √n
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        # Check for divisors from 5 to √n
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    # Problem 2: Count Primes (Sieve of Eratosthenes)
    def count_primes(self, n: int) -> int:
        """
        Time: O(n log log n) | Space: O(n)
        Count prime numbers less than n using Sieve of Eratosthenes
        """
        if n <= 2:
            return 0
        
        # Create boolean array "prime[0..n-1]" and initialize all entries as true
        prime = [True] * n
        prime[0] = prime[1] = False  # 0 and 1 are not prime
        
        p = 2
        while p * p < n:
            if prime[p]:
                # Update all multiples of p
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1
        
        # Count prime numbers
        return sum(prime)
    
    # Problem 3: Greatest Common Divisor (GCD)
    def gcd(self, a: int, b: int) -> int:
        """
        Time: O(log min(a,b)) | Space: O(1)
        Find GCD using Euclidean algorithm
        """
        while b:
            a, b = b, a % b
        return abs(a)
    
    def gcd_recursive(self, a: int, b: int) -> int:
        """Recursive version of GCD"""
        if b == 0:
            return abs(a)
        return self.gcd_recursive(b, a % b)
    
    # Problem 4: Least Common Multiple (LCM)
    def lcm(self, a: int, b: int) -> int:
        """
        Time: O(log min(a,b)) | Space: O(1)
        Find LCM using the formula: lcm(a,b) = (a * b) / gcd(a,b)
        """
        return abs(a * b) // self.gcd(a, b)
    
    # Problem 5: Power of Two
    def is_power_of_two(self, n: int) -> bool:
        """
        Time: O(1) | Space: O(1)
        Check if n is power of 2 using bit manipulation
        """
        return n > 0 and (n & (n - 1)) == 0
    
    def is_power_of_two_alternative(self, n: int) -> bool:
        """Alternative approach using logarithms"""
        if n <= 0:
            return False
        return math.log2(n).is_integer()
    
    # Problem 6: Power of Three
    def is_power_of_three(self, n: int) -> bool:
        """
        Time: O(1) | Space: O(1)
        Check if n is power of 3 using largest power of 3 in 32-bit range
        """
        # 3^19 = 1162261467 is the largest power of 3 in 32-bit range
        return n > 0 and 1162261467 % n == 0
    
    def is_power_of_three_iterative(self, n: int) -> bool:
        """Alternative iterative approach"""
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
    
    # Problem 7: Happy Number
    def is_happy(self, n: int) -> bool:
        """
        Time: O(log n) | Space: O(log n)
        Check if a number is happy using cycle detection
        """
        def get_sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_sum_of_squares(n)
        
        return n == 1
    
    def is_happy_floyd(self, n: int) -> bool:
        """Happy number using Floyd's cycle detection (constant space)"""
        def get_sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        slow = fast = n
        while True:
            slow = get_sum_of_squares(slow)
            fast = get_sum_of_squares(get_sum_of_squares(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
    
    # Problem 8: Ugly Number
    def is_ugly(self, n: int) -> bool:
        """
        Time: O(log n) | Space: O(1)
        Check if n is ugly (only has prime factors 2, 3, 5)
        """
        if n <= 0:
            return False
        
        # Remove all factors of 2, 3, and 5
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        
        return n == 1
    
    # Problem 9: Perfect Squares
    def num_squares(self, n: int) -> int:
        """
        Time: O(n√n) | Space: O(n)
        Find minimum number of perfect squares that sum to n using DP
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]
    
    def num_squares_bfs(self, n: int) -> int:
        """BFS approach for perfect squares"""
        from collections import deque
        
        if n == 0:
            return 0
        
        queue = deque([n])
        visited = {n}
        level = 0
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                
                i = 1
                while i * i <= current:
                    next_val = current - i * i
                    if next_val == 0:
                        return level
                    if next_val not in visited:
                        visited.add(next_val)
                        queue.append(next_val)
                    i += 1
        
        return level
    
    # Problem 10: Factorial Trailing Zeroes
    def trailing_zeroes(self, n: int) -> int:
        """
        Time: O(log n) | Space: O(1)
        Count trailing zeroes in n! by counting factors of 5
        """
        count = 0
        i = 5
        while i <= n:
            count += n // i
            i *= 5
        return count
    
    # Problem 11: Integer to Roman
    def int_to_roman(self, num: int) -> str:
        """
        Time: O(1) | Space: O(1)
        Convert integer to roman numeral using greedy approach
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = ""
        for i in range(len(values)):
            count = num // values[i]
            if count:
                result += symbols[i] * count
                num -= values[i] * count
        
        return result
    
    # Problem 12: Roman to Integer
    def roman_to_int(self, s: str) -> int:
        """
        Time: O(n) | Space: O(1)
        Convert roman numeral to integer
        """
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        for char in reversed(s):
            value = roman_values[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        
        return result
    
    def roman_to_int_forward(self, s: str) -> int:
        """Alternative forward pass approach"""
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        for i in range(len(s)):
            current_value = roman_values[s[i]]
            if i + 1 < len(s) and current_value < roman_values[s[i + 1]]:
                result -= current_value
            else:
                result += current_value
        
        return result
    
    # Problem 13: Excel Sheet Column Number
    def title_to_number(self, column_title: str) -> int:
        """
        Time: O(n) | Space: O(1)
        Convert Excel column title to number (base-26 conversion)
        """
        result = 0
        for char in column_title:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result


# =============================================================================
# UTILITY FUNCTIONS AND ADDITIONAL HELPERS
# =============================================================================

class NumberTheoryUtils:
    """Additional utility functions for number theory problems"""
    
    @staticmethod
    def prime_factorization(n: int) -> List[int]:
        """
        Get prime factorization of a number
        Time: O(√n) | Space: O(log n)
        """
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
    
    @staticmethod
    def sieve_of_eratosthenes(n: int) -> List[bool]:
        """
        Generate prime sieve up to n
        Time: O(n log log n) | Space: O(n)
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False
        
        return is_prime
    
    @staticmethod
    def extended_gcd(a: int, b: int) -> tuple:
        """
        Extended Euclidean Algorithm
        Returns (gcd, x, y) such that a*x + b*y = gcd(a,b)
        """
        if b == 0:
            return a, 1, 0
        else:
            gcd, x1, y1 = NumberTheoryUtils.extended_gcd(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return gcd, x, y
    
    @staticmethod
    def mod_inverse(a: int, m: int) -> int:
        """
        Find modular multiplicative inverse of a modulo m
        """
        gcd, x, y = NumberTheoryUtils.extended_gcd(a, m)
        if gcd != 1:
            raise ValueError("Modular inverse does not exist")
        return (x % m + m) % m
    
    @staticmethod
    def fast_power(base: int, exp: int, mod: int = None) -> int:
        """
        Fast exponentiation using binary exponentiation
        Time: O(log exp)
        """
        if mod is None:
            result = 1
            while exp > 0:
                if exp & 1:
                    result *= base
                base *= base
                exp >>= 1
            return result
        else:
            result = 1
            base %= mod
            while exp > 0:
                if exp & 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp >>= 1
            return result


# =============================================================================
# TESTING AND DEMONSTRATION
# =============================================================================

def test_solutions():
    """Test all the implemented solutions"""
    sol = NumberTheorySolutions()
    utils = NumberTheoryUtils()
    
    print("🧮 Testing Number Theory Solutions")
    print("=" * 50)
    
    # Test Prime Check
    print("1. Prime Check:")
    test_cases = [17, 4, 2, 1, 97]
    for n in test_cases:
        print(f"   is_prime({n}) = {sol.is_prime(n)}")
    
    # Test Count Primes
    print("\n2. Count Primes:")
    for n in [10, 0, 2]:
        print(f"   count_primes({n}) = {sol.count_primes(n)}")
    
    # Test GCD
    print("\n3. GCD:")
    test_pairs = [(48, 18), (17, 13), (100, 25)]
    for a, b in test_pairs:
        print(f"   gcd({a}, {b}) = {sol.gcd(a, b)}")
    
    # Test LCM
    print("\n4. LCM:")
    for a, b in test_pairs:
        print(f"   lcm({a}, {b}) = {sol.lcm(a, b)}")
    
    # Test Power of Two
    print("\n5. Power of Two:")
    for n in [16, 3, 8, 6]:
        print(f"   is_power_of_two({n}) = {sol.is_power_of_two(n)}")
    
    # Test Power of Three
    print("\n6. Power of Three:")
    for n in [27, 0, 9, 1]:
        print(f"   is_power_of_three({n}) = {sol.is_power_of_three(n)}")
    
    # Test Happy Number
    print("\n7. Happy Number:")
    for n in [19, 2, 7]:
        print(f"   is_happy({n}) = {sol.is_happy(n)}")
    
    # Test Ugly Number
    print("\n8. Ugly Number:")
    for n in [6, 14, 8, 1]:
        print(f"   is_ugly({n}) = {sol.is_ugly(n)}")
    
    # Test Perfect Squares
    print("\n9. Perfect Squares:")
    for n in [12, 13, 1]:
        print(f"   num_squares({n}) = {sol.num_squares(n)}")
    
    # Test Trailing Zeroes
    print("\n10. Trailing Zeroes:")
    for n in [5, 10, 25]:
        print(f"   trailing_zeroes({n}) = {sol.trailing_zeroes(n)}")
    
    # Test Roman Conversions
    print("\n11-12. Roman Conversions:")
    test_nums = [3749, 58, 1994]
    for num in test_nums:
        roman = sol.int_to_roman(num)
        back_to_int = sol.roman_to_int(roman)
        print(f"   {num} → {roman} → {back_to_int}")
    
    # Test Excel Column
    print("\n13. Excel Column:")
    test_cols = ["A", "AB", "ZY"]
    for col in test_cols:
        print(f"   title_to_number('{col}') = {sol.title_to_number(col)}")


if __name__ == "__main__":
    test_solutions()
