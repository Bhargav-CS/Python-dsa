class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = (len(a) + len(b)) // len(a)
        for i in range(n+2) :
            c = a * i
            print(c)
            if b in c:
                return i
        
        return -1
    
# a = "abcd"
# b = "cdabcdab"
# a = "a"
# b = "aa"
a = "abc"
b =  "cabcabca"
sol = Solution()
print(sol.repeatedStringMatch(a, b))

