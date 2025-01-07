def countPairs (self, arr, target) :
    l,h,ans=0,len(arr)-1,0
    while l<h:
        val=arr[l]+arr[h]
        if val==target:
            if arr[l]==arr[h]:
                ans+=((h-l+1)*(h-l))//2
                break
            else:
                temp1,temp2=1,1
                while l<h and arr[l]==arr[l+1]:
                    l+=1
                    temp1+=1
                l+=1
                while l<h and arr[h]==arr[h-1]:
                    h-=1
                    temp2+=1
                h-=1
                ans+=temp1*temp2
        elif val<target:
            l+=1
        else:
            h-=1
    return ans