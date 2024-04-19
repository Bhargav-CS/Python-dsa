class Solution:
    def getPairsCount(self, arr, n, k):
        # Dictionary to store the frequency of each element in the array
        count_map = {}
        # Initialize the count of pairs
        count = 0

        # Iterate through each element in the array
        for num in arr:
            # Check if there is a number in the array that, when added to `num`, equals `k`
            # The complement of `num` is `k - num`
            if k - num in count_map:
                # If the complement is found, it means we can form a pair that sums up to `k`
                # Add the frequency of the complement to the count of pairs
                count += count_map[k - num]

            # Update the frequency of the current number in the map
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        return count
