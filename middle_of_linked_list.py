class node:
    
    def __init__(self) -> None:
        self.data = None
        self.next = None
        

class Linked_List:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next
            
            
class Solution:
    
    def findMid(self, head):
        
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow.data
            
def printList(head):
    temp = head
    
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print("")
    
    
list1 = Linked_List()
arr = [1, 2, 3, 4, 5]
# arr = [2, 4, 6, 7, 5, 1]

for i in arr:
    list1.insert(i)

sol = Solution()
print(sol.findMid(list1.head))
printList(list1.head)