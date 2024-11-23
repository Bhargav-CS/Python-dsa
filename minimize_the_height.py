class Solution:
    def getMinDiff(self, k, arr):
        arr.sort()
        n = len(arr)

        # Initial difference
        result = arr[-1] - arr[0]

        # Iterate through the array
        for i in range(n-1):

            # Calculate new min and max heights
            min_height = min(arr[0] + k, arr[i+1] - k)
            max_height = max(arr[i] + k, arr[-1] - k)

            # Update result
            result = min(result, abs(max_height - min_height))

        return result