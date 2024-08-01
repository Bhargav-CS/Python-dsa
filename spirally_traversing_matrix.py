from typing import List

class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix:List[List[int]]):
        # code here
        ans = []
        n, m = len(matrix), len(matrix[0])
        i, j = 0, 0
        eg = 0
        flag = True
        
        while i < n and j < m :
            ans.append(matrix[i][j])
            
            if flag:
                if j == m - 1: 
                    i = i + 1  
                elif i == eg:
                    # print("eg verified")
                    j = j + 1
                
            if i == n - 1 and j == m - 1:
                ans.append(matrix[i][j])
                flag = False
            
                if n == 1 or m == 1:
                    return ans, "returned ans"
                
                
            if not flag:
                if j == eg:
                    i = i - 1
               
                elif i == n - 1:
                    j = j - 1
                    
            if i == eg and j == eg:
                eg = eg + 1
                i = i + 1
                j = j + 1
                m = m - 1
                n = n - 1
                flag = True
            
            if len(ans) == len(matrix) * len(matrix[0]):
                return ans
    
# matrix = [[1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15,16]]

matrix = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]

# matrix = [[1,2],
#           [3,4],
#           [5,6],
#           [7,8]]

# matrix = [[41, 66, 47, 23]]

# matrix  = [[1],
#            [2],
#            [3],
#            [4]]

matrix = [[42, 23, 47],
          [47, 66, 8],
          [72, 53, 25],
          [69, 70, 82],
          [72, 49, 19],
          [7, 79, 33],
          [85, 41, 49],
          [3, 28, 78],
          [80, 12, 57],
          [21, 43, 48]]

sol = Solution()
print(sol.spirallyTraverse(matrix))