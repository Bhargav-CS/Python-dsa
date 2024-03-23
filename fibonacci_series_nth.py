class Solution:
    def series(self, n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append((fib[i-1] + fib[i-2]) % (10**9 + 7))
        return fib[:n+1]
        
    
n = 5
sol = Solution()
print(sol.series(n))  # Output: [0, 1, 1, 2, 3, 5]

