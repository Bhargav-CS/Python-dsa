from typing import List


class Solution:
    def search(self, n : int, k : int, arr : List[int]) -> int:
        for i in range(n):
            if arr[i] == k:
                return i+1
        return -1

sol = Solution()
n1 = 5
k1 = 16
arr1 = [9, 7, 2, 16, 4]
print(sol.search(n1, k1, arr1)) # 4

n2 = 7
k2 = 98
arr2 = [1,22,57,47,34,18,66]
print(sol.search(n2, k2, arr2)) # -1