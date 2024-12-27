def countPairs(self,arr, target):
    freq=dict()
    ans=0
    for item in arr:
        temp=freq.get(target-item,0)
        if temp:
            ans+=temp
        freq[item]=freq.get(item,0)+1
    return ans