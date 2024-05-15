class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        arr.sort()
        return arr
    
n = 5
arr = [4, 1, 3, 9, 7]
sol = Solution()
print(sol.bubbleSort(arr, n)) #[1, 3, 4, 7, 9]



