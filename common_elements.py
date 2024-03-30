class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        i, j, k = 0, 0, 0
        result = []
        while i < n1 and j < n2 and k < n3:
            if A[i] == B[j] == C[k]:
                result.append(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
        result = list(set(result))
        return result

A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
setA = {1,2,3,4,4,5,5}
sol = Solution()
print(sol.commonElements(A, B, C, len(A), len(B), len(C))) # 20 80
print(sorted(setA))