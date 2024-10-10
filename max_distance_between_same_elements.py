class Solution:
    
    def maxDistance(self, arr):
        
        hashmap = {x:[] for x in arr}
        
        for i in range(len(arr)):
            ls = hashmap.get(arr[i])
            ls.append(i)

        max_distance = 0
        
        for values in hashmap.values():
            curr_distance = values[-1] - values[0]
            max_distance = max(max_distance, curr_distance)
            
        return max_distance
            
        
# arr = [1, 1, 2, 2, 2, 1]
arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]

sol = Solution()
print(sol.maxDistance(arr))