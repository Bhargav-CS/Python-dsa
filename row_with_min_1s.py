class Solution:
    def minRow(self, n, m, a):
        min_ones = float('inf')
        min_row = -1
        
        for i in range(n):
            ones = sum(a[i])
            if ones < min_ones:
                min_ones = ones
                min_row = i
        
        return min_row + 1

n = 4
m = 4
a = [[1,1,1,1],
     [1,1,0,0],
     [0,0,1,1],
     [1,1,1,1]]

sol = Solution()
print(sol.minRow(n,m,a)) # 2