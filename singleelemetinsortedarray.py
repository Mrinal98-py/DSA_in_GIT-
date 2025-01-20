
arr = [1,2,2,4,4,5,5,6,6]

left, right = 0, len(arr) - 1

while left < right:
    mid = (left + right) // 2
    print("MID",mid)
    if mid % 2 == 1:
        mid -= 1
        print("NEW MID:",mid)
    if arr[mid] != arr[mid + 1]:
        right = mid
        print("Right pt",right)
    else:
        left = mid + 2
        print("Left pt",left)
print(arr[left])
