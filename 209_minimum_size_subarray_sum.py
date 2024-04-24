class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # initialize the left pointer
        left = 0
        # initialize the sum of the subarray
        sub_sum = 0
        # initialize the result
        res = float('inf')
        # iterate through the list
        for i in range(len(nums)):
            # add the current element to the subarray sum
            sub_sum += nums[i]
            # while the subarray sum is greater than or equal to the target
            while sub_sum >= target:
                # calculate the length of the subarray
                res = min(res, i - left + 1)
                # subtract the left element from the subarray sum
                sub_sum -= nums[left]
                # increment the left pointer
                left += 1
        # return the result
        return res if res != float('inf') else 0

target = 7
nums = [2,3,1,2,4,3]    
sol = Solution()
print(sol.minSubArrayLen(target, nums)) # 2