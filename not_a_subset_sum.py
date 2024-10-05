class Solution:
    def findSmallest(self, arr):
        # code here
        m=1
        for num in arr:
            if num>m:
                break
            m+=num
        return m
    
