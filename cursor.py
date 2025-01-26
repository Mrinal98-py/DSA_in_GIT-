def merge_sort(dict_arr):
    if len(dict_arr) <= 1:
        return dict_arr
    
    # Divide dictionary into two halves
    mid = len(dict_arr) // 2
    left = list(dict_arr.items())[:mid]
    right = list(dict_arr.items())[mid:]
    
    # Convert back to dictionaries for recursive calls
    left_dict = dict(left)
    right_dict = dict(right)
    
    # Recursively sort the two halves
    left_sorted = merge_sort(left_dict)
    right_sorted = merge_sort(right_dict)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = {}
    left_items = list(left.items())
    right_items = list(right.items())
    i = j = 0
    
    # Compare elements from both dictionaries and merge in descending order
    while i < len(left_items) and j < len(right_items):
        if left_items[i][1] >= right_items[j][1]:
            result[left_items[i][0]] = left_items[i][1]
            i += 1
        else:
            result[right_items[j][0]] = right_items[j][1]
            j += 1
    
    # Add remaining elements from left dictionary
    while i < len(left_items):
        result[left_items[i][0]] = left_items[i][1]
        i += 1
    
    # Add remaining elements from right dictionary
    while j < len(right_items):
        result[right_items[j][0]] = right_items[j][1]
        j += 1
    
    return result

# Example usage
if __name__ == "__main__":
    dict_arr = {
        'apple': 64,
        'banana': 34,
        'cherry': 25,
        'date': 12,
        'elderberry': 22,
        'fig': 11,
        'grape': 90
    }
    sorted_dict = merge_sort(dict_arr)
    print("Sorted dictionary by values:", sorted_dict)

