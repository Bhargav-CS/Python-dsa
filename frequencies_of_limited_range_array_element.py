class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        frequency = [0] * (N+1)
        
        for i in arr:
            if i <= N:
                frequency[i] += 1
        
        for i in range(1, N+1):
            arr[i-1] = frequency[i]
            
        return arr
        
        
    
    
N = 5
arr = [2, 3, 2, 3, 5]
P = 5
# N = 2
# arr = [8, 9]
# P = 9
# N = 4
# arr = [3, 3, 3, 3]
# P = 3
sol = Solution()
print(sol.frequencyCount(arr, N, P))


