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



======2nd solution=======
a = int(input("Enter a: "))
b = int(input("Enter b: "))
max_num = a if a<b else b

if a%b==0 and b%a==0:
    hcf = max_num
else:   
    while(max_num > 1):
        if a%max_num==0 and b%max_num==0:
            hcf = max_num
            break
        max_num -=1
    print(hcf)
