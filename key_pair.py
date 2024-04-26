class Solution:
    def hasArrayTwoCandidates(self, arr, n, x):
        tmp_hash = {}
        
        for i, num in enumerate(arr):
            if x - num in tmp_hash:
                return True
            
            tmp_hash[num] = i
            
        return False

n = 6
x = 16
arr = [1, 4, 45, 6, 10, 8]
sol = Solution()
print(sol.hasArrayTwoCandidates(arr, n, x))

