class Solution:
    def rotateArr(self, arr:list, d:int):
        d = d%len(arr)
        arr[d:], arr[:d] = arr[:d], arr[d:]
        return arr
        
    
arr = [1, 2, 3, 4, 5]
d = 2
# arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# d = 3

sol = Solution()
print(sol.rotateArr(arr, d))