# class Solution:
#     def reversedBits(self, x):
#         # code here
#         res = 0
#         for i in range(32):
#             res = res << 1
#             res = res | (x & 1)
#             x = x >> 1
#         return res


# x = 1
# sol = Solution()
# print(sol.reversedBits(x)) # output : 2147483648
