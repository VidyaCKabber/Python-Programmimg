string = "sadbutsad"
substring = "sad"

first_index = string.find(substring)
second_index = string.find(substring, first_index+len(substring))
print(second_index)
