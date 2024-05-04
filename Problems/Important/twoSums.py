# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution:
    # solution1
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if (nums[i]+nums[i+1]) == target:
                return [i, i+1]
        return []

    #solution 2
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if (nums[i]+nums[j]) == target:
                return [i, j]
    return []

# optimised final one
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            complement = target - num
            if(complement == num):
                if nums.count(num) > 1:
                    temp_arr = nums.copy()
                    temp_arr.reverse()
                    last_index_in_reversed = temp_arr.index(complement)
                    last_index = len(temp_arr) - 1 - last_index_in_reversed
                    return [i, last_index]
            elif complement in nums:
                return [i, nums.index(complement)]
        return []
        
nums = input()
target = input()
a = Solution()
res = a.twoSum1(nums, target)
print(res)

res = a.twoSum2(nums, target)
print(res)
