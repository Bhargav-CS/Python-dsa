class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n > time:
            return time + 1
        
        elif time > n:
            rem = time//(n-1)
            if rem % 2 == 0:
                return time%(n-1) + 1
            else:
                return n - (time%(n-1))

        else:
            return n - 1
                
        # return n - abs(n-1-time%(2*n - 2))
    
n = 6
time = 18
sol = Solution()
print(sol.passThePillow(n, time))