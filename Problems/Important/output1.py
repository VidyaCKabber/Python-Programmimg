# String = "google.com"

# # Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
output = {}

for char in String:
    char_count = String.count(char)
    output.update({char : char_count})
    
print(output)


for char in String:
    if char in output:
        output[char] = output[char] + 1
    else:
        output.update({char : 1})

print(output)
