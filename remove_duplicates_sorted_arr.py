class Solution:
    def remove_duplicate(self, A, N):
        if N == 0:
            return 0
        j = 0
        for i in range(1, N):
            if A[i] != A[j]:
                j += 1
                A[j] = A[i]
        return j + 1
    
N = 4
A = [1, 2, 2, 4]
sol = Solution()
print(sol.remove_duplicate(A, N)) # 3
    
