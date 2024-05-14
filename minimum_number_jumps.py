class Solution:
    def minJumps(self, arr, n):
        #code here
        if n == 1:
            return 0
        if arr[0] == 0:
            return -1
        maxR = arr[0]
        step = arr[0]
        jump = 1
        for i in range(1, n):
            if i == n - 1:
                return jump
            maxR = max(maxR, i + arr[i])
            step -= 1
            if step == 0:
                jump += 1
                if i >= maxR:
                    return -1
                step = maxR - i
        return -1
    
    
n = 6
arr = [1, 4, 3, 2, 6, 7]
sol = Solution()
print(sol.minJumps(arr, n)) #2