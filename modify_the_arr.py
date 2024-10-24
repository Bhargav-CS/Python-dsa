class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        outputArr=[]
        zeroCount = 0 
        
        for i in range(len(arr)-1): 
            if arr[i] == arr[i+1]:
                arr[i]=arr[i]*2
                arr[i+1]=0
        #print(arr)
        
        for value in arr: 
            if value!=0: 
                outputArr.append(value)
            else: 
                zeroCount+=1
        
        outputArr+=[0]*zeroCount
        
        return outputArr