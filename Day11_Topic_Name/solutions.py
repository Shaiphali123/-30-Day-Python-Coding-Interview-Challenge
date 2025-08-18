"""
Day 11: Two Pointer Approach - Find Pair with Target Sum
30-Day Python Coding Interview Challenge

Problem: Given a sorted array and target sum, find if a pair exists that sums to target.
Approach: Use two pointers (left and right) to efficiently find the pair in O(n) time.
"""

def has_pair_with_sum(arr, target):
    """
    Find if there exists a pair in sorted array that sums to target.
    
    Args:
        arr (List[int]): Sorted array of integers
        target (int): Target sum to find
    
    Returns:
        bool: True if pair exists, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Handle edge cases
    if len(arr) < 2:
        return False
    
    # Initialize two pointers
    left = 0
    right = len(arr) - 1
    
    # Move pointers toward each other
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return True  # Found the pair!
        elif current_sum < target:
            # Need larger sum, move left pointer right
            left += 1
        else:
            # Need smaller sum, move right pointer left
            right -= 1
    
    return False  # No pair found


def has_pair_with_sum_indices(arr, target):
    """
    Find indices of pair that sums to target (bonus version).
    
    Returns:
        tuple: (left_index, right_index) if pair exists, None otherwise
    """
    if len(arr) < 2:
        return None
    
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (left, right)  # Return indices of the pair
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None  # No pair found


def has_pair_with_sum_brute_force(arr, target):
    """
    Brute force solution for comparison - O(n²) time complexity.
    
    Args:
        arr (List[int]): Array of integers (doesn't need to be sorted)
        target (int): Target sum to find
    
    Returns:
        bool: True if pair exists, False otherwise
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)
    
    # Check every possible pair
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
    
    return False


def find_all_pairs_with_sum(arr, target):
    """
    Advanced version: Find ALL pairs that sum to target.
    
    Returns:
        List[tuple]: List of all pairs (as tuples) that sum to target
    """
    if len(arr) < 2:
        return []
    
    pairs = []
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            
            # Handle duplicates - move both pointers
            left += 1
            right -= 1
            
            # Skip duplicate values from left
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            
            # Skip duplicate values from right
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
                
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs


# Test function to demonstrate the solutions
def test_solutions():
    """Test all implemented solutions with various test cases."""
    
    test_cases = [
        ([1, 2, 4, 7, 11, 15], 15, True),   # Basic case
        ([1, 2, 3, 4, 5], 10, False),       # No pair exists
        ([-1, 0, 1, 2, 3], 2, True),        # Negative numbers
        ([1], 1, False),                     # Single element
        ([], 5, False),                      # Empty array
        ([2, 2, 2, 2], 4, True),            # Duplicates
        ([1, 2, 3, 4, 5, 6], 11, True),     # Multiple valid pairs
    ]
    
    print("=" * 60)
    print("TESTING TWO POINTER vs BRUTE FORCE SOLUTIONS")
    print("=" * 60)
    
    for i, (arr, target, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Expected: {expected}")
        
        # Test two pointer approach
        result_two_pointer = has_pair_with_sum(arr, target)
        print(f"Two Pointer Result: {result_two_pointer}")
        
        # Test brute force approach
        result_brute_force = has_pair_with_sum_brute_force(arr, target)
        print(f"Brute Force Result: {result_brute_force}")
        
        # Test indices version
        indices = has_pair_with_sum_indices(arr, target)
        if indices:
            print(f"Pair indices: {indices} -> values: ({arr[indices[0]]}, {arr[indices[1]]})")
        
        # Verify results match
        if result_two_pointer == result_brute_force == expected:
            print("✅ PASS - All methods agree and match expected result")
        else:
            print("❌ FAIL - Results don't match!")
        
        print("-" * 40)


def complexity_demo():
    """Demonstrate the time complexity difference between approaches."""
    import time
    
    print("\n" + "=" * 60)
    print("COMPLEXITY DEMONSTRATION")
    print("=" * 60)
    
    # Create larger test array
    large_arr = list(range(1, 10001))  # [1, 2, 3, ..., 10000]
    target = 19999  # Sum of last two elements
    
    print(f"Testing with array size: {len(large_arr)}")
    print(f"Target sum: {target}")
    
    # Time two pointer approach
    start_time = time.time()
    result_two_pointer = has_pair_with_sum(large_arr, target)
    two_pointer_time = time.time() - start_time
    
    print(f"\nTwo Pointer Approach:")
    print(f"Result: {result_two_pointer}")
    print(f"Time taken: {two_pointer_time:.6f} seconds")
    
    # Time brute force approach (with smaller array to avoid long wait)
    smaller_arr = list(range(1, 1001))  # [1, 2, 3, ..., 1000]
    smaller_target = 1999
    
    start_time = time.time()
    result_brute_force = has_pair_with_sum_brute_force(smaller_arr, smaller_target)
    brute_force_time = time.time() - start_time
    
    print(f"\nBrute Force Approach (smaller array - 1000 elements):")
    print(f"Result: {result_brute_force
