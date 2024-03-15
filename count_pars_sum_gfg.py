class Solution:
    def countPairs(self, mat1, mat2, n, x):
        pairs = 0
        mat2_dict = {}  # Create a dictionary to store the values of mat2

        # Populate the dictionary with the values of mat2
        for i in range(n):
            for j in range(n):
                if mat2[i][j] in mat2_dict:
                    mat2_dict[mat2[i][j]] += 1
                else:
                    mat2_dict[mat2[i][j]] = 1

        # Iterate through mat1 and calculate the target value
        for i in range(n):
            for j in range(n):
                target = x - mat1[i][j]

                # Check if the target value exists in mat2_dict
                if target in mat2_dict:
                    pairs += mat2_dict[target]

        return pairs
n = 3
x = 21
mat1 = [[1,5,6],
        [8,10,11],
         [15,16,18]]

mat2 = [[2,4,7],
         [9,10,12],
         [13,16,20]]

sol = Solution()
print(sol.countPairs(mat1, mat2, n, x)) # 4



