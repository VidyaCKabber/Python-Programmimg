lst = [1, 1, 0, 0,1, 1, 0, 1, 1]
# expected output -> [0, 0, 0, 1, 1, 1, 1, 1, 1]

count_of_zeros = lst.count(0)

for v in range(count_of_zeros):
    if lst[v] == 1:
        lst[v] = 0
    
for j in range(count_of_zeros, len(lst)):
    if lst[j] == 0:
        lst[j] = 1
    
print(lst)
