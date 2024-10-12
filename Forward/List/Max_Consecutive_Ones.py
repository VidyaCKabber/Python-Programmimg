# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

nums = [1, 0, 1, 1, 0, 1]

def a():
    if not nums:
        return False
        
    count = max_count = 0
    start = end = -1
    temp_start = -1
    
    for i, num in enumerate(nums):
        if num == 1: 
            if temp_start == -1:
                temp_start = i  # Mark the start of the sequence
            
            count += 1
            
            if count > max_count:
                max_count = count
                start = temp_start  # Update start only when max_count is updated
                end = i  # Current index is the end of the sequence
        else:
            count = 0  # Reset count when encountering a 0
            temp_start = -1  # Reset temp_start for next sequence of 1's
    
    return max_count, start, end
    
print(a())
