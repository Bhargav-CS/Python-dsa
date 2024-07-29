from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        left = 0
        right = 1
        
        while right < len(prices):
            if prices[left] < prices[right]:
                currP = prices[right] - prices[left]
                maxP = max(currP, maxP)
                right += 1
                
            else:
                left = right
                right += 1       
                
        return maxP
    
prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
prices = [7, 5, 3, 4, 1, 6]
sol = Solution()
print(sol.maxProfit(prices))