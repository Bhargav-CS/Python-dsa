class Solution:
    def findCoverage(self, matrix):
        n, m = len(matrix), len(matrix[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    #left search
                    if (j - 1) >=0 and matrix[i][j-1]:
                        ans +=1
                        
                    #right search
                    if (j + 1) < m and matrix [i][j+1]:
                        ans += 1
                    
                    #down search
                    if (i + 1) < n and matrix[i+1][j]:
                        ans +=1
                        
                    #up search
                    if (i - 1) >= 0 and matrix[i-1][j]:
                        ans +=1
                        
        return ans
                        
matrix = [[0, 1, 0],
          [0, 1, 1],
          [0, 0, 0]]

# matrix = [[0, 0, 0],
#           [0, 1, 0],
#           [0, 0, 0]]

# matrix = [[0, 1]]

sol = Solution()
print(sol.findCoverage(matrix))