# adding new value to tuple
abc = (1, 2, 'vidya', 4, 7)
new_t = abc[0:2] + (123,) + abc[2:]
print(new_t)
