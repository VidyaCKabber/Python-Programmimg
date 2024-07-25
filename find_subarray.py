# Given a non-empty array N, of non-negative integers, the degree of this array is defined as the maximum frequency of any one of its elements. Your task is to find the smallest possible length of a (# contiguous) subarray of N, that has the same degree as N. For example, in the array [1 2 2 3 1], 
# integer 2 occurs maximum of twice. Hence the degree is 2.


T = input("No of array elements: ")
N = list(map(int, input("Enter array elements separated by space: ").split()))

frequency_of_ele = {i: N.count(i) for i in N}
max_values_key = max(frequency_of_ele, key=frequency_of_ele.get)

first_index = -1
last_index = -1

for index, key in enumerate(N):
    if key == max_values_key:
        if first_index == -1:
            first_index = index
        last_index = index

subarray = N[first_index : last_index+1]
print(subarray)
