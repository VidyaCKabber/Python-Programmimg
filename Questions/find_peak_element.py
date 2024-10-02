Find Peak Element
Problem: A peak element is an element that is greater than its neighbors. Given an array nums, find a peak element.
Example:
Input: nums = [1,2,3,1]
Output: 2 (index of element 3)

def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left
