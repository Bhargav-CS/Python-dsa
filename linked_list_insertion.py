'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        # code here
        temp = Node(x)
        temp.next = head
        return temp
    
    
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        temp = Node(x)
        if head is None:
            return temp
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = temp
        return head
    
    