class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort the list
        nums.sort()
        # initialize the result list
        res = []
        # iterate through the list
        for i in range(len(nums)-2):
            # if the current element is greater than 0, break the loop
            if nums[i] > 0:
                break
            # if the current element is same as the previous element, continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # initialize the left and right pointers
            l, r = i+1, len(nums)-1
            # iterate through the list
            while l < r:
                # calculate the sum of the current triplet
                s = nums[i] + nums[l] + nums[r]
                # if the sum is less than 0, increment the left pointer
                if s < 0:
                    l += 1
                # if the sum is greater than 0, decrement the right pointer
                elif s > 0:
                    r -= 1
                # if the sum is 0, add the triplet to the result list
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # increment the left pointer
                    l += 1
                    # decrement the right pointer
                    r -= 1
                    # skip the duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        # return the result list
        return res

sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums)) # [[-1,-1,2],[-1,0,1]]