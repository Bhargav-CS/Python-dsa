class Node:
    
    def __init__(self, data) -> None:
        
        self.data = data
        self.next = None
        
        
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()
    
def loop_here(head, pos):
    if pos == 0:
        return 
    
    walk = head
    
    for _ in range(1, pos):
        walk = walk.next
        
    tail = head
    
    while tail.next:
        tail = tail.next
        
    tail.next = walk
    
    
class Solution:
    
    def countNodesInLoop(self, head):
        
        fast = slow = head
        
        try :
            while fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
                # print(fast.data)

                
                if slow == fast:
                    break
                
            if slow != fast:
                return 0
                
            fast = head
            
            while fast.next is not None and slow.next is not None:
                fast = fast.next
                slow = slow.next
                
                if fast == slow:
                    break
                
            count = 1
            
            fast = fast.next
            
            while fast != slow:
                fast = fast.next
                count += 1
                
            return count
        
        except AttributeError:
            return 0
            
        
            
            
        
            
    
arr = [25, 14, 19, 33, 10, 21, 39, 90, 58, 45]
arr = [5, 4]
k = 0
head = Node(arr[0])
tail = head

for value in arr[1:]:
    tail.next = Node(value)
    tail = tail.next
    
loop_here(head, k)

sol = Solution()
print(sol.countNodesInLoop(head))