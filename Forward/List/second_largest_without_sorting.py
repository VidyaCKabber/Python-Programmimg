lst = [2, 4, 2, 78, 81, 5, 19, 324]
unique_lst = list(set(lst))

first_largest = second_largest = float('-inf')

for num in unique_lst:
    if num > first_largest:
        second_largest = first_largest
        first_largest = num
    elif num > second_largest:
        second_largest = num

print(second_largest)
