class Solution:
    def compareFrac(self, str:str):
        str1, str2 = str.split(", ")
        if eval(str1) == eval(str2):
            return "equal"
        elif eval(str1) > eval(str2):
            return str1
        else:
            return str2
    
    
# str = "5/6, 11/45"
# str = "8/1, 8/1"
str = "10/17, 9/10"
sol = Solution()
print(sol.compareFract(str))