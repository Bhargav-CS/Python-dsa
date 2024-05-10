class Solution:  
    def CombinationSum2(self, arr, n, k):
        # code here
        
        def backtrack(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, n):
                if i > start and arr[i] == arr[i-1]:
                    continue
                if arr[i] > target:
                    break
                backtrack(i+1, target-arr[i], path+[arr[i]])
                
        arr.sort()
        res = []
        backtrack(0, k, [])
        return res
    
    

n = 6
k = 30
arr = [5, 10, 15, 20, 25, 30]
sol = Solution()
print(sol.CombinationSum2(arr, n, k)) #{ { 5, 10, 15 }, { 5, 25 }, { 10, 20 }, { 30 } }