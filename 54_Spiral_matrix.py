class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        left, right = 0, len(matrix[0]) 
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            # get every element in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # get wvery element in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            # get every element in the bottom row
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            # get every element in the left column
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res
    
    
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

sol = Solution()
print(sol.spiralOrder(matrix)) # [1,2,3,6,9,8,7,4,5]
