class Solution:
    def findFirstNode(self, head):
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if slow!=fast:
            return None
        while head!=slow:
            head=head.next
            slow=slow.next
        return head