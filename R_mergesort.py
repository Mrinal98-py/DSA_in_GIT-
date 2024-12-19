def merge_two_sort(a,b):

    s_arr = []
    i=j=0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            s_arr.append(a[i])
            i+=1
        else:
            s_arr.append(b[j])
            j+=1
    
    while i < len(a):
        s_arr.append(a[i])
        i+=1

    while j < len(b):
        s_arr.append(b[j])
        j+=1

    return s_arr

def merge_sort(arr):

    if len(arr) <=1:
        # print(arr)
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    l = merge_sort(left)
    r =merge_sort(right)

    return merge_two_sort(l,r)



if __name__ == '__main__':
#     a = [1,5,8,12,56,89,100]
#     b =[7,9,45,51]

    arr = [32,433,2,2,-3,212,32]
# print(merge_two_sort(a,b))
print(merge_sort(arr))
    
    while i < len(a):
        s_arr.append(a[i])
        i+=1