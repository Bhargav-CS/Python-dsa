

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        arr = []
        
        while head:
            arr.append(head.data)
            head = head.next
            
        arr[:] = arr[k:] + arr[:k]
        print(arr)
        
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()
    

# arr = [2, 4, 7, 8, 9]
# k = 3

arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 4

head = None
if arr:
    head = Node(arr[0])
    tail = head
    for num in arr[1:]:
        tail.next = Node(num)
        tail = tail.next
        
sol = Solution()
head = sol.rotate(head, k)
printList(head)