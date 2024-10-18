
class Solution:
    
    def getSingle(self,arr):
        # code here
        memo={}
        for i in arr:
            memo[i]=memo.get(i,0)+1
        for key,value in memo.items():
            if value % 2!=0:
                return key