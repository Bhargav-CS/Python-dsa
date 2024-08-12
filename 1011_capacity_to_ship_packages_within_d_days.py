class Solution:
    def shipWithinDays(self, weights, days):
        def canShip(capacity):
            total = 0
            days_needed = 1
            for weight in weights:
                if total + weight > capacity:
                    days_needed += 1
                    total = 0
                total += weight
            return days_needed <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left

weights = [3, 2, 2, 4, 1, 4]
days = 3

sol = Solution()
print(sol.shipWithinDays(weights, days))
# Expected output: 6