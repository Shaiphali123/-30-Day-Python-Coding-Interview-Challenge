from collections import deque, defaultdict
from typing import List, Tuple

"""
Day 12 – Sliding Window: Solutions (Python)
Author: Shaivi Connect

All functions below are O(n) using sliding-window/two-pointer patterns, unless noted.
Each function includes a short docstring with assumptions and edge cases.
"""

# 1) Max Sum Subarray of Size K (fixed window)
def max_sum_subarray_of_size_k(nums: List[int], k: int) -> int:
    """Return the maximum sum of any contiguous subarray of size k.
    Assumes 1 <= k <= len(nums). Works with negatives.
    """
    window_sum = sum(nums[:k])
    best = window_sum
    for r in range(k, len(nums)):
        window_sum += nums[r] - nums[r - k]
        if window_sum > best:
            best = window_sum
    return best

# 2) First Negative Number in Every Window of Size K (fixed window with deque)
def first_negative_in_every_window(nums: List[int], k: int) -> List[int]:
    """For each window of size k, output the first negative number, or 0 if none.
    Uses a deque of indices of negative numbers within the current window.
    """
    q: deque[int] = deque()
    res: List[int] = []

    # Initialize first window
    for i in range(min(k, len(nums))):
        if nums[i] < 0:
            q.append(i)

    if len(nums) >= k:
        res.append(nums[q[0]] if q else 0)

    # Slide
    for r in range(k, len(nums)):
        # remove out-of-window indices
        while q and q[0] <= r - k:
            q.popleft()
        if nums[r] < 0:
            q.append(r)
        res.append(nums[q[0]] if q else 0)

    return res

# 3) Longest Substring Without Repeating Characters (variable)
def length_of_longest_substring_no_repeat(s: str) -> int:
    """Return the length of the longest substring without repeating characters.
    Uses last-seen index map to jump left when a duplicate appears.
    """
    last = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best

# 4) Minimum Window Substring (variable with frequency map)
def min_window_substring(s: str, t: str) -> str:
    """Return the minimum window in s that contains all characters of t (with multiplicity),
    or "" if not found. ASCII-safe; for Unicode, collections.Counter still works.
    """
    if not t or not s:
        return ""

    need = defaultdict(int)
    for ch in t:
        need[ch] += 1
    required = len(need)

    have = 0
    window = defaultdict(int)
    best_len = float('inf')
    best = (0, 0)

    left = 0
    for right, ch in enumerate(s):
        window[ch] += 1
        if ch in need and window[ch] == need[ch]:
            have += 1
        while have == required:
            # update best
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best = (left, right)
            # shrink
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                have -= 1
            left += 1

    if best_len == float('inf'):
        return ""
    l, r = best
    return s[l:r+1]

# 5) Fruit Into Baskets (Longest Subarray with <=2 distinct)
def total_fruit(nums: List[int]) -> int:
    """Return length of the longest subarray containing at most 2 distinct values.
    """
    count = defaultdict(int)
    left = 0
    best = 0
    for right, x in enumerate(nums):
        count[x] += 1
        while len(count) > 2:
            y = nums[left]
            count[y] -= 1
            if count[y] == 0:
                del count[y]
            left += 1
        best = max(best, right - left + 1)
    return best

# 6) Longest Ones After K Flips (binary array, budget on zeros)
def longest_ones_after_k_flips(nums: List[int], k: int) -> int:
    """Given a binary array nums and k, return the length of the longest subarray
    with at most k zeros (we can flip zeros to ones).
    """
    left = 0
    zero_count = 0
    best = 0
    for right, x in enumerate(nums):
        if x == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

