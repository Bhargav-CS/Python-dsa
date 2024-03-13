class Solution:
    def isPowerofTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n & (n - 1) == 0:
            return True
        else:
            return False


sol = Solution()
print(sol.isPowerofTwo(3)) # True