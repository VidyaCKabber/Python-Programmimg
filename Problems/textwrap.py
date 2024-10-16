# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

# string string: a long string
# int max_width: the width to wrap to
# Returns

# string: a single string with newline characters ('\n') where the breaks should be
# Input Format

# The first line contains a string, .
# The second line contains the width, .

# Constraints

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX

n = 4
string1 = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
min1 = 0
res = []
for chars in range(min1, len(string1), n):
    res.append(string1[min1:chars])
    min1 = chars
    
res = list(filter(None, res))
print(res)
# YZ

import textwrap

def wrap(string, max_width):
    till_point = max_width
    final_paragraph = ''
    for i in range(0, len(string), till_point):
        sub_string = string[i:i+till_point]
        final_paragraph += sub_string+"\n"
    return final_paragraph

# solution 2
k = 4
prev = 0

for i in range(1, len(a)//k):
    s = a[prev: k*i]
    print(s)
    prev = k*i

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
