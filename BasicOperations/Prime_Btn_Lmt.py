ltm = int(input("Enter limit"))
def prime(limit):
    for i in range(2,limit):
        count = 0
        for j in range(2,i):
            if(i%j==0):
                count = count+1
                break
        if(count == 0):
            print(i)
prime(ltm)
