from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        i = 0
        
        intervals.sort()
        print(intervals)
        
        while i < n :
            try:
                if intervals[i][1] >= intervals[i+1][0]:
                    intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                    intervals.pop(i+1)
                else:
                    i = i + 1
                
            except IndexError:
                break
            
            
                
        return intervals
                
    
intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1, 4], [4, 5]]
# intervals = [[1, 4],[2, 3]]
# intervals = [[1,4],[0,2],[3,5]]
sol = Solution()
print(sol.merge(intervals))
