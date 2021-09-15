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
