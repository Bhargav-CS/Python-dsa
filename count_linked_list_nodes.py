class Solution:
    def getCount(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
            
        return count
    
    
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
arr = [1, 2, 3, 4, 5]
head = Node(arr[0])
tail = head

for value in arr[1:]:
    tail.next = Node(value)
    tail = tail.next

sol = Solution()
print(sol.getCount(head))