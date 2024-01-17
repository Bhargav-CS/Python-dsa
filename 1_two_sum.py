class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            print("complement is : ", complement)
            print("value of i is:" ,i ,"value of num is: ", num)
            print(num_dict)
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

object = Solution()
print(object.twoSum([2, 7, 11, 15], 9))