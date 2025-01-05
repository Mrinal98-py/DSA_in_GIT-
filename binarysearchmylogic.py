
def binarsearch(arr,key):
    size = len(arr)
    mid = size //2
    
    i  = 0
    if key == arr[mid]:
        
        print("found :",key)
        
    
    elif key > arr[mid]:
        arr[:] = arr[mid:]
        binarsearch(arr,key)
    
    elif key < arr[mid]:
        arr[:] = arr[:mid]
        binarsearch(arr,key)
    
    else:
        print("key is not in array")
        
        
arr = [0,12,23,34,45,56,67,78,89,90]

key = 90

binarsearch(arr,key)
            
        