def my_func (nums) :
    count = 0
    for i, j in enumerate (nums) :
        if i > count: 
            return False
        count = max(count, i + j)
    return True

print (my_func([3, 2, 1, 0, 4]))
