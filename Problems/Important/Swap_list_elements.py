nums = [30, 5, 8, 20, 15, 2]
mid_ele = len(nums) // 2

for i in range(mid_ele):
    temp = nums[i]
    nums[i] = nums[-1-i]
    nums[-1-i] = temp
    
print(nums) # [2, 15, 20, 8, 5, 30]

