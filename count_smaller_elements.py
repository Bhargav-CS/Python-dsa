from sortedcontainers import SortedList

class Solution:
    def constructLowerArray(self, arr):
        s_list = SortedList()
        ans = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            ans[i] = s_list.bisect_left(arr[i])
            s_list.add(arr[i])
        return ans
    
   
# from bisect import bisect_left

# class Solution:
#     def binarySearch(self, v, x):
#         l, h = 0, len(v) - 1
#         while l <= h:
#             mid = (l + h) // 2
#             if v[mid] == x:
#                 return mid
#             elif v[mid] > x:
#                 h = mid - 1
#             else:
#                 l = mid + 1
#         return -1

#     def constructLowerArray(self, arr):
#         v = sorted(arr)
#         t = [0] * len(arr)
#         for i, num in enumerate(arr):
#             max_index = bisect_left(v, num)
#             t[i] = max_index
#             v.pop(max_index)
#         return t
    
    
arr = [12, 1, 2, 3, 0, 11, 4]

sol = Solution()
print(sol.constructLowerArray(arr)) # [6, 1, 1, 1, 0, 1, 0]


