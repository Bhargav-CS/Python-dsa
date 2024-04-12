class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        low = 0
        high = N - 1
        while low <= high:
            mid = low + (high - low) // 2
            if A[mid] == X:
                return mid
            elif A[mid] < X:
                low = mid + 1
            else:
                high = mid - 1
        return high
    



N  = 7
X = 0
A = [1,2,8,10,11,12,19]
sol = Solution()
print(sol.findFloor(A,N,X))