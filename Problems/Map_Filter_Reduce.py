# Map Function
# Description
# Using the map function, create a list 'cube', which consists of the cube of numbers in input_list.
# For e.g. if the input list is [5,6,4,8,9], the output should be [125, 216, 64, 512, 729].

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
#Write your code here
cube = list(map(lambda x : x ** 3, input_list))
print(cube)

# Using the function map, count the number of words that start with ‘S’ in input_list.
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

count = sum(map(lambda x: x.startswith("S"), input_list))
#Type your code here 




print(count)

# Using the function filter, count the number of words that start with ‘S’ in input_list.

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

count = len(list(filter(lambda x: x.startswith("S"), input_list)))
#Type your code here 

print(count)



# Map Function
# Description
# Create a list ‘name’ consisting of the combination of the first name and the second name from list 1 and 2 respectively. 

# For e.g. if the input list is:
# [ ['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]

# the output list should be the list:
# ['Ankur Narang', 'Avik Sarkar', 'Kiran R', 'Nitin Sareen']

# Note: A

import ast,sys
import functools
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
first_name = input_list[0]
last_name = input_list[1]

def combine_names(first, last):
    return f"{first} {last}"
    
name = list(map(combine_names, first_name, last_name))
print(name)

# Filter Function
# Description
# Extract a list of numbers that are multiples of 5 from a list of integers named input_list.

# Note: Use the filter() function.
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_answer = list(filter(lambda x : x%5==0, input_list))
print(list_answer)


# Filter Function
# Description
# You are given a list of strings such as input_list =  ['hdjk', 'salsap', 'sherpa'].
# Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.
# Note: Use the filter() function.

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
sp = list(filter(lambda x : x.startswith("s") and x.endswith("p"), input_list))
print(sp)

# Reduce Function
# Description
# Using the Reduce function, concatenate a list of words in input_list, and print the output as a string.
# If input_list = ['I','Love','Python'], the output should be the string 'I Love Python'.
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
from functools import reduce
#write your code here.
res = reduce(lambda x, y: f"{x}{y}",input_list)
print(res)


# Reduce Function
# Description
# You are given a list of numbers such as input_list = [31, 63, 76, 89]. Find and print the largest number in input_list using the reduce() function.
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
from functools import reduce
answer = reduce(lambda x, y: x if x>y else y, input_list)
print(answer)



# Filter Function
# Description
# You are given a list of strings such as input_list = ['hdjk', 'salsap', 'sherpa'].
# Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.
# Sample Input:
# ['soap','sharp','shy','silent','ship','summer','sheep']
# Sample Output:
# ['soap', 'sharp', 'ship', 'sheep']

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
sp = list(filter(lambda x:x.startswith("s") and x.startswith("p"),  input_list))
print(sp)





