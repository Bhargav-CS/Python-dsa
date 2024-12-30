class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        a = set(a)
        b = set(b)
        
        a = a.union(b)
        return len(a)
    
a = [1, 2, 3, 4, 5]
b = [1, 2, 3]


sol = Solution()
print(sol.findUnion(a, b))