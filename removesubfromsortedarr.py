def removeDuplicates(nums) -> int:
    # if not nums:
    #     return 0
    
    write_index = 1
    
    for i in range(1, len(nums)):
        print("nums[i]",nums[i],"nums[i-1]",nums[i-1])
        if nums[i] != nums[i - 1]:
            print("nums[write_index]",nums[write_index],"nums[i]", nums[i])
            nums[write_index] = nums[i]
            print("write_index",write_index)
            write_index += 1
            print("nums",nums)
            
    print(nums[:write_index])
    return write_index

nums = [2,3,3,3,4,4,5,6,6,6]
print(removeDuplicates(nums))

# def remdub(nums):
#     for i in range(1,len(nums)):
#         if nums[i] != nums[i - 1]:
            