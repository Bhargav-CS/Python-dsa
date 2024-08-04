class Solution:
    def maximumMeetings(self,n,start,end):
        # Code here
        meetings = [(i, start[i], end[i]) for i in range(n)]
        meetings.sort(key=lambda x: x[2])
        count = 1
        end_time = meetings[0][2]
        for i in range(1, n):
            if meetings[i][1] > end_time:
                
                count += 1
                
                end_time = meetings[i][2]
        
        return count
            
    
n = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
sol = Solution()
print(sol.maximumMeetings(n, start, end)) # 4