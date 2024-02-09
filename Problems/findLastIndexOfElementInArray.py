my_list = [1, 2, 3, 4, 2, 5, 2]
element = 2

for index, value in enumerate(my_list):
    if value == element:
        last_index = index
        
print(last_index)
