"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 
An input string is valid if:
 
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

input_str = "((())"
input_str1 = "[]{}()"


def is_valid(s):
    stack = []
    maping_str = {')': '(', '}': '{', ']':'['}
    for char in s:
        if char in maping_str: # close brackers
            top_element = stack.pop() if stack else '#'
            if maping_str[char] != top_element:
                return False
        else:
            stack.append(char) # put open brackets
    
    return not stack

print(is_valid(input_str))
