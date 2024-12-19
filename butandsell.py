nums = [7,5,3,6,4,1]


min = min(nums)
min_i = nums.index(min)
# print(min_i)
new = nums[min_i:]
max = max(new)

v = max-min

print(v)




