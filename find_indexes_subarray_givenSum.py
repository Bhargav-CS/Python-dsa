class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       hashmap = {}
       curr_sum = 0
       
       for i in range(n):
           curr_sum = curr_sum + arr[i]
           if curr_sum == s:
               return 1, i+1
            #    print("subarray starts from 0 to", i)
            #    break
            
           if curr_sum - s in hashmap:
               return hashmap[curr_sum - s]+2, i+1
            #    print("subarray starts from", hashmap[curr_sum - s]+1, i)
            #    break
           hashmap[curr_sum] = i
       return -1
           
           
       
   
arr = [1, 2, 3, 7, 5]
n = 5
s = 12
sol = Solution()
print(sol.subArraySum(arr, n, s))