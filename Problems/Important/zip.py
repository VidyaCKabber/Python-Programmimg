a = [1, 2, 3, 5]
b = [7, 8, 9]
c = [1, 8, 9, 4]
a = [(x + y - z) for (x,y, z) in zip(a,b, c)] 
print(a)
