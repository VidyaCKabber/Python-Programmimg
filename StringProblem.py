# String Problem

# In a certain encrypted message which has information about the location(area, city), the characters are jumbled such that first character of the first word is followed by the first character of the second word, then it is followed by second character of the first word and so on

# In other words, let’s say the location is bandra, mumbai

# The encrypted message says ‘bmaunmdbraai’.

# Sample Input:
# bmaunmdbraai

# Sample Output:
# bandra, mumbai

# Let’s say the size or length of the two words would not match, then the smaller word is appended with # and then encrypted in the above format.
# With this in mind, write a code to identify the right location and print it as place, city.

import ast,sys
input_str = sys.stdin.read()
msg1 = ''
msg2 = ''

for index, char in enumerate(input_str):
    if char.isalnum():
        if index%2 ==0:
            msg1 +=char.strip()
        else:
            msg2 +=char.strip()
        
out = msg1+','+msg2
print(out)
