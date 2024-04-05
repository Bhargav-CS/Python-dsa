class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        max_right = A[N-1]
        leaders = [max_right]
        for i in range(N-2, -1, -1):
            if A[i] >= max_right:
                max_right = A[i]
                leaders.insert(0, max_right)
        return leaders
    


arr = [16,17,4,3,5,2]
n = 6
sol = Solution()
print(sol.leaders(arr, n)) # [17, 5, 2]