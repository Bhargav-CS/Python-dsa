class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        
        # Calculate left products and store in result
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Calculate right products and multiply with the result
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

# Example usage
nums = [10, 3, 5, 6, 2]
sol = Solution()
print(sol.productExceptSelf(nums))
    
