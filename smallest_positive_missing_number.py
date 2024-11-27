
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
            arr=[num for num in arr if num>0]
            num_set=set(arr)
            for i in range(1,len(arr)+2):
                if i not in num_set:
                    return i