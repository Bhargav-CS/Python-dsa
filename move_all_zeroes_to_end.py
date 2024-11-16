class Solution:
    def pushZerosToEnd(self, arr: list):
        n = len(arr)
        non_zero_index = 0
        
        for i in range(n):
            if arr[i] != 0:
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1
        
        return arr

# Example usage:
arr = [1, 2, 0, 4, 3, 0, 5, 0]
# arr = [10, 20, 30]
# arr = [0, 0]
sol = Solution()
print(sol.pushZerosToEnd(arr))