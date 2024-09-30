class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def merge(self, root1, root2):
        sorted_list = []
        self.in_order_traversal(root1, sorted_list)
        self.in_order_traversal(root2, sorted_list)
        sorted_list.sort()
        return sorted_list
    
    def in_order_traversal(self, root, sorted_list):
        if root is None:
            return
        self.in_order_traversal(root.left, sorted_list)
        sorted_list.append(root.data)
        self.in_order_traversal(root.right, sorted_list)

# Example usage
# Create two BSTs
root1 = Node(3)
root1.left = Node(1)
root1.right = Node(5)

root2 = Node(4)
root2.left = Node(2)
root2.right = Node(6)

sol = Solution()
print(sol.merge(root1, root2))  # Expected output: [1, 2, 3, 4, 5, 6]