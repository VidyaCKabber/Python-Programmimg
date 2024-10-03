string = "Vidya"

def is_pallindrom(s):
    temp = ''

    for char in s:
        temp =  char + temp

    if s == temp:
        return True
    return False

res = is_pallindrom(string)
if res:
    print("Given string is pallidrom")
else:
    print("Not a pallidrom")
