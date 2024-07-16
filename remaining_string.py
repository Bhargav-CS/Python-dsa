class Solution:
    def printString(self, s, ch, count):
        count_ = 0
        
        for i in range(len(s)):
            if s[i] == ch:
                count_ += 1
                
            if count_ == count:
                return s[i+1:]
            
        return ""
    
# s = "Thisisdemostring"
# ch = "i"
# count = 3

# s = "Thisisdemostri"
# ch = "i"
# count = 3

s = "abcd"
ch = "x"
count = 2
sol = Solution()
print(sol.printString(s, ch, count))


    