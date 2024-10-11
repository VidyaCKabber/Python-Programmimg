Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Attempted
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_sum = 0
        start = 0

        for end in range(len(nums)):
            sub_arr = nums[start : end+1]
            min_of_subarr = min(sub_arr)
            max_of_subarr = max(sub_arr)

            if max_of_subarr - min_of_subarr > limit:
                start += 1
            
            max_sum = max(max_sum, end - start+1)
            print(max_sum)

        return max_sum
