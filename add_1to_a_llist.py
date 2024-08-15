class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            
        self.size += 1
        
        
class Solution:
    def addOne(self, head):
        s = ""
        
        while head:
            s = s + str(head.data)
            head = head.next
            
        s = str(int(s) + 1)
        
        head = LinkedList()
        for char in s:
            head.insert(int(char))
            
        return head.head
            
        

def PrintList(head):
    while head:
        print(head.data, end="")
        head = head.next 
        

list1 = LinkedList()
arr = [8, 4, 2, 1, 4, 1, 1, 7, 6, 7, 7, 6]
first = arr[0]

for i in arr:
    list1.insert(i)

n1 = list1.size
resHead = Solution().addOne(list1.head)

n2 = 0
current = resHead

while current is not None:
    current = current.next
    n2 += 1
    
if n2 == 1:
    if n1>1:
        print("return the modified linkedlist")
    
    if n1==1:
        if first < 9:
            PrintList(resHead)
        else:
            print("return the modified linkedList")
            
else:
    PrintList(resHead)
    print()
    
    
