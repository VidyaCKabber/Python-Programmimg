# Selection sort 

# 1. Select min value in each iteration
# 2. Swap the it with iteration value of the current execution
# 3. Continue this for all arr elements

class Solution: 
    def selectionSort(self, arr,n):
        for i in range(n):
            min = arr[i]
            for j in range(i, n):
                if min > arr[j]:
                    temp = min
                    min = arr[j]
                    arr[j] = temp
            arr[i] = min
        return arr

if __name__ = 'main()':
    t = int(input())
    for _ in range(t);
        n = int(input())
        arr = list(map(int, input.strip().split()))
        Solution().selectionSort(arr, n)
        
        for i in range(arr):
            print(i, end(""))
        print()
