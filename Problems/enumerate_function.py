# enumerate --> If you need to loop over an iterable and you need an index of the item use emumerate function

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for item in enumerate(list1):
    print(item)
    
# output
    # (0, 'a')
    # (1, 'b')
    # (2, 'c')
    # (3, 'd')
    # (4, 'e')
    # (5, 'f')
    # (6, 'g')
    # (7, 'h')

for index, value in enumerate(list1):
    print(f'{index} : {value}')
    
# output
    # 0 : a
    # 1 : b
    # 2 : c
    # 3 : d
    # 4 : e
    # 5 : f
    # 6 : g
    # 7 : h
