class Solution:
    def mergeArrays(self, a, b):
        n, m = len(a), len(b)
        gap = (n + m + 1) // 2  
        def next_gap(gap):
            if gap <= 1:
                return 0
            return (gap + 1) // 2
        
        while gap > 0:
            i, j = 0, gap
            while j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                i += 1
                j += 1
            j -= n 
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1
            i = 0
            while j < m:
                if b[i] > b[j]:
                    b[i], b[j] = b[j], b[i]
                i += 1
                j += 1
            gap = next_gap(gap)
    
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
sol = Solution()
print(sol.mergeArrays(a, b))