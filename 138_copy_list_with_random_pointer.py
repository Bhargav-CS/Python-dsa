"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return None
        
        # create a copy of each node and insert it in the list
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # assign random pointers to the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # separate the original and the new list
        current = head
        new_head = head.next
        new_current = new_head
        while current:
            current.next = new_current.next
            current = current.next
            if current:
                new_current.next = current.next
                new_current = new_current.next
        
        return new_head