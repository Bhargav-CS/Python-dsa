class Solution:
    def longestPalin(self, S):
        # code here
        n = len(S)
        if n == 0:
            return ""
        if n == 1:
            return S
        start = 0
        max_len = 1
        for i in range(1, n):
            low = i - 1
            high = i
            while low >= 0 and high < n and S[low] == S[high]:
                if high - low + 1 > max_len:
                    start = low
                    max_len = high - low + 1
                low -= 1
                high += 1
            low = i - 1
            high = i + 1
            while low >= 0 and high < n and S[low] == S[high]:
                if high - low + 1 > max_len:
                    start = low
                    max_len = high - low + 1
                low -= 1
                high += 1
        return S[start:start + max_len]
    
    
    
S = "aaaabbaa"
sol = Solution()
print(sol.longestPalin(S)) # aabbaa
    
