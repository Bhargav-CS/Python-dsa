class Solution:
    def totalCount(self, k, arr):
        return sum(map(lambda x: (x + k - 1) // k, arr))