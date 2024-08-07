# You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

# A valid credit card from ABCD Bank has the following characteristics:

# ► It must start with a ,  or .
# ► It must contain exactly  digits.
# ► It must only consist of digits (-).
# ► It may have digits in groups of , separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have  or more consecutive repeated digits.

# Examples:

# Valid Credit Card Numbers

# 4253625879615786
# 4424424424442444
# 5122-2368-7954-3214
# Invalid Credit Card Numbers

# 42536258796157867       #17 digits in card number → Invalid 
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
# Input Format

# The first line of input contains an integer .
# The next  lines contain credit card numbers.

# Constraints


# Output Format

# Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

# Sample Input

# 6
# 4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456
# Sample Output

# Valid
# Valid
# Invalid
# Valid
# Invalid
# Invalid
# Explanation

# 4123456789123456 : Valid
# 5123-4567-8912-3456 : Valid
# 61234--8912-3456 : Invalid, because the card number is not divided into equal groups of .
# 4123356789123456 : Valid
# 51-67-8912-3456 : Invalid, consecutive digits  is repeating  times.
# 5123456789123456 : Invalid, because space '  ' and - are used as separators.



import re

N = int(input())

ABCD_Bank_credits = []

for i in range(N):
    value = input()
    ABCD_Bank_credits.append(value)
    
  
def has_consecutive_repeating_four_digit(crd_num):
    match = re.search(r'(\d)\1{3,}', crd_num)
    return bool(match)
    
def number_len_check_when_underscore(crd_num):
    s = all(len(l)==4 for l in crd_num.split('-'))
    return s

def check_credit_card(credit_num):
    clean_card_num = credit_num.replace('-', '')
    
    if credit_num[0] not in "456":
        return "Invalid"
    if len(credit_num) < 16:
        return "Invalid"
    if len(credit_num)!=16 and has_consecutive_repeating_four_digit(clean_card_num):
        return "Invalid"
    if '-' in credit_num:
        if credit_num.count('-') != 3:
            return "Invalid"
        elif credit_num.count('-') == 3 and not number_len_check_when_underscore(credit_num): 
            return "Invalid"
    return "Valid"

for credit_num in ABCD_Bank_credits:
    print(check_credit_card(credit_num))
