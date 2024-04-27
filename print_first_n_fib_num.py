class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        if n == 0:
            return []
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]
        fibb = [1, 1]
        for i in range(2, n):
            fibb.append(fibb[i-1] + fibb[i-2])
        return fibb[:n]
    

n = 5
sol = Solution()
print(sol.printFibb(n)) # [1, 1, 2, 3, 5]