string = ["vidya", "rama", "sima", "tanukadad"]
string1 = string.copy()

first_largest = max(string1, key=len)
print(first_largest)
string1.remove(first_largest)
second_largest = max(string1, key=len)
print(second_largest)
