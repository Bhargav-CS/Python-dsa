class Solution:
    def padovanSequence(self, n):
        MOD = 10**9+7
        a, b, c = 1, 1, 1

        for i in range(3, n+1):
            cur = (a + b) % MOD
            a, b, c = b, c, cur

        return c if n > 2 else 1

n = 9833
sol = Solution()
print(sol.padovanSequence(n))

