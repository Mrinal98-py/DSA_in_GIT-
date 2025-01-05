def search(arr,key):
    
    lower = 0
    upper = len(arr)-1
    
    while lower <= upper:
        mid = (lower + upper) // 2
        
        if arr[mid] == key:
            print("key Found",key,"index",mid + 1)
            break
        else:
            if arr[mid] < key:
                lower = mid+1
            else:
                upper = mid-1
                
arr = [0,1,2,3,4,5,6,7,8]

search(arr,4)
    