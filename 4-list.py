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


print(merge_list_remove_duplicates_v2([1,2,3,4,5],[2,3,4,5,6]))
