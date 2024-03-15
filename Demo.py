mat1 = [[1,5,6],
        [8,10,11],
         [15,16,18]]
      
mat2 = [[2,4,7],
         [9,10,12],
         [13,16,20]]

# mat1 = [[1,2],
#         [3,4]]

# mat2 = [[4,5],
#         [6,7]]
n = 3
x = 21
def countPairs(mat1, mat2, n, x):
   count = 0
   mat2_sorted = [sorted(row) for row in mat2]  # Sort each row of mat2

   for i in range(n):
      for j in range(n):
         target = x - mat1[i][j]  # Calculate the target value
         left = 0
         right = n - 1

         while left < n and right >= 0:
            if mat2_sorted[left][right] == target:
               count += 1
               left += 1
               right -= 1
            elif mat2_sorted[left][right] < target:
               left += 1
            else:
               right -= 1

   return count


print(countPairs(mat1, mat2, n, x)) # 4