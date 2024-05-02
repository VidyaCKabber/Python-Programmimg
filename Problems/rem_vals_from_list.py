# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.


arr = [1, 2, 32, 1, 3,23,4, 4,4,4,2,1,23,5]
rem_val = 23
rem_val_count = arr.count(rem_val)
if rem_val_count > 0:
    for i in range(rem_val_count):
        arr.remove(rem_val)
else:
    print("val not found")
print(arr)
