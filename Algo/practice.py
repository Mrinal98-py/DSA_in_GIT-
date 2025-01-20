def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        left_arr = merge_sort(left)
        right_arr = merge_sort(right)
        
        return merge(left_arr,right_arr)
        
def merge(left_arr,right_arr):
    sorted_arr = []
    i=j=0
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sorted_arr.append(left_arr[i])
            i+=1
        else:
            sorted_arr.append(right_arr[j])
            j+=1
            
    sorted_arr = sorted_arr + left_arr[i:]
    sorted_arr = sorted_arr + right_arr[j:]
    
    return sorted_arr

arr = [54,34,23,234,335,462,12,3]

print(merge_sort(arr))

