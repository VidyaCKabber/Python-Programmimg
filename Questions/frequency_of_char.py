arr = [1, 2, 3, 4, 2, 2, 5, 2, 6]

output_dict = {}

for num in arr:
    if num not in output_dict:
        output_dict[num] = 1
else:
    output_dict[num] +=1

print(output_dict)
