from typing import List

class Solution:
    def help(self, pattern: str, string: str, i: int, j: int, dp: List[List[int]]) -> int:
        if i == len(pattern) and j == len(string):
            return 1
        if i == len(pattern):
            return 0
        if j == len(string) and pattern[i] == '*':
            return self.help(pattern, string, i + 1, j, dp)
        if j == len(string):
            return 0
        if pattern[i] != '?' and pattern[i] != '*' and pattern[i] != string[j]:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        a = b = c = 0
        if pattern[i] == '*':
            a = self.help(pattern, string, i + 1, j, dp)
            b = self.help(pattern, string, i, j + 1, dp)
        
        c = self.help(pattern, string, i + 1, j + 1, dp)
        
        dp[i][j] = a | b | c
        return dp[i][j]
    
    def wildCard(self, pattern: str, string: str) -> int:
        dp = [[-1 for _ in range(len(string))] for _ in range(len(pattern))]
        return self.help(pattern, string, 0, 0, dp)

# Example usage
pattern = "ba*a?"
string = "baaabab"
sol = Solution()
print(sol.wildCard(pattern, string))  # Expected output: 1 (True)