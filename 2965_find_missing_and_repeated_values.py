from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        set_g = set()
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] not in set_g:
                    set_g.add(grid[i][j])
                else:
                    A = grid[i][j]
                    set_g.add(0)

        print(set_g)
        for i in range(len(set_g)):
            print(i+1)
            if i+1 not in set_g:
                B = i+1
                print(B)
                
        return [A, B]
    
grid = [[1,3],[2,2]]
# grid =[[9,1,7],[8,9,2],[3,4,6]]
sol = Solution()
print(sol.findMissingAndRepeatedValues(grid))