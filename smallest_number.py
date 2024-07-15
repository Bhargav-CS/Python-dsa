class Solution:
    def smallestNumber(self, s, d):
        # code here
        # for i in range(10**(d-1),10**d):
        #     i = str(i)
        #     num = sum(list(map(int, i)))
        #     print("num is ", i, "sum is", num)
        #     if num == s:
        #         return i
        
        # return -1
                
        i = 10**(d-1)
        i = str(i)
        num = sum(list(map(int, i)))
        i = int(i)
        if num == s:
            return i
        
        elif s < 10:
            return i + s - 1
        
        i = i + 9
        while i < 10**d:
            i = str(i)
            num = sum(list(map(int, i)))
            i = int(i)
            if num == s:
                return i
            
            i = i + 10
            
        return -1
                 
    
s = 9
d = 2
sol = Solution()
print(sol.smallestNumber(s, d))