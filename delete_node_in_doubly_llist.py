class Solution:
    def delete_node(self, head, x):
        # code here
        # 1 based indexing
        if x == 1:
            return head.next
        curr = head
        for i in range(x-2):
            curr = curr.next
        curr.next = curr.next.next
        
        return head
    
    