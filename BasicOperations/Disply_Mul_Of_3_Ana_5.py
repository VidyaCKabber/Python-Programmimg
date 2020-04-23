def sumOfMul(limit):
    sum = 0
    for num in range(0,limit+1):
        if(num%3==0 or num%5==0):
            sum = sum + num
    return sum

print(sumOfMul(10))
