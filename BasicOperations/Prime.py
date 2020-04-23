def CheckDivision(num):
    if(num%3 == 0):
        print(num, " is divisible by 3")
    elif(num%7 == 0):
        print(num," is divisible by 7")
    elif(num%9 == 0):
        print(num, " is divisible by 9")
    elif(num%11 == 0):
        print(num, " is divisible by 11")
    else:
        return

num = int(input("Enter number to check prime or not : "))
count = 0
if(num > 1):
    for i in range(2,num):
        if(num%i == 0):
            count = count+1
            break
    if(count == 0):
        print(num, " is a prime number")
    else:
        print(num, " is not a prime number")
        CheckDivision(num)
else:
    print("1 or negative numbers are not fall into prime number category ")
