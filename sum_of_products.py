class Solution:
    def pairAndSum(self, n, arr):
        out = 0
        for i in range(32):
            cnt = 0
            for j in range(n):
                if arr[j] & (1 << i):
                    cnt += 1
            pairs = cnt * (cnt - 1) // 2
            out += pairs * (1 << i)
        return out

# Test the function
n = 3
arr = [5, 10, 15]

sol = Solution()
print(sol.pairAndSum(n, arr))  # Output: 15