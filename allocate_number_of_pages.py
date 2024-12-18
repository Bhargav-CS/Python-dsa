class Solution:
    
    #Function to find minimum number of pages.
    def cntStudents(self,arr,pages):
        students=1
        pagesStudent=0
        n=len(arr)
        for i in range(n):
            if pagesStudent+arr[i]<=pages:
                pagesStudent+=arr[i]
            else:
                students+=1
                pagesStudent=arr[i]
        return students
    
    def findPages(self, arr, k):
        if len(arr)<k:
            return -1
        l,h=max(arr),sum(arr)
        while l<=h:
            mid=(l+h)//2
            students=self.cntStudents(arr,mid)
            if students>k:
                l=mid+1
            else:
                h=mid-1
        return l