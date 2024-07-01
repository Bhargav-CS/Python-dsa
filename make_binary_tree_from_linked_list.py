# User function Template for python3

'''
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''

#Function to make binary tree from linked list.
def convert(head):
    # code here
    if head is None:
        return None
    root = Tree(head.data)
    head = head.next
    q = [root]
    while head:
        parent = q.pop(0)
        left = None
        right = None
        if head:
            left = Tree(head.data)
            q.append(left)
            head = head.next
        if head:
            right = Tree(head.data)
            q.append(right)
            head = head.next
        parent.left = left
        parent.right = right
    return root 

