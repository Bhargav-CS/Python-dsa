class Solution:
    def countElements(self, a, b, n, query, q):
        out = []
        count = 0
        b.sort()  # Sort the array b in ascending order
        
        for i in range(q):
            # Use binary search to find the index of the first element in b that is greater than a[query[i]]
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if b[mid] <= a[query[i]]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            count = left  # The count is the number of elements in b that are less than or equal to a[query[i]]
            out.append(count)
        
        return out
        
    

        

n = 4
a = [1,1,5,5]
b = [0,1,2,3]
q = 4
query = [0,1,2,3]

sol = Solution()
print(sol.countElements(a,b,n,query, q)) # [2, 2, 4, 4]
