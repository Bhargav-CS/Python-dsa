class Solution:
    def countTriangles(self, arr):
        n=len(arr)
        arr.sort()
        count=0
        
        if n<3:
            return 0
        
        for i in range(n-1,1,-1):
            left=0
            right=i-1
            
            while(left<right):
                s=arr[left]+arr[right]
                if s>arr[i]:
                    count+=(right-left)
                    right-=1


                else:
                    left+=1
        
        return count