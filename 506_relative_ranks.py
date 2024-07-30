from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = ["0"] * len(score)
        
        gold = score.index(max(score))
        ans[gold] = "Gold Medal"
        score[gold] = -1
        
        silver = score.index(max(score))
        ans[silver] = "Silver Medal"
        score[silver] = -2
        
        bronze = score.index(max(score))
        ans[bronze] = "Bronze Medal"
        score[bronze] = -3
        
        
        # print(score)
        
        for i in range(len(score) - 3):
            
            index = score.index(max(score))
            # print(max(score), index)
            ans[index] = str(i+4)
            score[index] = -1
            
        
        return ans
            
    
# score = [5,4,3,2,1]
score = [10,3,8,9,4]
sol = Solution()
print(sol.findRelativeRanks(score))

    
    
