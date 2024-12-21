def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        left_hand = merge_sort(left)
        right_hand =  merge_sort(right)
        
        return merge(left_hand,right_hand)
    
def merge(left_arr, right_arr):
    sorted_arr = []
    i = j = 0
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sorted_arr.append(left_arr[i])
            i+=1
        else:
            sorted_arr.append(right_arr[j])
            j+=1
            
#Method 0 to join list
    sorted_arr = sorted_arr + left_arr[i:]
    sorted_arr = sorted_arr + right_arr[j:]
    
#Method 1 to join list 
    # sorted_arr.extend(left_arr[i:])
    # sorted_arr.extend(right_arr[j:])

#method 2 ot join list    
    # while i < len(left_arr):
    #     sorted_arr.append(left_arr[i])
    #     i+=1
    
    # while j < len(right_arr):
    #     sorted_arr.append(right_arr[j])
    #     j+=1
        
    return sorted_arr

arr =  [32,32,543,2,42,1]
print(merge_sort(arr))