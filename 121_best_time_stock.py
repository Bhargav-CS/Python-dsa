class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = 10**4
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


        
        

prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices)) # 5