lst = [2, 4, 2, 78, 5, 19, 324]
unique_lst = list(set(lst))

largest_num = unique_lst[0]

for i in range(1, len(unique_lst)):
    if largest_num < unique_lst[i]:
        largest_num = unique_lst[i]
        
print(largest_num)
