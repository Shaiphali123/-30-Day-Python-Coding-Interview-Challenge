# Day 16: Python Interview Series
# Topic: Recursion & Backtracking Solutions

# -----------------------------------------------------------------------------
# 1. Factorial of a Number (Recursion)
# -----------------------------------------------------------------------------
def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.
    n! = n * (n-1) * (n-2) * ... * 1
    """
    # Base Case: Factorial of 0 or 1 is 1. This stops the recursion.
    if n == 0 or n == 1:
        return 1
    # Recursive Case: n multiplied by the factorial of (n-1).
    else:
        return n * factorial(n - 1)

# -----------------------------------------------------------------------------
# 2. Fibonacci Sequence (Recursion)
# -----------------------------------------------------------------------------
def fibonacci(n):
    """
    Calculates the nth term of the Fibonacci sequence using recursion.
    The sequence starts 0, 1, 1, 2, 3, 5, 8, ...
    Note: This implementation is simple but highly inefficient due to
    recalculating the same values multiple times.
    """
    # Base Case 1: The 0th term is 0.
    if n <= 0:
        print("Input should be a positive integer")
        return None
    elif n == 1:
        return 0
    # Base Case 2: The 1st and 2nd terms are 1 (adjusting for 0-based vs 1-based).
    # Let's consider fib(1)=0, fib(2)=1, etc.
    elif n == 2:
        return 1
    # Recursive Case: The sum of the two preceding numbers.
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# -----------------------------------------------------------------------------
# 3. Tower of Hanoi
# -----------------------------------------------------------------------------
def tower_of_hanoi(n, source_rod, destination_rod, auxiliary_rod):
    """
    Solves the Tower of Hanoi puzzle for n disks.
    The objective is to move the entire stack to another rod, obeying the rules:
    1. Only one disk can be moved at a time.
    2. A larger disk cannot be placed on top of a smaller disk.
    """
    # Base Case: If there is only one disk, move it directly.
    if n == 1:
        print(f"Move disk 1 from {source_rod} to {destination_rod}")
        return
    # Recursive Step 1: Move n-1 disks from source to auxiliary rod.
    tower_of_hanoi(n - 1, source_rod, auxiliary_rod, destination_rod)
    # Step 2: Move the nth (largest) disk from source to destination rod.
    print(f"Move disk {n} from {source_rod} to {destination_rod}")
    # Recursive Step 3: Move the n-1 disks from auxiliary to destination rod.
    tower_of_hanoi(n - 1, auxiliary_rod, destination_rod, source_rod)

# -----------------------------------------------------------------------------
# 4. Print all permutations of a string (Backtracking)
# -----------------------------------------------------------------------------
def string_permutations(s):
    """
    Generates all permutations of a given string using backtracking.
    """
    # Convert string to list of characters to allow swapping
    chars = list(s)
    result = []
    
    def backtrack(start_index):
        # Base Case: If we've reached the end of the string, we have a full permutation.
        if start_index == len(chars) - 1:
            result.append("".join(chars))
            return

        # Recursive Case: Iterate through the rest of the string
        for i in range(start_index, len(chars)):
            # Choose: Swap the current character with the start_index character
            chars[start_index], chars[i] = chars[i], chars[start_index]
            
            # Explore: Recurse on the rest of the string
            backtrack(start_index + 1)
            
            # Unchoose (Backtrack): Swap them back to restore the original state for other branches
            chars[start_index], chars[i] = chars[i], chars[start_index]

    backtrack(0)
    return result

# -----------------------------------------------------------------------------
# 5. N-Queens Problem
# -----------------------------------------------------------------------------
def solve_n_queens(n):
    """
    Solves the N-Queens problem using backtracking.
    Places N queens on an N×N chessboard so that no two queens attack each other.
    """
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check column upwards
        for i in range(row):
            if board[i][col] == "Q":
                return False
        # Check upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False
        # Check upper-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == "Q":
                return False
        return True

    def backtrack(row):
        # Base Case: If all queens are placed (i.e., we've reached the last row)
        if row == n:
            solutions.append(["".join(r) for r in board])
            return

        # Recursive Case: Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"  # Choose
                backtrack(row + 1)     # Explore
                board[row][col] = "."  # Backtrack (un-choose)
    
    backtrack(0)
    return solutions

# -----------------------------------------------------------------------------
# 6. Rat in a Maze Problem
# -----------------------------------------------------------------------------
def solve_rat_in_maze(maze):
    """
    Finds a path for a rat to go from the source (0,0) to the destination (N-1, N-1)
    in a maze. The rat can only move down or right. 1s are open paths, 0s are walls.
    """
    n = len(maze)
    # Create a solution matrix of the same size, initialized to 0s
    solution = [[0 for _ in range(n)] for _ in range(n)]

    def is_safe(row, col):
        # Check if the cell is within the board and is not a wall (maze[row][col] == 1)
        return 0 <= row < n and 0 <= col < n and maze[row][col] == 1

    def backtrack(row, col):
        # Base Case: If we have reached the destination
        if row == n - 1 and col == n - 1 and maze[row][col] == 1:
            solution[row][col] = 1
            return True

        # Recursive Case: Check if the current position is a valid move
        if is_safe(row, col):
            # Mark this cell as part of the solution path
            solution[row][col] = 1
            
            # Explore: Move Right
            if backtrack(row, col + 1):
                return True
            
            # Explore: Move Down
            if backtrack(row + 1, col):
                return True
            
            # Backtrack: If neither move works, unmark this cell and return False
            solution[row][col] = 0
            return False
            
        return False

    if backtrack(0, 0):
        return solution
    else:
        return "No solution found"


# -----------------------------------------------------------------------------
# Main execution block to demonstrate the functions
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- 1. Factorial ---")
    num_fact = 5
    print(f"Factorial of {num_fact} is: {factorial(num_fact)}\n")

    print("--- 2. Fibonacci Sequence ---")
    num_fib = 8
    print(f"The {num_fib}th term of Fibonacci is: {fibonacci(num_fib)}\n")

    print("--- 3. Tower of Hanoi ---")
    num_disks = 3
    print(f"Solving Tower of Hanoi for {num_disks} disks:")
    tower_of_hanoi(num_disks, 'A', 'C', 'B') # A=Source, C=Destination, B=Auxiliary
    print("")

    print("--- 4. String Permutations ---")
    my_string = "ABC"
    permutations = string_permutations(my_string)
    print(f"Permutations of '{my_string}': {permutations}\n")

    print("--- 5. N-Queens Problem ---")
    n_queens = 4
    queen_solutions = solve_n_queens(n_queens)
    print(f"Found {len(queen_solutions)} solutions for a {n_queens}x{n_queens} board:")
    for i, sol in enumerate(queen_solutions):
        print(f"Solution {i+1}:")
        for row in sol:
            print(row)
        print()

    print("--- 6. Rat in a Maze ---")
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    maze_solution = solve_rat_in_maze(maze)
    print("Maze problem:")
    if isinstance(maze_solution, list):
        for row in maze_solution:
            print(" ".join(map(str, row)))
    else:
        print(maze_solution)

