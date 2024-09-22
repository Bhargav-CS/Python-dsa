class Solution:
    def lps(self, s: str) -> int:
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1
        
        while i < n:
            print(s[i], s[length])
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    print("in here")
                    lps[i] = 0
                    i += 1
        
        return lps[-1]

# Example usage
str = "abab"
# str = "aaaa"
str = "bhargavpatkibhargav"
sol = Solution()
print(sol.lps(str))
