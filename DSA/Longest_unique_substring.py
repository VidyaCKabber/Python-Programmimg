string1 = "abbbc"
k = 5
length = len(string1)

# Initialize max_sum to an empty string
max_sum = ''

# Loop through the string and check for unique substrings of length k
for i in range(length - k + 1):
    temp_string = string1[i:i+k]
    unique_chars = len(set(temp_string))
    
    # If the substring has exactly k unique characters, update max_sum
    if unique_chars == k:
        max_sum = temp_string
        break

print(max_sum)
