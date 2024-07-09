class Solution:
    def threeSumClosest (self, arr, target):
        arr.sort()
        
        dif = float('inf')
        ans = float('inf')
        
        for i in range(len(arr)):
            start = i + 1
            end = len(arr) - 1
            
            while start < end :
                sum = arr[i] + arr[start] + arr[end]
                
                if sum == target:
                    return sum
                
                elif sum > target:
                    end -= 1
                    
                else:
                    start += 1
                    
                if abs(sum-target) < dif:
                    dif = abs(sum - target)
                    ans = sum
                
                elif abs(sum-target) == dif:
                    ans = max(ans, sum)
                    
        return ans
    

arr = [5, 2, 7, 5]
target = 13
sol = Solution()
print(sol.threeSumClosest(arr, target))