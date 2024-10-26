class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
        
class Solution:
    def count(self, head, key):
        # Code here
        count = 0
        while head:
            if head.data == key:
                count += 1
                
            head = head.next
                
        return count
            
