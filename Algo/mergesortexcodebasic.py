def merge_sorted(elements, key):
    if len(elements) <= 1:
        return elements
    
    mid = len(elements) // 2
    left = merge_sorted(elements[:mid], key)
    right = merge_sorted(elements[mid:], key)
    
    return merge_two_sorted_array(left, right, key)

def merge_two_sorted_array(left, right, key):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    
    return sorted_list

elements = [
    { 'name': 'vedanth', 'age': 17, 'time_hours': 1},
    { 'name': 'rajab', 'age': 12, 'time_hours': 3},
    { 'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
    { 'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
]

sorted_elements = merge_sorted(elements, 'time_hours')

for element in sorted_elements:
    print(element)

# Output:
# {'name': 'vedanth', 'age': 17, 'time_hours': 1}
# {'name': 'chinmay', 'age': 24, 'time_hours': 1.5}
# {'name': 'vignesh', 'age': 21, 'time_hours': 2.5}
# {'name': 'rajab', 'age': 12, 'time_hours': 3}
