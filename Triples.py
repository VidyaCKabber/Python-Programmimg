nums = [0,1,4,6,7,10]
diff = 3

def findNumberOfTriples(nums, diff):
    counter = 0

    for index, num in enumerate(nums):
        nums_j = diff + num
        nums_k = 2 * diff + num

        if nums_k in nums and nums_j in nums:
            jth_index = nums.index(nums_j)
            kth_index = nums.index(nums_k)
            if index < jth_index< kth_index:
                counter += 1

    return counter

result = findNumberOfTriples(nums, diff)
print(result)
