from typing import List
from heapq import heapify, heapreplace
from math import sqrt



class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-v for v in gifts]
        heapify(h)
        for _ in range(k):
            heapreplace(h, -int(sqrt(-h[0])))
        return -sum(h)
        
            
gifts = [25,64,9,4,100]
k = 4
sol = Solution()
print(sol.pickGifts(gifts, k))
