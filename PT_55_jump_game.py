class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # greedy Solution
        goal = len(nums) - 1
        for i in range(goal, -1, -1):
            print("i:", i)
            print("goal:", goal)
            print("i + nums[i]:", i + nums[i])
            print("goal condition:", i + nums[i] >= goal)
            if i + nums[i] >= goal:
                goal = i
                print("Updated goal:", goal)
        return not goal


# nums = [3,2,1,0,4]
nums = [2,3,1,1,4]
sol = Solution()
print(sol.canJump(nums))