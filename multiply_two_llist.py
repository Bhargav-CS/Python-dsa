class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
def new_node(data):
    return Node(data)

def push(head_ref, new_data):
    
    new_Node = new_node(new_data)
    new_Node.next = head_ref[0]
    head_ref[0] = new_Node

def reverse(r):
    prev = None
    cur = r[0]
    
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    
    r[0] = prev
    
    
def free_list(Node):
    while Node:
        temp = Node
        Node = Node.next
        
        del temp
        
def print_list(Node):
    while Node:
        print(Node.data, end=" ")
        Node = Node.next
        
    print()
    
    
class Solution:
    def multiply_two_lists(self, first, second):
        MOD = 1000000007
        num1 = 0
        num2 = 0
        
        while first is not None or second is not None:
            if first is not None:
                num1 = (num1 * 10 + first.data) % MOD
                first = first.next
                
            if second is not None:
                num2 = (num2 * 10 + second.data) % MOD
                second = second.next
                
        return (num1 * num2) % MOD
        
    
    
first, second = [None], [None]

arr = [499, 768, 632]
brr = [290, 69, 7]

for num in arr:
    push(first, num)
    
for num in brr:
    push(second, num)
    
reverse(first)
reverse(second)



sol = Solution()
res = sol.multiply_two_lists(first[0], second[0])
print(res)