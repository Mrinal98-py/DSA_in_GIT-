from collections import Counter

# Initialize the doors dictionary with 'false' values
doors = {i: 'false' for i in range(1, 101)}

# Function to flip the value
def flip(value):
    return 'true' if value == 'false' else 'false'

# Loop through numbers 1 to 5
for i in range(1, 101):
    for j in range(1, 101):
        if j % i == 0:
            doors[j] = flip(doors[j])

# Print the final state of the doors
# print(doors)

#  Print the final state of the doors
print("Final state of the doors:", doors)

# Count the 'true' and 'false' values
counts = Counter(doors.values())
print("Count of 'true' values:", counts['true'])
print("Count of 'false' values:", counts['false'])