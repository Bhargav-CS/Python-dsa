class Solution:
    def getCount(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 10
        
        count = [0] * 10
        nextDigit = [0] * 10
        i = 0
        j = 0
        totalCount = 0
        
        for i in range(10):
            count[i] = 1
        
        for i in range(2, n+1):
            for j in range(10):
                nextDigit[j] = count[j]
            
            count[0] = nextDigit[0] + nextDigit[8]
            count[1] = nextDigit[1] + nextDigit[2] + nextDigit[4]
            count[2] = nextDigit[2] + nextDigit[1] + nextDigit[3] + nextDigit[5]
            count[3] = nextDigit[3] + nextDigit[2] + nextDigit[6]
            count[4] = nextDigit[4] + nextDigit[1] + nextDigit[5] + nextDigit[7]
            count[5] = nextDigit[5] + nextDigit[2] + nextDigit[4] + nextDigit[6] + nextDigit[8]
            count[6] = nextDigit[6] + nextDigit[3] + nextDigit[5] + nextDigit[9]
            count[7] = nextDigit[7] + nextDigit[4] + nextDigit[8]
            count[8] = nextDigit[8] + nextDigit[0] + nextDigit[5] + nextDigit[7] + nextDigit[9]
            count[9] = nextDigit[9] + nextDigit[6] + nextDigit[8]
        
        for i in range(10):
            totalCount += count[i]
        
        return totalCount
	
	
n = 2
sol = Solution()
print(sol.getCount(n)) # 10