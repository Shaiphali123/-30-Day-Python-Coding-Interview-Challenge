# Day 4 – String Manipulation Solutions

# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Check palindrome
def is_palindrome(s):
    return s == s[::-1]

# 3. Count vowels and consonants
def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    v = sum(1 for char in s if char in vowels)
    c = sum(1 for char in s if char.isalpha() and char not in vowels)
    return v, c

# 4. Most frequent character
from collections import Counter
def most_frequent_char(s):
    count = Counter(s)
    return count.most_common(1)[0][0]

# 5. Remove duplicates
def remove_duplicates(s):
    seen = set()
    result = ''
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

# 6. Capitalize first letter of every word
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

# 7. Check anagrams
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# 8. Compress a string
def compress_string(s):
    if not s:
        return ""
    result = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result

# 9. Remove all whitespaces
def remove_spaces(s):
    return s.replace(" ", "")

# 10. Count words in a sentence
def word_count(s):
    return len(s.split())

# Test outputs
if __name__ == "__main__":
    print(reverse_string("Shaivi"))
    print(is_palindrome("madam"))
    print(count_vowels_consonants("Interview"))
    print(most_frequent_char("programming"))
    print(remove_duplicates("Shaiphali"))
    print(capitalize_words("hello world"))
    print(is_anagram("listen", "silent"))
    print(compress_string("aaabbc"))
    print(remove_spaces("a b c d"))
    print(word_count("Python is awesome"))
