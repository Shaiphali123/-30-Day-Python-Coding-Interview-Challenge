"""
Day 15: Sorting & Searching - Solutions
Covers interview coding questions + QA point of view problems
Author: Shaivi Connect
"""

# -------------------------------
# Sorting Algorithms
# -------------------------------

def bubble_sort(arr):
    """Bubble Sort Algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    """Quick Sort Algorithm"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """Merge Sort Algorithm"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# -------------------------------
# Searching Algorithms
# -------------------------------

def linear_search(arr, target):
    """Linear Search"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """Binary Search (works only on sorted array)"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# -------------------------------
# QA Point of View Problems
# -------------------------------

def find_duplicate_logs(logs):
    """
    QA Scenario:
    Detect duplicate log IDs in system execution logs.
    """
    seen = set()
    duplicates = []
    for log in logs:
        if log in seen:
            duplicates.append(log)
        else:
            seen.add(log)
    return duplicates


def validate_sorted_execution_times(times):
    """
    QA Scenario:
    Check if test execution times are sorted in ascending order.
    """
    return all(times[i] <= times[i + 1] for i in range(len(times) - 1))


def search_error_in_logs(logs, keyword="ERROR"):
    """
    QA Scenario:
    Search for ERROR keyword in execution logs using linear search.
    """
    return [i for i, log in enumerate(logs) if keyword in log]


# -------------------------------
# Example Test Cases
# -------------------------------

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Quick Sort:", quick_sort(arr.copy()))
    print("Merge Sort:", merge_sort(arr.copy()))

    sorted_arr = sorted(arr)
    print("Linear Search (22):", linear_search(sorted_arr, 22))
    print("Binary Search (25):", binary_search(sorted_arr, 25))

    logs = ["PASS", "ERROR: Timeout", "PASS", "ERROR: Crash", "PASS", "ERROR: Timeout"]
    print("Duplicate Logs:", find_duplicate_logs(logs))
    print("Validate Execution Times:", validate_sorted_execution_times([1, 2, 3, 4, 5]))
    print("Search ERROR in logs:", search_error_in_logs(logs, "ERROR"))
