class Solution:
    def printLargest(self, n, arr):
        arr.sort(key=lambda x: x*3, reverse=True)
        return ''.join(arr)
    