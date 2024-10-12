abc = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]

dictionary = {}
for i in abc:
    if i not in dictionary.keys():
        dictionary.update({i: 1})
    else:
        dictionary.update({i: dictionary[i]+1})

for key, value in dictionary.items():
    if value > 1:
        print(key)


# solution 2
abc = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]

def find_duplicates(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Example usage
duplicates = find_duplicates(abc)
print(duplicates)  # Output: [8, 5, 7]
