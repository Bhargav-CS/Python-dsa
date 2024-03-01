#User function Template for python3
class Solution:
    def sumBitDiff(self, arr, n):
        sum = 0
        for i in range(n):
            for j in range(n):
                sum += bin(arr[i]^arr[j]).count('1')
    	
        return sum
    

