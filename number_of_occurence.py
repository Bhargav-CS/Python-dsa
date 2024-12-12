class Solution:
    def countFreq(self, arr, target):
        return arr.count(target)
    
    
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
sol = Solution()
print(sol.countFreq(arr, target))
