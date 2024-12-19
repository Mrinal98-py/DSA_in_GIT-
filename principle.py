nums = [9,10,11,3,4,5,6,7,8]

max = max(nums)
max_i = nums.index(max)

print(max_i)

stwarr = nums[max_i+1:]
print(stwarr)
endarr = nums[:max_i+1]
print(endarr)

fix = stwarr+endarr
print(fix)

if fix == sorted(nums):
    print("true")
else:
    print("false")
