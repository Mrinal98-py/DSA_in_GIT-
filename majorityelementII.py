array = [3,2,3]
frequency_map = {}

# Iterate over the array
for element in array:
    # Increment count if element exists in map, else initialize to 1
    if element in frequency_map:
        frequency_map[element] += 1
    else:
        frequency_map[element] = 1

print("Frequency Map:", frequency_map)

# Calculate n
n = len(array) // 3

# Find elements with frequency greater than n
elements_more_than_n = [key for key, value in frequency_map.items() if value > n]

print("Elements with frequency more than n:", elements_more_than_n)
