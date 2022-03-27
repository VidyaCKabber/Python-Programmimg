# Find GCD of two integers

""" The way algorithms works
    1. For two integers a and b, where a>b, divide a by b
    2. If the reminder r is 0, then stop: GCD is b
    3. Otherwise, set a to b, b to r, and repeat the step 1 until is 0.
"""
a = int(input("Enter value for a: " ))
b = int(input("Enter value for b: " ))

while b != 0:
    t = a 
    a = b
    b = t % b
print(a)
