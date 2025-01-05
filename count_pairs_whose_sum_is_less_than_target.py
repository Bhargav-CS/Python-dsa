class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        count=0
        n=len(arr)
        i=0
        j=n-1
        arr.sort()
        while(i<j):
            if(arr[i]+arr[j]>=target): 
                j=j-1
            else:
                count=count+(j-i)
                i=i+1
        return count