class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        arr1.extend(arr2)
        arr1.sort()
        
        
        
        return arr1[len(arr1)//2 - 1] + arr1[len(arr1)//2]


# arr1 = [1, 2, 4, 6, 10]
# arr2 = [4, 5, 6, 9, 12]

arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]

sol = Solution()
print(sol.sum_of_middle_elements(arr1, arr2))