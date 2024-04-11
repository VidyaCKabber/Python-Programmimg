a = int(input("Enter a: "))
isPrime=True
# if number is divisible by only 1 and iteself is prime so if divisible by otheer number is not primt
if a<2:
    isPrime=False
else:
    for i in range(2, a):
        if(a%i == 0):
            isPrime = False
            break

print(isPrime)
