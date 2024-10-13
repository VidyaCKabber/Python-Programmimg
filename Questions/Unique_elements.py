arr = [1, 1, -1, 9, 8, 7, 12, 7, 7]

hash_table = set()
unique_elements_count = 0

for i, num in enumerate(arr):
    if num not in hash_table:
        hash_table.add(num)
        unique_elements_count += 1
    else:
        arr[i] = -1
        unique_elements_count -= 1

print(arr)
print(hash_table)
print(unique_elements_count)

#solution 2

def find_unique(arr):
    hash_map = {}
    unique = []

    for num in arr:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1
    
    for num, count in hash_map.items():
        if count == 1:
            unique.append(num)

    return unique

# Example Usage
arr = [1, 2, 3, 4, 5, 2, 3, 6, 7, 1]
unique = find_unique(arr)
print("Unique elements:", unique)  # Output: [4, 5, 6, 7]
