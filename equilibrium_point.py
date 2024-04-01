class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        if N == 1:
            return 1
        left_sum = 0
        right_sum = sum(A[1:])
        for i in range(1, N):
            left_sum += A[i-1]
            right_sum -= A[i]
            if left_sum == right_sum:
                return i+1
        return -1
    

n = 5
a = [1,3,5,2,2]
sol = Solution()
print(sol.equilibriumPoint(a, n)) # 3