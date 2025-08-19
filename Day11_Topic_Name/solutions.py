"""
Day 11 - Two Pointer Approach
30-Day Python Coding Interview Challenge
Author: Shaiphali Bhadani (Shaivi Connect)
"""

# 1. Pair with Target Sum
def two_sum(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

# 2. Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    if not nums:
        return 0
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
    return left + 1

# 3. Squares of a Sorted Array
def make_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n-1
    highest = n-1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[highest] = nums[left] ** 2
            left += 1
        else:
            result[highest] = nums[right] ** 2
            right -= 1
        highest -= 1
    return result

# 4. Triplet Sum to Zero (3-Sum)
def three_sum(nums):
    nums.sort()
    triplets = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return triplets

# 5. Dutch National Flag Problem (Sort Colors)
def sort_colors(nums):
    low, high = 0, len(nums)-1
    i = 0
    while i <= high:
        if nums[i] == 0:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
            i += 1
        elif nums[i] == 2:
            nums[high], nums[i] = nums[i], nums[high]
            high -= 1
        else:
            i += 1
    return nums

# 6. Check Palindrome
def is_palindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# 7. Container With Most Water
def max_area(height):
    left, right = 0, len(height)-1
    max_water = 0
    while left < right:
        max_water = max(max_water, min(height[left], height[right]) * (right-left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

# 8. Merge Two Sorted Arrays
def merge_sorted_arrays(nums1, nums2):
    i, j = 0, 0
    merged = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    return merged

# 9. Intersection of Two Sorted Arrays
def intersect_sorted(nums1, nums2):
    i, j = 0, 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result

# 10. Pair Sum in Rotated Sorted Array
def pair_in_rotated_array(arr, target):
    n = len(arr)
    # find pivot (smallest element index)
    pivot = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            pivot = i+1
            break
    left = pivot
    right = (pivot-1+n) % n
    while left != right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        if s < target:
            left = (left+1) % n
        else:
            right = (right-1+n) % n
    return False


# ------------------ Testing ------------------
if __name__ == "__main__":
    print("1. Two Sum ->", two_sum([1,2,3,4,6], 6))
    print("2. Remove Duplicates ->", remove_duplicates([2,3,3,3,6,9,9]))
    print("3. Squares ->", make_squares([-2,-1,0,2,3]))
    print("4. Three Sum ->", three_sum([-3,0,1,2,-1,1,-2]))
    print("5. Sort Colors ->", sort_colors([2,0,2,1,1,0]))
    print("6. Palindrome ->", is_palindrome("racecar"))
    print("7. Max Water ->", max_area([1,8,6,2,5,4,8,3,7]))
    print("8. Merge Arrays ->", merge_sorted_arrays([1,3,5],[2,4,6]))
    print("9. Intersection ->", intersect_sorted([1,2,4,5,6],[2,4,6,8]))
    print("10. Pair in Rotated Array ->", pair_in_rotated_array([11,15,6,8,9,10], 16))
