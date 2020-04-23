#29.Write a Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
num = int(input("Enter limit: "))
dict = {}
for i in range(1,num+1):
    key_value = {i : i*i}
    dict.update(key_value)
print(dict)