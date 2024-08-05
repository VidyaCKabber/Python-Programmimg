# Given a string that has multiple words reverse each word in its place and return the string.

string = "Given a string that has multiple words reverse each word in its place and return the string."

# go though each word, reverse and replace there only
str1 = string.split()
for index, word in enumerate(str1):
    if len(word) > 1:
        str1[index] = word[::-1]
str1 = ' '.join(str1)
print(str1)
