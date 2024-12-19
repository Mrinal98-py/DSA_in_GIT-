
# driver code
arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]
arr.sort()
rev=arr[::-1]
print(rev)
# Convert the list of numbers to a string with commas
result = ', '.join(map(str, rev))

print(result)
# This code is contributed by shinjanpatra
