pairs = 0
mat2_dict = {}

n = 3
x = 21
mat1 = [[1,5,6],
   [8,10,11],
   [15,16,18]]

mat2 = [[2,4,7],
   [9,10,12],
   [13,16,20]]

for i in range(n):
   for j in range(n):
      print(f"Processing mat2[{i}][{j}] = {mat2[i][j]}")
      if mat2[i][j] in mat2_dict:
         mat2_dict[mat2[i][j]] += 1
      else:
         mat2_dict[mat2[i][j]] = 1

print(f"mat2_dict: {mat2_dict}")

for i in range(n):
   for j in range(n):
      target = x - mat1[i][j]
      print(f"Processing mat1[{i}][{j}] = {mat1[i][j]}, target = {target}")

      if target in mat2_dict:
         pairs += mat2_dict[target]
         print(f"Found a pair: mat1[{i}][{j}] + mat2_dict[{target}]")

print(f"pairs: {pairs}")
