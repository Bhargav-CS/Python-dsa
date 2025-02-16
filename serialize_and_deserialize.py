
from collections import deque

class Solution:
    
    def serialize(self, root):
        ans=[]
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            ans.append(node.data)
            if node.data:
                q.append(node.left if node.left else Node(None))
                q.append(node.right if node.right else Node(None))
        return ans

    def deSerialize(self, arr):
        i=0
        root=Node(arr[i])
        i+=1
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            if arr[i]:
                node.left=Node(arr[i])
                q.append(node.left)
            i+=1
            if arr[i]:
                node.right=Node(arr[i])
                q.append(node.right)
            i+=1
        return root
    
