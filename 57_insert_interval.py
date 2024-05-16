class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # Append newInterval to intervals
        intervals.append(newInterval)
        # Sort the intervals
        intervals.sort()
        # Initialize an empty list to store the merged intervals
        merged = []
        # Iterate through the intervals
        for interval in intervals:
            # If the merged list is empty or the current interval's start is greater than the last interval's end
            if not merged or merged[-1][1] < interval[0]:
                # Append the interval to the merged list
                merged.append(interval)
            else:
                # Else, merge the last interval with the current interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    
    
    
intevals = [[1,3],[6,9]]
newInterval = [2,5]
sol = Solution()
print(sol.insert(intevals, newInterval)) #[[1,5],[6,9]]