# Insertion sort
# Traverse from left side to put (insert) element in the right position
#

class Solution:
    
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for i in range(1, n):
            key = arr[i]
            j = i-1
            
            while j>=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -=1
            
            arr[j+1] = key        
        return alist
