# Write a Python script that takes a string as input and performs the following:
#     • Removes all punctuation characters from the string.
#     • Converts the string to uppercase.
#     • Counts the number of words in the string.
#     Example Input: "This is, a test string!"
#     Expected Output: "THISISATESTSTRING 4"

import string

counter = 0

def remove_punctuation_char(fun):
    def wrapper(msg):
        tranlater = str.maketrans('', '', string.punctuation)
        fun(msg)
        return msg.translate(tranlater)
    return wrapper

def conver_string_to_upper(fun):
    def wrapper(msg):
        m = fun(msg)
        m = m.upper()
        return m.upper()
    return wrapper

def get_words_count(fun):
    def wrapper(msg):
        global counter
        my_str = fun(msg)
        words = my_str.split()
        counter = sum(1 for word in words if len(word) > 1)
        return my_str
    return wrapper

def join_all_chars(fun):
    def wrapper(msg):
        m = fun(msg)
        m = m.split()
        new_str = ''.join(m)
        return new_str
    return wrapper 
            

@join_all_chars
@conver_string_to_upper
@remove_punctuation_char
@get_words_count
def String_Operation(msg):
    return msg
    

msg = input("Enter a String : \n")
out = String_Operation(msg)
print(f"{out} {counter}")
    
