# A valid postal code  have to fullfil both below requirements:

#  must be a number in the range from  to  inclusive.
#  must not contain more than one alternating repetitive digit pair.
# Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

# For example:

# 121426 # Here, 1 is an alternating repetitive digit.
# 523563 # Here, NO digit is an alternating repetitive digit.
# 552523 # Here, both 2 and 5 are alternating repetitive digits.

# Sample Input 0

# 110000
# Sample Output 0

# False

postal_code = input()

def validate_postal_code(postal_code):
    try:
        int(postal_code) 
    except ValueError as e:
        return False
    
    if int(postal_code) < 100000 or int(postal_code) > 999999:
        return False
        
    for num in postal_code:
        if postal_code.count(num) > 1:
            return False
    return True
    
res = validate_postal_code(postal_code)
print(res)
