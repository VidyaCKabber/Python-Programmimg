#any () --> If any of the item is true. That means, non-empty or zero.


def contains_digits(sentence):
    return any( char.isdigit()
    for char in sentence)

assert contains_digits("Hi there ! 99") == True
assert contains_digits("Hi there !") == False
assert contains_digits("Hi there !") == False
print("All tests passed...")
