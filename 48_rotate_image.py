class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(n):
            matrix[i].reverse()
            
        return matrix
    
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.rotate(matrix)) # [[7,4,1],[8,5,2],[9,6,3]]