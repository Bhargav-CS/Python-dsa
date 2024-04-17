from typing import List


class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        # code here
        for i in range(0, n-1, 2):
            a[i], a[i+1] = a[i+1], a[i]
        return a

n = 5
a = [1,2,3,4,5]
sol = Solution()
print(sol.convertToWave(n, a)) #expected output is [2,1,4,3,5] the lexicographically smallest one.


