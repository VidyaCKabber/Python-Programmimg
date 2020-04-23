num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
divider = 1
while 1:
    if(num1%divider == 0 and num2%divider==0):
        hcf = divider
    if(divider == num1 or divider == num2):
        break
    divider = divider +1
print("HCF: ",hcf)

