class Solution:
    def findTriplet(self, arr):
        arr.sort()
        for i in reversed(range(len(arr))):
            target = arr[i]
            left , right = 0, i - 1
            
            while left < right:
                if arr[left] + arr[right] == target:
                    return True
                elif arr[left] + arr[right] > target:
                    right -= 1
                else:
                    left += 1
        
        return False