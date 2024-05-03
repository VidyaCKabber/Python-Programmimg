# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "pradeep"
# Output: 1
# Example 2:
# Input: s = "lovecodelanguage"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1

nput_string = "aabb"
repeated_char_index = -1
 
for char in input_string:
    char_count = input_string.count(char)
    if char_count == 1:
        repeated_char_index = input_string.index(char)
        break
print(repeated_char_index)
