nums = [1,2]
k = 3

Output =  [5,6,7,1,2,3,4]
k = k % len(nums)

slicefront = nums[:k]
sliceback = nums[-k:]

print("Slicefront is: ", slicefront)
print("Sliceback is: ", sliceback)

nums = sliceback+slicefront

print(nums)


print(k)