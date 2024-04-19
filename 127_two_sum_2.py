class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize two pointers
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            # Calculate the sum of the two elements at the pointers
            current_sum = numbers[left] + numbers[right]
            
            # If the sum equals the target, return the indices (1-indexed)
            if current_sum == target:
                return [left + 1, right + 1]
            # If the sum is less than the target, move the left pointer to the right
            elif current_sum < target:
                left += 1
            # If the sum is greater than the target, move the right pointer to the left
            else:
                right -= 1
        
        # If no solution is found, which shouldn't happen as per problem statement
        return []
