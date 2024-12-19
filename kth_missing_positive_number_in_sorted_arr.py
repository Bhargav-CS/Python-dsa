class Solution:
    def kthMissing(self, arr, k):
        # code here
        n=len(arr)
        p=arr[-1]-n
        if p<k:
            return arr[-1]+(k-p)
        i=0
        j=1
        while k>0:
            if arr[i]!=j:
                j+=1
                k-=1
            else:
                i+=1
                j+=1
        return j-1 