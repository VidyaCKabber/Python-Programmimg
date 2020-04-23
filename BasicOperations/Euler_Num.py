#Write a Python Program to Compute the Value of Euler's Number e. Use the Formula: e = 1 + 1/1! + 1/2! + …… 1/n!
def Factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
sum = 1
for n in range(1,num+1):
    sum = sum + (1/Factorial(n))
print(sum)	

