def bubble(arr):
    if len(arr) <= 1:
        return arr
    else:

        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j] ,arr[j+1] = arr[j+1], arr[j]
                # if arr[j] > arr[j+1]:
                #     arr[j], arr[j+1] = arr[j+1], arr[j]
        # return bubble(arr)
        return arr

arr = [223,43,43,46,5,34,34,4]
print(bubble(arr))            
    