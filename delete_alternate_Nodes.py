'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution:
    def deleteAlt(self, head):
            # code here
            curr=head
            if head.next is None:
                return head
            
            while curr.next:
                if curr.next.next is None:
                    curr.next=None
                    break
                curr.next=curr.next.next
                curr=curr.next
                
            return curr