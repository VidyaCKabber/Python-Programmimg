# Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 
# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # 0(n^2) -> for loop O(n) * count() function O(n)
        # res = [i for i in nums if nums.count(i) == 1][0]
        # return res


        # 0(n) -> for loop O(n) * add() and pop() functions have tc O(1)
        set1 = set()
        
        for i in nums:
            if i not in set1:
                set1.add(i)
            else:
                set1.remove(i)
        return list(set1)[0]

        #  0(n) -> for loop O(n) 
        # result = 0
        # for i in nums:
        #     result ^=i
        # return result

nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber(nums))
            
