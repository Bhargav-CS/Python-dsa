class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        if sorted(A) == sorted(B):
            return True
        else:
            return False
    
N = 5
A = [1,2,5]
B = [2,4,15]

sol = Solution()
print(sol.check(A, B, N))