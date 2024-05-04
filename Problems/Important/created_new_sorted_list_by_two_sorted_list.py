# You are given the heads of two sorted lists list1 and list2.

# Merge the two lists into one sorted list. 

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

list1 = [1,2,4]
list2 = [1,3,4]

list1.extend(list2)

for i in range(len(list1)-1):
    for j in range(0, len(list1)-i-1):
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
            
            
print(list1)
