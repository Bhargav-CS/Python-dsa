class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
       for i in A :
           if i not in B:
              return False
           else:
              return True
   

N = 5
A = [1,2,3,4,5,6,7,8,9,10]
B = [0,9,8,7,6,5,4,3,2,1]    
sol = Solution()
print(sol.check(A, B, N))