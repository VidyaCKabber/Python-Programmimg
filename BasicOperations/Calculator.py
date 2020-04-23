choice = int(input("Enter 1=>Addition, 2=>Substraction, 3=>Multiplication, 4=>Division\n"))
	
def Addition(a,b):
    return a+b

def Substraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b

def Division(a,b):
    return a/b

if(choice < 5):
    num1 = float(input("Enter first numbers "))
    num2 = float(input("Enter second numbers "))

    if(choice == 1):
        (Addition(num1,num2))
    elif(choice == 2):
        print(Substraction(num1,num2))
    elif(choice == 3):
        print(Multiplication(num1,num2))
    else:
        print(Division(num1,num2))
else:
    print("Invalid input")
