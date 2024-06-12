class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        count = 0
        while n>0:
            n = str(n)
            if "4" in n:
                count += 1
            n = int(n)
            n -= 1
            
        return count
    
n = 44
sol = Solution()
print(sol.countNumberswith4(n))
    