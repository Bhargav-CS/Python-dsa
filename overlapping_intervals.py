class Solution:
    def mergeOverlap(self, arr):
        # Step 1: Sort the intervals based on the starting times
        arr.sort(key=lambda x: x[0])
        
        # Step 2: Initialize the merged list
        merged = []
        
        for interval in arr:
            # If merged is empty or there is no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, merge the current interval with the last one
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged