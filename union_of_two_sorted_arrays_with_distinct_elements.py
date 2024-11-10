class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        a=set(a)
        b=set(b)
        c=a.union(b)
        c=list(c)
        c.sort()
        return c