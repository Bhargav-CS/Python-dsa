class Solution:
    def sameFreq(self, s):
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return freq

sol = Solution()
print(sol.sameFreq("xyxyxy")) 