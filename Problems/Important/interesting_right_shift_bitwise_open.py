def my_func (num) :
    data = [0]
    for i in range(1, num+1):
        data.append (data[i >> 1] + int (i & 1))
    return data
    
num = 6
print (my_func(num) )
