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

Here’s a step-by-step explanation of Merge Sort using the array [1, 8, 9, 10, 5], presented in a table.

Initial Array: [1, 8, 9, 10, 5]
Step-by-Step Table for Merge Sort:
Step	Action	Array	Left Half	Right Half	Merged Result
Step 1	Initial split into two halves	[1, 8, 9, 10, 5]	[1, 8]	[9, 10, 5]	
Step 2	Recursively split [1, 8]	[1, 8]	[1]	[8]	
Step 3	Merge [1] and [8]				[1, 8]
Step 4	Recursively split [9, 10, 5]	[9, 10, 5]	[9]	[10, 5]	
Step 5	Recursively split [10, 5]	[10, 5]	[10]	[5]	
Step 6	Merge [10] and [5]				[5, 10]
Step 7	Merge [9] and [5, 10]				[5, 9, 10]
Step 8	Merge [1, 8] and [5, 9, 10]				[1, 5, 8, 9, 10]
Detailed Explanation of Each Step:
Step 1: The array [1, 8, 9, 10, 5] is split into two halves: [1, 8] and [9, 10, 5].

Step 2: The left half [1, 8] is split into [1] and [8].

Step 3: [1] and [8] are already sorted (since they contain only one element each). We merge them to get [1, 8].

Step 4: The right half [9, 10, 5] is split into [9] and [10, 5].

Step 5: The subarray [10, 5] is split into [10] and [5].

Step 6: Merge [10] and [5]. Since 5 is smaller than 10, the merged result is [5, 10].

Step 7: Merge [9] and [5, 10]. We compare elements:

5 is smaller than 9, so 5 goes first.
9 is smaller than 10, so 9 goes next.
10 is added last. The merged result is [5, 9, 10].
Step 8: Finally, merge [1, 8] and [5, 9, 10]. Compare elements:

1 is smaller than 5, so 1 goes first.
5 is smaller than 8, so 5 goes next.
8 is smaller than 9, so 8 goes next.
9 and 10 are added in order. The final sorted array is [1, 5, 8, 9, 10].
Final Sorted Array: [1, 5, 8, 9, 10]

            
