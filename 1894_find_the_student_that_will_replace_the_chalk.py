from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        
        chalk_sum = sum(chalk)
        
        k = k % chalk_sum
        
        
        
        for i in range(n):
            k = k - chalk[i]
            
            if k < 0:
                return i
        
    
chalk = [5,1,5]
k = 22

# chalk = [3,4,1,2]
# k = 25

sol = Solution()
print(sol.chalkReplacer(chalk, k))