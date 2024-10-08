arr = [1, 2, 3]
flattened_list = [value for num in arr for value in (num, num ** 2, num ** 3)]
print(flattened_list)
