nums=[1,2,3,4,2]
for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    if nums[i]==nums[j]:
        nums.pop(j)
print(nums)