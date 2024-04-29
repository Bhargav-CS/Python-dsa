'''
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''

class Solution:
    def deleteK(self, head, k):
        if not head or k <= 0:
            return head
        
        if k == 1:
            return None
        
        count = 1
        curr = head
        prev = None
        
        while curr:
            if count % k == 0:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                prev = curr
            curr = curr.next
            count += 1
        
        return head
    