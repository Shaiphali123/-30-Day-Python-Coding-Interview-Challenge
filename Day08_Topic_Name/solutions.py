"""
Day 8 — Pattern Problems — Solutions
Shaivi Connect | 30-Day Python Coding Interview Challenge
"""

# 1. Right-angled Star Triangle
def right_angled_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)


# 2. Floyd’s Triangle
def floyds_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print()


# 3. Inverted Right Triangle of Numbers
def inverted_triangle_numbers(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


# 4. Centered Pyramid of Numbers
def centered_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# 5. Diamond of Stars
def diamond_of_stars(n):
    # Upper part
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower part
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


# 6. Numeric Palindrome Pyramid
def numeric_palindrome_pyramid(n):
    for i in range(1, n + 1):
        # ascending
        for j in range(1, i + 1):
            print(j, end="")
        # descending
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()


# 7. Hollow Diamond
def hollow_diamond(n):
    # Upper
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == (2 * i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
    # Lower
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == (2 * i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()


# 8. Zig-Zag / Wave Pattern
def zig_zag_pattern(rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
                print("*", end="")
            else:
                print(" ", end="")
        print()


# 9. Pascal’s Triangle
def pascal_triangle(n):
    from math import factorial
    for i in range(n):
        print(" " * (n - i), end="")
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print()


# 10. Alternating 0s and 1s Pyramid
def alternating_binary_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print((i + j) % 2, end="")
        print()


# -------------------------
# Example Run (Uncomment to Test)
# -------------------------
if __name__ == "__main__":
    print("1. Right-angled Triangle:")
    right_angled_triangle(4)

    print("\n2. Floyd's Triangle:")
    floyds_triangle(4)

    print("\n3. Inverted Triangle Numbers:")
    inverted_triangle_numbers(4)

    print("\n4. Centered Pyramid:")
    centered_pyramid(4)

    print("\n5. Diamond of Stars:")
    diamond_of_stars(3)

    print("\n6. Numeric Palindrome Pyramid:")
    numeric_palindrome_pyramid(5)

    print("\n7. Hollow Diamond:")
    hollow_diamond(3)

    print("\n8. Zig-Zag Pattern:")
    zig_zag_pattern(3, 9)

    print("\n9. Pascal's Triangle:")
    pascal_triangle(5)

    print("\n10. Alternating Binary Pyramid:")
    alternating_binary_pyramid(5)