# 7) Subarray Product Less Than K (positives)
def num_subarray_product_less_than_k(nums: List[int], k: int) -> int:
    """Return the count of contiguous subarrays with product < k.
    Requires all nums > 0. If k <= 1, result is 0.
    """
    if k <= 1:
        return 0
    prod = 1
    left = 0
    ans = 0
    for right, x in enumerate(nums):
        prod *= x
        while prod >= k:
            prod //= nums[left]
            # Use float division if non-int inputs; here ints -> integer division is safe
            # but to ensure correctness for any ints, use normal division then cast.
            # We'll use exact division since nums[left] > 0 and prod is product of ints.
            left += 1
        ans += right - left + 1
    return ans

# 8) Smallest Subarray With Sum >= S (positives)
def min_subarray_len_with_sum_at_least_s(nums: List[int], S: int) -> int:
    """Return minimal length of a contiguous subarray with sum >= S (positives), or 0 if none.
    """
    left = 0
    cur_sum = 0
    best = float('inf')
    for right, x in enumerate(nums):
        cur_sum += x
        while cur_sum >= S:
            best = min(best, right - left + 1)
            cur_sum -= nums[left]
            left += 1
    return 0 if best == float('inf') else best

# 9) Longest Subarray With Sum = Target (positives only)
def longest_subarray_sum_equals_target(nums: List[int], target: int) -> int:
    """Return length of the longest subarray with sum exactly target.
    Assumes all nums are non-negative (typical sliding-window precondition).
    If negatives exist, use prefix-sum hashmap instead (not implemented here).
    """
    left = 0
    cur_sum = 0
    best = 0
    for right, x in enumerate(nums):
        cur_sum += x
        while cur_sum > target and left <= right:
            cur_sum -= nums[left]
            left += 1
        if cur_sum == target:
            best = max(best, right - left + 1)
    return best

# 10) Count Substrings With At Most K Distinct Characters
def count_substrings_at_most_k_distinct(s: str, k: int) -> int:
    """Return the number of substrings with at most k distinct characters.
    Uses standard counting technique: at each right, add (right-left+1).
    """
    if k < 0:
        return 0
    count = defaultdict(int)
    left = 0
    total = 0
    distinct = 0
    for right, ch in enumerate(s):
        if count[ch] == 0:
            distinct += 1
        count[ch] += 1
        while distinct > k:
            left_ch = s[left]
            count[left_ch] -= 1
            if count[left_ch] == 0:
                distinct -= 1
            left += 1
        total += right - left + 1
    return total

# 11) Number of Nice Subarrays (Exactly K Odds)
def number_of_nice_subarrays(nums: List[int], k: int) -> int:
    """Return the count of subarrays with exactly k odd numbers.
    Uses atMost(K) - atMost(K-1) trick.
    """
    def at_most(K: int) -> int:
        left = 0
        odds = 0
        total = 0
        for right, x in enumerate(nums):
            if x % 2 == 1:
                odds += 1
            while odds > K:
                if nums[left] % 2 == 1:
                    odds -= 1
                left += 1
            total += right - left + 1
        return total
    return at_most(k) - at_most(k - 1)


# Optional: simple self-checks (can be extended)
if __name__ == "__main__":
    # 1
    assert max_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9
    # 2
    assert first_negative_in_every_window([12, -1, -7, 8, -15, 30, 16, 28], 3) == [-1, -1, -7, -15, -15, 0]
    # 3
    assert length_of_longest_substring_no_repeat("abcabcbb") == 3
    # 4
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    # 5
    assert total_fruit([1,2,1]) == 3
    # 6
    assert longest_ones_after_k_flips([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    # 7
    assert num_subarray_product_less_than_k([10,5,2,6], 100) == 8
    # 8
    assert min_subarray_len_with_sum_at_least_s([2,3,1,2,4,3], 7) == 2
    # 9
    assert longest_subarray_sum_equals_target([1,2,3,2,5], 5) == 2  # [2,3] or [5]
    # 10
    assert count_substrings_at_most_k_distinct("eceba", 2) == 9
    # 11
    assert number_of_nice_subarrays([1,1,2,1,1], 3) == 2
    print("All sample checks passed.")
