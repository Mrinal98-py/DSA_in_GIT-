# Example in Python
def find_index(arr, target):

  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

# Example usage
my_array = [10, 20, 30, 20, 5]
index = find_index(my_array, 5)
print(index)  # Output: 1 (index of the first 20)
