class Solution:

    def minIncrements(self, arr): 

        # Code here

        arr.sort()

        c=arr[0]

        r=0

        if len(arr)>1:

            for i in range(1, len(arr)):

                if arr[i]<=c:

                    r+=(c-arr[i])+1

                    arr[i]=c+1

                c=arr[i]

        return r