class Solution:
    def printLargest(self, n, arr):
        arr = list(map(str, arr))
        arr.sort(key=lambda x: x * 3, reverse=True)
        return ''.join(arr)

n = 5
arr = [3, 30, 34, 5, 9]

sol = Solution()
print(sol.printLargest(n, arr))