a = [1, 5, 6, 7, 9, 11]
b = [2, 4, 3, 10, 8, 12, 5]
output = [1,2,3,4,5,5,6,7,8,9,10,11,12]

# Simple Bubble Sort for sorting list b
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
    return arr

def merge_sorted_lists(a, b):
    output = []
    i = j = 0
    
    # Merge two sorted lists
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            output.append(a[i])
            i += 1
        else:
            output.append(b[j])
            j += 1

    # Append any remaining elements
    while i < len(a):
        output.append(a[i])
        i += 1

    while j < len(b):
        output.append(b[j])
        j += 1
    
    return output

# Sort list b and then merge
b_sorted = bubble_sort(b)
result = merge_sorted_lists(a, b_sorted)

print(result)
