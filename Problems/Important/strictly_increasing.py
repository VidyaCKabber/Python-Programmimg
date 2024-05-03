# Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.
 
# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
 
# Example:
# Input: nums = [1,2,10,5,7] Output: true
# Input: nums = [2,3,1,2] Output: false
# Input: nums = [1,1,1] Output: false


nums =  [1, 2, 10, 5, 7]

def check_strictly_increasing_list():
    count = 0
    n = len(nums)
    for j in range(n-1):
        if count <= 1:
            if nums[j] >= nums[j+1]:
                if nums[j+1] < nums[j-2]:
                    return False
                count +=1
        else:
            break
    if count<=1:
        return True
    return False
        
        
res = check_strictly_increasing_list()  
print(res)
