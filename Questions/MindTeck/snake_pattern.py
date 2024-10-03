# n = 3
 
# output:
 
# 123
# 654
# 789

n = 4
counter = 1
for row in range(n):
    temp = counter + (n-1)
    for col in range(n):
        if row %2 != 0 : # odd row
            print(temp, end="")
            temp -= 1
        else:
            print(counter, end="")
        counter += 1
    print()
