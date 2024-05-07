def myWrapper(n):
 return lambda a : a * n
mulFive = myWrapper(5) #n = 5
print(mulFive(2)) #a=2   # output => 10
