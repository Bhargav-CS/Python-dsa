from typing import List

class Solution:
    def maximumProfit(self, prices) -> int:
        n = len(prices)
        maxi = 0
        l,r = 0,0
        while r<n-1:
            if prices[r]<=prices[r+1]:
                profit = prices[r+1]-prices[l]
                maxi+=profit
            r+=1
            l+=1
        return maxi