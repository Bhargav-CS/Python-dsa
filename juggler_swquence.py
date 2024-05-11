class Solution:
    def jugglerSequence(self, n):
        # code here
        res = []
        res.append(n)
        while n != 1:
            if n % 2 == 0:
                n = int(n**0.5)
            else:
                n = int(n**1.5)
            res.append(n)
        return res
    
n = 5
sol = Solution()
print(sol.jugglerSequence(n)) # 9 27 140 11 36 6 2 1 