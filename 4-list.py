#lists

# Merge two lists and remove duplicates

def merge_list_remove_duplicates(list1: list, list2: list) -> list:
    return list(set(list1 + list2))

def merge_list_remove_duplicates_v2(list1: list, list2: list) -> list:
    merged = []
    for item in list1 + list2:
        if item not in merged:
            merged.append(item)
    return merged

# Find the second largest number in a list
def second_large_number(list1: list) -> int:
    list1.sort()
    length = len(list1)-1
    return list1[length-2]

def second_large_number_without_sort(list1: list) -> int:
    new_list = list1.copy()
    index = new_list.index(max(new_list))
    new_list.pop(index)
    return max(new_list)

"""""
Given a list of integers, rearrange it so that all positive numbers come before negative 
numbers, keeping relative order.
 Example: [3, -2, 5, -1, 0]  [3, 5, 0, -2, -1]
"""
def reorder_positives_negatives(list1: list):
    list_max = []
    for i in list1:
        if i >= 0:
            list_max.append(i)

    list_min = []
    for i in list1:
        if i < 0 :
            list_min.append(i)    
    return list_max + list_min







    