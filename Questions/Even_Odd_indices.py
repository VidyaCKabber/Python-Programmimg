string = "KTAARMNIALTNAAKDAU"
# print even and odd indices of this string as separate strings

odd_indices = ''
even_indices = ''
index = 0

for char in string:
    if index%2 == 0:
        even_indices += char
    else:
        odd_indices += char
    index += 1
        
print(odd_indices)
print(even_indices)
