def search(nums,target):
    
    lower = 0
    upper = len(nums)-1
    
    while lower <= upper:
        mid = (lower + upper) // 2
        
        if nums[mid] == target:
            print("target Found",target,"index",mid + 1)
            break
        else:
            if nums[mid] < target:
                lower = mid+1
            else:
                upper = mid-1
                
nums = [0,1,2,3,4,5,6,7,8]

search(nums,4)
    