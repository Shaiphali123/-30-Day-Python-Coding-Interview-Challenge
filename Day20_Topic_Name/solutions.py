"""
Day 20 – Set Operations Solutions
Python solutions for interview-style problems using sets.
"""

# Problem 1: Union of Two Sets
def union_of_sets(a, b):
    """Return the union of two sets."""
    return a.union(b)


# Problem 2: Intersection of Two Sets
def intersection_of_sets(a, b):
    """Return the intersection of two sets."""
    return a.intersection(b)


# Problem 3: Subset Check
def is_subset(a, b):
    """Check if set a is a subset of set b."""
    return a.issubset(b)


# Problem 4: Symmetric Difference
def symmetric_difference(a, b):
    """Return elements in either set but not in both."""
    return a.symmetric_difference(b)


# Problem 5: Remove Duplicates from List
def remove_duplicates(lst):
    """Remove duplicates from a list using set."""
    return set(lst)


# Problem 6: Common Elements in Multiple Sets
def common_in_three_sets(a, b, c):
    """Find elements common across three sets."""
    return a.intersection(b).intersection(c)


# Problem 7: Compare Sets for Equality
def are_sets_equal(a, b):
    """Check if two sets are equal."""
    return a == b


# Problem 8: Unique Elements Count
def count_unique_elements(lst):
    """Count number of unique elements in a list."""
    return len(set(lst))


# Problem 9: Real-world – Common Skills
def common_skills(applicant1, applicant2):
    """Find common skills between two applicants."""
    return applicant1.intersection(applicant2)


# Problem 10: Real-world – Unique Visitors
def unique_visitors(visitor_ids):
    """Return set of unique visitors from a list of IDs."""
    return set(visitor_ids)


# -------------------------
# Example Test Cases
# -------------------------
if __name__ == "__main__":
    print("✅ Day 20 – Set Operations Solutions")

    # Problem 1
    print("Union:", union_of_sets({1, 2, 3}, {3, 4, 5}))

    # Problem 2
    print("Intersection:", intersection_of_sets({1, 2, 3}, {2, 3, 4}))

    # Problem 3
    print("Subset:", is_subset({1, 2}, {1, 2, 3, 4}))

    # Problem 4
    print("Symmetric Difference:", symmetric_difference({1, 2, 3}, {3, 4, 5}))

    # Problem 5
    print("Remove Duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

    # Problem 6
    print("Common in Three Sets:", common_in_three_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}))

    # Problem 7
    print("Sets Equal:", are_sets_equal({1, 2, 3}, {3, 2, 1}))

    # Problem 8
    print("Unique Count:", count_unique_elements([1, 2, 2, 3, 4, 4, 5]))

    # Problem 9
    print("Common Skills:", common_skills({"Python", "SQL", "Git"}, {"Python", "Java", "Git"}))

    # Problem 10
    print("Unique Visitors:", unique_visitors([101, 102, 101, 103, 104, 102]))
