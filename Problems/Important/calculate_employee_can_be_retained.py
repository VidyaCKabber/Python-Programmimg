# In a company, there is a layoff due to recession. The company decided to remove maximum number of employees. Each employee has a unique identification number n. The managers also have a unique identification number x. A manager with identification number x is a mentor of an employee with identification number n if three conditions are satisfied: 
# 1. n is greater than or equal to the square of the number x.
# 2. n is strictly less than the square of the number (x+1).
# 3. n is divisible by x.
# The company owner has a range [l,r] in his mind. The company will keep only those employees whose identification number is in the range [l,r] and the employee has a mentor.
# You are given q queries. In each query, you are given two integers l and r telling the range [l,r]. For each query tell the number of employees who will not be removed from the company.
# (Note: the id of the employer and manager can be the same since they are from different departments.)

# Input Format
# The first line contains Q, the number of queries.
# Next, Q lines contain two integers l and r, telling the start and end of range respectively. 

# Constraints
# 1<= n <= 10000
# 1<= l,r <= 10^18

# Output Format
# For each query print the number of employees who are kept by the company.

# Sample TestCase 1
# Input
# 1
# 5 10
# Output
# 3
  
import math

def calculate_employee_can_be_retained(l, r):
    count =0
    for n in range(l, r):
        max_x = math.isqrt(r)
        for x in range(1, max_x+1):
            x_2 = x**2
            x_1_2 = (x+1)**2
            if(n >= x_2 and n<= x_1_2 and n%x==0):
                count +=1
    return count

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(calculate_employee_can_be_retained(l, r))
