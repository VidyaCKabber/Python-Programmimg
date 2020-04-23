print("Enter the coefficients of the form ax^3 + bx^2 + cx + d: ")
list = []
coefficients = ['a: ','b: ','c: ','d: ']
print("Enter a,b,c and d value:\n ")
for i in range(4):
    value = float(input(coefficients[i]))
    #Store coefficients in a list
    list.append(value)

#Value for x
x = float(input("Enter x value: "))

sum = 0
exp = 4
#Evaluate the equation
for i in range(0,4):
    exp = exp - 1
    sum = sum + (x**exp) * list[i]
print("Value of the polynomial is: ",sum)

