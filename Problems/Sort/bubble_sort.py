a = [1, 3, 5, 4, 6]

# bubble sort
# [1,3, 4, 5, 6]
n = len(a)
for i in range(n-1):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)
            
