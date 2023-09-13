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
