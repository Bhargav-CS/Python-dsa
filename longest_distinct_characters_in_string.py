class Solution:
    def longestUniqueSubstr(self, s):
        count=[-1]*26
        n=len(s)
        preIndx=-1
        ans=0
        for i in range(n):
            pos=ord(s[i])-ord("a")
            if count[pos]!=-1:
                preIndx=max(preIndx,count[pos])
            count[pos]=i
            ans=max(ans,i-preIndx)
        return ans