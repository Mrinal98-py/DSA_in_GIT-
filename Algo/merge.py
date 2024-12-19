
def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    else:

        min = len(arr)//2
        left = arr[:min]
        right = arr[min:]

        l = merge_sort(left)
        r = merge_sort(right)

        return merge_two_sorted_lsit(l,r)


def merge_two_sorted_lsit(a,b):

    sorted_list =[]

    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i < len_a:
        sorted_list.append(a[i])
        i+=1
    
    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list        


if __name__ == '__main__':
    a = [1,5,8,12,56,89,100]
    b =[7,9,45,51]

print(merge_two_sorted_lsit(a,b))