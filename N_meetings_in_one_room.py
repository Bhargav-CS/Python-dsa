class Solution:
    def maximumMeetings(self,n,start,end):
        # Code here
        # Create a list of tuples with the index, start time, and end time
        meetings = [(i, start[i], end[i]) for i in range(n)]
        # Sort the meetings by their end time
        meetings.sort(key=lambda x: x[2])
        # Initialize the count of meetings
        count = 1
        # Initialize the end time of the first meeting
        end_time = meetings[0][2]
        # Iterate through the meetings
        for i in range(1, n):
            # If the start time of the current meeting is greater than or equal to the end time of the previous meeting
            if meetings[i][1] > end_time:
                # Increment the count of meetings
                count += 1
                # Update the end time of the previous meeting
                end_time = meetings[i][2]
        # Return the count of meetings
        return count
            
    
n = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
sol = Solution()
print(sol.maximumMeetings(n, start, end)) # 4