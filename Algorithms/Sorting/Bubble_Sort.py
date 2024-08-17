# Bubble sort
#. 1. Swap adjacent elemements
#. 2. At the end of each iteration max value pushed to the last 

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr

if __name__ = '__main__':
  t = int(input())
  for _ in range(t);
      n = int(input())
      arr = list(map(int, input.strip().split()))
      Solution().selectionSort(arr, n)
        
      for i in range(arr):
          print(i, end(""))
      print()
