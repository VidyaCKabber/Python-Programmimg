import string

def contains_digits(sentence):
    return any( char in string.punctuation
    for char in sentence)

assert contains_digits("Hi there ! 99") == True
assert contains_digits("Hi there") == False
assert contains_digits("Hi there !") == False
print("All tests passed...")
