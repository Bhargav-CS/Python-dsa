class Solution:
    def printArr(self, n, arr):
        # printing array elements with spaces
        for ele in arr:
            print(ele, end=" ")
        print("\n")
        

    def setToZero(self, n, arr):
        # setting all elements to zero
        for i in range(n):
            arr[i] = 0
              

    def xor1ToN(self, n, arr):
        # doing xor with indices
        for i in range(n):
            arr[i] = arr[i]^i

sol = Solution()
n = 10
arr = [1,2,3,4,5,6,7,8,9,10]

sol.xor1ToN(n, arr)
sol.printArr(n, arr)
sol.setToZero(n, arr)
sol.printArr(n, arr)
