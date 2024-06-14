class Solution:
    def armstrongNumber(self, n):
        n = str(n)
        number = 0
        for i in n:
            i = int(i)
            number += i**3
        
        n = int(n)
        if number == n:
            return "Yes"
        else:
            return "No"         

n = 153
sol = Solution()
print(sol.armstrongNumber(n))
