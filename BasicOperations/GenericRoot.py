num = int(input("Enter a number : "))

while(num >= 10):
    temp = 0
    while(num > 0):
        rem = num % 10
        temp = temp + rem
        num = num // 10
    else:
        num = temp
print(temp)



def generic_root(n):
    # If the number is 0, the generic root is 0
    if n == 0:
        return 0
    # If n is divisible by 9, and n is not 0, the result is 9
    return 9 if n % 9 == 0 else n % 9

# Input from the user
number = int(input("Enter a number: "))

# Calculate and print the generic root
result = generic_root(number)
print(f"The generic root of {number} is: {result}")
