def maxWater(self, arr):
        n=len(arr)
        waterFill=0
        lmax,rmax=0,0
        st,end=0,n-1
        while st<end:
            if arr[st]<arr[end]:
                if arr[st]<lmax:
                    waterFill+=lmax-arr[st]
                else:
                    lmax=arr[st]
                st+=1
            else:
                if arr[end]<rmax:
                    waterFill+=rmax-arr[end]
                else:
                    rmax=arr[end]
                end-=1
        return waterFill