def print_all_subarrays(arr):
    n = len(arr)
    # Iterate over all possible starting points
    for i in range(n):
        # Iterate over all possible ending points
        for j in range(i, n):
            # Print subarray arr[i:j+1]
            print(arr[i:j+1])
            new_arr = arr[i:j+1]

                

# Example usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print_all_subarrays(arr)
