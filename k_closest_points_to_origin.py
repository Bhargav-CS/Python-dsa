from typing import List
import heapq

class Solution:
    def kClosest(self, points:List[List[int]], k:int) -> List[List[int]]:
        hashmap = {index:value for index, value in enumerate(points)}
        
        for i in range(len(points)):
            hashmap[i] = (points[i][0] ** 2) + points[i][1] ** 2

        sorted_items = sorted(hashmap.items(), key=lambda kv:(kv[1], kv[0]))
        out = []
        for i in range(k):
            out.append(points[sorted_items[i][0]])
            
        return out
            
        
k = 2
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
sol = Solution()
print(sol.kClosest(points, k))