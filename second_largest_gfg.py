import heapq

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr = list(set(arr))
        arr.sort()

        try:
            return arr[-2]
        
        except IndexError:
            return -1
        
        
    
arr = [12, 35, 1, 10, 34, 1]
# arr = [10, 10, 10]
# arr = [10, 5, 10]
sol = Solution()
print(sol.getSecondLargest(arr))