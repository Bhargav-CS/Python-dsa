class Solution:
    def search(self, arr, key):
        try:
            return arr.index(key)
        except ValueError:
            return -1
            
    
    
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 10
arr = [3, 5, 1, 2]
key = 6
sol = Solution()
print(sol.search(arr, key))
