class Solution:
    def thirdLargest(self,a, n):
        return sorted(set(a))[-3] if len(set(a)) >= 3 else -1
    
a = [2,4,1,3,5]
N = 5 
sol = Solution()
print(sol.thirdLargest(a, N)) # 3