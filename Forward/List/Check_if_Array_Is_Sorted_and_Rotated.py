class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <=0:
            return False # Single or empty array cannot be rotated

        if len(set(nums)) == 1:
            return True

        check_break_point = 0

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                check_break_point += 1
            
        if nums[-1] > nums[0]:
            check_break_point += 1
        
        return check_break_point == 1

nums = [3,4,5,1,2]
res = Solution(nums)
print(res)
