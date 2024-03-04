class Solution:
    def swapElements(self, arr, n):
        for i in range(n):
            if i+2<n:
                arr[i], arr[i+2] = arr[i+2], arr[i]
        return arr