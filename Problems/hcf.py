a = int(input("Enter a: "))
b = int(input("Enter b: "))
divider = a if a > b else b
res = 1

while divider > 1:
    if(a%divider==0 and b%divider==0):
        res = divider
        break
    else:
        divider = divider - 1
    
print(res)
