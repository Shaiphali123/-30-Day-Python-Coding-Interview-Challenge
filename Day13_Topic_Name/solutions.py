# Day 13: Hashing Techniques - Solutions

# Problem 1: First Non-Repeating Character in a String
def first_non_repeating_char(s: str) -> str:
    from collections import Counter
    count = Counter(s)
    for ch in s:
        if count[ch] == 1:
            return ch
    return None


# Problem 2: Check if two arrays are equal or not (considering frequency)
def arrays_equal(arr1, arr2):
    from collections import Counter
    return Counter(arr1) == Counter(arr2)


# Problem 3: Find intersection of two arrays
def array_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


# Problem 4: Check if a pair with given sum exists in array
def has_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    return False


# Problem 5: Count distinct elements in every window of size k
def count_distinct_in_window(arr, k):
    from collections import defaultdict
    result = []
    freq = defaultdict(int)
    for i in range(k):
        freq[arr[i]] += 1
    result.append(len(freq))
    for i in range(k, len(arr)):
        freq[arr[i - k]] -= 1
        if freq[arr[i - k]] == 0:
            del freq[arr[i - k]]
        freq[arr[i]] += 1
        result.append(len(freq))
    return result


# Problem 6: Find subarray with given sum
def subarray_with_sum(arr, target):
    prefix_sum = 0
    seen = {}
    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum == target:
            return (0, i)
        if prefix_sum - target in seen:
            return (seen[prefix_sum - target] + 1, i)
        seen[prefix_sum] = i
    return None


# Problem 7: Find if array contains duplicate within k distance
def contains_nearby_duplicate(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False


# Problem 8: Group Anagrams together
def group_anagrams(words):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())


# Problem 9: Longest substring without repeating characters
def longest_unique_substring(s: str) -> int:
    seen = {}
    start = 0
    max_len = 0
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        max_len = max(max_len, i - start + 1)
    return max_len


# Problem 10: Count frequency of elements in array
def frequency_count(arr):
    from collections import Counter
    return dict(Counter(arr))


# Driver code for testing
if __name__ == "__main__":
    print("First Non-Repeating Char:", first_non_repeating_char("aabbcdeff"))
    print("Arrays Equal:", arrays_equal([1, 2, 3], [3, 2, 1]))
    print("Array Intersection:", array_intersection([1,2,3,4], [3,4,5]))
    print("Has Pair with Sum:", has_pair_with_sum([1,2,4,5], 6))
    print("Count Distinct in Window:", count_distinct_in_window([1,2,1,3,4,2,3], 4))
    print("Subarray with Sum:", subarray_with_sum([1,2,3,7,5], 12))
    print("Contains Nearby Duplicate:", contains_nearby_duplicate([1,2,3,1,4], 3))
    print("Group Anagrams:", group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print("Longest Unique Substring Length:", longest_unique_substring("abcabcbb"))
    print("Frequency Count:", frequency_count([1,2,2,3,3,3,4]))
