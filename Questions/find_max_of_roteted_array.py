nums = [3,4,5, 9, 0, 1,2]

def find_max_of_roteted_array(nums):
    left , right = 0, len(nums)-1
    
    while left < right:
        mid = (left + right) //2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
            
    return nums[left-1]
    
    
print(find_max_of_roteted_array(nums))
