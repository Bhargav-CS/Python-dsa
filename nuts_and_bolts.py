class Solution:
    def matchPairs(self, n, nuts, bolts):
		# code here
        nuts.sort()
        bolts.sort()
    
n = 5
nuts = ["@", "%", "$", "#", "^"]
bolts = ["%", "@", "#", "$", "^"]
sol = Solution()
print(sol.matchPairs(n, nuts, bolts))

priority = ["!", "#", "$", "%", "&", "*", "?", "@", "^"]
priority.sort()
print(priority)
nuts.sort()
print(nuts)