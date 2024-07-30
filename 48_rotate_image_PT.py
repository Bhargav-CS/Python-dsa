from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        
        #Transpose
        
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        print("matrix transpose:")
        print(matrix)
        #Reflection
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
                
        print("matrix after reflection:")
        print(matrix)
    
    
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

sol = Solution()
print(sol.rotate(matrix))