class Solution:
    def pattern(self, arr):
        for row in arr:
            if row == row[::-1]:
                return str(arr.index(row)) + " R"
            
        result = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
        
        for column in result:
            if column == column[::-1]:
                return str(result.index(column)) + " C"
            
        return -1
    
# arr = [[1, 0, 0],
#        [0, 1, 0],
#        [1, 1, 0]]

arr = [[1, 0],
        [1, 0]]

sol = Solution()
print(sol.pattern(arr))

