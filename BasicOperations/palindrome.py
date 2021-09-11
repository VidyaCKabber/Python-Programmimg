n = int(input("Enter number to reverse it : "))
temp = n

rem = 0
while (n > 0):
    m = n % 10
    rem = rem * 10 + m
    n = n // 10

if temp == rem:
    print("It is palindrome")
else:
    print("Number is not palindrome")
