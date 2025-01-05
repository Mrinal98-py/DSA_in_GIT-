nums = [1,1,0,1,1,1]
# Output: 3
i  = j = 0 

max = 0

for i in range(len(nums)):
    if nums[i] == 1 and nums[j+1] == 1:
        max +=1
    if nums[i] == 0:
        i = j
        j = j + 1

print (max+1)
