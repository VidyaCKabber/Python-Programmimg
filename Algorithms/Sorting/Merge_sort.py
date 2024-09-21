def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    return merge(left_arr, right_arr)
    
def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
  
arr = [1, 9, 8, 5, 10]
res = merge_sort(arr)
print(res)

Iteration	Call Stack (Top to Bottom)
1	merge_sort([1, 8, 10, 2, 4, 0])
2	merge_sort([1, 8, 10])
3	merge_sort([1])
4	(pop merge_sort([1]))
5	merge_sort([8, 10])
6	merge_sort([8])
7	(pop merge_sort([8]))
8	merge_sort([10])
9	(pop merge_sort([10]))
10	merge([8], [10])
11	(pop merge([8], [10]))
12	merge([1], [8, 10])
13	(pop merge([1], [8, 10]))
14	merge_sort([2, 4, 0])
15	merge_sort([2])
16	(pop merge_sort([2]))
17	merge_sort([4, 0])
18	merge_sort([4])
19	(pop merge_sort([4]))
20	merge_sort([0])
21	(pop merge_sort([0]))
22	merge([4], [0])
23	(pop merge([4], [0]))
24	merge([2], [0, 4])
25	(pop merge([2], [0, 4]))
26	merge([1, 8, 10], [0, 2, 4])
27	(pop merge([1, 8, 10], [0, 2, 4])
