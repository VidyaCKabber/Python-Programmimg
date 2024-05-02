# find the longest subarray in the given array whose sum equals the target.
array = [1, 1, 2, 3, 4, 5]
target = 10


result = []
for j in range(len(array)):
    add = 0 
    count = 0
    for i in array[j:]:
        if add != target and add < target:
            add +=i
            count+=1
    if(add == target):
        result.append(count)
print(max(result))
