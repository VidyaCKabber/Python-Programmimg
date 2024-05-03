arr = [1, 3, 5, 4, 6]

# bubble sort
# [1,3, 4, 5, 6]
n = len(arr)
for i in range(1, n):
    key = arr[i]
    j = i-1
    
    while j >=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = key
            
print(arr)
