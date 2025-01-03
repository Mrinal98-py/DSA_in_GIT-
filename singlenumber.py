#find the single frequency of num
nums = [2,2,1]

size = len(nums) 

space = []

for i in range(size):
    if nums[i] in nums[i+1:]:
        # print(nums[i])
        # print(nums[i:])
        continue
    else:
        # print("no",nums[i])
        space.append(nums[i])
        
print(space[-1])