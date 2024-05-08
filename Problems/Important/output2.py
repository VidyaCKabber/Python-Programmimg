lst = [333,1234,43,56,8734]
N=3
# Result should be -> [,124,4,56,874]

lst = list(map(str, lst))

for index, word in enumerate(lst):
    if str(N) in word:
        word = word.replace(str(N), '')
    if word == '':
        lst[index] = word
    else:
        lst[index] = int(word)
lst = list(filter(lambda x : x!= '', lst))
print(lst)
