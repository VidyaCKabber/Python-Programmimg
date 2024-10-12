# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

from collections import OrderedDict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = list(OrderedDict.fromkeys(nums))

        return temp

# other solution

print(frozenset(nums))


# other solution

nums = [1, 2, 3, 1, 2, 4, 5, 6, 3]

def remove_duplicates(lst):
    
    for i in range(len(lst)-1, -1, -1):
        
        if lst[i] in lst[:i]:
            lst.pop(i)
            
    return lst
# Remove duplicates while preserving order
nums_no_duplicates = remove_duplicates(nums)

print(nums_no_duplicates)

# solution 2

def remove_duplicates(nums):
    seen = set()
    result = []
    
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

# Example usage
nums = [1, 2, 3, 1, 2, 4, 5, 6, 3]
unique_nums = remove_duplicates(nums)
print(unique_nums)  # Output: [1, 2, 3, 4, 5, 6]

