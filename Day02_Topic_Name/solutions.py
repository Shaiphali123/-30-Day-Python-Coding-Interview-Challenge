# Day 2 Solutions – Lists, Tuples, Sets & Dictionaries

# Problem 1: Reverse a List
def reverse_list(lst):
    return lst[::-1]

# Problem 2: Sum of Tuple Elements
def sum_of_tuple(tpl):
    return sum(tpl)

# Problem 3: Remove Duplicates from List
def remove_duplicates(lst):
    return list(set(lst))

# Problem 4: Frequency of Elements
def element_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Problem 5: Access Nested Dictionary
def get_nested_value(data):
    try:
        return data["student"]["marks"]["math"]
    except KeyError:
        return "Key not found"

# Problem 6: Intersection of Two Sets
def intersection_of_sets(set1, set2):
    return set1 & set2


# Testing the functions
if __name__ == "__main__":
    print("Problem 1 Output:", reverse_list([1, 2, 3, 4]))
    print("Problem 2 Output:", sum_of_tuple((1, 2, 3, 4)))
    print("Problem 3 Output:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    print("Problem 4 Output:", element_frequency(['a', 'b', 'a', 'c', 'b', 'a']))
    
    nested_data = {
        "student": {
            "name": "Alice",
            "marks": {
                "math": 95
            }
        }
    }
    print("Problem 5 Output:", get_nested_value(nested_data))
    print("Problem 6 Output:", intersection_of_sets({1, 2, 3}, {2, 3, 4}))
