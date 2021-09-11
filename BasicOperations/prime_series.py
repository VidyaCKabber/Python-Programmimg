n = int(input("Enter lower limit: "))
m = int(input("Enter upper limit : "))

print("Prim numbers between {0} and {1} are :".format(n,m))
for j in range(n,m+1):
    for i in range(2,j):
        if j % i == 0:
            break
    else:
        print(j)
