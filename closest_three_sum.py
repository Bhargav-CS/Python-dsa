
class Solution:
    def threeSumClosest(self, arr:list, target:int):
        hashmap = {}
        
        # {-7: 9, 9: -7, 8: -6, 3: -1, 1: 1}
        
        for ele in arr:
            hashmap[ele] = target - ele
            
        left = 0
        right = 1
        curr_sum = 0
        max_sum = 0
        while left < len(arr) and right < len(arr):
            value = arr[left] + arr[right]
            try:
                rev = list(hashmap.keys())[list(hashmap.values()).index(value)]
                if (arr.index(rev) != arr[left] or arr.index != arr[right]):
                    return target
                
            except ValueError:
                right += 1
                if right == len(arr) - 1:
                    left += 1
                    right = left + 1
        
        return
                
            
                    
        
            
            
        
    
arr1 = [-7, 9, 8, 3, 1, 1]
target1 = 2
arr2 = [5, 2, 7, 5]
target2 = 13
sol = Solution()
print(sol.threeSumClosest(arr2, target2))

