lst = [333,1234,43,56,8734]
N=3
# Result should be -> [,124,4,56,874]

lst = list(map(str, lst))
new_lst = lst.copy()
lst.remove(lst[0])

for index, word in enumerate(new_lst):
    if str(N) in word:
        word = word.replace(str(N), '')
        if word == '':
            word = 0
    lst[index] = int(word)
print(lst)
