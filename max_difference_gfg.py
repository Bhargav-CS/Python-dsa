class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        left = []
        right = []
        st = []
        
        
        for i in range(n):
            while st and st[-1] >= arr[i]:
                st.pop()
            if not st:
                left.append(0)
            else:
                left.append(st[-1])
            st.append(arr[i])
        
        st.clear()
        
        
        for i in range(n-1, -1, -1):
            while st and st[-1] >= arr[i]:
                st.pop()
            if not st:
                right.append(0)
            else:
                right.append(st[-1])
            st.append(arr[i])
        
        right.reverse()
        
        
        maxi = float('-inf')
        for i in range(len(left)):
            maxi = max(maxi, abs(left[i] - right[i]))
        
        return maxi


arr = [2, 1, 8]
sol = Solution()
print(sol.findMaxDiff(arr))