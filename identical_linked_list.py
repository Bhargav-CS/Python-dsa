import li

class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
        
class LinkedList:
    def __inti__(self):
        self.head = None
        
    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        
def printList(head):
        while head:
            print(head.data, end = " ")
            head = head.next
        print() 
        
        
def createList(arr, n):
    lis = LinkedList()
    for i in range(n):
        lis.insert(arr[i])
    
    return lis.head

               
        
def areIdentical(head1, head2):
    while (head1 != None and head2 != None):
        if (head1.data != head2.data):
            return False
        head1 = head1.next
        head2 = head2.next
        
    if (head1 == None and head2 == None):
        return True
    return False