class Solution:
    def duplicates(self, arr, n):
        seen = set()
        duplicates = set()
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        return sorted(list(duplicates)) or [-1]


# arr = [0,3,1,2]
# n = 4
arr = [2, 3, 1, 2, 3]
n = 5
sol = Solution()
print(sol.duplicates(arr, n)) # 2 3