class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        A = set(A)
        B = set(B)

        
        

N = 5
A = [16, 1, 2, 14, 13, 17, 1]
B = [14, 1, 16, 2, 13, 2, 17]
sol = Solution()
print(sol.check(A,B,N))