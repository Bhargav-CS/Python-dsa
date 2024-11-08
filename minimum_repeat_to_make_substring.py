import math

class Solution:
    def minRepeats(self, s1, s2):
        min_repeats = math.ceil(len(s2) / len(s1))
        repeated_s1 = s1 * min_repeats
        
        if repeated_s1.find(s2) != -1:
            return min_repeats
        
        repeated_s1 += s1
        if repeated_s1.find(s2) != -1:
            return min_repeats + 1
        
        return -1

# Example usage:
# s1 = "ww"
# s2 = "www"
# sol = Solution()
# print(sol.minRepeats(s1, s2))  # Output: 2

s1 = "abcd"
s2 = "cdabcdab"
sol = Solution()
print(sol.minRepeats(s1, s2))  # Output: 3