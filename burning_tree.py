from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s:str):
    if (len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))

    root = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
    size += 1

    i = 1

    while (size > 0 and i< len(ip)):
        currNode = q[0]
        q.popleft()
        size -= 1

        currVal = ip[i]

        if (currVal != "N"):
            currNode.left = Node(int(currVal))

            q.append(currNode.left)
            size += 1

        i += 1

        if(i>len(ip)):
            break

        currVal = ip[i]

        if currVal != "N":
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size += 1

        i += 1

    return root


class Solution:
    def maxDepth(self, node):
        if node is None:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

    def traverse(self, node, target):
        # base case
        if node is None:
            return 0
        
        # target found, hence returning distance from it
        if node.data == target:
            self.ans = max(self.ans, self.maxDepth(node.right))
            self.ans = max(self.ans, self.maxDepth(node.left))
            return 1
        
        val = self.traverse(node.left, target)
        
        # (val != 0) means target was found at distance = val
        if val != 0:
            # finding max Depth on right as target was on left
            self.ans = max(self.ans, val + self.maxDepth(node.right))
            return val + 1

        val = self.traverse(node.right, target)
        
        # (val != 0) means target was found at distance = val
        if val != 0:
            # finding max Depth on left as target was on right
            self.ans = max(self.ans, val + self.maxDepth(node.left))
            return val + 1

        return 0

    def minTime(self, root, target):
        self.ans = 0
        self.traverse(root, target)
        return self.ans

# Example usage
line = "1 2 3 4 5 N 6 N N 7 8 N 9 N N N N N 10"
target = 8
root = buildTree(line)
sol = Solution()
print(sol.minTime(root, target))