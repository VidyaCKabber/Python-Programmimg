# Given an array arr[] sorted in ascending order of size N and an integer K. Check if K is present in the array or not.

# The time complexity of this solution is O(log N) because it uses binary search to find the target element in the sorted array. 
# The space complexity is O(1) because it only uses a constant amount of extra space regardless of the input size.

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        
        if not arr:
            return -1
            
        low = 0
        high = len(arr) -1 
    
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == K:
                return 1
            elif arr[mid] < K:
                low = mid + 1
            else:
                high = mid - 1
            
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.searchInSorted(A, N, K))

# } Driver Code Ends
