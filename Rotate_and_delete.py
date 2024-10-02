class Solution:
    def rotateDelete(self, arr):
        n = len(arr)
        a = n // 4
        b = n % 4
        a += 1
        
        if b == 0:
            return arr[a - 1]
        elif b == 1:
            return arr[a]
        elif b == 2:
            return arr[a]
        elif b == 3:
            return arr[a + 1]

# Example usage
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [1, 2, 3, 4, 5, 6]
arr = [1, 2, 3, 4]
sol = Solution()
print(sol.rotateDelete(arr))  # Expected output will depend on the array size and values