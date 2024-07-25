class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Solution:
	def helper(self, nums, left, right):
		# base case
		if left > right:
			return None
		
		mid = left + (right - left) // 2
		node = Node(nums[mid])
		node.left = self.helper(nums, left, mid - 1)
		node.right = self.helper(nums, mid + 1, right)
		return node
	
	def sortedArrayToBST(self, nums):
		# Code here
		root = self.helper(nums, 0, len(nums) - 1)
		return root