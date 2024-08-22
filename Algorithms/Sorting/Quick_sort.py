Array: [3, 6, 8, 10, 1, 2, 1]
Step-by-Step Execution with Stack Table


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))



1. Initial Call
Array: [3, 6, 8, 10, 1, 2, 1]
Pivot Calculation: len(arr) // 2 = 7 // 2 = 3, so pivot = 10
Partitioning:
Left: [3, 6, 8, 1, 2, 1] (elements less than 10)
Middle: [10] (elements equal to 10)
Right: [] (no elements greater than 10)
Stack Table After Initial Call
Depth	Array	Pivot	Left	Middle	Right
0	[3, 6, 8, 10, 1, 2, 1]	10	[3, 6, 8, 1, 2, 1]	[10]	[]
Now, Quick Sort will recursively sort the Left array [3, 6, 8, 1, 2, 1].

2. First Recursive Call (Sorting [3, 6, 8, 1, 2, 1])
Array: [3, 6, 8, 1, 2, 1]
Pivot Calculation: len(arr) // 2 = 6 // 2 = 3, so pivot = 1
Partitioning:
Left: [] (no elements less than 1)
Middle: [1, 1] (elements equal to 1)
Right: [3, 6, 8, 2] (elements greater than 1)
Stack Table After First Recursive Call
Depth	Array	Pivot	Left	Middle	Right
0	[3, 6, 8, 10, 1, 2, 1]	10	[3, 6, 8, 1, 2, 1]	[10]	[]
1	[3, 6, 8, 1, 2, 1]	1	[]	[1, 1]	[3, 6, 8, 2]
Next, Quick Sort will recursively sort the Right array [3, 6, 8, 2].

3. Second Recursive Call (Sorting [3, 6, 8, 2])
Array: [3, 6, 8, 2]
Pivot Calculation: len(arr) // 2 = 4 // 2 = 2, so pivot = 8
Partitioning:
Left: [3, 6, 2] (elements less than 8)
Middle: [8] (elements equal to 8)
Right: [] (no elements greater than 8)
Stack Table After Second Recursive Call
Depth	Array	Pivot	Left	Middle	Right
0	[3, 6, 8, 10, 1, 2, 1]	10	[3, 6, 8, 1, 2, 1]	[10]	[]
1	[3, 6, 8, 1, 2, 1]	1	[]	[1, 1]	[3, 6, 8, 2]
2	[3, 6, 8, 2]	8	[3, 6, 2]	[8]	[]
Now, Quick Sort will recursively sort the Left array [3, 6, 2].

4. Third Recursive Call (Sorting [3, 6, 2])
Array: [3, 6, 2]
Pivot Calculation: len(arr) // 2 = 3 // 2 = 1, so pivot = 6
Partitioning:
Left: [3, 2] (elements less than 6)
Middle: [6] (elements equal to 6)
Right: [] (no elements greater than 6)
Stack Table After Third Recursive Call
Depth	Array	Pivot	Left	Middle	Right
0	[3, 6, 8, 10, 1, 2, 1]	10	[3, 6, 8, 1, 2, 1]	[10]	[]
1	[3, 6, 8, 1, 2, 1]	1	[]	[1, 1]	[3, 6, 8, 2]
2	[3, 6, 8, 2]	8	[3, 6, 2]	[8]	[]
3	[3, 6, 2]	6	[3, 2]	[6]	[]
Finally, Quick Sort will recursively sort the Left array [3, 2].

5. Fourth Recursive Call (Sorting [3, 2])
Array: [3, 2]
Pivot Calculation: len(arr) // 2 = 2 // 2 = 1, so pivot = 2
Partitioning:
Left: [] (no elements less than 2)
Middle: [2] (elements equal to 2)
Right: [3] (elements greater than 2)
Stack Table After Fourth Recursive Call
Depth	Array	Pivot	Left	Middle	Right
0	[3, 6, 8, 10, 1, 2, 1]	10	[3, 6, 8, 1, 2, 1]	[10]	[]
1	[3, 6, 8, 1, 2, 1]	1	[]	[1, 1]	[3, 6, 8, 2]
2	[3, 6, 8, 2]	8	[3, 6, 2]	[8]	[]
3	[3, 6, 2]	6	[3, 2]	[6]	[]
4	[3, 2]	2	[]	[2]	[3]
Returning Results:
As the recursion unwinds, the sorted sub-arrays are returned and combined:

Depth 4: The recursion returns [2] + [3] = [2, 3].
Depth 3: The recursion returns [2, 3] + [6] + [] = [2, 3, 6].
Depth 2: The recursion returns [2, 3, 6] + [8] + [] = [2, 3, 6, 8].
Depth 1: The recursion returns [] + [1, 1] + [2, 3, 6, 8] = [1, 1, 2, 3, 6, 8].
Depth 0: The final result is [1, 1, 2, 3, 6, 8] + [10] + [] = [1, 1, 2, 3, 6, 8, 10].
