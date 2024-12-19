def print_all_subarrays(arr):
    subarrays = [arr[i:j+1] for i in range(len(arr)) for j in range(i, len(arr))]
    for subarray in subarrays:
        print(subarray)

# Example usage
arr = [1, 2, 3, 4]
print_all_subarrays(arr)
