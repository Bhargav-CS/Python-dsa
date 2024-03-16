class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        #code here
        return len(set(a+b))

n = 6
m = 2
a = [85, 25, 1, 32, 54, 6]
b = [85, 2]
sol = Solution()
print(sol.doUnion(a, n, b, m)) # 4