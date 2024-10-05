class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        if head is None or head.next == head:
            return head
        
        prev = None
        curr = head
        next_node = None
        tail = head

        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == head:
                break
        
        tail.next = prev
        head = prev

        return head

    def deleteNode(self, head, key):
        if head is None:
            return None

        if head.data == key:
            if head.next == head:
                return None

            tail = head
            while tail.next != head:
                tail = tail.next

            head = head.next
            tail.next = head

            return head

        temp = head
        while temp.next != head: 
            if temp.next.data == key:
                temp.next = temp.next.next
                break
            temp = temp.next

        return head