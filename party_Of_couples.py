class Solution:
    def findSingle(self, n, arr):
        # code here
        freq = {}
        for ele in arr:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1
        
        for ele, count in freq.items():
            if count % 2 == 1:
                return ele

n = 5
arr = [1, 2, 3, 2, 1]
sol = Solution()
print(sol.findSingle(n, arr))