def cloneLinkedList(self, head):
    curr=head
    while curr:
        temp=Node(curr.data)
        temp.next=curr.next
        curr.next=temp
        curr=temp.next
    curr=head
    while curr:
        if curr.random:
            curr.next.random=curr.random.next
        curr=curr.next.next
    curr=head
    newHead=curr.next
    while curr:
        temp=curr.next
        curr.next=temp.next
        curr=temp.next
        if curr:
            temp.next=curr.next
    return newHead