class Solution:
    def sumMatrix(self, n, q):
        # code here
        if q == 1:
            return 0
        
        if n == q:
            return q-1
        
        if q>2*n:
            return 0
        
        elif n<q:
            diff = q-n
            return (n+1-diff)
        
        else:
            diff = n-q
            return (n-1-diff)
            
        
        
    
# n = 4
# q = 7
# n = 5
# q = 4
n = 1
q = 3
sol = Solution()
print(sol.sumMatrix(n, q))

