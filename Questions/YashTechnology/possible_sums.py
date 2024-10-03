a=[1,5,9,6,5,4,7]
n=10
result = []

hash_map = {}

for num in a:
    diff = n - num
    
    if diff in hash_map:
        result.append((diff, num))
    else:
        hash_map[num] = diff
    
print(hash_map)
print(result)
 
# {1: 9, 5: 5, 6: 4, 7: 3}
# [(1, 9), (5, 5), (6, 4)]
