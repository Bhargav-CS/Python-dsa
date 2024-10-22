class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        ans = 0 # Num same occurence
        count_x = 0 # Counter of num x upto index i
        count_y = 0 # Counter of num y upto index i
       
        # Dict to count indices with specific (count_x-count_y)
        diff = {0:1} # Count 0 occurence before starting
        
        for i in range(len(arr)):
            # Update counters
            if arr[i] == x:
                count_x += 1
            if arr[i] == y:
                count_y += 1
            # Unpdate num same occurence
            ans += diff.get(count_x - count_y, 0)
            # Update Dict
            diff[count_x - count_y] = diff.get(count_x - count_y, 0) + 1
 
        return ans