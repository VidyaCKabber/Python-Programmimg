# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
# For example:

# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print i
# This prints:

# ('python', ['awesome', 'language'])
# ('something-else', ['not relevant'])
# In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

# Example

# Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

# For the first word in group B, 'a', it appears at positions  and  in group A. The second word, 'c', does not appear in group A, so print .

# Expected output:

# 1 3
# -1
# Input Format

# The first line contains integers,  and  separated by a space.
# The next  lines contains the words belonging to group .
# The next  lines contains the words belonging to group .

# Constraints




# Output Format

# Output  lines.
# The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

# Sample Input

# STDIN   Function
# -----   --------
# 5 2     group A size n = 5, group B size m = 2
# a       group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a       group B contains 'a', 'b'
# b
# Sample Output

# 1 2 4
# 3 5
# Explanation

# 'a' appeared  times in positions ,  and .
# 'b' appeared  times in positions  and .
# In the sample problem, if 'c' also appeared in word group , you would print .


# Solution 1
# from collections import defaultdict

# input_dict = defaultdict(list)

# inputs = input()
# n, m = map(int, inputs.split())

# # enter group A words
# for i in range(n):
#     a_word = input()
#     input_dict['A'].append(a_word)
    
# # enter group B words
# for j in range(m):
#     b_word = input()
#     input_dict['B'].append(b_word)

# result = {}

# for b_word in input_dict.get('B'):
#     result.update({b_word : [-1]})
#     for position, a_word in enumerate(input_dict.get('A'), start=1):
#         if b_word == a_word:
#             if result[b_word][0] == -1:
#                 result[b_word][0] = position
#             else:
#                 result[b_word].append(position)
            
# for key, values in result.items():
#     for i in values:
#         print(i, end=' ')
#     print()

# Solution 2
# from collections import defaultdict

# input_dict = defaultdict(list)

# inputs = input()
# n, m = map(int, inputs.split())

# # enter group A words
# for i in range(n):
#     a_word = input()
#     input_dict['A'].append(a_word)
    
# # enter group B words
# for j in range(m):
#     b_word = input()
#     input_dict['B'].append(b_word)

# # input_dict = {'A' : ['a', 'b', 'c', 'a'], 'B' : ['d', 'a']}
# result = defaultdict(list)
# A = input_dict.get('A')
# B = input_dict.get('B')

# for b_word in B:
#     if b_word not in A:
#         result[b_word].append(-1)
#     else:
#         positions = [index+1 for index, a_word in enumerate(A) if b_word == a_word]
#         result[b_word] = positions
                
            
# for values in result.values():
#     for i in values:
#         print(i, end=' ')
#     print()

# Optimised soluction 3
from collections import defaultdict

input_dict = defaultdict(list)

inputs = input()
n, m = map(int, inputs.split())

# enter group A words
for i in range(n):
    a_word = input()
    input_dict['A'].append(a_word)
    
# enter group B words
for j in range(m):
    b_word = input()
    input_dict['B'].append(b_word)


result = defaultdict(list)
A = input_dict.get('A')
B = input_dict.get('B')


position_dict = defaultdict(list)
result = defaultdict(list)

for index, value in enumerate(A):
    position_dict[value].append(index+1)
    
    
for b_word in B:
    if b_word in position_dict:
        result[b_word] = position_dict[b_word]
    else:
        result[b_word].append(-1)
        
for b_word in B:
    print(' '.join(map(str, result[b_word])))

