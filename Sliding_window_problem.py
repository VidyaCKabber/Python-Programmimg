# Find the maximum sum of any subarray of size k in a given array.

arr = [2, 1, 5, 1, 3, 2, 6]
k = 3

window = sum(arr[:k])
max_sum = window
j = k+1

for i in range(1, len(arr)+1-k):
    window = sum(arr[i:j])
    j += 1
    if window > max_sum:
        max_sum = window
    
print(max_sum)
