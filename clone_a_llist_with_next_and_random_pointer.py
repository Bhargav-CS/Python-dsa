class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.random = None
        
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
def insert(tail, data):
    tail.next = Node(data)
    return tail.next

def setrandom(head, a, b):
    h = head
    i = 1
    
    while i < a and h:
        h = h.next
        i += 1
        
    an = h
    
    h = head
    i = 1
    
    while i < b and h:
        h = h.next
        i += 1
        
    if an:
        an.random = h
        
        
def validation(head, res):
    headp = head
    resp = res
    
    d = {}
    
    while head and res:
        
        if head == res:
            return
        
        if head.data != res.data:
            return
        
        if head.random:
            if not res.random:
                return
            
            if head.random.data != res.random.data:
                return
            
        elif res.random:
            return
        
        if head not in d:
            d[head] = res
        
        head = head.next
        res = res.next
        
    if not head and res:
        return
    
    elif head and not res:
        return
    
    head = headp
    res = resp
    
    while head:
        
        if head == res:
            return
        
        if head.random:
            if head.random not in d:
                return
            if d[head.random] != res.random:
                return
            
        head = head.next
        res = res.next
        
    return True

class Solution:
    
    def copyList(self, head):
        if not head:
            return None
        
        h = head
        while h:
            temp = h.next
            h.next = Node(h.data)
            h.next.next = temp
            h = temp
            
        h = head
        while h:
            if h.random:
                h.next.random = h.random.next
            h = h.next.next
            
        h = head
        res = h.next
        temp = res
        
        while h:
            h.next = h.next.next
            h = h.next
            
            if temp.next:
                temp.next = temp.next.next
                temp = temp.next
                
        return res
    
    