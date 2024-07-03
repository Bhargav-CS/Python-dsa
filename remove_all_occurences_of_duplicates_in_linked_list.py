class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def removeAllDuplicates(self, head):
        if head is None:
            return None
        
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            if current.next and current.data == current.next.data:
                while current.next and current.data == current.next.data:
                    current = current.next
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
            
        return dummy.next
      

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node
        
    def printList(self, head):
        if head is None:
            print(" ")
            return
        
        curr_node = head
        while curr_node:
            print(curr_node.data, end = " ")
            curr_node = curr_node.next
        print(" ")
        
t = int(input())
for cases in range(t):
    N = int(input())
    a = LinkedList()
    nodes = list(map(int, input().strip().split()))
    
    for x in nodes:
        a.append(x)
    
    sol = Solution()
    head = sol.removeAllDuplicates(a.head)
    a.printList(head)