class Solution:
    def longestSubarray(self, nums, target):
        current_sum = 0
        max_length = 0
        index_map = {0: -1}  # Tracks the earliest occurrence of a cumulative sum
        
        for index, num in enumerate(nums):
            current_sum += num
            
            # Check if the current cumulative sum has been seen before
            if current_sum not in index_map:
                index_map[current_sum] = index  # Store the first occurrence
            
            # Check for a subarray that sums to the target
            if current_sum - target in index_map:
                max_length = max(max_length, index - index_map[current_sum - target])
        
        return max_length