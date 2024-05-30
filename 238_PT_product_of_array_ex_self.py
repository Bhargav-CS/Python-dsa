class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            print(f"Prefix: {prefix}, res: {res}")
            
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            print(f"Postfix: {postfix}, res: {res}")
            
        return res
    
nums = [1, 2, 3, 4]
sol = Solution()
print(sol.productExceptSelf(nums))