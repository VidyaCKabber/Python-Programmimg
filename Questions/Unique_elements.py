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
