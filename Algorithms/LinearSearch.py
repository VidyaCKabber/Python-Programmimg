arr = [10, 23, 45, 70, 11, 15]
target = 70


def linearSearch():
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
print(linearSearch())
