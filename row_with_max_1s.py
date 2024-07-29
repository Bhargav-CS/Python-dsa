class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        ans = -1
        max_sum = 0
        
        for i in range(n):
            curr_sum = sum(arr[i])
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = i
                
        return ans        
    
arr = [[0, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]]

arr = [[0, 0],
       [1, 1]]

arr = [[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

sol = Solution()
print(sol.rowWithMax1s(arr))
