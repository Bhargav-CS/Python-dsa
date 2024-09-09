class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        arr.sort()
        return arr
    
arr = [0, 2, 1, 2, 0]
sol = Solution()
print(sol.sort012(arr))