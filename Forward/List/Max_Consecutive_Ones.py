# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = max_counter = 0

        for num in nums:
            if num == 1:
                count += 1
                if count > max_counter:
                    max_counter += 1
            else:
                count = 0

        return max_counter

nums = [1,1,0,1,1,1]
obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))
