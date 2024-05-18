from typing import List

class Solution:
    def findPeakElement(self, a):
        a.sort()
        return a[len(a) - 1]
    
    
a = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
sol = Solution()
print(sol.findPeakElement(a)) # 6