class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        
        print("")
        
        
class Solution:
    def isPalindrome(self, head):
        if values == values[::-1]:
            return True
        
        else:
            return False
        

llist = LinkedList()
values = [1, 2, 1, 1, 2, 1]
# values = [1, 2, 3, 4]

for i in reversed(values):
    llist.push(i)
    
flag = Solution().isPalindrome(llist.head)

if flag:
    print("true")

else:
    print("false")
