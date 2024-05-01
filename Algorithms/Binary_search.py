def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) //2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid +1 
        else:
            high = mid -1
    return -1
    
arr = [1, 3, 4, 7, 9]
target = 7
index = binary_search(arr, target)
print("Index of", target, ":", index)
