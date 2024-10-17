class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        f,s=head,head.next
        p1,p2=f,s
        while s and s.next:
            f.next=s.next
            s.next=s.next.next
            f=f.next
            s=s.next
        f.next=None
        return [p1,p2]
