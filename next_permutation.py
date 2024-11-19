class Solution:
    def reverse(self,arr,s,e):
        while s<e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1

    def nextPermutation(self, arr):
        n=len(arr)
        idx=n-2
        while idx>=0 and arr[idx]>=arr[idx+1]:
            idx-=1
        if idx>=0:
            i=n-1
            while arr[i]<=arr[idx]:
                i-=1
            arr[idx],arr[i]=arr[i],arr[idx]
        self.reverse(arr,idx+1,n-1)
    
    
arr = [2, 4, 1, 7, 5, 0]
sol = Solution()
print(sol.nextPermutation(arr))