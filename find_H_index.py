class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n = len(citations)
        citations.sort()
        h = 0
        for i in range(n):
            h = max(h, min(citations[i], n-i))
        return h
    
    
    
    
citations = [3, 0, 5, 3, 0]
sol = Solution()
print(sol.hIndex(citations)) # 3