import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next 
    print()
    
class Solution:
    def mergeKLists(self, arr):
        head = arr[0]
        curr = head
        while curr.next:
            curr = curr.next
        for i in range(1,len(arr)):
            n = arr[i]
            curr.next = n
            while curr.next:
                curr = curr.next
        result = []
        curr = head
        while curr:
            result.append(curr.data)
            curr = curr.next
        result.sort()
        head1 = Node(-1)
        curr = head1
        i=0
        while i<len(result):
            temp = Node(result[i])
            curr.next = temp
            curr = curr.next
            i+=1
        return head1.next
        
           
    
    
arr = [[1, 2, 3], [4, 5], [5, 6], [7, 8]]
lists = []

for i in range(len(arr)):
    values = arr[i]
    head = None
    temp = None
    
    for value in values:
        newNode = Node(value)
        if head is None:
            head = newNode
            temp = head
        else:
            temp.next = newNode
            temp = temp.next
    lists.append(head)

    
sol = Solution()
head = sol.mergeKLists(lists)
printList(head)