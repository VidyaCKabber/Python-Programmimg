def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insert_new_element(arr, element):
    # Insertion sort to place the new element in the correct place
    i = len(arr) - 1
    while i >= 0 and arr[i] > element:
        i -= 1
    arr.insert(i + 1, element)
    return arr

# Example usage:
arr = [2, 4, 5, 6, 9]
arr = insertion_sort(arr)  # Initial sort
print("Sorted Array:", arr)
arr = insert_new_element(arr, 7)  # Insert new element
print("Array after Insertion:", arr)
 
