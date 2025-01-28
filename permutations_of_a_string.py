from itertools import permutations

class Solution:
    def findPermutation(self, s):
        return list(set("".join(i) for i in permutations(s)))
        pass
    
    
s = "ABC"
sol = Solution()
print(sol.findPermutation(s))