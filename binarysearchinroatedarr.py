# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
nums = [5,6,7,0,1,2]

# nums = [100,90,80,70,60,50,40,30]
target = 0

left = 0
right = len(nums)-1

while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] >= nums[left]:
        if nums[left] <= target <= nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid] <= target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
        
        
            
            
    # else:
    #     if nums[mid] < target:
    #         lower = mid+1
    #     else:
    #         upper = mid-1
            