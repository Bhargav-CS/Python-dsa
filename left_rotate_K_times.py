class Solution:
    def rotateMatrix(self, k, mat):
        out = []
        for row in mat:
            n = len(row)
            rotate = k%n
            row.extend(row)
            need = row[rotate:rotate+n]
            out.append(need)    
        return out
            
            
    
k = 12
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

sol = Solution()
print(sol.rotateMatrix(k, mat))

# arr = [1, 2, 3]
# n = len(arr)
# rotate = k%n
# arr.extend(arr)
# print(arr)
# print(arr[rotate:rotate+n])