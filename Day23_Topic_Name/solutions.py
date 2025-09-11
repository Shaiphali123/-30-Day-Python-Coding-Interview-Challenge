# Day 23 - Bit Manipulation in Python (QA Focused)
# Solutions to Problem.html

# -------------------------------
# Problem 1: Odd or Even
# -------------------------------
def check_odd_even(n: int) -> str:
    return "Odd" if (n & 1) else "Even"


# -------------------------------
# Problem 2: Power of 2
# -------------------------------
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


# -------------------------------
# Problem 3: Unique Number in a List
# -------------------------------
def find_unique(nums: list[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res


# -------------------------------
# Problem 4: Swap Two Numbers
# -------------------------------
def swap_numbers(a: int, b: int) -> tuple[int, int]:
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# -------------------------------
# Test Cases
# -------------------------------
if __name__ == "__main__":
    # Problem 1
    print("Problem 1: Odd or Even")
    print(f"7 → {check_odd_even(7)}")
    print(f"10 → {check_odd_even(10)}")
    print()

    # Problem 2
    print("Problem 2: Power of 2")
    print(f"16 → {is_power_of_two(16)}")
    print(f"18 → {is_power_of_two(18)}")
    print()

    # Problem 3
    print("Problem 3: Unique Number in List")
    nums = [2, 3, 5, 3, 2]
    print(f"{nums} → {find_unique(nums)}")
    print()

    # Problem 4
    print("Problem 4: Swap Two Numbers")
    a, b = 5, 7
    print(f"Before swap: a={a}, b={b}")
    a, b = swap_numbers(a, b)
    print(f"After swap: a={a}, b={b}")
