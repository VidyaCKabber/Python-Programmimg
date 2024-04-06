# find values which are repeated multiple times in list and how many times values repeated

abc = [1, 2, 3, 1, 2, 4, 2]
duplicates = {}
for i in abc:
    if i not in duplicates.keys():
        value_count = abc.count(i)
        if value_count > 1:
            duplicates.update({i : value_count})
print(duplicates)
