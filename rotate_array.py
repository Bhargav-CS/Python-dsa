class Solution:
    def rotateArr(self, A, D, N):
        D = D % N  # Reduce D to be within the range of N
        A[:D] = reversed(A[:D])  # Reverse the first D elements
        A[D:] = reversed(A[D:])  # Reverse the remaining N-D elements
        A[:] = reversed(A[:])  # Reverse the entire array
        return A

A = [1,2,3,4,5]
D = 2
N = 5

sol = Solution()
print(sol.rotateArr(A, D, N)) # [3,4,5,1,2]