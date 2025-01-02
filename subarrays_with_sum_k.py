class Solution:
    def countSubarrays(self, arr, k):
        d={0:1}
        s=0
        count=0
        for i in arr:
            s+=i
            count+=d.get(s-k,0)
            d[s]=d.get(s,0)+1
        return count 