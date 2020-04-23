num = int(input("Enter a binary number: "))
def storeEachDigit(num):
    count = 0
    list = []
    while(num):
        num = int(num)
        rem = num%10
        #Store each digit of entered array
        list.append(rem)
        num = num/10
        num = int(num)
        #Reverse the list while returning  
    return list[::-1]

def BinaryToGray():
    #Calling storeEachDigt method
    stored_elmts = storeEachDigit(num)
    result = []

    for i in range(0, len(stored_elmts)):
        print(stored_elmts[i])

        if(i==0):
            result.append(stored_elmts[i])
        else:
            result.append(stored_elmts[i-1] ^ stored_elmts[i])
    return result
result= BinaryToGray()

#Display gray code
print("Gray code of binary value ",num," is: ") 
for i in result:
    print(i,end="")

